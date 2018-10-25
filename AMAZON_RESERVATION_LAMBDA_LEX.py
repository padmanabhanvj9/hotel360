from sqlwrapper import gensql,dbget,dbput
import json
from flask import Flask,request, jsonify
import datetime
def AMAZON_RESERVATION_LAMBDA_LEX(request):
    d = {}
    arrivalsdate = request.args.get('arrival')
    depaturedate = request.args.get('depature')
    #arrivalsdate = request.json['arrival']
    #depaturedate = request.json['depature']
    d['arrival']  = arrivalsdate
    d['depature']  = depaturedate
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    #reservation = {'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}], sort_keys=True, indent=4))
def amazon_insert(request):
    d = {}
    arrivalsdate = request.json['arrival']
    depaturedate = request.json['depature']
    d['arrival']  = arrivalsdate
    d['depature']  = depaturedate
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    #reservation = {'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}], sort_keys=True, indent=4))
def CheckConfirmation(request):
    no = request.json['confirmation_number']
    print(no)
    no = no.upper()
    c_no = b_id = json.loads(dbget("select count(*) from reservation.res_reservation where \
                                    res_confnumber= '"+no+"' "))
    print(c_no[0]['count'],type(c_no[0]['count']))
    if c_no[0]['count'] != 0 : 
       return(json.dumps({"ServiceStatus":"Success","Return_code":"Valid"}))
    else:
       return(json.dumps({"ServiceStatus":"Success","Return_code":"Invalid"}))
def checkinguest(request):
    
        confir = request.json['confirmation_number']
        confir = confir.upper()
        mobile = request.json['mobile']
        #phone = request.json['mobile']
        RES_Log_Date = datetime.datetime.utcnow().date()
        print(RES_Log_Date)
        RES_Log_Date = str(RES_Log_Date)
        psql = json.loads(dbget("select res_arrival from reservation.res_reservation where res_confnumber = '"+confir+"' and pf_mobileno = '"+mobile+"'"))
        print(psql)
        #today_arrival = psql[0]['res_arrival']
        if RES_Log_Date == psql[0]['res_arrival']:
            sql = dbput("update reservation.res_reservation set res_guest_status = 'checkin' where res_confnumber = '"+confir+"'")
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'checkin success','ReturnCode':'Valid'}, sort_keys=True, indent=4))
   
        else:
              return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Checkin a Today Guest arrivals only','ReturnCode':'Invalid'}, sort_keys=True, indent=4))

        #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Please say valid mobile number','ReturnCode':'Invalid'}, sort_keys=True, indent=4))
   
def Checkroom(request):
        confir = request.json['confirmation_number']
        confir = confir.upper()
        room = request.json['Room']
        c_no = b_id = json.loads(dbget("select count(*) from reservation.res_reservation where \
                                    res_confnumber= '"+confir+"' and res_room = '"+room+"' "))
        if c_no[0]['count'] != 0 : 
          return(json.dumps({"StatusCode":"Success","Return_code":"Valid"}))
        else:
          return(json.dumps({"StatusCode":"Failure","Return_code":"Invalid"}))
