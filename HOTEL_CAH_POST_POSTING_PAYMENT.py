import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_CAH_POST_POSTING_PAYMENT(request):
    res_id = request.json['res_id']

    s = dbget("select payment_code_id,payment_type,payment_code,currency_id,currency_type from cashiering.payment_code inner join cashiering.billing_currency on cashiering.payment_code.payment_code_id = cashiering.billing_currency.currency_id where cashiering.payment_code.payment_code_id = "+res_id+"")
    s = json.loads(s)

    print(s)
    #return(json.dumps(s,t))
    return(json.dumps(s,indent=4))



   


