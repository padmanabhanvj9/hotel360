from sqlwrapper import gensql
import json
def Hotel_RES_GET_SELECT_Restype():
    #s = ['restype','restype_description']
    sql_value = gensql('select','reservation.restype','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Alertarea():
 
    sql_value = gensql('select','reservation.alertarea','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Alertcode():
 
    sql_value = gensql('select','reservation.alertcode','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Origin():
 
    sql_value = gensql('select','reservation.origin','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Source():
 
    sql_value = gensql('select','reservation.res_source','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Payment():
    sql_value = gensql('select','reservation.payment','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Market():
    sql_value = gensql('select','reservation.market','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Department():
    sql_value = gensql('select','reservation.department','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Transaction_code():
    sql_value = gensql('select','reservation.transaction_code','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_depositrule():
    sql_value = gensql('select','reservation.depositrule','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_CancelReason():
    sql_value = gensql('select','reservation.cancel_reason','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Cardtype():
    sql_value = gensql('select','reservation.cardtype','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Waitlist_reason():
    sql_value = gensql('select','reservation.waitlist_reason','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Privileges():
   sql_value = gensql('select','reservation.privileges','*')
   result = json.loads(sql_value)
   print(result)
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
