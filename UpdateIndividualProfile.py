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
    PF_Firstname = request.json['PF_Firstname']
    PF_Lastname = request.json['PF_Lastname']
    PF_Language = request.json['PF_Language']
    PF_Title = request.json['PF_Title']
    PF_Mobileno = request.json['PF_Mobileno']
    PF_Individual_Address = request.json['PF_Individual_Address']
    PF_Home_Address = request.json['PF_Home_Address']
    PF_Individual_City = request.json['PF_Individual_City']
    PF_Individual_Postalcode  = request.json['PF_Individual_Postalcode']
    PF_Individual_Country = request.json['PF_Individual_Country']
    PF_Individual_State = request.json['PF_Individual_State']
    PF_Salutation = request.json['PF_Salutation']
    PF_Individual_VIP = request.json['PF_Individual_VIP']
    PF_Nationality = request.json['PF_Nationality']
    PF_Date_Of_Birth = request.json['PF_Date_Of_Birth']
    PF_Passport = request.json['PF_Passport']
    PF_Type = request.json['PF_Type']
    PF_Individual_Communication1 = request.json['PF_Individual_Communication1']
    PF_Individual_Communication2 = request.json['PF_Individual_Communication2']
    PF_Individual_Communication3 = request.json['PF_Individual_Communication3']
    PF_Individual_Commtype1 = request.json['PF_Individual_Commtype1']
    PF_Individual_Commtype2 = request.json['PF_Individual_Commtype2']
    PF_Individual_Commtype3 = request.json['PF_Individual_Commtype3']

    # call gensql for connect DB and execute the query
    d = {} # define dictionary 
    d['PF_Firstname'] = PF_Firstname
    d['PF_Lastname'] = PF_Lastname
    d['PF_Language'] = PF_Language
    d['PF_Title'] = PF_Title
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Individual_Address'] = PF_Individual_Address
    d['PF_Home_Address'] = PF_Home_Address
    d['PF_Individual_City'] = PF_Individual_City
    d['PF_Individual_Postalcode'] = PF_Individual_Postalcode
    d['PF_Individual_Country'] = PF_Individual_Country
    d['PF_Individual_State'] = PF_Individual_State
    d['PF_Salutation'] = PF_Salutation
    d['PF_Individual_VIP'] = PF_Individual_VIP
    d['PF_Nationality'] = PF_Nationality
    d['PF_Date_Of_Birth'] = PF_Date_Of_Birth
    d['PF_Passport'] = PF_Passport
    d['PF_Type'] = PF_Type
    d['PF_Individual_Communication1'] = PF_Individual_Communication1
    d['PF_Individual_Communication2'] = PF_Individual_Communication2
    d['PF_Individual_Communication3'] = PF_Individual_Communication3
    d['PF_Individual_Commtype1'] = PF_Individual_Commtype1
    d['PF_Individual_Commtype2'] = PF_Individual_Commtype2
    d['PF_Individual_Commtype3'] = PF_Individual_Commtype3


    
    #Include buisness logic before calling Sql Query(Optional)
    sql_value = gensql('insert','profile.pf_individual_profile',d) # eg: insert into test  (business_id)  values ('?') 
    #gensql('select','table_name','*',d) # eg: select * from test  where  business_id='?'  
    #gensql('update','table_name',d,e) # eg: update test  set  business_id='?'  where  b_id='?'

    #Include buisness logic after Sql Query
    data = d.get("PF_Mobileno")
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
    PF_Log_Description = "Create Individual Profile" + " "+PF_Firstname
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

