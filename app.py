from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("user_input")
    
    # Dummy response — you can connect to IBM model here later
    reply = f"Great choice! {user_input} is a wonderful destination to explore."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
