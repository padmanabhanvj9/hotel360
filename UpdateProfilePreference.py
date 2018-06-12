from sqlwrapper import gensql
import json

def UpdateProfilePreference(request):
    d = request.json
    #print(d)
    e = { k : v for k,v in d.items() if k in ('pf_id,preference_id')}
    #print(e)
    f = { k : v for k,v in d.items() if k not in ('pf_id,preference_id') }
    print(f)    
    sql_value = gensql('update','profile.pf_preference',f,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
