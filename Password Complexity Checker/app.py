from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("At least 8 characters.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include numbers.")

    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        feedback.append("Use special characters.")

    if strength == 5:
        rating = "Strong 💪"
    elif 3 <= strength < 5:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    return rating, feedback

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result, suggestions = check_password_strength(password)
    return jsonify({"result": result, "suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
