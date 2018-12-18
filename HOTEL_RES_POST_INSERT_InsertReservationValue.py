from sqlwrapper import gensql
import json
def Hotel_RES_POST_INSERT_RestypeInsert(request):
    d = request.json
    sql_value = gensql('insert','reservation.restype',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Alertarea(request):
    d = request.json
    sql_value = gensql('insert','reservation.alertarea',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Alertcode(request):
    d = request.json
    sql_value = gensql('insert','reservation.alertarea',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Origin(request):
    d = request.json
    sql_value = gensql('insert','reservation.origin',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Source(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_source',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Payment(request):
    d = request.json
    sql_value = gensql('insert','reservation.payment',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Market(request):
    d = request.json
    sql_value = gensql('insert','reservation.market',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Department(request):
    d = request.json
    sql_value = gensql('insert','reservation.department',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Transaction_code(request):
    d = request.json
    sql_value = gensql('insert','reservation.transaction_code',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Depositrule(request):
    d = request.json
    sql_value = gensql('insert','reservation.depositrule',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_CancelReason(request):
    d = request.json
    sql_value = gensql('insert','reservation.cancel_reason',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def Hotel_RES_POST_INSERT_Cardtype(request):
    d = request.json
    sql_value = gensql('insert','reservation.cardtype',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))

def Hotel_RES_POST_INSERT_Waitlist_reason(request):
    d = request.json
    sql_value = gensql('insert','reservation.waitlist_reason',d)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def Hotel_RES_POST_INSERT_Privileges(request):
   d = request.json
   sql_value = gensql('insert','reservation.privileges',d)
   print(sql_value)
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
