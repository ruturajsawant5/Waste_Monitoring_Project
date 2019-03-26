from flask import Flask,render_template,json
import mysql.connector
app = Flask(__name__)

#cache thingy
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# ***************************************

# MainPage
@app.route("/")
def index():
	return render_template('index.html')

# graph page
@app.route("/stats")
def stats():
	return render_template('graph.html')


# **************************************

#api route for sending bindetails
@app.route("/api/getBinDetails")
def BinDetails():
	mydb = mysql.connector.connect(host="wastemgmt.cwzqmidbioqe.ap-south-1.rds.amazonaws.com",user="root",passwd="target123",database="wasteCollection")
	mycursor = mydb.cursor()

	mycursor.execute('SELECT * FROM RawData2 ORDER BY id DESC LIMIT 1')

	myresult = mycursor.fetchall()
	res = myresult[0];
	r1=res[1]
	r2=res[2]
	r3=res[3]

	finalres={'capacity1':r1,'capacity2':r2,'capacity3':r3}
	# return jsonify(finalres)
	response = app.response_class(response=json.dumps(finalres),status=200,mimetype='application/json')
	return response

#api route for sending graph details
@app.route("/api/getGraphDetails")
def GraphDetails():
	mydb = mysql.connector.connect(host="wastemgmt.cwzqmidbioqe.ap-south-1.rds.amazonaws.com",user="root",passwd="target123",database="wasteCollection")
	mycursor = mydb.cursor()

	mycursor.execute('SELECT * FROM (SELECT * FROM RawData2 ORDER BY id DESC LIMIT 10)var1 ORDER BY ID')

	myresult = mycursor.fetchall()
	print(myresult)

	finalres={'data':myresult}	
	# finalres={[{'capacity1':myresult[0][1],'capacity2':myresult[0][2],'capacity3':myresult[0][3],'dateData1':myresult[0][4]},{}]}
	# return jsonify(finalres)
	response = app.response_class(response=json.dumps(finalres),status=200,mimetype='application/json')
	return response


if __name__=='__main__':
	#app.run(debug=True)
	app.run()
