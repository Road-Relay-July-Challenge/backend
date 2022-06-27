from flask import Flask
from auth import auth_api

app = Flask(__name__)
app.register_blueprint(auth_api, url_prefix='/auth')

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
        app.run()