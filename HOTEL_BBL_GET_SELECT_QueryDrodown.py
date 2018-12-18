import json
from sqlwrapper import gensql,dbget

def HOTEL_BBL_GET_SELECT_BusinessBlockStatus():

    sql_value = gensql('select','business_block.block_status','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_BBL_GET_SELECT_InventoryContrtol():

    sql_value = gensql('select','business_block.inventory_control','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_BBL_GET_SELECT_MeetingSpaceType():

    sql_value = gensql('select','business_block.meeting_space_type','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_BBL_GET_SELECT_Block_Type():

    sql_value = gensql('select','business_block.block_type','*')
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_BBL_POST_INSERT_BusinessBlockStatus(request):
    d = request.json
    sql_value = gensql('insert','business_block.block_status',d)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': "Record Inserted Successfully"  ,'ReturnCode':'RIS'},indent=4))
def HOTEL_BBL_POST_INSERT_InventoryContrtol(request):
    d = request.json
    sql_value = gensql('insert','business_block.inventory_control',d)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': "Record Inserted Successfully"  ,'ReturnCode':'RIS'},indent=4))
def HOTEL_BBL_POST_INSERT_MeetingSpaceType(request):
   d = request.json
   sql_value = gensql('insert','business_block.meeting_space_type',d)

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': "Record Inserted Successfully"  ,'ReturnCode':'RIS'},indent=4))
def HOTEL_BBL_POST_INSERT_Block_Type(request):
    d = request.json
    sql_value = gensql('insert','business_block.block_type',d)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': "Record Inserted Successfully"  ,'ReturnCode':'RIS'},indent=4))
