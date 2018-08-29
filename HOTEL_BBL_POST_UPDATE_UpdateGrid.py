from sqlwrapper import gensql,dbget,dbput
import json
def HOTEL_BBL_POST_UPDATE_UpdateGrid(request):
    c = request.json
    a,e = {},{}
    q = 0
    rate1,rate2 = 0,0
    grid_list = c['grid']
    #print("input ..................",d)
    for d in grid_list:
        
        a = { k : v for k,v in d.items() if v != '' if k not in ('block_id','roomtype_id')}
        print(a)
        e = { k : v for k,v in d.items() if k != '' if k in ('block_id','roomtype_id')}
        print(e)
         
        sql = gensql('update','business_block.grid',a,e)
        print(sql)
        block_id = e.get('block_id')
        roomtype_id = e.get('roomtype_id')
        psql1 = json.loads(dbget("select type from room_management.room_type where id = '"+roomtype_id+"'"))
        print("working",psql1)
        #room_type = a.get('type')
        total_count = a.get('total_rooms')
        print("type",psql1[0]['type'],type(psql1[0]['type']))
        if psql1[0]['type']== 'Kngn':
           sql = dbput("update business_block.current_grid set kngn = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
           print(sql)
        elif psql1[0]['type'] =='Kngs':
             sql = dbput("update business_block.current_grid set kngs = '"+total_count+"' where block_id='"+block_id+"'  and grid_type in (1,2)")
             print(sql)
        elif psql1[0]['type'] =='Ksbn':
             sql = dbput("update business_block.current_grid set Ksbn = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql) 
        elif psql1[0]['type'] == 'Ksbs':
             print("workingits fine")
             sql = dbput("update business_block.current_grid set ksbs = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql)
        elif psql1[0]['type'] =='Sjsn' :
             sql = dbput("update business_block.current_grid set sjsn = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql)
        elif psql1[0]['type'] =='Sdbn':
             sql = dbput("update business_block.current_grid set sdbn = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql)
        elif psql1[0]['type'] =='Sjss':
             sql = dbput("update business_block.current_grid set sjss = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql)
        elif psql1[0]['type'] =='Comp':
             sql = dbput("update business_block.current_grid set comp = '"+total_count+"' where block_id='"+block_id+"' and grid_type in (1,2)")
             print(sql)
    sqlvalue = json.loads(dbget("select total_rooms,rate_one,rate_two,rate_three,rate_four,occupancy_one,\
                                 occupancy_two,occupancy_three,occupancy_four from business_block.grid where \
                                 block_id = '"+block_id+"'"))

    #print(sqlvalue)
    for i in sqlvalue:
        q = q + i['total_rooms']
    totalrooms = q
    print("totalrooms",totalrooms,type(totalrooms))
    updateval = dbput("update business_block.block_business_details set total_rooms_perday='"+str(totalrooms)+"' where block_id ='"+str(block_id)+"'")
    print(updateval)
    for i in sqlvalue:
       
          rate1 = ((i['occupancy_one'] * i['rate_one']) + (i['occupancy_two'] * i['rate_two']) + (i['occupancy_three']*i['rate_three']) + (i['occupancy_four']*i['rate_four']))
          print("rate1",rate1)
          rate2 += rate1
          print("firstrate",rate2)
    print("net_revenue",rate2)
    Average_Rate = (rate2/totalrooms)
    print(Average_Rate,type(Average_Rate))
   # s['block_id'] = block_id
   # s['room_nights'] = totalrooms
    #s['net_revenue'] = rate2
    #s['net_rate'] = Average_Rate
    #s['room_nights_available'] = totalrooms
    sql2 = dbput("update business_block.room_revenue set room_nights='"+str(totalrooms)+"',net_revenue='"+str(rate2)+"',net_rate='"+str(Average_Rate)+"',room_nights_available='"+str(totalrooms)+"' where block_id='"+block_id+"'")
    print(sql2)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
   
def HOTEL_BBL_POST_SELECT_SelectRoomingList_Roomtype(request):
    d = request.json['block_id']

    data1 = json.loads(dbget("select roomtype_id,available_rooms,room_type.type from business_block.grid join \
                             room_management.room_type on grid.roomtype_id = room_type.id where block_id="+d+" "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return_value':data1,'Return': 'Record Retrieved Successfully','ReturnCode':'RRS'}, sort_keys=True, indent=4))

def HOTEL_BBL_POST_UPDATE_UpdateRoomingList_Roomtype(request):
     #block_id = request.json['block_id']
    d = request.json
    x,a,e,y = {},{},{},{}
    x = d['data']
    for i in x:
        y = { k : v for k,v in i.items() if v != '' if k not in ('type')}
        
        a = { k : v for k,v in y.items() if v != '' if k not in ('block_id','roomtype_id')}
        print(a)
        e = { k : v for k,v in y.items() if k != '' if k in ('block_id','roomtype_id')}
        print(e)
            
        
        sql = gensql('update','business_block.grid',a,e)
        print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def HOTEL_BBL_POST_SELECT_SelectRoomtype(request):
    block_id =request.json['block_id']
    s = []
    p = 0
    sql = json.loads(dbget("select roomtype_id from business_block.grid where block_id='"+block_id+"'"))
    print(sql)
    for i in sql:
        print(i['roomtype_id'])
        psql = json.loads(dbget("select * from room_management.room_type where  room_type.id = '"+str(i['roomtype_id'])+"'"))
        print(psql)
        #room_type = psql
        s.append(psql[0])
       # print(room_type)
    print(s)   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Retrieved Successfully','ReturnCode':'RRS','ReturnValue':s}, sort_keys=True, indent=4))
def HOTEL_BBL_POST_SELECT_gridservice(request):
    block_id =request.json['block_id']
    roomtype_id = request.json['roomtype_id']
    sql = json.loads(dbget("select room_type.type, business_block.grid.* \
                           from business_block.grid \
                           left join room_management.room_type on room_management.room_type.id = business_block.grid.roomtype_id where grid.block_id = '"+block_id+"' and grid.roomtype_id = '"+roomtype_id+"'"))

    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Retrieved Successfully','ReturnCode':'RRS','ReturnValue':sql}, sort_keys=True, indent=4))
