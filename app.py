from flask import Flask
from server.auth import auth_api
from server.team import team_api
from server.individual import individual_api
from server.config import DEBUG

app = Flask(__name__, static_url_path='', static_folder='server/build')
app.register_blueprint(auth_api, url_prefix='/auth')
app.register_blueprint(team_api, url_prefix='/team')
app.register_blueprint(individual_api, url_prefix='/individual')

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=DEBUG)