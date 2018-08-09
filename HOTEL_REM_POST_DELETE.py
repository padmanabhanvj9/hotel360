from sqlwrapper import gensql, dbget, dbput
import datetime
import json

def Delete_Negotiated_Rate(request):
    d = request.json
    print(dbput("delete from revenue_management.negotiated_rate where negotiated_code_id= "+d['negotiated_code_id']+" "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

def Delete_Rate_code(request):
    d = request.json
    dbput("delete from revenue_management.ratecode_setup where ratecode_id="+str(d['ratecode_id'])+" ")
    dbput("delete FROM revenue_management.rate_details where ratecode_id="+str(d['ratecode_id'])+" ")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

def Delete_Rate_details(request):
    d = request.json
    dbput("delete FROM revenue_management.rate_details where rate_details_id="+str(d['rate_details_id'])+" ")    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
