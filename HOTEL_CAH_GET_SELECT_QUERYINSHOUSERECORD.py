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
   print(sql_value)
   for i in sql_value:
      if i['res_block'] is None:
         if i['res_id'] in res_id_lists:
            pass
         else:
          res_id_lists.append(i['res_id'])
      else:
         if i['res_id'] in group_ids:
            pass
         else:
          group_ids.append(i['res_id'])
   print("individual profile",res_id_lists)
   print("ind+company",group_ids)
   for res_id_list in res_id_lists:
       amount = json.loads(dbget("select sum(posting_amount) FROM cashiering.billing_post where res_id='"+str(res_id_list)+"' \
                  and post_window in (1)"))
       deposit = json.loads(dbget("select sum(res_deposit_amount) from reservation.res_deposit where res_id='"+str(res_id_list)+"' "))
       payment=json.loads(dbget("select sum(postig_amount)FROM cashiering.posting_payment where res_id='"+str(res_id_list)+"' "))
       
       if payment[0]['sum'] is None:
         value = deposit[0]['sum'] - amount[0]['sum']
         print(value)
         final.append({"balance":value,'res_id':res_id_list})
       else:
          
          value = amount[0]['sum'] - (deposit[0]['sum'] + payment[0]['sum'])
          print(value)
          final.append({"balance":value,'res_id':res_id_list})
   if len(group_ids) != 0:
      for group_id in group_ids:
          amount = json.loads(dbget("select sum(posting_amount) FROM cashiering.billing_post where res_id='"+str(group_id)+"' \
                     and post_window in (1)"))
          payment=json.loads(dbget("select sum(postig_amount)FROM cashiering.posting_payment where res_id='"+str(group_id)+"' "))
          
          if payment[0]['sum'] is None:
            value = amount[0]['sum']
            print(value)
            final.append({"balance":value,'res_id':group_id})
          else:
             
             value = amount[0]['sum'] - payment[0]['sum']
             print(value)
             final.append({"balance":value,'res_id':group_id})
   list1 = [dict(s,balance=fin['balance']) for s in sql_value for fin in final if s['res_id'] == fin['res_id'] ]
   print(list1)
   '''
   print("sql_value", sql_value)
   for s in sql_value:
      print("s",s)
      for fin in final:
         print("fin",fin)
         print(s['res_id'],type(s['res_id']),fin['res_id'],type(fin['res_id']))
         if s['res_id'] == fin['res_id']:
            s['balance'] = fin['balance']
         else:
            pass
   '''         
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list1,'ReturnCode':'RRTS'},indent=4))
    

# select CURRENT_DATE) between res_arrival and res_depature and res_guest_status='Check out'
