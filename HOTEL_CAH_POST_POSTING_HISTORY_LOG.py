import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_CAH_POST_POSTING_HISTORY_LOG(request):

    res_id = request.json['res_id']
    
    sql_value = json.loads(dbget("SELECT * from cashiering.posting_history_log WHERE cashiering.posting_history_log.res_id="+res_id+""))
    sql_value1 = json.loads(dbget("SELECT * from cashiering.posting_changes_history_log WHERE cashiering.posting_changes_history_log.res_id="+res_id+""))
    sql_value2 = json.loads(dbget("SELECT * from cashiering.posting_original_history_log WHERE cashiering.posting_original_history_log.res_id="+res_id+""))

    print(sql_value)
    print(sql_value1)
    print(sql_value2)
    #return s

    return(json.dumps({"History": sql_value,"Changes": sql_value1,"Original": sql_value2},indent=4))
