from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_SELECT_QueryGrid(request):
    d = request.json
    block_id = d.get("block_id")
    sql =  json.loads(dbget("SELECT current_grid.*,grid_type_desc FROM business_block.current_grid join\
                                   business_block.grid_type on current_grid.grid_type = grid_type.grid_type_id \
                                   where block_id="+str(block_id)+" order by current_grid_id "))
    grid_data1 = []
    for data in sql:
      for k,v in data.items():
         if v is None:
           data[k] =  0        
         else:
           pass
      grid_data1.append(data)
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':grid_data1,'ReturnCode':'RRTS'},indent=4))
   
