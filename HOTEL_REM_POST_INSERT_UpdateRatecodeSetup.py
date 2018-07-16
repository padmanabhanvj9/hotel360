from sqlwrapper import gensql, dbget
import datetime
import json
def HOTEL_REM_POST_INSERT_UpdateRatecodeSetup(request):
    d = request.json
    today_date = str(datetime.datetime.utcnow().date())
    #end_sell_date = datetime.datetime.utcnow().date()
    begin_date = d.get("Begin_sell_date")
    print(begin_date,type(begin_date))
    end_date = d.get("End_sell_date")
    print(end_date, type(end_date))
    roomtype = d.get("Roomtype_id")
    print(roomtype)
    no = roomtype.split(',')
    print(no)
    #roomtype = roomtype.replace(',','')
    if today_date <= begin_date and begin_date <= end_date:
     for i in no:
       
       print(i)
       print('insert',i)
       d['Roomtype_id'] = i     
       gensql('insert','revenue_management.ratecode_setup',d)
     ratecode = d.get("Ratecode_id")
     rate = json.loads(dbget("select rate_description from revenue_management.ratecode where ratecode_id='"+ratecode+"'"))
       #rate = str(json.loads([0]['rate_description']))
     rate = rate[0]['rate_description']
     print(rate)
     roomtype = json.loads(dbget("select type from room_management.room_type where id in ("+roomtype+")"))
     print(roomtype)
     str1 = ''
     for i in roomtype:
           print(i)
           if len(str1) == 0:  
              str1 += str(i['type'])
           else:
              str1 += ','+ str(i['type'])
     print('string',str1)
     roomtype = str(roomtype[0]['type'])
     print(roomtype)
     begin_date = d.get("Begin_sell_date")
     end_date = d.get("End_sell_date")
     RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
     RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
     print(RES_Log_Time)
     RES_Log_Date = datetime.datetime.utcnow().date()
     print(RES_Log_Date)
     s = {}
     s['date'] = RES_Log_Date
     s['time'] = RES_Log_Time
     s['emp_name'] = "Daisy"
     s['action_type'] = "Rate setup for "+" "+rate
     s['action_description'] = rate+" "+"allow for these roomtype"+" "+str1
     s['rate_code_id'] = ratecode
     gensql('insert','revenue_management.revenue_activity_log',s)
    
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    else:
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Rate Setup only for upcoming days not past date','ReturnCode':'RS'}, sort_keys=True, indent=4))   
