from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/learning_platform_db"
mongo = PyMongo(app)

@app.route('/')
def home():
    return "MongoDB Connected!"

if __name__ == '__main__':
    app.run(debug=True)
