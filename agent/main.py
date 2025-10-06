from flask import Flask, jsonify, request
from flask_cors import CORS
from researcher import run_research

app = Flask(__name__)
CORS(app)

@app.route('/api/research', methods=['POST'])
def research():
    """
    Triggers the AI research agent and returns the report.
    """
    # The prompt from the frontend is not used yet, but could be passed to run_research
    # prompt = request.json.get('prompt', '')
    report = run_research(prompt="Find profitable SaaS products")
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True, port=5001)