from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
        except ValueError:
            return "Invalid amount entered!"
        category = request.form['category']
        desc = request.form['desc']

        with open("expenses.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, desc])
        return redirect("/")
    return render_template("add.html")

@app.route('/view')
def view():
    expenses = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return render_template("view.html", expenses=expenses)

@app.route("/total")
def total():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[0])
    except:
        pass

    return render_template("total.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)