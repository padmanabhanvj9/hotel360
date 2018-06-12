from sqlwrapper import gensql
import json

def UpdateProfileCreditcardRecord(request):
    d1 = request.json
    e = { k : v for k,v in d1.items() if k in ('pf_id,cc_id')}
    d = { k : v for k,v in d1.items() if k not in ('pf_id,cc_id')}
    sql_value = gensql('update','profile.pf_creditcard',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))


    

