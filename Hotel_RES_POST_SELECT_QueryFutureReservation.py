from sqlwrapper import dbget
import json
from datetime import datetime, timedelta
from flask import Flask,request, jsonify
app = Flask(__name__)
#@app.route("/ProfileFutureReservationRecord",methods=['POST'])
def ProfileFutureReservation(request):
    #N = 365
    current_date = datetime.utcnow().date()
    current_date = str(current_date)
    print(current_date)
    #date_N_days_ago = current_date + timedelta(days=1)
    #date_N_days_ago = date_N_days_ago.date()

    #date_N_days_ago = str(date_N_days_ago)
    #print (date_N_days_ago)
    pf_firstname = request.json['pf_firstname']
    pf_mobileno = request.json['pf_mobileno']
    sql_value = "select * from reservation.res_reservation where pf_firstname = '"+pf_firstname+"' and pf_mobileno = '"+pf_mobileno+"' and res_arrival >  '"+current_date+"' order by res_arrival desc"
    result = dbget(sql_value)
    #sql_value = gensql('select','reservation.res_reservation','*' 'ORDER BY res_arrival DESC')
    result = json.loads(result)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
