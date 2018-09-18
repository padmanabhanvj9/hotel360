from sqlwrapper import gensql
import json
from flask import Flask,request, jsonify
def AMAZON_RESERVATION_LAMBDA_LEX(request):
    d['arrival'] = request.args('arrival')
    d['depature'] = request.args('depature')
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
