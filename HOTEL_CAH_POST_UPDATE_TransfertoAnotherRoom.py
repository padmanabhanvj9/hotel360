import json
from sqlwrapper import gensql,dbput
import datetime
from ApplicationDate import application_date
def HOTEL_CAH_POST_UPDATE_TransfertoAnotherRoom(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','Res_room')}
    print("a",a)
    e = { k : v for k,v in d.items() if k != '' if k in ('Res_id','Res_room')}
    print("e",e)
    #option = a['transfer_option']
    #print(option)
    if a['transfer_option'] == "GP":
        pass
    elif a['transfer_option'] == "EF":
        print(dbput("update cashiering.billing_post set res_room="+a['to_room']+" \
                     where Res_id="+e['Res_id']+" and Res_room="+e['Res_room']+" "))
        #return(json.dumps({'Status': 'Success', 'StatusCode': '200', \
        #                   'Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
    else:
        print(dbput("update cashiering.billing_post set res_room="+a['to_room']+" \
                     where Res_id="+e['Res_id']+" and Res_room="+e['Res_room']+" and checkno='"+str(a['checkno'])+"' "))
        #return(json.dumps({'Status': 'Success', 'StatusCode': '200', \
        #                   'Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))    
        
    
    #sql_value = gensql('update','cashiering.billing_post',a,e)
    
    #print(sql_value)
    app_datetime = application_date()
    res_id = e.get("Res_id")
    window = str(a.get("res_room"))
    Posting_date = app_datetime[1]
    Revenue_date = app_datetime[1]

    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Admin"
    s['User_name'] = "Admin"
    s['Res_id'] = res_id
    s['Posting_action'] = "Window Transfer to Window "+ ""+window
    s['Posting_reason'] = "window Transfer to window "+ " "+window+" reservation id "+res_id
    s['Posting_description'] = "Transfer charges from one window to another window successfully"
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_changes_history_log',s)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    
