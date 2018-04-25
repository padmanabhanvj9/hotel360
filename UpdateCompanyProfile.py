from sqlwrapper import gensql
import datetime
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateCompanyProfile(request):
    PF_Firstname = request.json['PF_Firstname']
    PF_Lastname = request.json['PF_Lastname']
    PF_Language = request.json['PF_Language']
    PF_Title = request.json['PF_Title']
    PF_Mobileno = request.json['PF_Mobileno']
    PF_Account = request.json['PF_Account']
    PF_Company_Address = request.json['PF_Company_Address']
    PF_Business_Address = request.json['PF_Business_Address']
    PF_Company_City = request.json['PF_Company_City']
    PF_Company_Postalcode = request.json['PF_Company_Postalcode']
    PF_Company_Country = request.json['PF_Company_Country']
    PF_Company_State = request.json['PF_Company_State']
    PF_Owner = request.json['PF_Owner']
    PF_Territory = request.json['PF_Territory']
    PF_Type = request.json['PF_Type']
    PF_AR_Number = request.json['PF_AR_Number']
    PF_Ref_Currency = request.json['PF_Ref_Currency']
    PF_Company_Communication1 = request.json['PF_Company_Communication1']
    PF_Company_Communication2 = request.json['PF_Company_Communication2']
    PF_Company_Communication3 = request.json['PF_Company_Communication3']
    PF_Company_Commtype1 = request.json['PF_Company_Commtype1']
    PF_Company_Commtype2 = request.json['PF_Company_Commtype2']
    PF_Company_Commtype3 = request.json['PF_Company_Commtype3']
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Lastname'] = PF_Lastname
    d['PF_Language'] = PF_Language
    d['PF_Title'] = PF_Title
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Account'] = PF_Account
    d['PF_Company_Address'] = PF_Company_Address
    d['PF_Business_Address'] = PF_Business_Address
    d['PF_Company_City'] = PF_Company_City
    d['PF_Company_Postalcode'] = PF_Company_Postalcode
    d['PF_Company_Country'] = PF_Company_Country
    d['PF_Company_State'] = PF_Company_State
    d['PF_Owner'] = PF_Owner
    d['PF_Territory'] = PF_Territory
    d['PF_Type'] = PF_Type
    d['PF_AR_Number'] = PF_AR_Number
    d['PF_Ref_Currency'] = PF_Ref_Currency
    d['PF_Company_Communication1'] = PF_Company_Communication1
    d['PF_Company_Communication2'] = PF_Company_Communication2
    d['PF_Company_Communication3'] = PF_Company_Communication3
    d['PF_Company_Commtype1'] = PF_Company_Commtype1
    d['PF_Company_Commtype2'] = PF_Company_Commtype2
    d['PF_Company_Commtype3'] = PF_Company_Commtype3
   
    sql_value = gensql('insert','profile.pf_company_profile',d)
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
    PF_Log_Description = "Create Company Profile" + " "+PF_Firstname
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
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
