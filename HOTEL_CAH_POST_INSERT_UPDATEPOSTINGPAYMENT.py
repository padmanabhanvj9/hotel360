import json 
from sqlwrapper import gensql, dbget
import datetime

def HOTEL_CAH_POST_INSERT_UPDATEPOSTINGPAYMENT(request):
    d = request.json
    print(d)
    sql = gensql('insert','cashiering.posting_payment',d)
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
    s['Posting_reason'] = "Payment posted for"+" "+res_id
    s['Posting_description'] = "Payment posted successfully"
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_original_history_log',s)
   
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

   

