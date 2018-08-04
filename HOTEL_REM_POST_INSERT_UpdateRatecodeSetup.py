from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_INSERT_UpdateRatecodeSetup(request):
    d = request.json
    #print(d)
    e = { k : v for k,v in d.items() if k in ('begin_sell_date','end_sell_date','market_id','source_id','display_sequence')}
    print("0000",e)
    #rate_code_details = d['rate_code_details']
    #print(rate_code_details)
    #sell_controls = d['sell_controls']
    #print(sell_controls)
    #transaction_details = d['transaction_details']
    #print(transaction_details)
    #components = d['components']
    #print(components)
    #room_types = d['room_types']
    #print("room_types",room_types,type(room_types))
    #package = d['package']
    #print("package",package,type(package))
    gensql('insert','revenue_management.ratecode',d['rate_code_details'])
    #chang to max
    ratecode_id = json.loads(gensql('select','revenue_management.ratecode','max(ratecode_id) as id1',d['rate_code_details']))
    print(ratecode_id[0]['id1'])
    e['ratecode_id'] = ratecode_id[0]['id1']
    print("1111",e)
    room_types = d['room_types']
    room_id = json.loads(dbget("select max(rooms_id) as number1 from revenue_management.rooms_selected"))
    print("room_id",room_id[0]['number1'])
    for i in d['room_types']:
        #pass
        dbput("insert into revenue_management.rooms_selected (rooms_id,room_type_id) \
               values ('"+str(room_id[0]['number1']+1)+"','"+str(i)+"') ")
    e['rooms_id'] = int(room_id[0]['number1']+1)
    print("2222",e)
    package_id = json.loads(dbget("select max(packages_id) as number2 from revenue_management.packages_selected"))
    print("package_id",package_id[0]['number2'],type(package_id[0]['number2']))
    for j in d['package']:
        #pass
        dbput("insert into revenue_management.packages_selected (packages_id,package_code_id) \
               values ('"+str(package_id[0]['number2']+1)+"','"+str(j)+"')")
    e['packages_id'] =  int(package_id[0]['number2']+1)
    print("3333",e)
    gensql('insert','revenue_management.sell_control',d['sell_controls'])
    # change to max
    sell_id = json.loads(gensql('select','revenue_management.sell_control','max(sell_id) as id2',d['sell_controls']))
    print("sell_id",sell_id[0]['id2'])
    e['sell_control_id'] = int(sell_id[0]['id2'])
    print("4444",e)
    gensql('insert','revenue_management.tranction_details',d['transaction_details'])
    # change to max
    transaction_detail_id = json.loads(gensql('select','revenue_management.tranction_details','max(tranction_detail_id) as id3',d['transaction_details']))
    print("transaction_detail_id",transaction_detail_id[0]['id3'])
    e['transaction_details_id'] = int(transaction_detail_id[0]['id3'])
    print("5555",e)
    gensql('insert','revenue_management.rate_components',d['components'])
    # change to max
    components_id = json.loads(gensql('select','revenue_management.rate_components','max(components_id) as id4',d['components']))
    print("components_id",components_id[0]['id4'])
    e['rate_components_id'] = int(components_id[0]['id4'])
    print("6666",e)
    gensql('insert','revenue_management.ratecode_setup',e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
