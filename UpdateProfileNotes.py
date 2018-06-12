from sqlwrapper import gensql
import json

def UpdateProfileNotes(request):
    d = request.json
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
