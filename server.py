from flask import Flask, request, jsonify
import openai
import os
import os
openai.api_key = os.environ["OPENAI_API_KEY"]


app = Flask(__name__)

# ตั้งค่าคีย์ OpenAI (ใส่ตรงนี้หรือใช้ Environment Variable ก็ได้)
openai.api_key = os.environ.get("OPENAI_API_KEY", "ใส่คีย์ของคุณที่นี่")

@app.route("/")
def home():
    return "✅ MCP Server + OpenAI is ready!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_prompt = data.get("prompt", "")

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # หรือ gpt-4 ถ้าคุณมีสิทธิ์ใช้งาน
            messages=[{"role": "user", "content": user_prompt}]
        )
        answer = response.choices[0].message["content"]
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
