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
     s = json.loads(dbget("SELECT currency.id,currency.currency,currency.currency_description, \
                         * FROM packages.package_code \
                         left join profile.currency on currency.id = package_code.currency_id"))
     print(s)
     return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))

def season_code_revenue(request):
    s = json.loads(dbget("select * from revenue_management.season_code"))
    print(s)
    return(json.dumps({"Return": s,"Status": "Success","StatusCode": "200"},indent=4))


def Insert_season_code_revenue(request):
    d = request.json
    gensql('insert','revenue_management.season_code',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))
