from sqlwrapper import gensql
import json
def Hotel_RES_GET_SELECT_Restype():
    s = ['restype','restype_description']
    sql_value = gensql('select','reservation.restype',s)
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Alertarea():
 
    sql_value = gensql('select','reservation.alertarea','alertarea')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Alertcode():
 
    sql_value = gensql('select','reservation.alertcode','alertcode')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Origin():
 
    sql_value = gensql('select','reservation.origin','origincode,origindescription')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_GET_SELECT_Source():
 
    sql_value = gensql('select','reservation.res_source','sourcecode,sourcedescription')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Payment():
    sql_value = gensql('select','reservation.payment','paymenttype,transactioncode,payment_description')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Market():
    sql_value = gensql('select','reservation.market','marketgroup,marketgroup_description')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Department():
    sql_value = gensql('select','reservation.department','department')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_Transaction_code():
    sql_value = gensql('select','reservation.transaction_code','transaction_description')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def Hotel_RES_GET_SELECT_depositrule():
    sql_value = gensql('select','reservation.depositrule','deposit_rule')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
