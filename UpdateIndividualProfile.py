#Input Param: business_id, business_mobile, business_first_name, business_last_name, doj
#OutputParam: Record Inserted Successfully
#Purpose: It received input parameters from root file as JSON and passed those parameters to DB wrapper as dictionary/List,
#DB wrapper execute the sql query and return values back to this function.
#Date:13/03/2018
#Author: Aravinth,Daisy
# import packages are define top of the program
import datetime

from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)

# Below function is called from the root file 
def UpdateIndividualProfile(request):
    # syntax for get and assign the value from business_id   
  

    d = request.json
    
    #Include buisness logic before calling Sql Query(Optional)
    sql_value = gensql('insert','profile.pf_individual_profile',d) # eg: insert into test  (business_id)  values ('?') 
    #gensql('select','table_name','*',d) # eg: select * from test  where  business_id='?'  
    #gensql('update','table_name',d,e) # eg: update test  set  business_id='?'  where  b_id='?'

    #Include buisness logic after Sql Query
    data = d.get("PF_Mobileno")
    data1 = d.get("PF_Firstname")
    print(data)
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "daisy"
    Emp_Lastname = "veroni"
    PF_Action_Type = "New Profile"
    PF_Mobileno = data
    PF_Log_Description = "Create Individual Profile" + " "+data1
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    s['Emp_Lastname'] = Emp_Lastname
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = PF_Action_Type
    s['PF_Log_Description'] = PF_Log_Description
    s['PF_Mobileno'] = PF_Mobileno
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    # finally return the value from DB_Wrapper   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

