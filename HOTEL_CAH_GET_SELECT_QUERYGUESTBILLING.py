
import json
from sqlwrapper import gensql,dbget,dbput
import datetime
def HOTEL_CAH_POST_SELECT_QUERYGUESTBILLING(request):
    d = request.json
    print(d)
    res_data = json.loads(gensql('select','reservation.res_reservation',' res_guest_status,res_arrival, res_depature, res_rate_code, res_rate, \
                          res_adults, res_room_type,pf_id',d))
    print(res_data)
    if res_data[0]['pf_id'][0:3] == 'cpy':
        print(res_data[0]['pf_id'])
        profile_data = json.loads(dbget("select pf_account from profile.pf_company_profile where pf_id='cpy101'"))
        res_data[0]['company'] = profile_data[0]['pf_account']
    print(res_data)    
    billing_data = json.loads(dbget("select billing_post.posting_date,billing_code.posting_code,billing_code.posting_code_description,\
                          billing_post.posting_amount,billing_post.post_window_id \
                          from cashiering.billing_post  join cashiering.billing_code on cashiering.billing_post.post_code_id = \
                          cashiering.billing_code.posting_code_id inner join cashiering.posting_window on cashiering.billing_post.post_window_id=\
                          cashiering.posting_window.posting_window_id \
                          where cashiering.billing_post.res_id='"+d['res_id']+"' and \
                          cashiering.billing_post.res_room='"+d['res_room']+"' "))
    print(billing_data)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':res_data,"ReturnValue1":billing_data  ,'ReturnCode':'RRTS'},indent=4))



   

