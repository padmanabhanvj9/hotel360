from sqlwrapper import gensql,dbget
import json
def select_roomstatus():
   sql_value = json.loads(gensql('select','room_management.hkstatus','hkstatus_code'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_class():
   sql_value = json.loads(gensql('select','room_management.room_class','class'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_condition():
   sql_value = json.loads(gensql('select','room_management.room_condition','condition'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_hkstatus_code():
   sql_value = json.loads(gensql('select','room_management.hkstatus','hkstatus_code'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_room_type():
   sql_value = json.loads(gensql('select','room_management.room_type','type'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_room_no():
   sql_value = json.loads(dbget('SELECT rm_room FROM room_management.rm_room_list order by rm_room'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_discription():
   sql_value = json.loads(gensql('select','room_management.room_discription','discription'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_servicestatus_code():
   sql_value = json.loads(gensql('select','room_management.servicestatus','servicestatus_code'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_turndownstatus():
   sql_value = json.loads(gensql('select','room_management.turndownstatus','turndownstatus'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_():
   sql_value = json.loads(gensql('select','room_management.room_discription','discription'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
def select_():
   sql_value = json.loads(gensql('select','room_management.room_discription','discription'))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': sql_value ,'ReturnCode':'RRTS'},indent=4))
