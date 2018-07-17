from sqlwrapper import gensql, dbget, dbput
import json
import datetime



def HOTEL_CASH_RESERVATION_BALANCE(request):
    
    d = request.json
    
    res_id = request.json['res_id']
    
    sql1 = json.loads(dbget("SELECT SUM (posting_amount) AS total_posting_amount FROM cashiering.billing_post where res_id="+res_id+""))

    sql2 = json.loads(dbget("SELECT SUM (postig_amount) AS total_payment_amount FROM cashiering.posting_payment where res_id="+res_id+""))

    sql3 = json.loads(dbget("SELECT SUM (res_deposit_amount) AS total_deposite FROM reservation.res_deposit where res_id="+res_id+""))

    #sql4 = json.loads(dbget("select reservation.res_reservation.res_guest_status from reservation.res_reservation where res_id="+res_id+""))
    
    print(sql1,type(sql1))
    
    print(sql2)
    print(sql3)
    print(sql1)

    balance = sql2[0]['total_payment_amount'] + sql3[0]['total_deposite'] - sql1[0]['total_posting_amount']
    print(balance)

   
    
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    return(json.dumps({'Balance': balance}, sort_keys=True, indent=4))

