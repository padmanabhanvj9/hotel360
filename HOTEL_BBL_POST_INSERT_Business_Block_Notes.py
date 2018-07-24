import json
import random
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_BBL_POST_INSERT_Business_Block_Notes(request):
    d = request.json
    print(d)
    sql = gensql('insert','business_block.business_block_notes',d)
    print(sql)

    s = {}
    s['user_role'] = "Supervisor"
    block_id = d.get("block_id")
    sqlvalue = json.loads(dbget("select block_name from business_block.business_block where block_id = '"+block_id+"' "))
    
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = block_id
    s['action_type_id'] = "Business Block notes"
    s['description'] = "Business Block notes for"+" "+str(block_id)
    gensql('insert','business_block.business_block_activity_log',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

