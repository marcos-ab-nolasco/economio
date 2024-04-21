import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import api
from app.models import Base


@pytest.fixture()
def client():
    return TestClient(api)


@pytest.fixture()
def session():
    engine = create_engine(
        'sqlite:///:memory:'
    )  # cria um mecanismo SQLite db em memória usando SQLAlchemy.
    Session = sessionmaker(
        bind=engine
    )  # fábrica de sessões para conexão com banco de dados
    Base.metadata.create_all(engine)  # cria todas as tabelas
    yield Session()  # persiste e propaga ums instancia de session
    Base.metadata.drop_all(
        engine
    )  # no final do teste, apaga as tabelas em mémoria
