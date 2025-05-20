from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>AI Prompt Generator</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f2f2f2;
            padding: 40px;
            color: #333;
        }
        h1 {
            color: #222;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            max-width: 600px;
            margin-bottom: 30px;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: vertical;
        }
        button {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #2d89ef;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .reply {
            background: #fff;
            padding: 20px;
            border-left: 5px solid #2d89ef;
            border-radius: 10px;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <h1>🚀 AI Prompt Generator</h1>
    <form method="post">
        <label for="prompt">ใส่ข้อความเพื่อถาม GPT:</label><br><br>
        <textarea name="prompt" required>{{ prompt }}</textarea><br>
        <button type="submit">ส่งข้อความ</button>
    </form>

    {% if reply %}
    <div class="reply">
        <strong>✉️ คำตอบจาก GPT:</strong><br><br>
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
                reply = f"❌ เกิดข้อผิดพลาด: {str(e)}"
    return render_template_string(HTML_TEMPLATE, prompt=prompt, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
