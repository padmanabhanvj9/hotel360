from sqlwrapper import gensql, dbget, dbput
import json
import datetime



def HOTEL_CASH_RESERVATION_STATUS(request):
    
    d = request.json
    
    res_id = request.json['res_id']
    res_room = request.json['res_room']
    sql_value = json.loads(dbget("select reservation.res_reservation.res_guest_status from reservation.res_reservation where res_id="+res_id+" and res_room="+res_room+" "))
    

    balance = sql_value[0]['res_guest_status']

    if balance =="due out":
        status = "Check out"
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id="+res_id+" and res_room="+res_room+" ")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully',"ReturnCode":"RUS"}, sort_keys=True, indent=4))
    else:
        return(json.dumps({'Status':'Failure','Return':'Unable to update'}, sort_keys=True, indent=4))
    
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    #return(json.dumps({'Balance': balance,'status':sql4}, sort_keys=True, indent=4))

         
