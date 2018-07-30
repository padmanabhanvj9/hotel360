import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_BBL_POST_UPDATE_BusinessBlockStatus(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('block_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('block_id')}
    print(e)
    sql = gensql('update','business_block.business_block',a,e)
    print(sql)
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent=4))
