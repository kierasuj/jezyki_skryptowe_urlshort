from flask import Blueprint

health_router = Blueprint("health", __name__)

@health_router.route("/health")
def health_check():
    return jsonify({"status": "ok"}), 200