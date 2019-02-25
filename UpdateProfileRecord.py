import datetime
from sqlwrapper import gensql
import json
from ApplicationDate import application_date


def UpdateProfileRecord(request):

    res = request.json
    print(res)
    e = { k : v for k,v in res.items() if k in ('pf_id')}
    print(e['pf_id'])
    d = { k : v for k,v in res.items() if k not in ('pf_id')}
    if e['pf_id'][0:3] == 'cpy':
        sql_value = gensql('update','profile.pf_company_profile',d,e)
    else:
        sql_value = gensql('update','profile.pf_individual_profile',d,e)

    values = d.values()
    print(values)
    PF_Log_Description = ''
    for i in values:
       PF_Log_Description +=  i +" | "
    print(PF_Log_Description)   
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "Admin"
    s['Emp_Lastname'] = "User"
    app_datetime = application_date()
    s['PF_Log_Date'] = app_datetime[1]
    s['PF_Log_Time'] = app_datetime[2]
    s['PF_Action_Type'] = "Update Profile"
    s['PF_Log_Description'] = PF_Log_Description
    s['pf_id'] =  e['pf_id']
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully',
                       'ReturnCode':'RUS'}, sort_keys=True, indent=4))

   
