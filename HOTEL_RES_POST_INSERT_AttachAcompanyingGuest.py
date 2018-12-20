from sqlwrapper import gensql, dbget,dbput
import json
import datetime
def HOTEL_RES_POST_INSERT_AttachAcompanyingGuest(request):
    d = request.json
    d = { k : v for k,v in d.items() if  v != ''}
    gensql('insert','reservation.res_accompanying_guest',d)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Returncode':'RIS'},indent=2))


def HOTEL_RES_POST_INSERT_DetachAcompanyingGuest(request):
    d = request.json
    remove = dbput("delete from reservation.res_accompanying_guest \
                   where accompanying_id='"+str(d['accompanying_id'])+"' and \
                   res_unique_id = '"+str(d['res_unique_id'])+"' and res_id = '"+str(d['res_id'])+"'")

    
    return (json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','Returncode':'RDS'},indent=2))

def HOTEL_RES_POST_SELECT_QueryAccompanyingGuest(request):
    d = request.json
    sql = json.loads(gensql('select','reservation.res_accompanying_guest','*',d))
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return':'Record Retrieved Successfully','Returncode':'RTS','ReturnValue':sql},indent=2))
