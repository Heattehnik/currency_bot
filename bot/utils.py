import aiohttp


async def register_client(user_id, username, first_name, last_name):
    async with aiohttp.ClientSession() as session:
        data = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,

        }
        url = f'http://app:8000/api/v1/client/'
        async with session.post(url=url, data=data) as response:
            if response.status == 201:
                data = await response.json()
                return data


async def get_currency(user_id):
    async with aiohttp.ClientSession() as session:
        url = f'http://app:8000/api/v1/currency?user_id={user_id}'
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None


async def get_history(user_id):
    async with aiohttp.ClientSession() as session:
        url = f'http://app:8000/api/v1/history?user_id={user_id}'
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None


async def subscription(user_id, is_subscribed):
    async with aiohttp.ClientSession() as session:
        data = {
            "is_subscribed": is_subscribed
        }
        url = f'http://app:8000/api/v1/subscribe/{user_id}/'
        async with session.patch(url, data=data) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None
