import requests #update requirements.txt
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from db import db, BaseModel
from models.mixin_model import MixinModel

class PositionModel(BaseModel, MixinModel):
  __tablename__ = 'positions'
  id = Column(Integer, primary_key=True)
  latitude = Column(Float(precision=5))
  longitude = Column(Float(precision=5))
  date = Column(DateTime)
  address = Column(String(300))
  car_id = Column(Integer, ForeignKey('cars.id'))
  car = relationship('CarModel')
  
  def json(self):
    return {
      'latitude': self.latitude,
      'longitude': self.longitude,
      'date': self.date.isoformat(),
      'address': self.address
    }
    
  def resolve_address(self):
    try:
      response = requests.get(
        'https://nominatim.openstreetmap.org/reverse',
        params={
          'format': 'json',
          'lat': self.latitude,
          'lon': self.longitude,
        },
      )
      response.raise_for_status()  # raises exception for 4xx and 5xx HTTP status codes
      data = response.json()
      self.address = data.get('display_name', '')
      
    except Exception as e:
      print("Error during the request:", str(e))
      self.address = ''