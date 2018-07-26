import json
import random
from sqlwrapper import gensql,dbget,dbput
import datetime


def HOTEL_BBL_POST_INSERT_BusinessBlock(request):
    sql_value = json.loads(dbget("select count_id from business_block.count"))
    print(sql_value,type(sql_value))
    
    sql_value1 = sql_value[0]['count_id']
    #sql = int(sql_value1)
    print(sql_value1,type(sql_value1))

    count = sql_value1 + 1
    print(count)

    psql = dbput("update business_block.count set count_id = '"+str(sql_value[0]['count_id']+1)+"'")
    print(psql)
    d = request.json
    E = d['Inquiry']
    E = { k : v for k,v in E.items() if  v != ''} 
    print(E)
    E['block_id'] = count
    random_no = (random.randint(1000000000,9999999999))
    random_no = str(random_no)
    random_no = random_no[0:4]
    print(random_no)
    pf_id = E.get("pf_id")
    PF_ACCOUNT = json.loads(dbget("select pf_account from profile.pf_company_profile where pf_id = '"+pf_id+"'"))
    PF_ACCOUNT = PF_ACCOUNT[0]['pf_account']
    pf_account = PF_ACCOUNT[0:5]
    E['block_status'] = "Inquiry"
    E['block_code'] = random_no + pf_account
    E['block_name'] = PF_ACCOUNT
    sql = gensql('insert','business_block.business_block',E)
    print(sql)
    #inquiry grid
    id11 = E.get("block_id")
    g = d['Inquiry_grid']
    print(g,type(g))
    

    for i in g:
       j = { k : v for k,v in i.items() if  v != ''} 
       j['block_id'] = id11
    
       psql = gensql('insert','business_block.inquiry_grid',j)


    s = {}
    s['user_role'] = "Supervisor"
    blockname = E.get("block_name")
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    s['date'] = RES_Log_Date
    s['time'] = RES_Log_Time
    s['block_id'] = count
    s['action_type_id'] = "Business Block in inquiry status"
    s['description'] = "Business Block in inquiry status for"+" "+str(blockname)
    gensql('insert','business_block.business_block_activity_log',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_BBL_POST_SELECT_QueryInquiryGrid(request):
    d = request.json
    sql = json.loads(gensql('select','business_block.inquiry_grid','*',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
   
