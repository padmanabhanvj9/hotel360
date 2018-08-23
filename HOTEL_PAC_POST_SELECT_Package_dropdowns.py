from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_PAC_POST_SELECT_Forecastgroup(request):
    d = request.json
    x = json.loads(dbget("select * from packages.forecast_group"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))    

def HOTEL_PAC_POST_SELECT_Transactioncode(request):
    d = request.json
    x = json.loads(dbget("select * from packages.transaction_details"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))    

def HOTEL_PAC_POST_SELECT_Postingrhythm(request):
    d = request.json
    x = json.loads(dbget("select * from packages.posting_rhythm"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))    

def HOTEL_PAC_POST_SELECT_Calculaterule(request):
    d = request.json
    x = json.loads(dbget("select * from packages.calculate_rule"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))    

def HOTEL_PAC_POST_SELECT_Iteminventory(request):
    d = request.json
    x = json.loads(dbget("select * from packages.item_inventory"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))    
