from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_UPDATE_UpdateRatecodeSetup(request):
    d = request.json
    #print(d)
    e = { k : v for k,v in d.items() if k in ('rateheader_id','begin_sell_date','end_sell_date', 
                                              'market_id','source_id','display_sequence','rooms_id','packages_id')}
    print("0000",e)    
    rate_code_details = d['rate_code_details']
    #print("rate_code_details",rate_code_details)
    a = { k : v for k,v in rate_code_details.items()  if k not in ('ratecode_id')}
    b = { k : v for k,v in rate_code_details.items()  if k  in ('ratecode_id')}
    gensql('update','revenue_management.ratecode',a,b)
    e['ratecode_id'] = b['ratecode_id']
    
    sell_controls = d['sell_controls']
    #print("sell_controls",sell_controls)
    a = { k : v for k,v in sell_controls.items()  if k not in ('sell_id')}
    b = { k : v for k,v in sell_controls.items()  if k  in ('sell_id')}
    gensql('update','revenue_management.sell_control',a,b)
    e['sell_control_id'] = b['sell_id']
    
    transaction_details = d['transaction_details']
    #print("transaction_details",transaction_details)
    a = { k : v for k,v in transaction_details.items()  if k not in ('tranction_detail_id')}
    b = { k : v for k,v in transaction_details.items()  if k  in ('tranction_detail_id')}
    gensql('update','revenue_management.tranction_details',a,b)
    e['transaction_details_id'] = b['tranction_detail_id']
    
    components = d['components']
    #print("components",components)
    a = { k : v for k,v in components.items()  if k not in ('components_id')}
    b = { k : v for k,v in components.items()  if k  in ('components_id')}
    gensql('update','revenue_management.rate_components',a,b)
    e['rate_components_id'] = b['components_id']
    
    dbput("delete from revenue_management.rooms_selected where rooms_id='"+str(d['rooms_id'])+"' ")
    
    for i in d['room_types']:
        #pass
        dbput("insert into revenue_management.rooms_selected (rooms_id,room_type_id) \
               values ('"+str(d['rooms_id'])+"','"+str(i)+"') ")
        
    dbput("delete from revenue_management.packages_selected where packages_id='"+str(d['packages_id'])+"' ")
    
    for j in d['package']:
        #pass
        dbput("insert into revenue_management.packages_selected (packages_id,package_code_id) \
               values ('"+str(d['packages_id'])+"','"+str(j)+"')")
        
    a = { k : v for k,v in e.items()  if k not in ('rateheader_id')}
    b = { k : v for k,v in e.items()  if k  in ('rateheader_id')}
    
    print(gensql('update','revenue_management.ratecode_setup',a,b))
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
 
def HOTEL_REM_POST_UPDATE_Negotiated_Rate(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('rate_code_id')}
    b = { k : v for k,v in d.items() if v != '' if k in ('rate_code_id')}    
    gensql('update','revenue_management.negotiated_rate',a,b)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def HOTEL_REM_POST_UPDATE_RATE_DETAILS(request):
    d = request.json
    #print(d)
    x = { k : v for k,v in d.items() if k in ('days')}
    #print("x",x)
    a = x['days']
    #print("a",a)
    b = { k : v for k,v in d.items() if k in ('rate_days_id') if k not in ('days')}
    #print("b",b)
    gensql('update','revenue_management.rate_days',a,b)

    dbput("delete from revenue_management.rooms_selected where rooms_id='"+str(d['rooms_id'])+"' ")
    
    for i in d['room_types']:
        #pass
        dbput("insert into revenue_management.rooms_selected (rooms_id,room_type_id) \
               values ('"+str(d['rooms_id'])+"','"+str(i)+"') ")
    if d['rate_tier_id'] != 0:
       dbput("delete from revenue_management.packages_selected where packages_id='"+str(d['packages_id'])+"' ")
    
       for j in d['package']:
        #pass
          dbput("insert into revenue_management.packages_selected (packages_id,package_code_id) \
                values ('"+str(d['packages_id'])+"','"+str(j)+"')")

    b = { k : v for k,v in d.items() if k in ('rate_details_id')}
    a = { k : v for k,v in d.items() if k not in ('rate_details_id','days','room_types','package')}
    gensql('update','revenue_management.rate_details',a,b)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))




    
