from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():

    body = "Product 1"
    icon = "a long url"

    return render_template(
        "index.html",
        body_from_python=body,
        icon_from_python=icon
    )

if __name__ == "__main__":
    app.run(debug=True)