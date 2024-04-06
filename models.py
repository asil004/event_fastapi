from sqlalchemy import Column, Integer, ForeignKey, String, Date, Time
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    email = Column(String)
    password = Column(String)


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    image = Column(String)
    name = Column(String)


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    image = Column(String)
    name = Column(String)
    event = Column(Integer, ForeignKey("events.id"))


class EventDetail(Base):
    __tablename__ = "event_detail"

    id = Column(Integer, primary_key=True)
    address = Column(String)
    date = Column(Date)
    time = Column(Time)
    phone_number = Column(String)


class UsersEvents(Base):
    __tablename__ = "users_events"

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    event = Column(Integer, ForeignKey('events.id'))
    item = Column(Integer, ForeignKey('items.id'))
    event_detail = Column(Integer, ForeignKey('event_detail.id'))
