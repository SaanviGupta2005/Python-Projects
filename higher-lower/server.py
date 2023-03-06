import random

from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/")
def heading():
    return "<h1>Guess a number between 1 and 9</h1>" \
           '<img src = "https://media0.giphy.com/media/abHQ4aDqRqlyBTdAP0/giphy.gif?cid=ecf05e47uji511dye4ztd8ccbg5c39yb6vxnr7sqs8wzy93g&rid=giphy.gif&ct=g">'


random_number = random.randint(1, 9)
print(random_number)


@app.route("/<int:numberenter>")
def checking(numberenter):
    if numberenter == random_number:
        return '<h1 style = "color:green">You found me!</h1>' \
               '<img src="https://media4.giphy.com/media/JKcneNkriqxQbE8e49/giphy.gif?cid=ecf05e47g7ss3vrj4rxt8rtu055sxw0f44qjndqf09dp3b4p&rid=giphy.gif&ct=g" width=200, height=200>'
    elif numberenter > random_number:
        return '<h1 style = "color:red">Too High, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/7fXKHv8m86H5e/giphy.gif?cid=ecf05e47ligw8cm4do15lvmt6fcvuir90hjxvmmda1egz31t&rid=giphy.gif&ct=g" width=200, height=200>'
    elif numberenter < random_number:
        return '<h1 style = "color:blue">Too Low, try again!</h1>' \
               '<img src="https://media0.giphy.com/media/3ohhwGIssJMuuEUqxq/giphy.gif?cid=ecf05e47ls8w9s4tr7l0c406pucijginev4vc3yfmn9al9a7&rid=giphy.gif&ct=g" width=200, height=200>'


if __name__ == "__main__":
    app.run(debug=True)
