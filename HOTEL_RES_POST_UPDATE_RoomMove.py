from sqlwrapper import gensql,dbget, dbput
import json
def HOTEL_RES_POST_UPDATE_RoomMove(request):
    d = request.json
    res_id = d.get("Res_id")
    res_room = d.get("Res_room")
    sql_value = dbget("select res_room from reservation.res_reservation \
                       where res_id = '"+res_id+"'")
    sql_value = json.loads(sql_value)
    if len(sql_value) != 0:
          data = '0'
          psql = dbput("update reservation.res_reservation set res_room='"+data+"' where res_id = '"+res_id+"'")
          print(psql)
          a,e = {},{}
          e['Res_id'] = res_id
          a['Res_room'] = res_room
          sql_value = gensql('update','reservation.res_reservation',a,e)
          print(sql_value)
          return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

