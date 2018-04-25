
from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateProfilePreference(request):
    PF_Firstname = request.json['PF_Firstname']
    PF_Mobileno =  request.json['PF_Mobileno']


    PF_Preference_Group = request.json['PF_Preference_Group']
    PF_Preference_Description = request.json['PF_Preference_Description']
    PF_Guest_Preference = request.json['PF_Guest_Preference']
    pf_preference_group_desc = request.json['pf_preference_group_desc']
    d = {}
    e = {}
    e['PF_Firstname'] = PF_Firstname
    e['PF_Mobileno'] = PF_Mobileno
   
    d['PF_Preference_Group'] = PF_Preference_Group
    d['PF_Preference_Description'] = PF_Preference_Description
    d['PF_Guest_Preference'] = PF_Guest_Preference
    d['pf_preference_group_desc'] = pf_preference_group_desc
      
    sql_value = gensql('update','profile.pf_preference',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
