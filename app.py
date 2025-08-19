# app.py
from flask import Flask, request, jsonify, send_from_directory
from backend import generate_report, answer_question

app = Flask(__name__, static_folder='.')

# store last report in-memory for the demo (simple approach)
_last_report_cache = {}

@app.route('/')
def index():
    return send_from_directory('.', 'ui.html')

@app.route('/api/astro', methods=['POST'])
def api_astro():
    data = request.get_json() or {}
    name = data.get('name', 'Unknown')
    dob = data.get('dob')    # expected YYYY-MM-DD
    tob = data.get('tob')    # expected HH:MM (optional)
    place = data.get('place', '')
    if not dob or not name:
        return jsonify({"error": "Missing required fields: name and dob (date of birth)."}), 400

    report = generate_report(name, dob, tob, place)
    # store for next question
    _last_report_cache['report'] = report
    _last_report_cache['timestamp'] = __import__('time').time()
    return jsonify(report)

@app.route('/api/question', methods=['POST'])
def api_question():
    data = request.get_json() or {}
    question = data.get('question', '')
    report = _last_report_cache.get('report')
    if not report:
        return jsonify({"error": "No report available. Please request the astrology report first."}), 400
    answer = answer_question(question, report)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    # For development only: python app.py
    app.run(host='0.0.0.0', port=5000, debug=True)
