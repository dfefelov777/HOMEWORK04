"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"



async def fetch_json(session,url):
    async with session.get(url) as response:
        return await response.json()


async def get_user_data():
    async with aiohttp.ClientSession() as users_get_data:
        return await fetch_json(users_get_data,USERS_DATA_URL)

async def get_post_data():
    async with aiohttp.ClientSession() as posts_get_data:
        return await fetch_json(posts_get_data, POSTS_DATA_URL)


