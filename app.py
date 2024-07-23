from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def fetch_db():
    connection = sqlite3.connect(r"data\recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table'")
    all_tables = cursor.fetchall()
    idx = random.randint(0, len(all_tables))-1
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM "+ table_name+ ";")
    table_records = cursor.fetchall()
    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " "+ char for char in title])
    print(title)
    ingredients = []
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty+" "+ unit + " of "+ name)
    return title, ingredients

@app.route("/recipe")
def greet():
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)
    return render_template("recipe.html", title=title, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)