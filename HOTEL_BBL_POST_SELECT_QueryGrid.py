from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_SELECT_QueryGrid(request):
    d = request.json
    block_id = d.get("block_id")
    sql =  json.loads(gensql('select','business_block.current_grid','*',block_id))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
   
