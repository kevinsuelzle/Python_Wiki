from marshmallow_enum import EnumField
from sqlalchemy import Enum
import enum
from config import db, ma
from marshmallow import fields


# Enum to store the gear type.
# Enum ensures that the database columns can only contain one of the specified values
class GearEnum(enum.Enum):
    manual = 'manual'
    automatic = 'automatic'


# Enum to store the engine type.
class TypeEnum(enum.Enum):
    diesel = 'diesel'
    petrol = 'petrol'


# Database model for cars table
class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(255))
    color = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    type = db.Column(Enum(TypeEnum))
    gear = db.Column(Enum(GearEnum))
    price = db.Column(db.Double())
    stock = db.Column(db.Integer(), default=10)

    def __init__(self, name, image, color, type, gear, brand, price):
        self.name = name
        self.image = image
        self.color = color
        self.type = type
        self.gear = gear
        self.brand = brand
        self.price = price


# Database model for orders table
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    from_date = db.Column(db.DateTime())
    to_date = db.Column(db.DateTime())
    car_id = db.Column(db.Integer(), db.ForeignKey(Car.id), primary_key=True)
    car = db.relationship('Car', foreign_keys='Order.car_id')

    def __init__(self, name, email, phone_number, from_date, to_date, car_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.from_date = from_date
        self.to_date = to_date
        self.car_id = car_id


# Marshmallow schema for car object
class CarSchema(ma.Schema):
    type = EnumField(TypeEnum, by_value=True)
    gear = EnumField(GearEnum, by_value=True)

    class Meta:
        fields = ('id', 'name', 'color', 'image', 'brand', 'price', 'gear', 'type', 'stock')


# Marshmallow schema for order object
class OrderSchema(ma.Schema):
    car = fields.Nested(CarSchema)

    class Meta:
        fields = ('id', 'name', 'email', 'phone_number', 'from_date', 'to_date', 'car')


# Instantiating the schema for single and list of object(by passing a param "many=True")
car_schema = CarSchema()
cars_schema = CarSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
