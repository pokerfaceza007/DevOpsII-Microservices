from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = us.car_name()
    data = [x for x in _user if x["name"]==name]

    if data:
        us.update_car(name,category,price,instock)
        return jsonify({'message': 'Update Successfully'}), 200
    else:
        return jsonify({'message': 'Fail to update.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)