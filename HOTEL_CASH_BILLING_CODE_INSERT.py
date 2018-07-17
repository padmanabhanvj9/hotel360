import json
from sqlwrapper import gensql
import datetime

def HOTEL_CASH_BILLING_CODE_INSERT(request):
    d = request.json
    print(d)
    gensql('insert','cashiering.billing_code',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))


