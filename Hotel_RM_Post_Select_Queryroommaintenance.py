from sqlwrapper import dbget,dbfetch
import json
from flask import Flask,request, jsonify

def hotel_rm_post_select_queryroommaintenance(request):
    sql = json.loads(dbget("select * from room_management.rm_room_mainteanance_acitivity_log join \
                            room_management.rm_room_list on \
                            room_management.rm_room_mainteanance_acitivity_log.rm_room = \
                            room_management.rm_room_list.rm_room"))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
    
