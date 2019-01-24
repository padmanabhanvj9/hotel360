from sqlwrapper import gensql,dbget
import json
import datetime
#from datetime import timedelta  

def HOTEL_BBL_POST_INSERT_Grid(request):
    d = request.json['grid']
    #print(d['block_id'],type(d['block_id']))
    print(d)

    i,l,s = {},{},{}
    q,type_id = 0,1
    rate1,rate2 = 0,0
    gridapp,current_grid = [],{}
    
    for i in d:
     for k,v in i.items():
      if v is '':
          i[k] =  0        
      else:
          pass     
     gridapp.append(i)
    #print("append",gridapp)
    
    for l in gridapp:
        e = { k : v for k,v in l.items() if k not in ('roomtype')}
        #b_id = { k : v for k,v in l.items() if k  in ('block_id')}
        
        gensql('insert','business_block.grid',e)
        st_date = datetime.datetime.strptime(l['grid_startdate'],"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(l['grid_enddate'], "%Y-%m-%d").date()
        print("for loop")
        while st_date <= end_date:
              
              type_id = 1
              while type_id <= 3:
                 count = json.loads(dbget(" select count(grid_type) from business_block.current_grid \
                                            where block_id="+l['block_id']+" and curnt_date='"+str(st_date)+"' and \
                                            grid_type="+str(type_id)+""))
                 
                 print(count)
                 if count[0]['count'] == 0:
                     current_grid['block_id'] = l['block_id']
                     current_grid['curnt_date'] = st_date
                     current_grid['grid_type'] = type_id
                     if type_id == 3:
                         current_grid[''+l['roomtype']+''] = 0
                     else:    
                        current_grid[''+l['roomtype']+''] = l['total_rooms']

                     gensql('insert','business_block.current_grid',current_grid)
                 else:
                     a,b = {},{}
                     b['block_id'] = l['block_id']
                     b['curnt_date'] = st_date
                     b['grid_type'] = type_id
                     if type_id == 3:
                         a[''+l['roomtype']+''] = 0
                     else:    
                        a[''+l['roomtype']+''] = l['total_rooms']
                     gensql('update','business_block.current_grid',a,b)
                 current_grid = {}
                 type_id += 1
              st_date = st_date + datetime.timedelta(days=1)
              
#    grid_data = json.loads(dbget("SELECT current_grid.*,grid_type_desc FROM business_block.current_grid join\
#                                   business_block.grid_type on current_grid.grid_type = grid_type.grid_type_id \
#                                   where block_id="+str(l['block_id'])+" "))
    grid_data =  json.loads(dbget("SELECT current_grid.*,grid_type_desc FROM business_block.current_grid join\
                                   business_block.grid_type on current_grid.grid_type = grid_type.grid_type_id \
                                   where block_id="+str(l['block_id'])+" order by current_grid_id "))
    #print("grid_data",grid_data)
    grid_data1 = []
    for data in grid_data:
      for k,v in data.items():
         if v is None:
           data[k] =  0        
         else:
           pass
      grid_data1.append(data)
    print("---------------------------------------------------------------")
    #print("grid_data1",grid_data1)
    block_id = d[0]['block_id']
    #print(block_id)
    

    
    
    sqlvalue = json.loads(dbget("select total_rooms,rate_one,rate_two,rate_three,rate_four,occupancy_one,\
                                 occupancy_two,occupancy_three,occupancy_four from business_block.grid where \
                                 block_id = '"+block_id+"'"))

    print(sqlvalue)
    #<-----------count ------>
    for i in sqlvalue:
        q = q + i['total_rooms']
    totalrooms = q
    print("totalrooms",totalrooms,type(totalrooms))
    
    for i in sqlvalue:
       
          rate1 = ((i['occupancy_one'] * i['rate_one']) + (i['occupancy_two'] * i['rate_two']) + (i['occupancy_three']*i['rate_three']) + (i['occupancy_four']*i['rate_four']))
          print("rate1",rate1)
          rate2 += rate1
          print("firstrate",rate2)
    print("net_revenue",rate2)
    Average_Rate = (rate2/totalrooms)
    print(Average_Rate,type(Average_Rate))
    s['block_id'] = block_id
    s['room_nights'] = totalrooms
    s['net_revenue'] = rate2
    s['net_rate'] = Average_Rate
    s['room_nights_picked'] = '0'
    s['room_nights_available'] = totalrooms
    sql2 = gensql('insert','business_block.room_revenue',s)
    print(sql2)
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnValue':grid_data1,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
