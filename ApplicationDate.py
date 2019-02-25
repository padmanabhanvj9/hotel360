from sqlwrapper import gensql, dbget,dbput
import json
from datetime import datetime
import pytz

def application_date():
    date = json.loads(dbget("select roll_business_date from endofday.business_date"))
    #print(date, date[0]['roll_business_date'], type(date[0]['roll_business_date']))
    
    now = datetime.now()
    # assuming now contains a timezone aware datetime
    tz = pytz.timezone('Asia/Kolkata')
    your_now = now.astimezone(tz)
    #print(your_now)
    #print(your_now.strftime('%H:%M:%S'), type(your_now.strftime('%H:%M:%S')))
    current_datetime = date[0]['roll_business_date']+' '+your_now.strftime('%H:%M:%S')
    print(current_datetime)
    return(current_datetime, date[0]['roll_business_date'], your_now.strftime('%H:%M:%S'))


#a = application_date()
