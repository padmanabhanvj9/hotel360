from flask import Flask,request
import json
from sqlwrapper import gensql,dbget
import datetime

def ratecategory(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.ratecategory',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def ratecode(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.ratecode',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def market(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.market',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def sourcetab(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.source',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def crrencytab(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.currency',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def negotiated(request):
    d = request.json
    print(d)
    gensql('insert','revenue_management.negotiated_rate',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
def ratedetailss(request):
    d = request.json
    print(d)
    roomtype = d.get("Roomtype_id")
    print(roomtype)
    no = roomtype.split(',')
    print(no)
    for i in no:
       
       print(i)
       print('insert',i)
       d['Roomtype_id'] = i   
       gensql('insert','revenue_management.rate_details',d)
    ratecode = d.get("Ratecode_id")
    rate = json.loads(dbget("select rate_description from revenue_management.ratecode where ratecode_id='"+ratecode+"'"))
    #rate = str(json.loads([0]['rate_description']))
    rate = rate[0]['rate_description']
    print(rate)
    begin_date = d.get("Begin_sell_date")
    end_date = d.get("End_sell_date")
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    s = {}
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['emp_name'] = "Daisy"
    s['action_type'] = "Rate setup for "+" "+rate
    s['action_description'] = "Rate fixed for"+" "+str(rate)+" "+"between"+" "+str(begin_date)+" "+"to"+" "+str(end_date)
    s['rate_code_id'] = ratecode
    gensql('insert','revenue_management.revenue_activity_log',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
           
