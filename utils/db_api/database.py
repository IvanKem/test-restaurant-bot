from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql

from data.config import db_pass, db_user, host

db = Gino()


class Bucket(db.Model):
    __tablename__ = 'bucket'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    full_name = Column(String(100))
    soup = Column(Integer, default=0)
    salad = Column(Integer, default=0)
    salad_price = Column(Integer, default=0)
    soup_price = Column(Integer, default=0)
    sum_price = Column(Integer, default=0)

class Purchase(db.Model):
    __tablename__ = 'purchases'
    query: sql.Select

    user_id = Column(BigInteger, primary_key=True)
    full_name = Column(String(100))
    soup = Column(Integer, default=0)
    salad = Column(Integer, default=0)
    sum_price = Column(Integer, default=0)
    email = Column(String(200))


class DBCommands:

    async def get_user(self, user_id, full_name):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()

        if user is None:
            await self.add_new_user(user_id, full_name)
            user = {user_id: user_id, full_name: full_name}
            return user

        return user


    async def add_new_user(user_id, full_name):
        user = await Bucket.create(user_id=user_id, full_name=full_name)


    async def add_salad(self, user_id, price):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        count = user.salad
        salad_price = user.salad_price

        await Bucket.update.values(soup=count + 1, salade_price=salad_price + price).where(
            Bucket.user_id == user_id).gino.status()


    async def add_soup(self, user_id, price):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        count = user.soup
        soup_price = user.soup_price

        await Bucket.update.values(soup=count + 1, soup_price=soup_price+price).where(
            Bucket.user_id == user_id).gino.status()


    async def bucket_sum_get(self, user_id):
        user = await Bucket.query.where(Bucket.user_id == user_id).gino.first()
        sum_price = user.sum_salad_price + user.sum_soup_price
        await Bucket.update.values(sum_price=sum_price).where(
            Bucket.user_id == user_id).gino.status()

        return sum_price, user.salad, user.salad_price, user.soup. user.soup_price



    async def create_new_purchase(self,  user_id, full_name, soup , salad ,sum_price ,email):
        user = await Purchase.create(user_id=user_id, full_name=full_name, soup=soup,salad=salad,
                                   sum_price=sum_price, email=email)
        return user


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/gino')
    # Create tables
    db.gino: GinoSchemaVisitor

    await db.gino.create_all()

