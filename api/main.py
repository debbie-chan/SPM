from flask import render_template
from .src.app import create_app

db_uri = (
    "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK@clusterlms.k10xd.mongodb.net/lms"
)
app = create_app(db_uri)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
