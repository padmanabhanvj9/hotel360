import json
from sqlwrapper import gensql,dbget,dbput
import datetime



def HOTEL_CAH_POST_FOLIO_HISTORY(request):
    
    s = json.loads(dbget("select cashiering.billing_post.*, cashiering.reservation_folio.*,reservation.res_reservation.pf_firstname \
                          from cashiering.reservation_folio join cashiering.billing_post \
                          on billing_post.folio_no = reservation_folio.folio_no join reservation.res_reservation on \
                          reservation.res_reservation.res_id = reservation_folio.res_id"))
    
    print(s)

    return(json.dumps({"Return": s,"ReturnCode": "RDS","Status": "Success","StatusCode": "200"},indent=4))
