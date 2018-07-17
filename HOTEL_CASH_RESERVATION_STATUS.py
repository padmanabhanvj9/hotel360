from sqlwrapper import gensql, dbget, dbput
import json
import datetime



def HOTEL_CASH_RESERVATION_STATUS(request):
    
    d = request.json
    
    res_id = request.json['res_id']

    sql_value = json.loads(dbget("select reservation.res_reservation.res_guest_status from reservation.res_reservation where res_id="+res_id+""))
    

    balance = sql_value[0]['res_guest_status']

    if balance =="due out":
        status = "Check out"
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id in ("+res_id+")")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully'}, sort_keys=True, indent=4))
    else:
        return(json.dumps({'Status':'not able to update'}, sort_keys=True, indent=4))
    
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    #return(json.dumps({'Balance': balance,'status':sql4}, sort_keys=True, indent=4))

         
