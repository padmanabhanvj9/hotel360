from sqlwrapper import gensql,dbget
import json
import datetime
from ApplicationDate import application_date

def UpdateProfileCreditcard(request):
    d = request.json
    #print(d)
    #PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    #PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    #print(PF_Log_Time)
   
    gensql('insert','profile.pf_creditcard',d)
    sql_value = json.loads(dbget("select cc_id from profile.pf_creditcard \
                                   where pf_creditcard_no='"+d['PF_Creditcard_No']+"' \
                                   and pf_expiration_date='"+d['PF_Expiration_Date']+"'"))
    #print(sql_value)
    s = {}
    s['Emp_Id'] = '121'
    s['Emp_Firstname'] = "Admin"
    s['Emp_Lastname'] = "User"
    app_datetime = application_date()
    s['PF_Log_Date'] = app_datetime[1]
    s['PF_Log_Time'] = app_datetime[2]
    s['PF_Action_Type'] = "Profile Creditcard"
    s['PF_Log_Description'] = "credit card details"
    s['pf_id'] = d['pf_id']
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Return_value':sql_value[0]['cc_id'],'ReturnCode':'RIS'}, sort_keys=True, indent=4))


def UpdateProfileCreditcardnew(request):
    d = request.json
    #print(d)
    gensql('insert','profile.pf_creditcard',d)
    sql_value = json.loads(dbget("select cc_id from profile.pf_creditcard \
                                   where pf_creditcard_no='"+d['PF_Creditcard_No']+"' \
                                   and pf_expiration_date='"+d['PF_Expiration_Date']+"' "))
    #print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Return_value':sql_value[0]['cc_id'],'ReturnCode':'RIS'}, sort_keys=True, indent=4))
   
