from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    from datetime import datetime
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
        except ValueError:
            return "Invalid amount entered!"

        category = request.form['category']
        desc = request.form['desc']
        date = request.form['date']
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        with open("expenses.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, desc, date])
        return redirect("/")
    return render_template("add.html")

@app.route('/view')
def view():
    expenses = []
    query = request.args.get("q")

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):

                if query:
                    if query.lower() in row[1].lower() or query.lower() in row[2].lower() or query in row[0] or query in row[3]:
                        expenses.append((i, row))
                else:
                    expenses.append((i, row))
    except:
        pass
    return render_template("view.html", expenses=expenses, query=query)

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

@app.route("/summary")
def summary():
    summary_data = {}
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[0])

                if category in summary_data:
                    summary_data[category] += amount
                else:
                    summary_data[category] = amount
    except:
        pass
    return render_template("summary.html", summary = summary_data)
@app.route("/delete/<int:index>")
def delete(index):
    expenses = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

        #remove selected expense
        if 0 <= index < len(expenses):
            expenses.pop(index)

        #rewrite file
        with open("expenses.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
    except:
        pass
    return redirect("/view")

@app.route("/edit/<int:index>", methods = ["GET", "POST"])
def edit(index):
    expenses = []
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
    except:
        pass

    if request.method == "POST":
        amount = request.form['amount']
        category = request.form['category']
        desc = request.form['desc']

        expenses[index] = [amount, category, desc]

        with open("expenses.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        return redirect("/view")

    expense = expenses[index]
    return render_template("edit.html", expense = expense, index = index)

@app.route("/monthly")
def monthly():
    totals = {}

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[0])
                date = row[3]
                month = date[:7]

                if month in totals:
                    totals[month] += amount
                else:
                    totals[month] = amount
    except:
        pass

    return render_template("monthly.html", totals = totals)

if __name__ == "__main__":
    app.run()