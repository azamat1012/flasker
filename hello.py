from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route("/")
def index():
    f_name = "Tom"
    stuff = "This is a Bold Text"

    favorite_pizza = ['Pepperoni', 'Cheese', 41]
    return render_template("index.html", first_name=f_name, stuff=stuff, favorite_pizza=favorite_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 400


# Internal Sever Error
@app.errorhandler(500)
def interal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
