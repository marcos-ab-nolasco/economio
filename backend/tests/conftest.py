import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import get_session
from app.main import api
from app.models.user import Base, User


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(api) as client:
        api.dependency_overrides[get_session] = get_session_override
        yield client

    api.dependency_overrides.clear()


@pytest.fixture()
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )  # cria um mecanismo SQLite db em memória usando SQLAlchemy.
    Session = sessionmaker(
        bind=engine
    )  # fábrica de sessões para conexão com banco de dados
    Base.metadata.create_all(engine)  # cria todas as tabelas
    yield Session()  # persiste e propaga ums instancia de session
    Base.metadata.drop_all(
        engine
    )  # no final do teste, apaga as tabelas em mémoria


@pytest.fixture()
def user(session):
    user = User(username='Teste', email='teste@test.com', password='testtest')
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
