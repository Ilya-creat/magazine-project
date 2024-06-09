import os

from flask import Flask, render_template, request, jsonify
from models.sql import DataBase

app = Flask(__name__, subdomain_matching=True)
app.config.from_object(__name__)  # load configuration
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'dbase.db')))
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
dbase = DataBase(app.config["DATABASE"])


@app.route('/')
def main():
    result = dbase.get_products_all()
    return render_template('index.html', products=result)


# API
@app.route('/api/search', methods=["POST", "GET"])
def searching():
    rs = request.get_json()
    search = rs['text'].split()
    result = dbase.get_product(*search)
    return jsonify({
        "fragments": render_template("product_fragment.html", products=result)
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
