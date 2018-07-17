import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_CASH_SELECT_POSTING_WINDOW(request):
    s = dbget("select * from cashiering.posting_window")
    print(s)
    return s

