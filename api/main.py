from src.app import create_app

if __name__ == "__main__":
    db_uri = (
        "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
        "@clusterlms.k10xd.mongodb.net/lms"
    )
    app = create_app(db_uri)
    app.run(host="0.0.0.0", port=5000, debug=True)
