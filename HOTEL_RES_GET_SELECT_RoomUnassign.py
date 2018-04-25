from sqlwrapper import gensql, dbput
import json
import requests
from flask import Flask,request,jsonify
def HOTEL_RES_GET_SELECT_RoomUnassign():
    PF_Mobileno = request.args['PF_Mobileno']
 
  
  
    '''d['PF_Mobileno'] = PF_Mobileno
    s = ['RES_Room']
    sql_value = gensql('select','reservation.res_reservation',s,d)
    sql_value = json.loads(sql_value)
    #sql_value = sql_value[0]
    print(sql_value)
    print(d)
    mobile = d.get('PF_Mobileno')
    print(mobile)
    #print (sql_value["res_room"])
    for x in sql_value:
        print (x['res_room'])'''



    #if x['res_room'] != 'null' or x['res_room'] == 0:
    data = '0'
    sql = ("update reservation.res_reservation set res_room = "+data+" where pf_mobileno = "+PF_Mobileno+" ")
    print(sql)
    dbput(sql)
        

    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':'Room UnAssigned Successfully'  ,'ReturnCode':'RUAS'},indent=4))
