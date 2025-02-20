from flask import Blueprint, request, jsonify
from app import db
from app.models import Expert

expert_bp = Blueprint("experts", __name__)

@expert_bp.route("/api/experts", methods=["POST"])
def add_expert():
    """Store expert data from frontend to the database."""
    data = request.json
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    try:
        expert = Expert(
            name=data["name"],
            profession=data["profession"],
            qualification=data["qualification"],
            experience=int(data["experience"]),
            package_range=data["package_range"],
            work_environment=data["work_environment"],
            market_status=data["market_status"],
            reviews=data["reviews"]
        )
        db.session.add(expert)
        db.session.commit()

        return jsonify({"message": "Expert registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
