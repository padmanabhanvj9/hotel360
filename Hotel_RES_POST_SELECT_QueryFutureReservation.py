from sqlwrapper import dbget
import json
from flask import Flask,request, jsonify
from ApplicationDate import application_date


def ProfileFutureReservation(request):
    #N = 365
    app_datetime = application_date()
    current_date = app_datetime[1]
    print(current_date)

    pf_firstname = request.json['pf_firstname']
    pf_mobileno = request.json['pf_mobileno']
    sql_value = "select * from reservation.res_reservation where \
                 pf_firstname = '"+pf_firstname+"' and pf_mobileno = '"+pf_mobileno+"' \
                 and res_arrival >  '"+current_date+"' order by res_arrival desc"
    
    result = dbget(sql_value)

    result = json.loads(result)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
