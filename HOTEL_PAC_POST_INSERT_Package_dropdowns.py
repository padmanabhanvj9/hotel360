from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_PAC_POST_INSERT_Forecastgroup(request):
    d = request.json
    gensql('insert','packages.forecast_group',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Transactioncode(request):
    d = request.json
    gensql('insert','packages.transaction_details',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Attributes(request):
    d = request.json
    gensql('insert','packages.attributes',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Postingrhythm(request):
    d = request.json
    gensql('insert','packages.posting_rhythm',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Calculaterule(request):
    d = request.json
    gensql('insert','packages.calculate_rule',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Iteminventory(request):
    d = request.json
    gensql('insert','packages.item_inventory',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))
