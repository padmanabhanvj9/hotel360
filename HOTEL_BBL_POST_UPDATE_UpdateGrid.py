from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_UPDATE_UpdateGrid(request):
    d = request.json
    a,e = {},{}
    a = { k : v for k,v in d.items() if v != '' if k not in ('block_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('block_id')}
    print(e)
     
    sql = gensql('update','business_block.grid',a,e)
    print(sql)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
   
