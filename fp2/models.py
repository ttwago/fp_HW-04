from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    email = Column(String, primary_key=True)
    fam = Column(String)
    otc = Column(String)
    name = Column(String)
    phone = Column(String)
    perevals = relationship('Pereval', back_populates='user')


class Coords(Base):
    __tablename__ = 'coords'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)
    pereval = relationship('Pereval', back_populates='coords')


class Level(Base):
    __tablename__ = 'level'

    id = Column(Integer, primary_key=True)
    winter = Column(String)
    summer = Column(String)
    autumn = Column(String)
    spring = Column(String)
    pereval_id = Column(Integer, ForeignKey('pereval.id'))
    pereval = relationship('Pereval', back_populates='level')


class Pereval(Base):
    __tablename__ = 'pereval'

    STATUS_CHOICES = [
        'new',
        'pending',
        'accepted',
        'rejected',
    ]

    id = Column(Integer, primary_key=True)
    beautyTitle = Column(String)
    title = Column(String)
    other_titles = Column(String)
    connect = Column(String)
    add_time = Column(DateTime)
    coord_id = Column(Integer, ForeignKey('coords.id'))
    coords = relationship('Coords')
    status = Column(Enum(*STATUS_CHOICES, name='status_enum'), default='new')
    user_email = Column(String, ForeignKey('users.email'))
    user = relationship('User', back_populates='pereval')
    images = relationship('PerevalImages', back_populates='pereval')
    level = relationship('Level', back_populates='pereval')


class PerevalImages(Base):
    __tablename__ = 'pereval_images'

    id = Column(Integer, primary_key=True)
    image_name = Column(String)
    title = Column(String)
    pereval_id = Column(Integer, ForeignKey('pereval.id'))
    pereval = relationship('Pereval', back_populates='images')