import datetime
from sqlwrapper import gensql, dbget, dbput
import json
from flask import Flask,request, jsonify
app = Flask(__name__)

def HOTEL_BBL_POST_INSERT_BusinessBlockDefinite(request):
    d = request.json
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    #print(RES_Log_Date)
    x,y,z,p,q,result_dic = {},{},{},{},{},{}
#<--------------------definite-------------------------------->
    #x = { k : v for k,v in d.items() if  k  in ('Definite')}
    #print(x)
    x = d['Definite']
    x = { k : v for k,v in x.items() if  v != ''}
    print("Definite",x,type(x),len(x))
    if len(x) != 0:
        sqlvalue = json.loads(dbget("select confirmation_no from business_block.group_confirmation"))
        print(sqlvalue,type(sqlvalue))
        sqlvalue = int(sqlvalue[0]['confirmation_no'])

        
        confirmation_no = sqlvalue + 1
        print(confirmation_no,type(confirmation_no))
        psql = dbput("update business_block.group_confirmation set confirmation_no = '"+str(confirmation_no)+"'")
        print(psql)
        x['confirmation_no'] = confirmation_no
        result_dic['ConfirmationNumber'] = confirmation_no
        sql1 = gensql('insert','business_block.business_block_definite',x)
        print(sql1)
      
    else:
       pass
#<---------------------------rooms tab-------------------------->   
    #y = { k : v for k,v in d.items()if v != ''  if  k  in ('Rooms')}
    y = d['Rooms']
    y = { k : v for k,v in y.items() if  v != ''}
    print("Rooms",y,type(y),len(y))
    if len(y) != 0:
        sql2 = gensql('insert','business_block.block_room',y)
        print(sql2)
        s = {}
        s['user_role'] = "Supervisor"
        blockid = y.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Group Reservation"
        s['description'] = "Group Confirmation Number is"+" "+str(confirmation_no)
        gensql('insert','business_block.business_block_activity_log',s)
    else:
        pass
#<------------------------details tab----------------------------->    
    #z = { k : v for k,v in d.items()if v != ''  if  k  in ('Block_details')}
    z = d['Block_details']
    z = { k : v for k,v in z.items() if  v != ''}
    print("Block_details",z,type(z),len(z))
    if len(z) != 0:
        sql3 = gensql('insert','business_block.block_business_details',z)
        print(sql3)
        s = {}
        s['user_role'] = "Supervisor"
        blockid = z.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Business Block Details"
        s['description'] = "Business Block Details for"+" "+str(blockid)
        gensql('insert','business_block.business_block_activity_log',s)
    else:
        pass
#<---------------------------------catering----------------------->    
    #p = { k : v for k,v in d.items()if v != ''  if  k  in ('Catering')}
    #print(p)
    p = d['Catering']
    p = { k : v for k,v in p.items() if  v != ''}
    print("Catering",p,type(p),len(p))
    if len(p) != 0:
        sql4 = gensql('insert','business_block.block_catering',p)
        print(sql4)
        s = {}
        s['user_role'] = "Supervisor"
        blockid = p.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Block Catering"
        s['description'] = "Block Catering for"+" "+str(blockid)
        gensql('insert','business_block.business_block_activity_log',s)
        
    else:
        pass
#<---------------------------cancelroom & catering----------------->   
    #q = { k : v for k,v in d.items()if v != ''  if  k  in ('Cancel')}
    q = d['Catering Cancel']
    q = { k : v for k,v in q.items() if  v != ''}
    r = d['Room Cancel']
    r = { k : v for k,v in r.items() if  v != ''}
    print("Room Cancel",r,type(r),len(r))
    print("Catering Cancel",q,type(q),len(q))
    if len(q) != 0:
        sql_value = json.loads(dbget("select catering_cancel_no from business_block.catering_cancel_no"))
        sql_value1 = sql_value[0]['catering_cancel_no']
        cancel_no = sql_value1 + 1
        psql = dbput("update business_block.catering_cancel_no set catering_cancel_no = '"+str(sql_value[0]['catering_cancel_no']+1)+"'")
        q['catering_cancel_no'] = cancel_no
        result_dic['CateringCancellation'] = cancel_no
        sql5 =  gensql('insert','business_block.block_cancel_catering',q)
      
        s = {}
        s['user_role'] = "Supervisor"
        blockid = q.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Catering cancel"
        s['description'] = "Catering  cancelled for"+" "+str(blockid)
        gensql('insert','business_block.business_block_activity_log',s)
    elif len(r) !=  0:
            sql_value = json.loads(dbget("select room_cancel_no from business_block.room_cancel_no"))
            sql_value1 = sql_value[0]['room_cancel_no']
            room_cancel_no = sql_value1 + 1 
            psql = dbput("update business_block.room_cancel_no set room_cancel_no = '"+str(sql_value[0]['room_cancel_no']+1)+"'")
       
            q['room_cancel_no'] = room_cancel_no
            result_dic['RoomCancellation'] = room_cancel_no
            sql5 =  gensql('insert','business_block.block_cancel_catering',q)
          
            s = {}
            s['user_role'] = "Supervisor"
            blockid = q.get("block_id")

            s['date'] = RES_Log_Date
            s['time'] = RES_Log_Time
            s['block_id'] = blockid
            s['action_type_id'] = "Room cancel"
            s['description'] = "Room cancelled for"+" "+str(blockid)
            gensql('insert','business_block.business_block_activity_log',s)
  
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':confirmation_no,'RoomCancellation':room_cancel_no,'CateringCancellation':cancel_no,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    print(result_dic)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Number':result_dic,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
   
