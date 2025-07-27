from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            code = soup.prettify()
        except Exception as e:
            code = f"⚠️ Error: {e}"
    return render_template("index.html", code=code)

if __name__ == "__main__":
    app.run(debug=True)
