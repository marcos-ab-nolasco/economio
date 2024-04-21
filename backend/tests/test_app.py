from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import UserPublic, UserSchema


def test_root_deve_retornar_ok_e_ola_mundo(client: TestClient):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_user_created(client: TestClient):
    sent_user_mock = UserSchema(
        username='alice', email='alice@example.com', password='123'
    ).model_dump()

    response = client.post(url='/users/', json=sent_user_mock)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == UserPublic(**sent_user_mock).model_dump()


def test_read_users(client: TestClient):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'alice', 'email': 'alice@example.com'}]
    }


def test_update_user(client: TestClient):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'username': 'bob', 'email': 'bob@example.com'}


def test_delete_user(client: TestClient):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
