import json
from sqlwrapper import gensql,dbget,dbput
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
    i = json.loads(dbget("select count(*) from revenue_management.negotiated_rate where rate_code_id="+str(d['rate_code_id'])+""))
    print(i)
    if int(i[0]['count']) == 0 :
       gensql('insert','revenue_management.negotiated_rate',d)
       return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
    else:
       return(json.dumps({"Return": "Record Already Exist","ReturnCode": "RAE","Status": "Success","StatusCode": "200"},indent=4)) 
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))


def ratedetailss(request):
    d = request.json
    #print(d)
    #print(d['rate_tier_id'])

    
    e = { k : v for k,v in d.items() if k not in ('days','room_types','package')}
    #print(e)
    room_id = json.loads(dbget("select max(rooms_id) as number1 from revenue_management.rooms_selected"))
    #print("room_id",room_id[0]['number1'])    
    for i in d['room_types']:
        #pass
        dbput("insert into revenue_management.rooms_selected (rooms_id,room_type_id) \
               values ('"+str(room_id[0]['number1']+1)+"','"+str(i)+"') ")
    e['rooms_id'] = int(room_id[0]['number1']+1)
    #print("2222",e)
    if d['rate_tier_id'] == 0:
            
       package_id = json.loads(dbget("select max(packages_id) as number2 from revenue_management.packages_selected"))
       print("package_id",package_id[0]['number2'],type(package_id[0]['number2']))
       for j in d['package']:
         print(j)
         dbput("insert into revenue_management.packages_selected (packages_id,package_code_id) \
               values ('"+str(package_id[0]['number2']+1)+"','"+str(j)+"')")
       e['packages_id'] =  int(package_id[0]['number2']+1)
    print("3333",e)
    gensql('insert','revenue_management.rate_days',d['days'])
    #days_id = json.loads(gensql('select','revenue_management.rate_days','rate_days_id',d['days']))
    days_id = json.loads(dbget("select max(rate_days_id) as number3 from revenue_management.rate_days"))
    print("days",days_id[0]['number3'])
    e['rate_days_id'] = int(days_id[0]['number3'])
    print("4444",e)
    gensql('insert','revenue_management.rate_details',e)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))
           
