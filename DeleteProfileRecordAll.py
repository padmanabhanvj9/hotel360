from sqlwrapper import gensql,dbput
import json

def DeleteProfileCreditCard(request):
         pf_id = request.json['pf_id']
         cc_id = request.json['cc_id']
         sql = ("delete from profile.pf_creditcard where pf_id = '"+pf_id+"' and cc_id = '"+cc_id+"' ")
         print(sql)             
         dbput(sql)
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
  
def DeleteProfileNegotiate(request):
         pf_id = request.json['pf_id']
         negotiate_id = request.json['negotiate_id']
         sql = ("delete from profile.pf_negotiated_rate where pf_id = '"+pf_id+"' and negotiate_id = '"+negotiate_id+"' ")
         print(sql)             
         dbput(sql)
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
 
def DeleteProfileNotes(request):
         pf_id = request.json['pf_id']
         Notes_id = request.json['notes_id']
         sql = ("delete from profile.pf_notes where pf_id = '"+pf_id+"' and notes_id = '"+Notes_id+"' ")
         print(sql)             
         dbput(sql)
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
 
def DeleteProfilePreference(request):
         pf_id = request.json['pf_id']
         preference_id = request.json['preference_id']
         sql = ("delete from profile.pf_preference where pf_id = '"+pf_id+"' and preference_id = '"+preference_id+"' ")
         print(sql)             
         dbput(sql)
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
 
