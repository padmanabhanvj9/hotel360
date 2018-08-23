from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_PAC_POST_INSERT_Packages(request):
    d = request.json
    print(d)
    e = { k : v for k,v in d.items() if k not in ('alternates','item_inventory_selected_id')}
    print("0000",e)
    
    alternate_id = json.loads(dbget("select max(alternate_id) as number1 from packages.alternate_selected"))
    print("alternate_id",alternate_id[0]['number1'])
    for i in d['alternates']:
        #pass
        dbput("insert into packages.alternate_selected (alternate_id,package_code_id) \
               values ('"+str(alternate_id[0]['number1']+1)+"','"+str(i)+"') ")
    e['alternates_selected_id'] = int(alternate_id[0]['number1']+1)
    print("1111",e)

    item_inventory_id = json.loads(dbget("select max(item_id) as number2 from packages.item_inventory_selected"))
    print("item_inventory_id",item_inventory_id[0]['number2'])
    for i in d['item_inventory_selected_id']:
        #pass
        dbput("insert into packages.item_inventory_selected (item_id,item_inventory_id) \
               values ('"+str(item_inventory_id[0]['number2']+1)+"','"+str(i)+"') ")
    e['item_inventory_selected_id'] = int(item_inventory_id[0]['number2']+1)
    print("2222",e)
    
    gensql('insert','packages.package_code',e)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))

def HOTEL_PAC_POST_INSERT_Packagesdetails(request):
    d = request.json
    print(d)
    gensql('insert','packages.package_details',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully',
                       'ReturnCode':'RIS'}, sort_keys=True, indent=4))
 
