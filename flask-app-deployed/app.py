from flask import Flask, render_template, json
import mysql.connector
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# DB fails
def load_fake_data():
    with open("fake_data.json", "r") as f:
        return json.load(f)

# ***************************************

# Main Page
@app.route("/")
def index():
    return render_template('index.html')

# Graph Page
@app.route("/stats")
def stats():
    return render_template('graph.html')

# ***************************************

# API route for sending bin details
@app.route("/api/getBinDetails")
def BinDetails():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM RawData2 ORDER BY id DESC LIMIT 1')
        myresult = mycursor.fetchall()
        res = myresult[0]
        r1, r2, r3 = res[1], res[2], res[3]
        finalres = {'capacity1': r1, 'capacity2': r2, 'capacity3': r3}
    except Exception as e:
        print(f"DB error: {e}. Loading fake data.")
        finalres = load_fake_data()['latest']
    response = app.response_class(response=json.dumps(finalres), status=200, mimetype='application/json')
    return response

# API route for sending graph details
@app.route("/api/getGraphDetails")
def GraphDetails():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM (SELECT * FROM RawData2 ORDER BY id DESC LIMIT 10) var1 ORDER BY id')
        myresult = mycursor.fetchall()
        finalres = {'data': myresult}
    except Exception as e:
        print(f"DB error: {e}. Loading fake data.")
        finalres = load_fake_data()['graph']
    response = app.response_class(response=json.dumps(finalres), status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
