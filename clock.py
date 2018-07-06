from apscheduler.schedulers.blocking import BlockingScheduler
from sqlwrapper import gensql, dbget, dbput
import datetime
import json
sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=10)
def timed_job():
    tomorrow = datetime.datetime.utcnow()+datetime.timedelta(days=1)
    tomorrow = str(tomorrow)
    print(tomorrow)
    
    sql_value = dbget("select res_unique_id from reservation.res_reservation where res_depature='"+tomorrow+"'")
    sqlvalue = json.loads(sql_value)
    print("sqlval",sqlvalue)
    if len(sqlvalue) != 0:
        res_unique_id = ''
        for  i in sqlvalue:
            if len(res_unique_id) == 0:
                res_unique_id += "'"+str(i['res_unique_id'])+"'"
            else:
                res_unique_id += ","+"'"+str(i['res_unique_id'])+"'"
        print(res_unique_id) 

        status = "due out"
       
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id in ("+str(res_unique_id)+")")

        print('This job is run every three minutes.')
    else:
        pass
    tomorrow = datetime.datetime.utcnow()+datetime.timedelta(days =1)
    tomorrow = str(tomorrow)
    print(tomorrow)
    
    sql_value = dbget("select res_unique_id from reservation.res_reservation where res_arrival='"+tomorrow+"'")
    sqlvalue = json.loads(sql_value)
    print("sqlval1",sqlvalue)
    if (len(sqlvalue) != 0):
        res_id = ''
        for  i in sqlvalue:
            if len(res_unique_id) == 0:
                res_unique_id += "'"+str(i['res_unique_id'])+"'"
            else:
                res_unique_id += ","+"'"+str(i['res_unique_id'])+"'"
        print(res_unique_id) 

        status = "due in"
        
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id in ("+str(res_unique_id)+")")
        print(sql_value)
    else:
        pass
    
    today = datetime.datetime.utcnow().date()
    today = str(today)
    print(today)
    
    sql_value = dbget("select res_unique_id from reservation.res_reservation where res_arrival='"+today+"'")
    sqlvalue = json.loads(sql_value)
    print("sqlval2",sqlvalue)
    if (len(sqlvalue) != 0):
        res_id = ''
        for  i in sqlvalue:
            if len(res_unique_id) == 0:
                res_unique_id += "'"+str(i['res_unique_id'])+"'"
            else:
                res_unique_id += ","+"'"+str(i['res_unique_id'])+"'"
        print(res_unique_id) 

        status = "arrival"
        
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id in ("+str(res_unique_id)+")")
        print(sql_value)
    else:
        pass
@sched.scheduled_job('interval', hours=10)
def yesterday_job():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    yesterday = str(yesterday)
    print(yesterday)
    sql_value = dbget("select res_unique_id from reservation.res_reservation where res_arrival='"+yesterday+"' and res_guest_status in ('arrival')")
    sqlvalue = json.loads(sql_value)
    print("sqlval3",sqlvalue)
    if (len(sqlvalue) != 0):
        res_id = ''
        for  i in sqlvalue:
            if len(res_unique_id) == 0:
                res_unique_id += "'"+str(i['res_unique_id'])+"'"
            else:
                res_unique_id += ","+"'"+str(i['res_unique_id'])+"'"
        print(res_unique_id) 

        status = "no show"
        
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id in ("+str(res_unique_id)+")")
        print(sql_value)
    else:
        pass
#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
#def scheduled_job():
 #   print('This job is run every weekday at 5pm.')

sched.start()
