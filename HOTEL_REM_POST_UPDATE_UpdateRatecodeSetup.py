from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup(request):
    d = request.json
    print(d)
    e = { k : v for k,v in d.items() if k in ('begin_sell_date','end_sell_date','market_id','source_id','display_sequence')}
    print("0000",e)    
    rate_code_details = d['rate_code_details']
    print(rate_code_details)
    sell_controls = d['sell_controls']
    print(sell_controls)
    transaction_details = d['transaction_details']
    print(transaction_details)
    components = d['components']
    print(components)
    room_types = d['room_types']
    print("room_types",room_types,type(room_types))
    package = d['package']
    print("package",package,type(package))    
    #gensql('update','',a,e)
    a,e = {},{}
    a = { k : v for k,v in d.items() if v != '' if k not in ('block_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('block_id')}
    return(json.dumps({"Status": "Success","StatusCode": "200"},indent=4))
 
def HOTEL_REM_POST_UPDATE_Negotiated_Rate(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('rate_code_id')}
    b = { k : v for k,v in d.items() if v != '' if k in ('rate_code_id')}    
    gensql('update','revenue_management.negotiated_rate',a,b)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    
