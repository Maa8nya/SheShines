from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ✅ Configure database BEFORE importing models
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_password@localhost/Experts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # ✅ Define db here

from app.startup_ideas.routes import startup_ideas_bp
from app.networking.routes import networking_bp
from app.skillswap.routes import skillswap_bp
from app.chatbot.routes import chatbot_bp
from app.expert_routes import expert_bp  

# ✅ Register Blueprints AFTER db is set
app.register_blueprint(startup_ideas_bp, url_prefix="/startup-ideas")
app.register_blueprint(networking_bp, url_prefix="/networking")
app.register_blueprint(skillswap_bp, url_prefix="/api/skill-swap")
app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
app.register_blueprint(expert_bp)

@app.route("/")
def home():
    return "Welcome to SheShines Backend!"
