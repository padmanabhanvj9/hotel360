import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_CASH_BILLING_CODE_SELECT(request):
    s = dbget("select * from cashiering.billing_code")
    print(s)
    return s

