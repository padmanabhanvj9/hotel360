
import json
from sqlwrapper import dbget
from sqlwrapper import gensql
import datetime

def HOTEL_CAH_GET_SELECT_QUERYGUESTBILLING(request):
    s = dbget("select * from reservation.res_reservation")
    print(s)
    return s



   

