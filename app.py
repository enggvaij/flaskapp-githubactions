from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello , This project is to Automate Flask App Deployment -AWS "


if __name__ == '' :
    app.run(host='0.0.0.0' , port =5000)
