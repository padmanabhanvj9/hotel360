import json
from sqlwrapper import gensql,dbget,dbput
import datetime

def HOTEL_CAH_POST_SELECT_QUERYGUESTBILLING(request):

    d = request.json
    #print(d)
    res_data = json.loads(gensql('select','reservation.res_reservation',' res_guest_status,res_arrival, res_depature, res_rate_code, res_rate, \
                          res_adults, res_room_type,pf_id,res_guest_balance',d))
    #print(res_data)
    if res_data[0]['pf_id'][0:3] == 'cpy':
        #print("if")
        profile_data = json.loads(dbget("select pf_account from profile.pf_company_profile where pf_id='"+res_data[0]['pf_id']+"'"))
        #print(profile_data)
        res_data[0]['company'] = profile_data[0]['pf_account']
    else:
        #print("else")
        res_data[0]['company'] = ''
    #print(res_data)    
    billing_data = json.loads(dbget("select billing_post.*,billing_code.* \
                          from cashiering.billing_post  join cashiering.billing_code on cashiering.billing_post.post_code_id = \
                          cashiering.billing_code.posting_code_id \
                          where cashiering.billing_post.res_id='"+d['res_id']+"' and \
                          cashiering.billing_post.res_room='"+d['res_room']+"' "))
    #print("billing",billing_data,type(billing_data))
    w1,w2,w3,w4,window1,window = 0,0,0,0,{},[]
    for i in billing_data:
        if int(i['post_window']) == 1:
            w1 += int(i['posting_amount'])
        elif int(i['post_window']) == 2:
            w2 += int(i['posting_amount'])
        elif int(i['post_window']) == 3:
            w3 += int(i['posting_amount'])
        else:
            w4 += int(i['posting_amount'])
    #print(w1,w2,w3,w4,type(w1))        
    window1['w1_total'] = w1
    window1['w2_total'] = w2
    window1['w3_total'] = w3
    window1['w4_total'] = w4
    window.append(window1)
    #billing_data.append(window)
    #print(billing_data)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':res_data,"ReturnValue1":billing_data,"ReturnValue2":window,'ReturnCode':'RRTS'},indent=4))



   

