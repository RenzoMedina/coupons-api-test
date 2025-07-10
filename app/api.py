from flask import Flask, request, jsonify
from app.coupons import getFinalPrice

app = Flask(__name__)

@app.route("/price", methods=['POST'])
def get_price():
    data = request.get_json()
    price = data.get('price')
    coupon = data.get('coupon')
    tax_rate = data.get('tax_rate',0.19)

    final = getFinalPrice(price, coupon, tax_rate)
    return jsonify({"price_final":final})