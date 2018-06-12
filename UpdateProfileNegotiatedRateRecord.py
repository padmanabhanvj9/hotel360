from sqlwrapper import gensql
import json

def UpdateProfileNegotiatedRateRecord(request):
    d1 = request.json
    e = { k : v for k,v in d1.items() if k in ('pf_id,negotiate_id')}
    d = { k : v for k,v in d1.items() if k not in ('pf_id,negotiate_id')}
    print(e,d)
    sql_value = gensql('update','profile.pf_negotiated_rate',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))


    
