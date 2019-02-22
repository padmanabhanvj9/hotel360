from sqlwrapper import gensql, dbget
import json


def HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD(request):
   
   value1 = json.loads(dbget("SELECT pf_company_profile.pf_account,res_reservation.* FROM reservation.res_reservation \
                               left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                               where res_reservation.res_guest_status in ('checkin','due out') and res_room_type not in ('PM') "))
   #print(value1) 
   value2 = json.loads(dbget("select pf_company_profile.pf_account,res_reservation.* from reservation.res_reservation \
                            left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                             where CURRENT_DATE between res_arrival and res_depature and res_guest_status='Check out' and res_room_type not in ('PM') "))  
   #print(value2)
   sql_value = value1+value2

   for res_idlist in sql_value:
       res_id_list = res_idlist['res_id']
       amount = json.loads(dbget("select sum(posting_amount) FROM cashiering.billing_post where res_id='"+str(res_id_list)+"' \
                  and post_window in (1)"))
       deposit = json.loads(dbget("select sum(res_deposit_amount) from reservation.res_deposit where res_id='"+str(res_id_list)+"' "))
       payment=json.loads(dbget("select sum(postig_amount)FROM cashiering.posting_payment where res_id='"+str(res_id_list)+"' "))
       
       if payment[0]['sum'] is None:
          payment[0]['sum'] = 0
       if amount[0]['sum'] is None:
          amount[0]['sum'] = 0
       if deposit[0]['sum'] is None:
          deposit[0]['sum'] = 0
       res_balance = amount[0]['sum'] - (deposit[0]['sum'] + payment[0]['sum'])
       res_idlist['balance'] = res_balance
       print(res_idlist['pf_firstname'],"- deposit: ", deposit,"payment: ",payment,
             "posting_amount: ", amount, "Balance: ",res_idlist['balance'])
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value,'ReturnCode':'RRTS'},indent=4))
    


