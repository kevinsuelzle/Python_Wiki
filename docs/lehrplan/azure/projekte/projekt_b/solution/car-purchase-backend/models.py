import enum
from config import db, ma
from marshmallow import fields


class GearEnum(enum.Enum):
    manual = 'manual'
    automatic = 'automatic'


class TypeEnum(enum.Enum):
    diesel = 'diesel'
    petrol = 'petrol'


# Database model for cars table
class CarModel(db.Model):
    __tablename__ = "car_models"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(255))
    price = db.Column(db.Double())

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image


# Database model for car-gears table
class CarGear(db.Model):
    __tablename__ = "car_gears"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    price = db.Column(db.Double())

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Database model for car-types table
class CarType(db.Model):
    __tablename__ = "car_types"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    price = db.Column(db.Double())

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Database model for orders table
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    total_price = db.Column(db.Double())
    car_model_id = db.Column(db.Integer(), db.ForeignKey(CarModel.id), primary_key=True)
    car_model = db.relationship('CarModel', foreign_keys='Order.car_model_id')
    car_gear_id = db.Column(db.Integer(), db.ForeignKey(CarGear.id), primary_key=True)
    car_gear = db.relationship('CarGear', foreign_keys='Order.car_gear_id')
    car_type_id = db.Column(db.Integer(), db.ForeignKey(CarType.id), primary_key=True)
    car_type = db.relationship('CarType', foreign_keys='Order.car_type_id')

    def __init__(self, name, email, phone_number, car_model_id, car_gear_id, car_type_id, total_price):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.car_model_id = car_model_id
        self.car_gear_id = car_gear_id
        self.car_type_id = car_type_id
        self.total_price = total_price


# Marshmallow schema for car config object
class CarConfigSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price')


# Marshmallow schema for car-models object
class CarModelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'image')


# Marshmallow schema for order object
class OrderSchema(ma.Schema):
    car_model = fields.Nested(CarConfigSchema)
    car_gear = fields.Nested(CarConfigSchema)
    car_type = fields.Nested(CarConfigSchema)

    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
            'total_price',
            'car_model',
            'car_gear',
            'car_type'
        )


# Instantiating the schema for single and list of object(by passing a param "many=True")
car_model_schema = CarModelSchema()
cars_model_schema = CarModelSchema(many=True)
cars_config_schema = CarConfigSchema(many=True)
orders_schema = OrderSchema(many=True)
