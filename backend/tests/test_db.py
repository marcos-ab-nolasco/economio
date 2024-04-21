from sqlalchemy import select

from app.models.user import User


def test_create_user(session):
    new_user = User(username='amanda', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'amanda'))

    assert user.username == 'amanda'
