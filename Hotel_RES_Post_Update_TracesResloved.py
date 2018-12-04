import datetime
#from datetime import datetime,timedelta
from sqlwrapper import gensql, dbget
import json
def Hotel_RES_Post_Update_TracesResloved(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','res_unique_id','traces_id')}
    #print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','res_unique_id','traces_id')}
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    a['resloved_by'] = "Daisy"
    a['resloved_on'] = RES_Log_Date
    a['res_traces_status'] = 'Resloved'
    sql_value = gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

   
