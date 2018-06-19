from sqlwrapper import dbput,gensql
import json

def Hotel_Rm_Post_Update_Updateroomstatus(request):
    if request.json.get('RM_Room_Status') and request.json.get('RM_Room'):
        room_status = request.json['RM_Room_Status']
        room_no = request.json['RM_Room']
        d,e={},{}
        d['RM_Room_Status'] = room_status
        e['RM_Room'] = room_no
        gensql('update','room_management.RM_Room_List',d,e)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    elif  request.json.get('RM_Room_Status') and request.json.get('Room_List'):
        room_status = request.json['RM_Room_Status']
        room_list = request.json['Room_List']
        a= dbput("update room_management.RM_Room_List  set  RM_Room_Status='"+room_status+"'  where  RM_Room in ("+room_list+")")
        print(a)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    elif  request.json.get('RM_Room_Status') and request.json.get('From_Room') and request.json.get('To_Room'):
        room_status = request.json['RM_Room_Status']
        from_room = request.json['From_Room']
        to_room = request.json['To_Room']
        from_room = int(from_room)
        to_room = int(to_room)  
        stri = ''
        for i in range(from_room,to_room+1):
            i = str(i)
            if stri == '':
               stri += i
            else:
               stri += ','+i 
        print(stri)
        a= dbput("update room_management.RM_Room_List  set  RM_Room_Status='"+room_status+"'  where  RM_Room in ("+stri+")")
        print(a)        
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

