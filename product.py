import hashlib
import base58
import bip39
from mnemonic import Mnemonic
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.PublicKey import ECC
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
try:
    uri = "mongodb+srv://thuccua2004:VB39hefIin7Riwx8@cluster0.28nrq.mongodb.net/"
    client = MongoClient(uri)
    db_product = client["JackWallet"]['products']
    print("Kết nối MongoDB thành công!")
except Exception as e:
    print(f"Kết nối MongoDB thất bại: {e}")
@app.route('/insert_product', methods=['POST'])
def Insert_product():
    data_product = request.get_json()
    name_product = data_product.get('name_product')
    image_product = data_product.get('image_product')
    price_product = data_product.get('price_product')
    product_desc = data_product.get('product_desc')
    try:
        product = {
            "name_product": name_product,
            "image_product": image_product,
            "price_product": price_product,
            "product_desc": product_desc,
        }
        inser_pro =  db_product.insert_one(product)
        if(inser_pro):
             return jsonify({
                'Code': 200,
                'messenger': "Inser ok",
            })
    except Exception as e:
        print(f"Lỗi khi thêm dữ liệu vào MongoDB: {e}")
if __name__ == '__main__':
    app.run(debug=True)