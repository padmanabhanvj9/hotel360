from sqlwrapper import gensql, dbget,dbput
import json
import datetime
def Hotel_END_OF_Day_POST_countrycheck(request):
   today_date = datetime.datetime.utcnow().date()
   print(today_date)
   #country1 = json.loads(dbget("select pf_company_profile.pf_company_country  ,res_reservation.* from reservation.res_reservation \
    #                      left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.pf_id \
     #                     where res_arrival='"+str(today_date)+"'"))
   coutry2 = json.loads(dbget("select pf_individual_profile.pf_individual_country  ,res_reservation.* from reservation.res_reservation \
                          left join profile.pf_individual_profile on pf_individual_profile.pf_id = res_reservation.pf_id \
                          where res_arrival='"+str(today_date)+"'"))
   
 
  # country1  = country1 + coutry2
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':coutry2,'ReturnCode':'RRTS'},indent=2))

def Hotel_END_OF_Day_POST_Departure_Not_Checkedout(request):
 
   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)
   date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   result = json.loads(dbget("select * from reservation.res_reservation \
                            where res_guest_status = 'due out' and res_depature = '"+str(date)+"' and res_guest_balance  = 0"))
   
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result,'ReturnCode':'RRTS'},indent=4))

def Hotel_END_OF_Day_POST_Roll_Business_date(request):
   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)
   tomorrow_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   dbput("update endofday.business_date set roll_business_date = '"+str(tomorrow_date)+"'")
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':'Record Updated Successfully','ReturnCode':'RUS'},indent=4))

def Hotel_END_OF_Day_POST_Posting_Rooms_charges(request):
   print("Hello world")
   run_charges,d = [],{}
   date = json.loads(dbget("select roll_business_date from endofday.business_date"))
   print(date)

   #****************************************Posting Rooms and tax charges **************************************************
   sql_value = json.loads(dbget("select * from reservation.res_reservation \
                                 where res_arrival <= '"+str(date[0]['roll_business_date'])+"' and res_depature >='"+str(date[0]['roll_business_date'])+"'"))
   for i in sql_value:
      d['res_room'] = i['res_room']
      d['res_id'] = i['res_id']
      d['posting_amount'] = i['res_rate']
      d['posting_date'] = date[0]['roll_business_date']
      d['post_code_id'] = '5020'
      d['post_window'] = '1'
      d['posting_supplement'] = 'Night Audit Posting'
      d['posting_reference'] = 'Night Audit Posting posting room chrages'
      d['posting_quantity'] = '1'
      d['emp_id'] = 1
      gensql('insert','cashiering.billing_post',d)
      run_charges.append({'room':i['res_room'],
                          'name':i['pf_firstname'],
                          'posting':'posting room and tax'})
   #****************************************Fixed Charges ********************************************************************
      
   fixed_charge = json.loads(dbget("select res_reservation.res_room, \
	                           res_fixed_charges.res_id, fixed_charges_occurrence, fixed_charges_begin_date, \
                                   fixed_charges_end_date, fixed_charges_transaction_code, fixed_charges_article_code, fixed_charges_amount, \
                                   fixed_charges_quantity, fixed_charges_supplement, fixed_charges_id, res_fixed_charges.res_unique_id \
	                           FROM reservation.res_fixed_charges \
                                   left join reservation.res_reservation on res_reservation.res_unique_id = res_fixed_charges.res_unique_id \
	                           where fixed_charges_begin_date <= '"+str(date[0]['roll_business_date'])+"' and fixed_charges_end_date >='"+str(date[0]['roll_business_date'])+"'"))


   for fix_cha in fixed_charge:
      fixed_charge_code = json.loads(dbget("select posting_code from cashiering.billing_code \
                                            where posting_code_description = '"+fix_cha['fixed_charges_transaction_code']+"'"))
      d['res_room'] = fix_cha['res_room']
      d['res_id'] = fix_cha['res_id']
      d['posting_amount'] = fix_cha['fixed_charges_amount']
      d['posting_date'] = date[0]['roll_business_date']
      d['post_code_id'] = fixed_charge_code[0]['posting_code']
      d['post_window'] = '1'
      d['posting_supplement'] = 'Night Audit Posting'
      d['posting_reference'] = 'Night Audit Posting posting fixed chrages'
      d['posting_quantity'] = fix_cha['fixed_charges_quantity']
      d['emp_id'] = 1
      gensql('insert','cashiering.billing_post',d)
      
      #run_charges = [ x['fixed_charges']='fixed charges run' for x in run_charges if x['room'] == fix_cha['res_room'] ]
      for x in run_charges:
          if x['room'] == fix_cha['res_room']:
             i = run_charges.index(x)
             print("i", i)
             run_charges[i]['fixed_charges'] = 'fixed charges run'

   #***********************************************Posting Packages***********************************************************
             
             
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':run_charges,'ReturnCode':'RRTS'},indent=4))

