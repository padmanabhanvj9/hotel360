from sqlwrapper import gensql,dbget
import json
def HOTEL_FD_GET_SELECT_QueryQueueReservation(request):
    d = request.json
    query = ''
    sql = "select * from room_management.rm_queue_room"
    for name,val in d.items():
      if val != '':      
        if len(query) == 0:
           query += " where "
        else:
           query += " and " 
        if val != '':
           query += ""+name+" = '"+val+"' "
    #print(sql+query)
    sql1 = sql+query
    print(sql1)
    #sql_value = gensql('select','room_management.rm_queue_room','*',d)
    #sql_value = json.loads(sql_value)
    #print(sql_value)
    res = dbget(sql1)
    print(res)
    sql_value = json.loads(res)
    print(sql_value)
   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

