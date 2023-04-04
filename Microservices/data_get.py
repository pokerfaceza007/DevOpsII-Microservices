from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

@app.route('/car', methods=['GET'])
def item():
    _car = us.car_name()
    return jsonify(_car)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1