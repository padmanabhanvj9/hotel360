from sqlwrapper import gensql
import json

def UpdateProfileNotesRecord(request):
    d1 = request.json
    e = { k : v for k,v in d1.items() if k in ('pf_id,notes_id')}
    d = { k : v for k,v in d1.items() if k not in ('pf_id,notes_id')}
    print(e,d)
    sql_value = gensql('update','profile.pf_notes',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
