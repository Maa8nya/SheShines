# ✨ SheShines - Women's Empowerment Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey.svg)](https://flask.palletsprojects.com/)

A comprehensive web platform designed to empower women entrepreneurs through startup guidance, mentorship connections, and skill-sharing opportunities, powered by an AI chatbot for personalized recommendations.

## 🌟 Key Features

| Feature | Description | Technology |
|---------|------------|------------|
| 💡 **Startup Ideas** | Curated business ideas with implementation guides | Flask, SQLite |
| 👩‍🏫 **Mentorship** | Connect with experienced women mentors | WebSockets |
| 🔄 **Skill Exchange** | Peer-to-peer skill sharing marketplace | JavaScript |
| 🤖 **AI Chatbot** | Personalized suggestions using NLP | Hugging Face Transformers |


## 🛠️ Tech Stack

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Responsive Design (Mobile-first)
- Interactive UI with Animations

**Backend:**
- Python 3.8+
- Flask web framework
- SQLAlchemy ORM

**AI Components:**
- Hugging Face Transformers
- Custom-trained NLP model
- Dialogflow integration

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for frontend dependencies)
- Hugging Face API key

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/SheShines.git
cd SheShines

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your Hugging Face API key in .env
