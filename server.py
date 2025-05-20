from flask import Flask, request, jsonify, render_template_string
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

# HTML หน้าแรก (เขียนตรงในโค้ดเลยก็ได้)
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>🧠 AI Prompt Generator</title>
</head>
<body style="font-family: sans-serif; margin: 50px;">
    <h1>🚀 ส่ง Prompt ไปหา GPT</h1>
    <form method="POST">
        <label for="prompt">Prompt:</label><br>
        <textarea name="prompt" rows="4" cols="50" required>{{ prompt }}</textarea><br><br>
        <button type="submit">ส่งหา GPT</button>
    </form>

    {% if reply %}
    <h3>✉️ ตอบกลับ:</h3>
    <div style="border:1px solid #ccc; padding:10px; max-width:500px;">
        {{ reply }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prompt = ""
    reply = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                reply = response.choices[0].message["content"]
            except Exception as e:
                reply = f"เกิดข้อผิดพลาด: {str(e)}"

    return render_template_string(HTML_FORM, prompt=prompt, reply=reply)
