import json
from sqlwrapper import gensql,dbget
import datetime



def HOTEL_CAH_POST_POSTING_PAYMENT_INSERT(request):
    d = request.json
    print(d)
    gensql('insert','cashiering.posting_payment',d)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))


   

