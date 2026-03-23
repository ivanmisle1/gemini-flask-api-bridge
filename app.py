from flask import Flask
from config import Config
from routes.gemini import askGemini_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(askGemini_bp)