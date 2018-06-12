from sqlwrapper import gensql
import json

def UpdateNegotiatedRate(request):
    d = request.json
    sql_value = gensql('insert','profile.pf_negotiated_rate',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))


