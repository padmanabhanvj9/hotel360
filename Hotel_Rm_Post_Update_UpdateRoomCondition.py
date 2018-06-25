from sqlwrapper import gensql,dbfetch
import json

def hotel_rm_post_update_updateroomcondition(request):
   dict1 = request.json
   print(dict1)
   e = { k : v for k,v in dict1.items() if k in ('rm_room')}
   print(e)
   d = { k : v for k,v in dict1.items() if k not in ('rm_room')}
   print(d)
   print(gensql('update','room_management.rm_room_condition',d,e))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    

