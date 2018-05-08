from sqlwrapper import gensql
from flask import Flask,request, jsonify
def AMAZON_RESERVATION_LAMBDA_LEX(request):
    d = request.json
    sql_value = gensql('insert','amazonlex.reservation',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
