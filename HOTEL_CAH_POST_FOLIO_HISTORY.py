import json
from sqlwrapper import gensql,dbget,dbput
import datetime



def HOTEL_CAH_POST_FOLIO_HISTORY(request):
    
    s = json.loads(dbget("SELECT  cashiering.billing_post.res_id,post_id, posting_amount, posting_date, post_code_id, arrangement_code, checkno, posting_supplement, posting_reference, posting_quantity, total_posting,pf_firstname,cashiering.posting_window.posting_window_number FROM cashiering.billing_post inner join reservation.res_reservation  on cashiering.billing_post.res_id = reservation.res_reservation.res_id inner join cashiering.posting_window on cashiering.billing_post.post_window_id = cashiering.posting_window.posting_window_id"))
    
    print(s)

    return(json.dumps({"Return": s,"ReturnCode": "RDS","Status": "Success","StatusCode": "200"},indent=4))
