"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import get_post_data,get_user_data
from models import engine,Base,User,Post,Session
from sqlalchemy.ext.asyncio import AsyncSession



async def db_init():
    async with engine.begin() as connect_db:
        await connect_db(Base.metadata.create_all)

async def create_users(db:AsyncSession,users_data):
    for user in users_data:
        db_user=User(
            username=user['username'],
            email=user['email']
        )
        db.add(db_user)
    await db.commit()


async def create_posts(db: AsyncSession, posts_data):
    for post in posts_data:
        db_post = Post(
            user_id=post['user_id'],
            title=post['title'],
            body=post['body']
        )
        db.add(db_post)
    await db.commit()


async def async_main():
    async with Session() as session:
        await db_init()

        users_data, posts_data = await asyncio.gather(get_post_data(), get_user_data())
        await create_users(session, users_data())
        await create_posts(session, posts_data())


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
