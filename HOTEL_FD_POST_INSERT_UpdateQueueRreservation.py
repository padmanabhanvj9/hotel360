import psycopg2
import datetime
from flask import Flask,request, jsonify
import json
def HOTEL_FD_POST_INSERT_UpdateQueueRreservation(request):
    RM_Qtime = request.json['RM_Qtime']
    RM_Room = request.json['RM_Room']
    RM_Room_Type = request.json['RM_Room_Type']
    RM_Room_Status = request.json['RM_Room_Status']
    RM_FO_Status = request.json['RM_FO_Status']
    PF_Firstname = request.json['PF_Firstname']
    RM_VIP = request.json['RM_VIP']
    PF_Mobileno = request.json['PF_Mobileno']
    RM_Room_Class = request.json['RM_Room_Class']
    

    #RM_Queue = request.json['RM_Queue']
    RM_Queue_Date = datetime.datetime.utcnow().date()
    print(RM_Queue_Date)
    RM_Queue_Date = str(RM_Queue_Date)
    con = psycopg2.connect(user='akvwghpxnyalss',password='bc0080c7c0f0b55e162582666cf6b39227c6160e2759dbb0d7f28d58190952cd',host='ec2-54-235-146-184.compute-1.amazonaws.com',port='5432',database='dfbvc8j8egd076')
    cur = con.cursor()
    #a = { k : v for k,v in d.items() if k == 'PF_Mobileno'}
    #sql_value = gensql('select','room_management.rm_queue_room','count(*)',a)
    sql = "select count(*)from room_management.rm_queue_room where  rm_queue_date='"+RM_Queue_Date+"'"
    print(sql)
    cur.execute(sql)
    i = cur.fetchone()
    for queue_count in i :
        queue_count = int(queue_count)
        print(queue_count)
    if queue_count is 0 :
             sql = "insert into  room_management.rm_queue_room VALUES ('"+RM_Qtime+"','"+RM_Room+"','"+RM_Room_Type+"','"+RM_Room_Status+"','"+RM_FO_Status+"','"+PF_Firstname+"','"+RM_VIP+"',"+PF_Mobileno+",'"+RM_Room_Class+"','0','"+RM_Queue_Date+"')"
             print(sql)
             cur.execute(sql)
             con.commit()

    #sql_value = gensql('insert','room_management.rm_queue_room',d)   
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

    sql= "select rm_queue from room_management.rm_queue_room where rm_queue_date='"+RM_Queue_Date+"'"
    cur.execute(sql)
    i = cur.fetchone()
    for no in i: 
         print(no,type(no))
         no = int(no)
    no+=1
    print(no,type(no))
    no = str(no)
    sql = ("update room_management.rm_queue_room set rm_queue='"+no+"' where rm_queue_date= '"+RM_Queue_Date+"' and pf_mobileno = "+PF_Mobileno+"")
    print(sql)
    cur.execute(sql)
    con.commit()
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
