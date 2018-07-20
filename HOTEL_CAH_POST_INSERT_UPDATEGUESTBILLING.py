import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_CAH_POST_INSERT_UPDATEGUESTBILLING(request):

    result = request.json
    #print(result)
    d = result['bills']
    #print(d)
    res_id = result['Res_id']
    res_room = result['res_room']
    Total_amount = result['Total_amount']
    Total_posting = result['Total_posting']
    print(res_id,res_room,Total_amount,type(res_id),type(res_room),type(Total_amount))
    #print(d,type(d),len(d))
    Posting_date = datetime.datetime.utcnow().date()

    fo_count = json.loads(dbget('select * from cashiering.folio_number'))
    print(fo_count[0]['folio_no'],type(fo_count[0]['folio_no']))
    dbput("update cashiering.folio_number set folio_no = "+str(fo_count[0]['folio_no']+1)+" ")
    folio = {}
    folio['res_id'],folio['total_posting'],folio['total_amount'],folio['folio_no'] = res_id,Total_posting,Total_amount,fo_count[0]['folio_no']+1    
    gensql('insert','cashiering.reservation_folio',folio)
 
    
    for i in range(len(d)):
        #print(i)
        #print(d,type(d),len(d))
        d[i]['Posting_date'] = Posting_date
        d[i]['Res_id'] = res_id
        d[i]['res_room'] = res_room
        d[i]['folio_no'] = fo_count[0]['folio_no']+1
        #print(d)
        gensql('insert','cashiering.billing_post',d[i])

   
    #dbput("update reservation.res_reservation set res_guest_balance = res_guest_balance + "+str(int(Total_amount))+" \
    #       where res_id='"+res_id+"' and res_room='"+res_room+"' ")
    
    Revenue_date = datetime.datetime.utcnow().date()

    s = {}
    s['Posting_date'] = Posting_date
    s['Revenue_date'] = Revenue_date
    s['User_role'] = "Supervisor"
    s['User_name'] = "david"
    s['Res_id'] = res_id
    s['Posting_action'] = "General posting"
    s['Posting_reason'] = "Payment posted for"+ " "+res_id
    s['Posting_description'] = "Payment posted "
    gensql('insert','cashiering.posting_history_log',s)
    gensql('insert','cashiering.posting_original_history_log',s)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

   

