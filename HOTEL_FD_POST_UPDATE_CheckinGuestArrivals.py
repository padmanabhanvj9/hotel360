
from sqlwrapper import gensql, dbget, dbput
import json
import datetime
def HOTEL_FD_POST_UPDATE_CheckinGuestArrivals(request):
    
   d = request.json
   res_id = d.get("Res_id")
   unique_id = d.get("Res_unique_id")
   pf_id = d.get("pf_id")
   a = {}
   RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
   RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
   print(RES_Log_Time)
   RES_Log_Date = datetime.datetime.utcnow().date()
   print(RES_Log_Date)
   RES_Log_Date = str(RES_Log_Date)
   arrival = dbget("select res_arrival, res_adults,res_room from reservation.res_reservation where res_id = '"+res_id+"' and pf_id = '"+pf_id+"' and res_unique_id = '"+unique_id+"'")
  
   arrival = json.loads(arrival)
   print(arrival)
   print(arrival[0]['res_arrival'],type(arrival[0]['res_arrival']))
   today_arrival = (arrival[0]['res_arrival'])
   adult = arrival[0]['res_adults']
   room = arrival[0]['res_room']
   print(room,type(room))

   print(today_arrival)
   if RES_Log_Date == today_arrival:
       p = {}
       p['res_id'] = res_id
       p['res_unique_id'] = unique_id
       sql_value = gensql('select','room_management.rm_queue_room','rm_queue',p)
       sql_value = json.loads(sql_value)
 
       if len(sql_value) != 0:
          psql = dbput("delete from room_management.rm_queue_room where res_id = '"+res_id+"' and res_unique_id = '"+unique_id+"'")
          print(psql)
       else:
          pass
       e = {}
       e['Res_id'] = res_id
       e['pf_id'] = pf_id
       e['res_unique_id'] = unique_id
       a['Res_guest_status'] = "checkin"
       
       sql_value = gensql('update','reservation.res_reservation',a,e)
       print(sql_value)
       res_id = e.get("Res_id")
       Emp_Id = '121'
       Emp_Firstname = "daisy"
       s = {}
       s['Emp_Id'] = Emp_Id
       s['Emp_Firstname'] = Emp_Firstname
       
       s['RES_Log_Date'] = RES_Log_Date
       s['RES_Log_Time'] = RES_Log_Time
       s['RES_Action_Type'] = "Checkin a guest"
       s['RES_Description'] = "Checked in a guest"
       s['Res_id'] = res_id
       sql_value = gensql('insert','reservation.res_activity_log',s)
       fo_status = "occupied"
       res_status = "checkin"
       sql_value = dbput("update room_management.rm_room_list set rm_fo_status = '"+fo_status+"',rm_reservation_status = '"+res_status+"',rm_fo_person = "+str(adult)+" where rm_room in ("+str(room)+")")
       
       print(sql_value)
       alertcount = json.loads(dbget("select count(*) from reservation.res_alert where res_id = '"+str(res_id)+"' \
                                      and res_unique_id = '"+str(unique_id)+"'"))
       print(alertcount)
       if alertcount[0]['count'] !=0:
          alertvalue = json.loads(dbget("select * from reservation.res_alert where res_id = '"+str(res_id)+"' \
                                      and res_unique_id = '"+str(unique_id)+"'"))
          return(json.dumps({'Status': 'Success', 'StatusCode': '200', 'alertvalue':alertvalue,'Return': 'Alert Got Successfully','ReturnCode':'AGS'}, sort_keys=True, indent=4))
       else:
          
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

       
   else:
      return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Checkin a Today Guest arrivals only','ReturnCode':'CTG'}, sort_keys=True, indent=4))
