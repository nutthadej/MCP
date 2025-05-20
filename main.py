from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Prompt to GPT</title></head>
<body>
    <h1>🚀 ส่ง Prompt ไปยัง GPT</h1>
    <form method="post">
        <textarea name="prompt" rows="4" cols="50">{{ prompt }}</textarea><br>
        <button type="submit">ส่ง</button>
    </form>
    {% if reply %}
    <h3>✉️ ตอบกลับ:</h3>
    <pre>{{ reply }}</pre>
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
                reply = f"❌ Error: {str(e)}"
    return render_template_string(HTML_FORM, prompt=prompt, reply=reply)
