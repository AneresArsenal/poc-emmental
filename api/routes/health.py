from flask import current_app as app, jsonify

from repository.health import check_health


@app.route('/health', methods=['GET'])
def get_health():
    health = check_health()
    return_code = 200 if health['working'] else 500
    return jsonify(health), return_code
