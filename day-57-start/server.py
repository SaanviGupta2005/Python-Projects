from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    now = dt.datetime.now()
    current_year = now.year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<path:name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = response.json()
    gender = gender_data["gender"]
    responses = requests.get(f"https://api.agify.io?name={name}")
    age_data = responses.json()
    age = age_data["age"]
    return render_template("index1.html",name=name, gen=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


