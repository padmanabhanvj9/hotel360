from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_INSERT_CalculateRoomRevenue(request):
    
    d = request.json
    s = {}
    block_id = d.get("block_id")
    psql = dbget("select count_one,count_two,count_three from business_block.grid where block_id = '"+block_id+"'")
    sqlvalue = json.loads(psql)
    print(sqlvalue)
    #<-----------count ------>
    count1 = sqlvalue[0]['count_one']
    print(type(count1),count1)
    count2 = sqlvalue[0]['count_two']
    print(type(count2),count2)
    count3 = sqlvalue[0]['count_three']
    print(type(count3),count3)
    #<------------rate------------>
    '''rate1 = sqlvalue[0]['rate_one']
    print(type(rate1),rate1)
    rate2 = sqlvalue[0]['rate_two']
    print(type(rate2),rate2)
    rate3 = sqlvalue[0]['rate_three']
    print(type(rate3),rate3)'''
    rate1 = int("223")
    rate2 = int("234")
    rate3 = int("236")

    room_nights = count1 + (count2+count3)
    print(room_nights,type(room_nights))

    total_rooms_rate = (count1 * rate1) + (count2 * rate2) + (count3 * rate3)
    print(total_rooms_rate,type(total_rooms_rate))

    Average_Rate = (total_rooms_rate/room_nights)
    print(Average_Rate,type(Average_Rate))
    s['block_id'] = block_id
    s['room_nights'] = room_nights
    s['net_revenue'] = total_rooms_rate
    s['net_rate'] = Average_Rate
    s['room_nights_available'] = room_nights
    sql2 = gensql('insert','business_block.room_revenue',s)
    print(sql2)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
