import datetime
from sqlwrapper import gensql, dbget, dbput
import json
from flask import Flask,request, jsonify
app = Flask(__name__)
@app.route("/HOTEL_BBL_POST_INSERT_GroupReservations",methods = ['POST'])
def HOTEL_BBL_POST_INSERT_GroupReservation(request):
    
    d = request.json
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
   # roomtypes = d.get("Res_Room_type")
    block_id = d.get("Res_block_code")
    #psql = json.loads(dbget("select roomtype_count_one, roomtype_count_two, roomtype_count_three, rooms_per_day \
    #              from business_block.business_block where block_id = '"+block_id+"'"))
    #countone = psql[0]['roomtype_count_one']
    #counttwo = psql[0]['roomtype_count_two']
    #countthree = psql[0]['roomtype_count_three']
    sql = json.loads(dbget("SELECT start_date,end_date,nights,pf_id,roomtype_count_one,roomtype_count_two,roomtype_count_three, rooms_per_day,roomtype_one,room_management.room_type.type typeone ,roomtype_two ,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.business_block.roomtype_two) as typetwo,roomtype_three,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.business_block.roomtype_three) as typethree \
                            from business_block.business_block inner join room_management.room_type on room_management.room_type.id = business_block.business_block.roomtype_one where business_block.business_block.block_id = '"+block_id+"'")) 
    psql = json.loads(dbget("select market.marketgroup_description,res_source.sourcedescription,origin.origindescription,confirmation_no from business_block.business_block_definite \
                        left join reservation.market \
                      on reservation.market.id = business_block.business_block_definite.market_id left join reservation.res_source \
                    on reservation.res_source.id = business_block.business_block_definite.source_id left join reservation.origin \
                    on reservation.origin.id = business_block.business_block_definite.origin_id where business_block.business_block_definite.block_id = '"+block_id+"'"))
    print(sql,int(len(sql[0])/2))
    market = psql[0]['marketgroup_description']
    source = psql[0]['sourcedescription']
    origin = psql[0]['origindescription']
    confirmation= psql[0]['confirmation_no']
    startdate = sql[0]['start_date']
    enddate = sql[0]['end_date']
    nights = sql[0]['nights']
    profile = sql[0]['pf_id']
    countone = sql[0]['roomtype_count_one']
    counttwo = sql[0]['roomtype_count_two']
    countthree = sql[0]['roomtype_count_three']
    roomtype_one = sql[0]['typeone']
    roomtype_two = sql[0]['typetwo']
    roomtype_three = sql[0]['typethree']
    number_of_rooms = sql[0]['rooms_per_day']
    number_of_rooms = int(number_of_rooms)
    print(number_of_rooms,type(number_of_rooms))
    print(countone,type(countone))
    print(counttwo,type(counttwo))
    print(countthree,type(countthree))
    print(roomtype_one,type(roomtype_one))
    print(roomtype_two,type(roomtype_two))
    print(roomtype_three,type(roomtype_three))
    #print(countone,counttwo,countthree)
    #keys = list(sql[0].keys())
    #values = list(sql[0].values())
    #print(keys,values,type(keys))
    #k,l = 0,1
    #for i in range(int(len(sql[0])/2)):
    #    print(keys[k],values[k],keys[l],values[l])
    #    k+=2
    #    l+=2
    d['res_arrival'] = startdate
    d['res_depature'] = enddate
    d['res_nights'] = nights
    d['pf_id'] = profile
    d['res_market'] = market
    d['res_source'] = source
    d['res_origin'] = origin
    d['res_confnumber'] = confirmation
    d['res_guest_status'] = "reserved"
    #d['res_block_code'] = block_id
    d['res_number_of_rooms'] = str(1)
    d['created_by'] = "Ranimanagama"
    d['created_on'] = RES_Log_Date
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    d['Res_id'] = Res_id
    for i in range(countone):
        d['res_room_type'] = roomtype_one

        gensql('insert','reservation.res_reservation',d)
    for i in range(counttwo):
        d['res_room_type'] = roomtype_two

        gensql('insert','reservation.res_reservation',d) 
    for i in range(countthree):
        d['res_room_type'] = roomtype_three
  
        gensql('insert','reservation.res_reservation',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

   
