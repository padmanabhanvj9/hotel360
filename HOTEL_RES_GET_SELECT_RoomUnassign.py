from sqlwrapper import gensql, dbput
import json
import requests
from flask import Flask,request,jsonify
def HOTEL_RES_GET_SELECT_RoomUnassign(request):
    Res_id = request.json['Res_id']
   
    data = '0'
    sql = dbput("update reservation.res_reservation set res_room = "+data+" where res_id = "+Res_id+" ")

    print(sql)

    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':'Room UnAssigned Successfully'  ,'ReturnCode':'RUAS'},indent=4))
