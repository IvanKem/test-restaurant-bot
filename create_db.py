from utils.db_api.database import create_db

import aiogram
import asyncio
async def main():

    await create_db()

asyncio.run(main())