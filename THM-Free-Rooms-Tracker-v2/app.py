from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
STATE_FILE = "room_state.json"

@app.route('/save', methods=['POST'])
def save_state():
    data = request.get_json()
    total = len(data)
    checked = sum(1 for v in data.values() if v)
    unchecked = total - checked

    # Combine stats and room states in one dict
    output = {
        "stats": {
            "total_rooms": total,
            "checked": checked,
            "unchecked": unchecked
        },
        "rooms": data
    }

    with open(STATE_FILE, 'w') as f:
        json.dump(output, f, indent=4)  # Pretty-print JSON

    return jsonify({"status": "success"})

@app.route('/load', methods=['GET'])
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
        # Return only the "rooms" object for frontend compatibility
        return jsonify(data.get("rooms", {}))
    else:
        return jsonify({})

@app.route('/stats')
def stats():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
        total = len(data)
        checked = sum(1 for v in data.values() if v)
        unchecked = total - checked

        # Build a simple HTML response
        html = f"<h2>Room State Stats</h2>"
        html += f"<p><b>Total rooms:</b> {total}<br>"
        html += f"<b>Checked (true):</b> {checked}<br>"
        html += f"<b>Unchecked (false):</b> {unchecked}</p>"
        html += "<pre>"
        for k, v in data.items():
            html += f"{k}: {v}\n"
        html += "</pre>"
        return html
    else:
        return "<p>No room_state.json found.</p>"

@app.route('/')
def home():
    return render_template('THM-Free-Rooms-Tracker.html')

if __name__ == '__main__':
    app.run(debug=True)