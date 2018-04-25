from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateProfileNotesRecord(request):
    d,e = {},{}
    res = request.json
    print(res)
    for name,val in res.items():
 
       if  name == 'PF_Mobileno' or name == 'PF_Firstname':
          e[name] = ""+val+""
       else :
           d[name] = ""+val+""
    print(e,d)
    sql_value = gensql('update','profile.pf_notes',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
