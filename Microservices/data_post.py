from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

@app.route('/car_add', methods=['POST'])
def register():
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    instock = request.form['instock']

    _user = us.car_name()
    data = [x for x in _user if x["name"]==name]
    if (data):
        return jsonify({'message': 'Cannot create user.'}), 401
    else:
        us.car_name_add(name,category,price,instock)
        return jsonify({'message': 'Name Has Been Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
