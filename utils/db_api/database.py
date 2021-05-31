from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String, Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql

from data.config import db_pass, db_user, host

db = Gino()


class Bucket(db.Model):
    __tablename__ = 'bucket'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(100))

    soup = Column(Integer, default=0)
    salad = Column(Integer, default=0)
    salad_price = Column(Integer, default=0)
    soup_price = Column(Integer, default=0)
    sum_price = Column(Integer, default=0)


class Purchase(db.Model):
    __tablename__ = 'purchases'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    soup = Column(Integer, default=0)
    salad = Column(Integer, default=0)
    salad_price = Column(Integer, default=0)
    soup_price = Column(Integer, default=0)
    sum_price = Column(Integer, default=0)
    email = Column(String(200))


class DBCommands:

    async def get_user(self, user_id, username=None):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()

        if user is None:
            await self.add_new_user(user_id, username)

        return user

    async def add_new_user(user_id, username):
        await Bucket.create(user_id=user_id, username=username)
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        return user

    async def add_salad(self, user_id, quantity: int, price: int):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        count = user.salad
        salad_price = user.salad_price

        await Bucket.update.values(salad=int(count) + int(quantity), salad_price=int(salad_price) + int(price)).where(
            Bucket.user_id == user_id).gino.status()

    async def add_soup(self, user_id, quantity: int, price: int):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        count = user.soup
        soup_price = user.soup_price

        await Bucket.update.values(soup=int(count) + int(quantity),
                                   soup_price=int(soup_price) + int(price)).where(
            Bucket.user_id == user_id).gino.status()

    async def bucket_sum_get(self, user_id):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        sum = user.salad_price + user.soup_price
        await Bucket.update.values(sum_price=sum).where(
            Bucket.user_id == user_id).gino.status()
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        return user.sum_price

    async def clean_bucket(self, user_id):
        await Bucket.update.values(soup=0, salad=0, salad_price=0, soup_price=0).where(
            Bucket.user_id == user_id).gino.status()

    async def create_new_purchase(self, username, soup, salad, salad_price, soup_price, sum_price, email=None):
        user = await Purchase.create(username=username, soup=soup, salad=salad,
                                     salad_price=salad_price, soup_price=soup_price, sum_price=sum_price, email=email)



async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/gino')
    # Create tables
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    await db.gino.create_all()
