from sqlwrapper import gensql, dbget, dbput
import datetime
import json

def Delete_Negotiated_Rate(request):
    d = request.json
    print(dbput("delete from revenue_management.negotiated_rate where negotiated_code_id= "+d['negotiated_code_id']+" "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
