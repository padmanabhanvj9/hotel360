from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_INSERT_CalculateRoomRevenue(request):
    
    d = request.json
    s = {}
    q = 0
    rate1,rate2 = 0,0
    block_id = d.get("block_id")
    psql = dbget("select total_rooms,rate_one,rate_two,rate_three,rate_four,occupancy_one,occupancy_two,occupancy_three,occupancy_four from business_block.grid where block_id = '"+block_id+"'")
    sqlvalue = json.loads(psql)
    print(sqlvalue)
    #<-----------count ------>
    for i in sqlvalue:
        q = q + i['total_rooms']
        #print("summa",i['total_rooms'])
        #print("plus",q)
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
    s['room_nights_available'] = totalrooms
    sql2 = gensql('insert','business_block.room_revenue',s)
    print(sql2)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
