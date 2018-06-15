#Input Param: 
#OutputParam: Record Inserted Successfully
#Purpose: This service used for crate individual profile
#Date:13/03/2018
#UpdateDate:11/06/2018
#Author: Aravinth
#import packages are define top of the program
import datetime
from sqlwrapper import gensql,dbget,dbput
import json

# Below function is called from the root file 
def UpdateIndividualProfile(request):   
    d = request.json
    select = json.loads(dbget("select * from profile.profile_id"))
    print(select,type(select),len(select))
    print(select[0]['profile_id'])
    id1 = "ind"+str(select[0]['profile_id']+1)
    print(id1)
    update = dbput("update profile.profile_id set profile_id = '"+str(select[0]['profile_id']+1)+"'")
    d['pf_id'] = id1
    sql_value = gensql('insert','profile.pf_individual_profile',d) 
    
    data1 = d.get("PF_Firstname")
    
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    
    PF_Log_Description = "Create Individual Profile" + " "+data1
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "daisy"
    s['Emp_Lastname'] = "veroni"
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = "New Profile"
    s['PF_Log_Description'] = PF_Log_Description
    s['pf_id'] = id1
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    # finally return the value from DB_Wrapper   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

