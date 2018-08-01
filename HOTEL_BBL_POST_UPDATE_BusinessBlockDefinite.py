import datetime
from sqlwrapper import gensql, dbget, dbput
import json
def HOTEL_BBL_POST_UPDATE_BusinessBlockDefinite(request):
    d = request.json
    
    x,y,z,p,r,a,e,b,c ,f,g,h,i,m,n,u,w = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
    rm_can1,rm_can2,cat_can1,cat_can2,result_dic ={},{},{},{},{}
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    #print(RES_Log_Date)
    
    x = d['Definite']
   
    a = { k : v for k,v in x.items() if v != '' if k not in ('block_id')}
    print(a)
    e = { k : v for k,v in x.items() if k != '' if k in ('block_id')}
    print(e)
     
    print("Definite",a,type(a),len(a))
    if len(a) != 0:
       sql1 = gensql('update','business_block.business_block_definite',a,e)
       print(sql1)
       s = {}
       blockid = e.get("block_id")
       s['user_role'] = "Supervisor"
       s['date'] = RES_Log_Date
       s['time'] = RES_Log_Time
       s['block_id'] = blockid
       s['action_type_id'] = "Update block header"
       values = a.values()
       print(values)
       RES_Description = ''
       for i in values:
        if  RES_Description == '':
           RES_Description +=  i 
        else:
           RES_Description +=  "|" + i
       print(RES_Description)
    
       s['description'] = RES_Description
       gensql('insert','business_block.business_block_activity_log',s)
      
    else:
       pass
    #<---------------------------rooms tab-------------------------->   
    #y = { k : v for k,v in d.items()if v != ''  if  k  in ('Rooms')}
    y = d['Rooms']
    
    b = { k : v for k,v in y.items() if v != '' if k not in ('block_id')}
    print(b)
    c = { k : v for k,v in y.items() if k != '' if k in ('block_id')}
    print(c)
    
    print("Rooms",b,type(b),len(b))
    if len(b) != 0:
        
        sql2 = gensql('update','business_block.block_room',b,c)
        print(sql2)
        
    else:
        pass
    #<------------------------details tab----------------------------->    
    #z = { k : v for k,v in d.items()if v != ''  if  k  in ('Block_details')}
    z = d['Block_details']
   
    f = { k : v for k,v in z.items() if v != '' if k not in ('block_id')}
    print(f)
    g = { k : v for k,v in z.items() if k != '' if k in ('block_id')}
    print(g)
    print("Block_details",f,type(f),len(f))
    if len(f) != 0:
        
        sql3 = gensql('update','business_block.block_business_details',f,g)
        print(sql3)

    else:
        pass
    #<---------------------------------catering----------------------->    
    #p = { k : v for k,v in d.items()if v != ''  if  k  in ('Catering')}
    #print(p)
    p = d['Catering']
   
    h = { k : v for k,v in p.items() if v != '' if k not in ('block_id')}
    print(h)
    i = { k : v for k,v in p.items() if k != '' if k in ('block_id')}
    print(i)
    print("Catering",h,type(h),len(h))
    if len(h) != 0:
        
        sql4 = gensql('update','business_block.block_catering',h,i)
        print(sql4)
        
    else:
        pass



    #<--------------------------------concurrent meeting tab-------------------------------->
    r = d['block_meeting']
    
    m = { k : v for k,v in r.items() if v != '' if k not in ('block_id')}
    print(m)
    n = { k : v for k,v in r.items() if k != '' if k in ('block_id')}
    print(n)
    print("block_meeting",m,type(m),len(m))
    if len(m) != 0:
        
        sql5 = gensql('update','business_block.block_meeting',m,n)
        print(sql5)
    #<---------------------room cancel or catering cancel------------------------------------>
        
    u = d['Catering Cancel']
    cat_can1 = { k : v for k,v in u.items() if v != '' }
    print(cat_can1)
    
    w = d['Room Cancel']
    rm_can1 = { k : v for k,v in w.items() if v != '' }
    print(rm_can1)
    
    print("Room Cancel",rm_can1,type(rm_can1),len(rm_can1))
    print("Catering Cancel",cat_can1,type(cat_can1),len(cat_can1))
    if len(cat_can1) != 0:
        sql_value = json.loads(dbget("select catering_cancel_no from business_block.catering_cancel_no"))
        sql_value1 = sql_value[0]['catering_cancel_no']
        cancel_no = sql_value1 + 1
        psql = dbput("update business_block.catering_cancel_no set catering_cancel_no = '"+str(sql_value[0]['catering_cancel_no']+1)+"'")
        cat_can1['catering_cancel_no'] = cancel_no
        result_dic['CateringCancellation'] = cancel_no
        sql5 =  gensql('insert','business_block.block_cancel_catering',cat_can1)
      
        s = {}
        s['user_role'] = "Supervisor"
        blockid = cat_can1.get("block_id")

        s['date'] = RES_Log_Date
        s['time'] = RES_Log_Time
        s['block_id'] = blockid
        s['action_type_id'] = "Catering cancel"
        s['description'] = "Catering  cancelled for"+" "+str(blockid)
        gensql('insert','business_block.business_block_activity_log',s)
    elif len(rm_can1) !=  0:
            sql_value = json.loads(dbget("select room_cancel_no from business_block.room_cancel_no"))
            sql_value1 = sql_value[0]['room_cancel_no']
            room_cancel_no = sql_value1 + 1 
            psql = dbput("update business_block.room_cancel_no set room_cancel_no = '"+str(sql_value[0]['room_cancel_no']+1)+"'")
       
            rm_can1['room_cancel_no'] = room_cancel_no
            result_dic['RoomCancellation'] = room_cancel_no
            sql5 =  gensql('insert','business_block.block_cancel_catering',rm_can1)
          
            s = {}
            s['user_role'] = "Supervisor"
            blockid = rm_can1.get("block_id")

            s['date'] = RES_Log_Date
            s['time'] = RES_Log_Time
            s['block_id'] = blockid
            s['action_type_id'] = "Room cancel"
            s['description'] = "Room cancelled for"+" "+str(blockid)
            gensql('insert','business_block.business_block_activity_log',s)
  

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','Number':result_dic,'ReturnCode':'RUS'}, sort_keys=True, indent=4))
   
