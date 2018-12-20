from sqlwrapper import gensql,dbget
import json
def select_roomstatus():
   sql_value = json.loads(gensql('select','room_management.room_status','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_class():
   sql_value = json.loads(gensql('select','room_management.room_class','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_condition():
   sql_value = json.loads(gensql('select','room_management.room_condition','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_hkstatus_code():
   sql_value = json.loads(gensql('select','room_management.hkstatus','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
#*******************************room type********************
def select_room_type():
   sql_value = json.loads(gensql('select','room_management.room_type','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_room_no():
   sql_value = json.loads(dbget('SELECT rm_room FROM room_management.rm_room_list order by rm_room'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_discription():
   sql_value = json.loads(gensql('select','room_management.room_discription','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_servicestatus_code():
   sql_value = json.loads(gensql('select','room_management.servicestatus','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_turndownstatus():
   sql_value = json.loads(gensql('select','room_management.turndownstatus','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_room_service_status():
   sql_value = json.loads(gensql('select','room_management.room_service_status','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_mainteanance_reason():
   sql_value = json.loads(gensql('select','room_management.mainteanance_reason','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_floor():
   sql_value = json.loads(gensql('select','room_management.floor','*'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
