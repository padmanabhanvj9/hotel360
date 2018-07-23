import json
import random
from sqlwrapper import gensql,dbget,dbput
import datetime
def HOTEL_BBL_POST_UPDATE_Business_Block_Update(request):
    d = request.json
    x = d['Inquiry']
    a = { k : v for k,v in x.items() if v != '' if k not in ('block_id')}
    print(a)
    e = { k : v for k,v in x.items() if k != '' if k in ('block_id')}
    print(e)
    sql = gensql('update','business_block.business_block',a,e)
    print(sql)
    y = d['Inquiry_grid']
    print(y)


    for i in y:
       print(i)
       p = { k : v for k,v in i.items() if v != '' if k not in ('block_id','inquiry_grid_id')}
       print(p)
       q = { k : v for k,v in i.items() if k != '' if k in ('block_id','inquiry_grid_id')}
       print(q)
       print(gensql('update','business_block.inquiry_grid',p,q))
       



    s = {}
    values = a.values()
    print(values)
    RES_Description = ''
    for i in values:
       if  RES_Description == '':
           RES_Description +=  i
       else:
           RES_Description +=  "|" + i
    print(RES_Description)
    s['user_role'] = "Supervisor"
    block_id = e.get("block_id")
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = block_id
    s['action_type_id'] = "Update Business Block"
    s['description'] = RES_Description
    gensql('insert','business_block.business_block_activity_log',s)
    
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent=4))
