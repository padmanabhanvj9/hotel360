from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_PAC_POST_UPDATE_Packages(request):
    d = request.json
    print(d)
    x = { k : v for k,v in d.items() if k not in ('alternates','alternate_id',
                                                  'item_inventory_selected_id','item_id')}
    print("adsfasd",x)
    
    dbput("delete from packages.item_inventory_selected where item_id='"+str(d['item_id'])+"' ")
    
    for i in d['item_inventory_selected_id']:
        #pass
        dbput("insert into packages.item_inventory_selected (item_id,item_inventory_id) \
               values ('"+str(d['item_id'])+"','"+str(i)+"') ")
        
    dbput("delete from packages.alternate_selected where alternate_id='"+str(d['alternate_id'])+"' ")
    
    for i in d['alternates']:
        #pass
        dbput("insert into packages.alternate_selected (alternate_id,package_code_id) \
               values ('"+str(d['alternate_id'])+"','"+str(i)+"') ")
       
    
    d={}
    a = { k : v for k,v in x.items()  if k in ('package_code_id')}
    b = { k : v for k,v in x.items()  if k  not in ('package_code_id') }
    #c = { k : v for k,v in b.items()  if k  not in ('package_code') }
    print("a.......",a['package_code'])
    b['package_code'] = a['package_code']
    print("b.......values",b)
    d['package_code_id'] = a['package_code_id']
    print(d)
    gensql('update','packages.package_code',b,d)
      
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4)) 
