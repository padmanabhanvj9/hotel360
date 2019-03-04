from sqlwrapper import dbget,gensql,dbput
import json

def hotel_rm_post_select_queryroomlist(request):
    sql = 'select * from room_management.RM_Room_List order by rm_room'
    print(sql)      
    db_res = json.loads(dbget(sql))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':db_res  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_insert_roomcount(request):
   d = request.json

   sqlcount = json.loads(dbget("select count(*) from room_management.room_available where rm_room = '"+str(d['rm_room'])+"' \
                                and rm_date = '"+str(d['rm_date'])+"'"))
   print(sqlcount)
   if sqlcount[0]['count'] == 0:
       gensql('insert','room_management.room_available',d)
       return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                      "Status": "Success","StatusCode": "200"},indent=4))

   else:
       print("else part")

       dbput("update room_management.room_available set available_count = available_count + "+str(d['available_count'])+" ,total_count = total_count + "+str(d['total_count'])+" \
            where rm_room = '"+str(d['rm_room'])+"' and rm_date= '"+str(d['rm_date'])+"' ")
       return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                      "Status": "Success","StatusCode": "200"},indent=4))

   
