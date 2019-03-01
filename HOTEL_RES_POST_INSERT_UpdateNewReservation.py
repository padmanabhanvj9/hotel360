import datetime
from sqlwrapper import gensql, dbget, dbput
import random
import json
from ApplicationDate import application_date

def HOTEL_RES_POST_INSERT_UpdateNewReservation(request):
    d = request.json
    datelist = []
    d = { k : v for k,v in d.items() if  v != ''}
    PF_Mobileno = str(d.get("PF_Mobileno"))
    print(PF_Mobileno)
    RES_Arrival = str(d.get("RES_Arrival"))
    print(RES_Arrival)
    RES_Depature = str(d.get("RES_Depature"))
    RES_Arrival_date = datetime.datetime.strptime(RES_Arrival, '%Y-%m-%d').date()
    initial=datetime.datetime.strptime(d['RES_Depature'], '%Y-%m-%d').date()
    depature_minus = initial - datetime.timedelta(days=1)
    delta = initial - RES_Arrival_date         # timedelta
    print(delta)
   
    sqlcount = ("select count(*) from reservation.res_reservation \
                 where pf_mobileno = '"+PF_Mobileno+"' and RES_Arrival = '"+RES_Arrival+"' and RES_Depature = '"+RES_Depature+"'")
    countdata = dbget(sqlcount)
    countdata = json.loads(countdata)
    print(countdata)
    print(countdata[0]['count'],type(countdata[0]['count']))
    #************************************checkin count for room available***********************
    normal_count = json.loads(dbget("select count(*) from room_management.room_available where rm_date between '"+str(d['RES_Arrival'])+"' \
                                     and '"+str(depature_minus)+"' and rm_room = '"+str(d['RES_Room_Type'])+"'"))
                              
    if delta.days==normal_count[0]['count']:
        pass
    else:

       return(json.dumps({'Status': 'Failure', 'StatusCode': '200','Return': 'Roomtype or date is not Declare','ReturnCode':'RODND'}, sort_keys=True, indent=4)) 
  
    #*****************************************************checking all date room available*****************
    booking_count = json.loads(dbget("select * from room_management.room_available where rm_room= '"+str(d['RES_Room_Type'])+"'\
                                  and rm_date between '"+str(d['RES_Arrival'])+"' and '"+str(depature_minus)+"' order by rm_date"))
    for check_booking in booking_count:
    
      if int(d['RES_Number_Of_Rooms']) > check_booking['available_count']:
        
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Booking is Not Available','ReturnCode':'BNA'}, sort_keys=True, indent=4)) 


        #date1 = date1 + datetime.timedelta(days=7)

    #***********************************reservation already exist*****************************
    if countdata[0]['count'] > 0:
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Reservation Already Exist','ReturnCode':'RAE'}, sort_keys=True, indent=4)) 

    app_datetime = application_date()
    Emp_Id = '121'
    Emp_Firstname = "Admin"
    d['created_on'] = app_datetime[1]
    d['created_by'] = Emp_Firstname
    
    random_no = (random.randint(1000000000,9999999999))
    random_no = str(random_no)
    random_no = random_no[0:4]
    print(random_no)
    mobile = d.get("PF_Mobileno")
    mobile = mobile[0:3]
    mobile = str(mobile)
    conf = mobile + random_no
    print(mobile)
    RES_Confnumber = "PMS" + conf
    print(RES_Confnumber)
    d['RES_Confnumber'] = RES_Confnumber
    d['RES_Guest_Status'] = "reserved"
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    d['Res_id'] = Res_id

    number_of_rooms = d.get("RES_Number_Of_Rooms")
    number_of_rooms = int(number_of_rooms)
    print(number_of_rooms,type(number_of_rooms))
    for number in range(number_of_rooms):
        d['RES_Number_Of_Rooms'] = str(1)
        sql_value = gensql('insert','reservation.res_reservation',d)
        bookedcount = dbput("update room_management.room_available set available_count=available_count - \
                            '"+str(d['RES_Number_Of_Rooms'])+"', \
                            booked_count = booked_count + '"+str(d['RES_Number_Of_Rooms'])+"' where rm_room = \
                            '"+str(d['RES_Room_Type'])+"' and \
                            rm_date between '"+str(d['RES_Arrival'])+"' and '"+str(depature_minus)+"' ")
                                                                                                                
    print(d)
    data = d.get("PF_Firstname")
    number = d.get("RES_Confnumber")
    t = {}
    t['RES_Confnumber'] = number
    reservation_id = gensql('select','reservation.res_reservation','res_id',t)
    reservation_id = json.loads(reservation_id)
    print(reservation_id[0]['res_id'],type(reservation_id[0]['res_id']))
    reservation_id = reservation_id[0]['res_id']
    print(reservation_id,type(reservation_id))
    booking_count = len(str(reservation_id))
    
    RES_Action_Type = "New Reservation"
    RES_Description = "Reservation created successfully for" + " "+data+" "+"with Number of rooms reserved is "+" "+ str(number_of_rooms) + " "+"And the Confirmation Number is" + " " + number
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    app_datetime = application_date()
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    s['Res_id'] = reservation_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':RES_Confnumber,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def Reservationdonutchart():
    app_datetime = application_date()
    RES_Log_Date = app_datetime[1]
    print(RES_Log_Date)
    checkincount = json.loads(dbget("select count(*) from reservation.res_reservation where res_arrival = '"+str(RES_Log_Date)+"' and res_guest_status in ('checkin')"))
    print(checkincount)
    checkout = json.loads(dbget("select count(*) from reservation.res_reservation where res_arrival = '"+str(RES_Log_Date)+"' and res_guest_status in ('Check out')"))
    print(checkout)
    reservation = json.loads(dbget("select count(*) from reservation.res_reservation where created_on = '"+str(RES_Log_Date)+"' and res_guest_status in ('reserved')"))
    print(reservation)
    json_input = [
                   {"title":"checkin","value":checkincount[0]['count'] },
                   {"title":"checkout","value":checkout[0]['count']},
                   {"title":"reservation","value":reservation[0]['count']}
                 ]   
    return(json.dumps({"Return":"Record Retrieved Sucessfully","Return_Code":"RTS","Status": "Success","Status_Code": "200","Returnvalue":json_input},indent=2))
    
