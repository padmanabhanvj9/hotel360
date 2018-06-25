from sqlwrapper import gensql
import json
def insert_roomstatus(request):
    d = request.json   
    sql_value = gensql('insert','room_management.room_status',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_class(request):
    d = request.json   
    sql_value = gensql('insert','room_management.room_class',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_condition(request):
    d = request.json   
    sql_value = gensql('insert','room_management.room_condition',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def insert_hkstatus_code(request):
    d = request.json   
    sql_value = gensql('insert','room_management.hkstatus',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_room_type(request):
    d = request.json
    sql_value = gensql('insert','room_management.room_type',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))    
def insert_room_no(request):
    d = request.json
    sql_value = gensql('insert','room_management.rm_room_list',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))    
def insert_room_discription(request):
    d = request.json
    sql_value = gensql('insert','room_management.room_discription',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_servicestatus_code(request):
    d = request.json
    sql_value = gensql('insert','room_management.servicestatus',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_turndownstatus(request):
    d = request.json
    sql_value = gensql('insert','room_management.turndownstatus',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def insert_room_service_status(request):
    d = request.json
    sql_value = gensql('insert','room_management.room_service_status',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def insert_mainteanance_reason(request):
    d = request.json
    sql_value = gensql('insert','room_management.mainteanance_reason',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def insert_floor(request):
    d = request.json
    sql_value = gensql('insert','room_management.floor',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))


