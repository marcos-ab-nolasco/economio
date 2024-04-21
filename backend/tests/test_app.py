from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import User, UserPublic, UserSchema


def test_root_deve_retornar_ok_e_ola_mundo(client: TestClient):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client: TestClient):
    sent_user_mock = UserSchema(
        username='alice', email='alice@example.com', password='123'
    ).model_dump()

    response = client.post(url='/users/', json=sent_user_mock)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == UserPublic(id=1, **sent_user_mock).model_dump()


def test_read_users(client: TestClient):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client: TestClient, user: User):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client: TestClient, user: User):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == UserPublic(**{
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }).model_dump()


def test_delete_user(client: TestClient, user: User):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
