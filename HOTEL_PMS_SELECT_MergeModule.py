from sqlwrapper import gensql, dbget,dbput
import json
import datetime

date = json.loads(dbget("select roll_business_date from endofday.business_date"))
print(date)
next_day = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    
def Hotel_PMS_Select_GetTodayRoomAvailabilityArrival(request):
    
    final = []
    todays_date = datetime.datetime.utcnow().date()
    sql = json.loads(dbget("SELECT 'checkin' as dash_board ,COUNT(*) FROM reservation.res_reservation WHERE res_guest_status='checkin' and res_arrival='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            SELECT 'checkout' , COUNT(*) FROM reservation.res_reservation WHERE res_guest_status='Check out' and res_depature='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            SELECT 'arrival' ,COUNT(*) FROM reservation.res_reservation WHERE res_guest_status ='arrival' and res_arrival='"+str(date[0]['roll_business_date'])+"' \
                            union \
                            select 'due_out' , count(*) from reservation.res_reservation where res_guest_status='due out' and  res_depature ='"+str(next_day)+"' \
                            union \
                            select 'reservation' ,count(*) from reservation.res_reservation where created_on='"+str(date[0]['roll_business_date'])+"' \
                            union  \
                            select 'room_availability' ,count(*) from room_management.rm_room_list where rm_reservation_status='not reserved'  "))
    print(sql)
   
   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))

