from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def HOTEL_RES_POST_INSERT_WaitlistReservation(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_waitlist',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
