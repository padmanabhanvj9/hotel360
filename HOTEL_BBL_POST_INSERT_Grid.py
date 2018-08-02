from sqlwrapper import gensql
import json
def HOTEL_BBL_POST_INSERT_Grid(request):
    d = request.json
    x = {}
    for k,v in d.items():
     print(k,v)
     if v is '':
          d[k] =  0
          print(d)
     else:
          pass
   
    print(d)
    
    sql2 = gensql('insert','business_block.grid',d)
    print(sql2)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
