from flask import Flask, request, jsonify
import openai  # atau langsung konekin ke gue nanti

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Simulasi respon AI (Nanti bisa konek ke ChatGPT atau AI lo sendiri)
    response = {"reply": f"Gue denger lo bilang: {user_message}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
