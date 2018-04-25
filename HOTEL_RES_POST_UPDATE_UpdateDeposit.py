from sqlwrapper import gensql
import json
def HOTEL_RES_POST_UPDATE_UpdateDeposit(request):
    
    d,e = {},{}
    res = request.json
    print(res)
    for name,val in res.items():
 
       if  name == 'PF_Mobileno' or name == 'PF_Firstname':
          e[name] = ""+val+""
       else :
           d[name] = ""+val+""
    print(e,d)
    sql_value = gensql('update','reservation.res_deposit',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
