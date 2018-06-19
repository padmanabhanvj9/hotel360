from sqlwrapper import gensql,dbfetch
import json

def hotel_rm_post_update_updateroomdiscrepancies(request):
    i = {}
    if request.json.get('RM_Room') and request.json.get('RM_HK_Status'):
        RM_Room = request.json['RM_Room']
        RM_HK_Status = request.json['RM_HK_Status']
        res = dbfetch("select rm_fo_status from room_management.RM_Room_List where RM_Room = "+RM_Room+"")
        res = res[0]
        d,e = {},{}
        e['RM_Room'] = RM_Room
        d['RM_HK_Status'] = RM_HK_Status
        print(gensql('update','room_management.RM_Room_List',d,e))
        if res != RM_HK_Status:
            print(res,RM_HK_Status)
            if res == 'occupied' and RM_HK_Status == 'vaccant':
               i['rm_room_discrepancy'] = 'sleep'
               i['rm_room'] = RM_Room
            else:
               i['rm_room_discrepancy'] = 'skip'
               i['rm_room'] = RM_Room
            print(gensql('insert','room_management.rm_room_discrepancy',i))
        #print(gensql('update','room_management.RM_Room_List',d,e))    
    elif request.json.get('RM_Room') and request.json.get('RM_HK_Person'):
        RM_Room = request.json['RM_Room']
        RM_HK_Person = request.json['RM_HK_Person']
        res = dbfetch("select rm_fo_person from room_management.RM_Room_List where RM_Room = "+RM_Room+"")
        res = res[0]
        print(type(res))
        d,e = {},{}
        e['RM_Room'] = RM_Room
        d['RM_HK_Person'] = RM_HK_Person
        print(gensql('update','room_management.RM_Room_List',d,e))
        if res != RM_HK_Person:    
            i['rm_room_discrepancy'] = 'person'
            i['rm_room'] = RM_Room
            print(gensql('insert','room_management.rm_room_discrepancy',i))    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    
#print(gensql('update','room_management.RM_Room_List',d,e))
