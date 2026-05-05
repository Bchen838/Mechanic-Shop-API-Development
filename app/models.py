from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date
from typing import List

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

service_mechanics = db.Table(
    'service_mechanic',
    Base.metadata,
    db.Column('service_ticket_id', db.ForeignKey('service_tickets.id'), primary_key=True),
    db.Column('mechanic_id', db.ForeignKey('mechanics.id'), primary_key=True)
)


class Customer(Base): 
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    number: Mapped[str] = mapped_column(db.String(20), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)

    service_tickets: Mapped[List['Service_Ticket']] = db.relationship(back_populates='customer')


class Service_Ticket(Base):
    __tablename__ = 'service_tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    vin: Mapped[str] = mapped_column(db.String(17), nullable=False)
    service_desc: Mapped[str] = mapped_column(db.String(500), nullable=False)
    service_date: Mapped[date] = mapped_column(db.Date, nullable=False)

    customer: Mapped['Customer'] = db.relationship(back_populates='service_tickets')
    mechanics: Mapped[List['Mechanic']] = db.relationship(secondary=service_mechanics, back_populates='service_tickets')

class Mechanic(Base):
    __tablename__ = 'mechanics'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    salary: Mapped[float] = mapped_column(db.Float, nullable=False)

    service_tickets: Mapped[List['Service_Ticket']] = db.relationship(secondary=service_mechanics, back_populates='mechanics')