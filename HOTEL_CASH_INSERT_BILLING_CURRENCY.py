import json
from sqlwrapper import gensql
import datetime



def HOTEL_CASH_INSERT_BILLING_CURRENCY(request):
    d = request.json
    print(d)
    gensql('insert','cashiering.billing_currency',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

if __name__ == "__main__":
         app.run(host="192.168.1.4",port=5000)
