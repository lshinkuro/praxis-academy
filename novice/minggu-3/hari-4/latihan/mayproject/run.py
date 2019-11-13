
from flask import Flask,render_template,Response,json,request
import mysql.connector  as mariadb

app= Flask(__name__)


mariadb_connection = mariadb.connect(
    user='root',
    password='123456',
    database='testdb')
cursor = mariadb_connection.cursor()
cursor.execute("SELECT name ,age,address FROM CUSTOMERS ;")
cursor.execute("INSERT INTO CUSTOMERS VALUES (7, 'Muffy', 24, 'Indore', 10000.00 );")




@app.route('/',methods=['GET'])
def hello():
 

    aDict = []
    for (name,age,address) in cursor:
        dicts = {'name':name,'ages':age,'address':address}
        aDict.append(dicts)

    
    return Response(response=json.dumps(aDict),mimetype='application/json')

@app.route('/hello/',methods=['POST'])
def bebas():
    req =request.get_json()
    print(req)


    return req

if __name__=="__main__":
    app.run(debug=True)


