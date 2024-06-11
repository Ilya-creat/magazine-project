import ast
import os
import uuid

from flask import Flask, redirect, render_template, request, jsonify, url_for

from models.payment import Payment
from models.smtp import SMTP
from models.sql import DataBase
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__, subdomain_matching=True)
app.config.from_object(__name__)  # load configuration
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'dbase.db')))
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
dbase = DataBase(app.config["DATABASE"])


@app.route('/')
def main():
    result = dbase.get_products_all()
    return render_template('index.html', products=result)


@app.route("/payment/merchant")
def pay():
    return render_template('success.html')


@app.route('/redirect', methods=["POST"])
def redirect():
    w = request.args
    if "page" in w.keys():
        if "payment" in w.get("page"):
            res = request.get_json()
            # print(res)
            uuid_ = uuid.uuid4().hex
            pay = Payment(uuid_, res["user"], res["number"], res["address"], res["order"], dbase)
            rs = []
            sm = 0
            for i in res["order"]:
                i = ast.literal_eval(i)
                rs.append({
                    "name": i["products"]["name"],
                    "count": i["products"]["count"],
                    "price": i["products"]["price"]
                })
            sm += float(i["products"]["price"]) * int(i["products"]["count"])
            # ... merchent create
            check = True
            if check:
                SMTP(res["email"]).send_emai(uuid_, rs, sm)
                return jsonify({
                    "url": "/payment/merchant"
                })
    return ""


# API
@app.route('/api/search', methods=["POST", "GET"])
def searching():
    rs = request.get_json()
    if rs['text']:
        search = rs['text'].split()

        result = dbase.get_products_all()
        res = [{"id": str(i.id),
                "bool": False} for i in result]
        result = dbase.get_product(*search)
        for j in result:
            for i in range(len(res)):
                if str(j.id) == res[i]["id"]:
                    res[i]["bool"] = True
        return jsonify({
            "products": res
        })
    else:
        result = dbase.get_products_all()
        res = [{"id": str(i.id),
                "bool": True} for i in result]
        return jsonify({
            "products": res
        })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
