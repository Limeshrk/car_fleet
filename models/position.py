from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import db, BaseModel
from models.mixin_model import MixinModel

class PositionModel(BaseModel, MixinModel):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float(precision=5))
    longitude = Column(Float(precision=5))
    date = Column(DateTime)

    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('CarModel')