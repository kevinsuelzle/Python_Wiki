from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer   , primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Item {self.name}>'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/item', methods=['POST'])
def add_item():
    data = request.get_json()
    existing_item = Item.query.filter_by(name=data['name']).first()

    if existing_item:
        existing_item.quantity += data['quantity']
        existing_item.updated = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': f'Quantity of existing item "{existing_item.name}" updated to {existing_item.quantity}.'}), 200
    else:
        new_item = Item(name=data['name'], quantity=data['quantity'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': f'Item "{new_item.name}" added with ID {new_item.id}'}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    item_data = [{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'last_updated': item.updated.strftime("%Y-%m-%d %H:%M:%S")} for item in items]
    return jsonify(item_data), 200

@app.route('/item/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data['name']
    item.quantity = data['quantity']
    item.updated = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': f'Item with ID {id} updated.'}), 200

@app.route('/item/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Item with ID {id} deleted.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
