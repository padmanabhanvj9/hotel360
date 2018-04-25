from sqlwrapper import dbput,gensql
import json

def hotel_rm_post_update_updateroomstatus(request):
    if request.args.get('RM_Room_Status') and request.args.get('RM_Room'):
        room_status = request.args['RM_Room_Status']
        room_no = request.args['RM_Room']
        d,e={},{}
        d['RM_Room_Status'] = room_status
        e['RM_Room'] = room_no
        gensql('update','room_management.RM_Room_List',d,e)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    elif  request.args.get('RM_Room_Status') and request.args.get('Room_List'):
        room_status = request.args['RM_Room_Status']
        room_list = request.args['Room_List']
        a= dbput("update room_management.RM_Room_List  set  RM_Room_Status='"+room_status+"'  where  RM_Room in ("+room_list+")")
        print(a)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    elif  request.args.get('RM_Room_Status') and request.args.get('From_Room') and request.args.get('To_Room'):
        room_status = request.args['RM_Room_Status']
        from_room = request.args['From_Room']
        to_room = request.args['To_Room']
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

