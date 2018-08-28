from sqlwrapper import gensql, dbget, dbput

import json

def HOTEL_PAC_POST_DELETE_Package(request):
    d = request.json
    dbput("delete from packages.package_code where package_code_id = "+str(d['package_code_id'])+" ")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_DELETE_Packagedetails(request):
    d = request.json
    dbput("delete from packages.package_details where packages_details_id = "+str(d['packages_details_id'])+" ")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
 
