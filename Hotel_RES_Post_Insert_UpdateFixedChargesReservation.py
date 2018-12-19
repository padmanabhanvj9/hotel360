from sqlwrapper import gensql,dbget
import datetime
from flask import Flask,request, jsonify
import json
def Hotel_RES_Post_Insert_UpdateFixedChargesReservation(request):

    d = request.json
    print(d)
    e = { k : v for k,v in d.items() if k in ('Res_id')}
    print(e)
    s = ['RES_Arrival','RES_Depature','PF_Firstname','PF_Mobileno','RES_Nights']
    sql_value = gensql('select','reservation.res_reservation',s,e)
    sql_value = json.loads(sql_value)
    print(sql_value,type(sql_value))
    data = sql_value[0]
    arrival = data['res_arrival']
    depature = data['res_depature']
    print(arrival,depature,type(arrival))
    arr_date = datetime.datetime.strptime(arrival, '%Y-%m-%d').date()
    dep_date = datetime.datetime.strptime(depature, '%Y-%m-%d').date()
    print("str1", arr_date,dep_date,type(arr_date))
    data1 = d.get('Fixed_Charges_Begin_Date')
    data2 = d.get('Fixed_Charges_End_Date')
    charges_begin_date = datetime.datetime.strptime(data1, '%Y-%m-%d').date()
    charges_end_date = datetime.datetime.strptime(data2, '%Y-%m-%d').date()
    print("str2",charges_begin_date,charges_end_date,type(charges_end_date))

    if charges_begin_date >= arr_date and charges_end_date  <= dep_date and arr_date <= charges_end_date:
       sql_value = gensql('insert','reservation.res_fixed_charges',d)
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'please enter valid date','ReturnCode':'PEVD'}, sort_keys=True, indent=4))

def Hotel_RES_Post_SELECT_QueryTransactioncodeCode(request):

    package_from = request.json['package_from']
    package_to = request.json['package_to']

    sql_value = json.loads(dbget("select packages.package_code.package_code,packages.package_code.short_description, \
                                    packages.package_details.package_code_id,packages.package_details.price from packages.package_details \
                                    join packages.package_code on packages.package_code.package_code_id =  packages.package_details.package_code_id \
                                    where '"+str(package_from)+"' <= packages.package_details.start_date or '"+str(package_to)+"' >= packages.package_details.end_date"))


    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_Post_SELECT_SelectFixedCharges(request):
    d = request.json
    sql_value = json.loads(dbget("select * from reservation.res_fixed_charges where res_id = '"+str(d['res_id'])+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
