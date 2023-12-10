from flask import Flask, request, jsonify
from config import db, app
from models import CarModel, CarType, CarGear, cars_config_schema, \
    cars_model_schema, Order, orders_schema, car_model_schema

with app.app_context():
    db.create_all()


# METHOD: POST
# PATH: /orders
# ROLE: Create the order to purchase a car
@app.route('/orders', methods=['Post'])
def create_orders():
    try:
        name = request.json['name']
        email = request.json['email']
        phone_number = request.json['phone_number']
        car_model_id = request.json['car_model_id']
        car_type_id = request.json['car_type_id']
        car_gear_id = request.json['car_gear_id']
        car_model = CarModel.query.get(car_model_id)
        car_type = CarType.query.get(car_type_id)
        car_gear = CarGear.query.get(car_gear_id)
        total_price = car_type.price + car_gear.price + car_model.price
        order = Order(name, email, phone_number, car_model_id, car_gear_id, car_type_id, total_price)
        db.session.add(order)
        db.session.commit()

        return {"success": True}, 201
    except Exception as ex:
        print(ex)
        return {"success": False, "message": "Unable to create order. Something went wrong!"}, 500


# METHOD: GET
# PATH: /car-models
# ROLE: Fetch car models
@app.route('/car-models', methods=['GET'])
def get_car_models():
    models = CarModel.query.all()
    result = cars_model_schema.dump(models)
    return jsonify(result), 200


# METHOD: GET
# PATH: /car-models/:id
# ROLE: Fetch car model by id
@app.route('/car-models/<id>', methods=['GET'])
def get_car_model(id):
    model = CarModel.query.get(id)
    result = car_model_schema.dump(model)
    return jsonify(result), 200


# METHOD: GET
# PATH: /car-types
# ROLE: Fetch car types
@app.route('/car-types', methods=['GET'])
def get_car_types():
    types = CarType.query.all()
    result = cars_config_schema.dump(types)
    return jsonify(result), 200


# METHOD: GET
# PATH: /car-gears
# ROLE: Fetch car gears
@app.route('/car-gears', methods=['GET'])
def get_car_gears():
    gears = CarGear.query.all()
    result = cars_config_schema.dump(gears)
    return jsonify(result), 200


# METHOD: GET
# PATH: /orders
# ROLE: Fetch all the orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = orders_schema.dump(orders)
    return jsonify(result), 200


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to car purchase API'})


if __name__ == "__main__":
    app.run(debug=True)
