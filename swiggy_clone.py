from flask import Flask, jsonify

app = Flask(__name__)

restaurants = [
    {"id": 1, "name": "Burger King", "cuisine": "Fast Food"},
    {"id": 2, "name": "Pizza Hut", "cuisine": "Italian"}
]

menu_items = {
    1: [
        {"item": "Whopper", "price": 199},
        {"item": "Fries", "price": 99},
    ],
    2: [
        {"item": "Veg Pizza", "price": 299},
        {"item": "Garlic Bread", "price": 149},
    ]
}

@app.route("/")
def home():
    return "Swiggy Clone Backend Running!"

@app.route("/restaurants")
def get_restaurants():
    return jsonify(restaurants)

@app.route("/menu/<int:restaurant_id>")
def get_menu(restaurant_id):
    return jsonify(menu_items.get(restaurant_id, []))

@app.route("/order")
def place_order():
    return {"message": "Order placed successfully!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

