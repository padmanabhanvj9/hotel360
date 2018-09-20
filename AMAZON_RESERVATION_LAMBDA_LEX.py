from sqlwrapper import gensql
import json
from flask import Flask,request, jsonify
def AMAZON_RESERVATION_LAMBDA_LEX(request):
    d = {}
   # arrivalsdate = request.args.get('arrival')
    #depaturedate = request.args.get('depature')
    arrivalsdate = request.json['arrival']
    depaturedate = request.json['depature']
    d['arrival']  = arrivalsdate
    d['depature']  = depaturedate
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    #reservation = {'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}], sort_keys=True, indent=4))
