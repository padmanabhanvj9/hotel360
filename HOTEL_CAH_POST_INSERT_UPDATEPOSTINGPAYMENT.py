import json 
from sqlwrapper import gensql, dbget,dbput
import datetime

def HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT(request):
    d = request.json
    print(d)
    e = { k : v for k,v in d.items() if v != "" }
    print(e)
    sql = gensql('insert','cashiering.posting_payment',e)
    print(sql)
    #d['Posting_date'] = Posting_date
    res_id = d.get("res_id")
    print(res_id)
    Posting_date = datetime.datetime.utcnow().date()
    Revenue_date = datetime.datetime.utcnow().date()
    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Supervisor"
    s['User_name'] = "david"
    s['Res_id'] = res_id
    s['Posting_action'] = "Night Audit posting"
    s['Posting_reason'] = "Payment posted for"+" "+res_id+ "and"+d.get("res_room")
    s['Posting_description'] = "Payment posted successfully"
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_original_history_log',s)
   
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENTCHECKOUT(request):
    d = request.json
    print(d)
    e = { k : v for k,v in d.items() if v != "" }
    print(e)
    sql = gensql('insert','cashiering.posting_payment',e)
    print(sql)
    #d['Posting_date'] = Posting_date
    res_id = d.get("res_id")
    #print(res_id)
    Posting_date = datetime.datetime.utcnow().date()
    Revenue_date = datetime.datetime.utcnow().date()
    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Supervisor"
    s['User_name'] = "david"
    s['Res_id'] = res_id
    s['Posting_action'] = "Night Audit posting"
    s['Posting_reason'] = "Payment posted for"+" "+res_id+ "and"+d.get("res_room")
    s['Posting_description'] = "Payment posted successfully"
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_original_history_log',s)
    balance = json.loads(dbget("select res_guest_balance from reservation.res_reservation \
                                where res_room="+d.get("res_room")+" and res_id="+d.get("res_id")+" "))
    print("balance",balance[0]['res_guest_balance'],type(balance[0]['res_guest_balance']))
    if int(balance[0]['res_guest_balance']) != 0:
        print(balance[0]['res_guest_balance'],type(balance[0]['res_guest_balance']))
        res_id = request.json['res_id']
        res_room = request.json['res_room']
        sql_value = json.loads(dbget("select reservation.res_reservation.res_guest_status from reservation.res_reservation where res_id="+res_id+" and res_room="+res_room+" "))
        balance1 = sql_value[0]['res_guest_status']

        if balance1 =="due out":
          status = "Check out"
          sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id="+res_id+" and res_room="+res_room+" ")
        else:
          return(json.dumps({'Status':'Failure','Return':'Unable to update'}, sort_keys=True, indent=4))
  
        return(json.dumps({"Return": "Record Inserted Successfully", \
                        "ReturnCode": "RIS","Status": "Success","StatusCode": "200", \
                        "Balance":balance[0]['res_guest_balance']},indent=4))    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200","Balance":0},indent=4))
  

