from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p> This is a paragraph</p>' \
           '<img src="https://media4.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid=ecf05e4738ai0jtke8tyr547a29gla309zml4v5i9m6gm6ub&rid=giphy.gif&ct=g" width=200 height=200>'

@app.route('/bye')
def say_bye():
    return "Bye"

# @app.route('/<name>/1')
# def greet(name):
    # return f"Hello {name}!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, You are {number} years old."




if __name__ == "__main__":
    app.run(debug=True)

