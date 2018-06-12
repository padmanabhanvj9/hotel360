from sqlwrapper import gensql,dbput
import json

def DeleteProfileRecord(request):
   pf_id = request.json['pf_id']
   print(pf_id)
   if pf_id[0:3] == 'ind':
         sql = ("delete from profile.pf_individual_profile where pf_id = '"+pf_id+"' ")
         print(sql)             
         dbput(sql)
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
   else :
        sql = ("delete from profile.pf_company_profile where pf_id = '"+pf_id+"' ")
        print(sql)   
        dbput(sql)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))


