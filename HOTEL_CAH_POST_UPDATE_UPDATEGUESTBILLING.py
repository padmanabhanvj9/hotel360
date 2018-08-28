
import json
from sqlwrapper import gensql,dbget
import datetime
#import request

def HOTEL_CAH_POST_UPDATE_UPDATEGUESTBILLING(request):

    d = request.json
    print(d)
    #d['Posting_date'] = Posting_date
    e = { k : v for k,v in d.items() if k in ('Res_id','post_id','res_room')}
    f = { k : v for k,v in d.items() if k not in ('Res_id','post_id','res_room')}
    print(e)
    gensql('update','cashiering.billing_post',f,e)

    res_id = d.get("Res_id")

    Posting_date = datetime.datetime.utcnow().date()
    Revenue_date = datetime.datetime.utcnow().date()
    result = json.loads(dbget("select log_link_id from cashiering.log_link where link_id='1' "))
    log_id = result[0]['log_link_id']+1
    print(log_id)
    dbput("update cashiering.log_link set log_link_id="+str(log_id)+" where link_id='1'")
    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Supervisor"
    s['User_name'] = "david"
    s['Res_id'] = res_id
    s['Posting_action'] = "Night Audit posting"
    s['Posting_reason'] = "Payment posted for"+ " "+res_id
    s['Posting_description'] = "Payment posted successfully"
    s['log_link_id'] = log_id
    gensql('insert','cashiering.posting_changes_history_log',s)
    gensql('insert','cashiering.posting_history_log',s)

    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent=4))


   

