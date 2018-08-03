import json
from sqlwrapper import gensql,dbget
import datetime

def rateselect(request):
    s = json.loads(dbget("select * from revenue_management.ratecategory"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def ratecodeselect(request):
    s = json.loads(dbget("select * from revenue_management.ratecode"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def marketselect(request):
    s = json.loads(dbget("select * from revenue_management.market"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def sourceselect(request):
    s = json.loads(dbget("select * from revenue_management.source"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def currencyselect(request):
    s = json.loads(dbget("select * from revenue_management.currency"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def room_types(request):
    s = json.loads(dbget("select * from revenue_management.room_type"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def packages_revenue(request):
    s = json.loads(dbget("SELECT * FROM revenue_management.packages_codes"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))
