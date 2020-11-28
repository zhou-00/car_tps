from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey

Base = declarative_base()

class Salesperson(Base): 
    __tablename__ = 'salesperson'

    salesperson_id = Column(Integer, primary_key=True) # primary key
    title = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    work_phone = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    pass


class Customer(Base): 
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    work_phone = Column(String(20), nullable=False, unique=True)
    pass


class Car(Base):
    __tablename__ = 'car'

    car_id = Column(Integer, primary_key=True) # primary key
    make = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    registration = Column(String(6), nullable=False, unique=True)
    manufacture_year = Column(Integer, nullable=False)
    colour = Column(String(255), nullable=False)


class Purchase(Base):
    __tablename__ = 'purchase'

    purchase_id = Column(Integer, primary_key=True) # primary key
    customer_id = Column(Integer, ForeignKey('customer.customer_id')) # foreign key
    salesperson_id = Column(Integer, ForeignKey('salesperson.salesperson_id')) # foreign key
    car_id = Column(Integer, ForeignKey('car.car_id')) # foreign key
    purchase_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)

