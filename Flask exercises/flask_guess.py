from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/guess_rev", methods=['GET', 'POST'])

def rev_guess():
    if request.method == 'GET':
        return render_template("guess_flask.html", guess = 500, min = 0, max = 1000)
    else:
        max = int(request.form.get('max'))
        min = int(request.form.get('min'))
        guess = int((max - min) / 2) + min
        if request.form.get('answer') == 'low':
            min = guess
            guess = int((max - min) / 2) + min
            return render_template("guess_flask.html", guess = guess, min = min, max = max)
        elif request.form.get('answer') == 'high':
            max = guess
            guess = int((max - min) / 2) + min
            return render_template("guess_flask.html", guess = guess, min = min, max = max)
        elif request.form.get('answer') == 'hit':
            result = "I am mighty. I've guessed again!"
            return render_template("guess_flask.html", result = result)


if __name__ == "__main__":
    app.run(debug=True)


