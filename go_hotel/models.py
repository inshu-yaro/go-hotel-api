from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String,DateTime, MetaData, ForeignKey
import datetime

Base = declarative_base()

class Access(Base):
	__tablename__ = 'accesses'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	hotel_number = Column(Integer)
	timestamp = Column(DateTime)
	def __init__(self, user_id, hotel_number, timestamp):
		self.user_id = user_id
		self.hotel_number = hotel_number
		self.timestamp = datetime.now()
	def __repr__(self):
		return "<Access('%s','%s', '%s')>" % (self.user_id, self.hotel_number, self.timestamp)

class Choise(Base):
	__tablename__ = 'choise'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	hotel_number = Column(Integer)
	timestamp = Column(DateTime)
	def __init__(self, user_id, hotel_number, timestamp):
		self.user_id = user_id
		self.hotel_number = hotel_number
		self.timestamp = datetime.now()
	def __repr__(self):
		return "<Access('%s','%s', '%s')>" % (self.user_id, self.hotel_number, self.timestamp)
