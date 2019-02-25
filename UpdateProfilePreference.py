from sqlwrapper import gensql
import json
import datetime
from ApplicationDate import application_date

def UpdateProfilePreference(request):
    #PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    #PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    #print(PF_Log_Time)
    #PF_Log_Date = datetime.datetime.utcnow().date()
    d = request.json
    #print(d)
    e = { k : v for k,v in d.items() if k in ('pf_id,preference_id')}
    #print(e)
    f = { k : v for k,v in d.items() if k not in ('pf_id,preference_id') }
    print(f)    
    sql_value = gensql('update','profile.pf_preference',f,e)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "Admin"
    s['Emp_Lastname'] = "User"
    app_datetime = application_date()
    s['PF_Log_Date'] = app_datetime[1]
    s['PF_Log_Time'] = app_datetime[2]
    s['PF_Action_Type'] = "Update Profile Preference"
    s['PF_Log_Description'] = d['PF_Preference_Group']
    s['pf_id'] = d['pf_id']
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
