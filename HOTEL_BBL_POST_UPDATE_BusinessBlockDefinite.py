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
    y = d['Rooms']
    block_id = y.get("block_id")
    #y = { k : v for k,v in r.items() if v != '' }
    print("jiok",y)
    sqlcount = json.loads(dbget("select count(*) from business_block.block_room where block_id ='"+block_id+"'"))
    #print(sqlcount)
    #b['block_id'] = block_id
    print("values",y)
    b = { k : v for k,v in y.items() if v != '' if k not in ('block_id')}
    print(b)
    #c['block_id'] = block_id
    c = { k : v for k,v in y.items() if k != '' if k in ('block_id')}
    print(c)
    
    #print("Rooms",b,type(b),len(b))  
    #print("block_meeting",m,type(m),len(m))
    y = { k : v for k,v in r.items() if v != '' }
    if sqlcount[0]['count'] == 0:
            print("insert room")
            #y = { k : v for k,v in r.items() if v != '' }
            #print("value is empty in room",y)
            gensql('insert','business_block.block_room',y)

    elif len(b)!=0:
        print("update room")
        sql2 = gensql('update','business_block.block_room',b,c)
        print(sql2)
        
   # else:
       # pass
    #<------------------------details tab----------------------------->    
    #z = { k : v for k,v in d.items()if v != ''  if  k  in ('Block_details')}
    z = d['Block_details']
    block_id = z.get("block_id")
    #z = { k : v for k,v in p.items() if v != ''}
    print("block details",z)
    sqlcount = json.loads(dbget("select count(*) from business_block.block_business_details where block_id ='"+block_id+"'"))
    print("deatils count",sqlcount)
    f = { k : v for k,v in z.items() if v != '' if k not in ('block_id')}
    print(f)
    g = { k : v for k,v in z.items() if k != '' if k in ('block_id')}
    print(g)
    #print("Block_details",f,type(f),len(f))
    z = { k : v for k,v in z.items() if v != ''}
    print(z)
    if sqlcount[0]['count'] == 0:
            print("insert details")
            #z = { k : v for k,v in p.items() if v != ''}
            gensql('insert','business_block.block_business_details',z)
         
    elif len(f) !=0 :
        print("update details")
        sql3 = gensql('update','business_block.block_business_details',f,g)
        print(sql3)

  
    #<---------------------------------catering----------------------->    
    #p = { k : v for k,v in d.items()if v != ''  if  k  in ('Catering')}
    #print(p)
    p = d['Catering']
    block_id = p.get("block_id")
    #p = { k : v for k,v in p.items() if v != ''}
    print("catering values",p)
    sqlcount = json.loads(dbget("select count(*) from business_block.block_catering where block_id ='"+block_id+"'"))
    print(sqlcount)
    h = { k : v for k,v in p.items() if v != '' if k not in ('block_id')}
    print("hhhhhhhhhhhhhhhhhhhh",h)
    i = { k : v for k,v in p.items() if k in ('block_id')}
    print(i)
    #print("Catering",h,type(h),len(h))
    p = { k : v for k,v in p.items() if v != ''}
    if sqlcount[0]['count'] == 0:
            print("insert catering")
            #p = { k : v for k,v in p.items() if v != ''}
            #print("values is empty",p)
            gensql('insert','business_block.block_catering',p)
            

    elif len(h) !=0 :
       print("update catering") 
       #i = { k : v for k,v in d.items()if v != ''} 
       sql4 = gensql('update','business_block.block_catering',h,i)
       print(sql4)
        
  



    #<--------------------------------concurrent meeting tab-------------------------------->
    r = d['block_meeting']
    block_id = r.get("block_id")
    #r = { k : v for k,v in r.items() if v != '' }
    sqlcount = json.loads(dbget("select count(*) from business_block.block_meeting where block_id ='"+block_id+"'"))
    #print(sqlcount)
        
    m = { k : v for k,v in r.items() if v != '' if k not in ('block_id')}
    print(m)
    n = { k : v for k,v in r.items() if k != '' if k in ('block_id')}
    print(n)
   
    #print("block_meeting",m,type(m),len(m))
    r = { k : v for k,v in r.items() if v != '' }
    if sqlcount[0]['count'] == 0:
            print("insert meeting")
            #r = { k : v for k,v in r.items() if v != '' }
            #print(r)
            gensql('insert','business_block.block_meeting',r)
    
    elif len(m) !=0 :
        print("update meeting")
        gensql('update','business_block.block_meeting',m,n)
      
   
    
    #<---------------------room cancel or catering cancel------------------------------------>
    '''   
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
  
    '''
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','Number':result_dic,'ReturnCode':'RUS'}, sort_keys=True, indent=4))
   
