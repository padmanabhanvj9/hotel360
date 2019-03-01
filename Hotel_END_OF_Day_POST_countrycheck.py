from sqlwrapper import gensql, dbget,dbput
import json
import datetime
from collections import Counter
from ApplicationDate import application_date
def get_rate(s):
   if s == 4:
       return('four_adult_rate')
   elif s == 3:
       return('three_adult_rate')
   elif s == 2:
       return('two_adult_rate')
   elif s == 1:
       return('one_adult_rate')
def HOTEL_REM_POST_SELECT_SelectRateForReservation(r_date, r_code, r_room, r_adult):
   print("inputs: ", r_date, r_code, r_room, r_adult)

   rate1 = json.loads(dbget("SELECT rates_all.rates_id, revenue_management.ratecode.*, \
                             rates_all.rate_details_id, season_code.*, rates_all.rate_date, \
                             rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                             rates_all.four_adult_rate, rates_all.one_child_rate,rates_all.two_child_rate,\
                             rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                             rate_tier.* from revenue_management.rates_all join \
                             revenue_management.season_code on \
                             rates_all.season_code_id = season_code.season_code_id join \
                             revenue_management.rate_tier on \
                             rates_all.rate_tier_id = rate_tier.rate_tier_id join \
                             revenue_management.ratecode on rates_all.ratecode_id = ratecode.ratecode_id \
                             where rate_date='"+r_date+"' and rate_code='"+r_code+"' "))
                             #where rate_date='"+r_date+"' "))
   print("rate1", rate1, len(rate1))
   if len(rate1) == 1:
       print("adult", r_adult)
       print("rate1[0][get_rate(r_adult)]", rate1[0][get_rate(r_adult)])
       return(rate1[0][get_rate(r_adult)])

   rooms = [rate['rooms_id'] for rate in rate1]
   print(rooms)
   r_id = ''
   for room in rooms:
       if len(r_id) == 0:
           r_id+= "'"+str(room)+"'"
       else:
           r_id+= ","+"'"+str(room)+"'"

   print(r_id)
   if len(r_id) !=0:
      rate2 = json.loads(dbget("select rooms_selected.*,room_type.type from revenue_management.rooms_selected \
                             join room_management.room_type\
                          on rooms_selected.room_type_id = room_type.id \
                          where rooms_id in ("+r_id+")"))
   
      print("rate2",rate2)

      for rates in rate2:

        if rates['type'] == r_room:
           print("type", rates['type'])
           ro_id = rates['rooms_id']
           break

      r_rate = [r[get_rate(r_adult)]  for r in rate1 if r['rooms_id']== ro_id]
      print("r_rate", r_rate[0])
      return(r_rate[0])
   else:
      return(0)
def Hotel_END_OF_Day_POST_countrycheck(request):
   app_datetime = application_date()
   today_date = app_datetime[1]
   print(today_date)
   #country1 = json.loads(dbget("select pf_company_profile.pf_company_country  ,res_reservation.* from reservation.res_reservation \
    #                      left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.pf_id \
     #                     where res_arrival='"+str(today_date)+"'"))
   coutry2 = json.loads(dbget("select pf_individual_profile.pf_individual_country  ,res_reservation.* from reservation.res_reservation \
                          left join profile.pf_individual_profile on pf_individual_profile.pf_id = res_reservation.pf_id \
                          where res_arrival <='"+str(today_date)+"' and res_depature >='"+str(today_date)+"' "))


  # country1  = country1 + coutry2
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':coutry2,'ReturnCode':'RRTS'},indent=2))

def Hotel_END_OF_Day_POST_Departure_Not_Checkedout(request):
   app_datetime = application_date()
   date = app_datetime[1]
   print(date)
   date = (datetime.datetime.strptime(date,'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   result = json.loads(dbget("select * from reservation.res_reservation \
                            where res_guest_status = 'due out' and res_depature = '"+str(date)+"' "))

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result,'ReturnCode':'RRTS'},indent=4))

def Hotel_END_OF_Day_POST_Roll_Business_date(request):
   app_datetime = application_date()
   date = app_datetime[1]
   print(date)
   tomorrow_date = (datetime.datetime.strptime(date,'%Y-%m-%d').date()) + datetime.timedelta(days=1)
   dbput("update endofday.business_date set roll_business_date = '"+str(tomorrow_date)+"'")
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Date':str(tomorrow_date),'ReturnValue':'Record Updated Successfully','ReturnCode':'RUS'},indent=4))

def Hotel_END_OF_Day_POST_Posting_Rooms_charges(request):
   print("Hello world")
   app_datetime = application_date()
   run_charges,d,fixed_rate_id = [],{},[]
   date = app_datetime[1]
   print(date)
   #****************************************Posting fixed rate****************************************************
   sql_value = json.loads(dbget("select res_arrival,res_depature,res_rate,res_id,fixed_rate	from reservation.res_fixed_rate \
                                 where res_arrival <= '"+str(date)+"' and res_depature >='"+str(date)+"' and res_room_type not in ('PM')"))
   print(sql_value)
   sql_count_value = json.loads(dbget("select count(*) from reservation.res_fixed_rate where res_arrival <= '"+str(date)+"' and res_depature >='"+str(date)+"'"))
   print(sql_count_value)
   fixed_rate_id = ''
   status = ['no show','cancel','waitlist','arrival']
   if sql_count_value[0]['count'] !=0:
      print("its cameeeee")
      for i in sql_value:
         
         if len(fixed_rate_id) == 0:
            fixed_rate_id+="'"+str(i['res_id'])+"'"
         else:
            fixed_rate_id+=","+"'"+str(i['res_id'])+"'"
            
         psql = json.loads(dbget("select res_block,res_room,pf_firstname,res_guest_status from reservation.res_reservation \
                                  where res_id = '"+str(i['res_id'])+"'  and res_room_type not in ('PM')"))
         for s in psql:
           if s['res_guest_status'] not in status:
               if s['res_block'] is None:
                  d['res_room'] = s['res_room']
                  d['res_id'] = i['res_id']
                  d['posting_amount'] = i['res_rate']
                  d['posting_date'] = date
                  d['post_code_id'] = '33'
                  d['post_window'] = '1'
                  d['posting_supplement'] = 'Fixed rate Posting'
                  d['posting_reference'] = 'Fixed rate Posting room chrages'
                  d['posting_quantity'] = '1'
                  d['emp_id'] = 1
                  gensql('insert','cashiering.billing_post',d)
                  run_charges.append({'room':s['res_room'],
                                      'name':s['pf_firstname'],
                                      'posting':'posting room and tax'})
               else:
                  d['res_room'] = s['res_room']
                  d['res_id'] = i['res_id']
                  d['posting_amount'] = i['res_rate']
                  d['posting_date'] = date
                  d['post_code_id'] = '33'
                  d['post_window'] = '2'
                  d['posting_supplement'] = 'Fixed rate Posting'
                  d['posting_reference'] = 'Fixed rate Posting room chrages'
                  d['posting_quantity'] = '1'
                  d['emp_id'] = 1
                  gensql('insert','cashiering.billing_post',d)
                  run_charges.append({'room':s['res_room'],
                                         'name':s['pf_firstname'],
                                         'posting':'posting room and tax'})
   print("sdadsa",fixed_rate_id,type(fixed_rate_id))
   
   if len(fixed_rate_id) > 0:
         
   #****************************************Posting Rooms and tax charges **************************************************
         psqlvalues = json.loads(dbget("select * from reservation.res_reservation \
                                       where res_arrival <= '"+str(date)+"' and res_depature >='"+str(date)+"' \
                                       and res_id not in ("+fixed_rate_id+") and res_guest_status not in ('no show','cancel','waitlist','arrival','reserved') and res_room_type not in ('PM')"))
   else:
         psqlvalues = json.loads(dbget("select * from reservation.res_reservation \
                                       where res_arrival <= '"+str(date)+"' and res_depature >='"+str(date)+"' \
                                       and res_guest_status not in ('no show','cancel','waitlist','arrival','reserved') and res_room_type not in ('PM')"))
   for i in psqlvalues:
         data = HOTEL_REM_POST_SELECT_SelectRateForReservation(date,i['res_rate_code'],i['res_room_type'],i['res_adults'])
         if i['res_block'] is None:       
            d['res_room'] = i['res_room']
            d['res_id'] = i['res_id']
            d['posting_amount'] = data
            d['posting_date'] = date
            d['post_code_id'] = '33'
            d['post_window'] = '1'
            d['posting_supplement'] = 'Room charges Posting'
            d['posting_reference'] = 'posting room chrages'
            d['posting_quantity'] = '1'
            d['emp_id'] = 1
            gensql('insert','cashiering.billing_post',d)
            run_charges.append({'room':i['res_room'],
                                'name':i['pf_firstname'],
                                'posting':'posting room and tax'})
         else:
            d['res_room'] = i['res_room']
            d['res_id'] = i['res_id']
            d['posting_amount'] = data
            d['posting_date'] = date
            d['post_code_id'] = '33'
            d['post_window'] = '2'
            d['posting_supplement'] = 'Room charges Posting'
            d['posting_reference'] = 'posting room chrages'
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
	                           where fixed_charges_begin_date <= '"+str(date)+"' and fixed_charges_end_date >='"+str(date)+"'"))


   for fix_cha in fixed_charge:
      fixed_charge_code = json.loads(dbget("select package_code_id from packages.package_code \
                                            where package_code = '"+fix_cha['fixed_charges_transaction_code']+"'"))
      d['res_room'] = fix_cha['res_room']
      d['res_id'] = fix_cha['res_id']
      d['posting_amount'] = fix_cha['fixed_charges_amount'] * fix_cha['fixed_charges_quantity']
      d['posting_date'] = date
      d['post_code_id'] = fixed_charge_code[0]['package_code_id']
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
   print("packages is pending")

   return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':run_charges,'ReturnCode':'RRTS'},indent=4))


def Hotel_END_OF_Day_POST_Run_guestbalance(request):
   res_id_lists,group_ids,final = [],[],[]
   '''
   value1 = json.loads(dbget("SELECT pf_company_profile.pf_account,res_reservation.* FROM reservation.res_reservation \
                               left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                               where res_reservation.res_guest_status in ('checkin','due out') "))
    print(value1) 
    value2 = json.loads(dbget("select pf_company_profile.pf_account,res_reservation.* from reservation.res_reservation \
                            left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
                             where CURRENT_DATE between res_arrival and res_depature and res_guest_status='Check out' "))  
    print(value2)
    sql_value = value1+value2
    print(sql_value)
    '''
   sql_value = json.loads(dbget("select * from reservation.res_reservation where res_arrival <= '2019-01-24' and res_depature >= '2019-01-24' \
	AND res_guest_status not in ('no show','cancel') and res_room_type not in ('PM')"))

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
   #return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final,'ReturnCode':'RRTS'},indent=4))

def Hotel_END_OF_Day_POST_Run_Additional_procedures(request):
    run_additional,list1,list2,no_show_count,list3,list4,dic_pancy,d = [],[],[],[],[],[],[],{}
    #********************* night audit date******************
    app_datetime = application_date()
    date = app_datetime[1]
    print(date)

    no_show_date = (datetime.datetime.strptime(date,'%Y-%m-%d').date()) - datetime.timedelta(days=1)
    #******************** Reservation No show***********************
    no_show = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(no_show_date)+"' \
                               and res_guest_status = 'arrival'"))
    #print(no_show)

    no_show_start_time = datetime.datetime.now()
    for no_show_report in no_show:
        no_show_count.append(no_show_report['res_guest_status'])
        no_show_update = dbput("update reservation.res_reservation set res_guest_status = 'no show' \
                               where res_id = '"+str(no_show_report['res_id'])+"' \
                               and res_unique_id = '"+str(no_show_report['res_unique_id'])+"'")

        #print(no_show_update)
    no_show_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation No Show","start_time":str(no_show_start_time.strftime("%H:%M:%S")),"end_time":str(no_show_end_time.strftime("%H:%M:%S")),"Iteration": len(no_show_count),"Status":"Completed"})
    #*********************************Due in ************************************************
    due_in_date = (datetime.datetime.strptime(date,'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    due_in = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(due_in_date)+"'"))
    due_in_start_time = datetime.datetime.now()
    for due_in_report in due_in:
        list1.append(due_in_report['res_unique_id'])
        due_in_update = dbput("update reservation.res_reservation set res_guest_status = 'due in' \
                               where res_id = '"+str(due_in_report['res_id'])+"' \
                               and res_unique_id = '"+str(due_in_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel,no show','waitilist')")
    due_in_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Due In",
                           "start_time":str(due_in_start_time.strftime("%H:%M:%S")),"end_time":str(due_in_end_time.strftime("%H:%M:%S")),"Iteration": len(list1),"Status":"Completed"})

    #************************************************* Due Out****************************************
    due_out_date = (datetime.datetime.strptime(date,'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    due_out = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_depature='"+str(due_out_date)+"'"))
    due_out_start_time = datetime.datetime.now()
    for due_out_report in due_out:
        list2.append(due_out_report['res_unique_id'])
        due_out_update = dbput("update reservation.res_reservation set res_guest_status = 'due out' \
                               where res_id = '"+str(due_out_report['res_id'])+"' \
                               and res_unique_id = '"+str(due_out_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel,no show','waitilist','arrival')")
    print(list2)
    due_out_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Due Out",
                           "start_time":str(due_out_start_time.strftime("%H:%M:%S")),"end_time":due_out_end_time.strftime("%H:%M:%S"),"Iteration": len(list2),"Status":"Completed"})

    #*******************************arrival ****************************************************************
    #arrival_date = (datetime.datetime.strptime(date[0]['roll_business_date'],'%Y-%m-%d').date()) + datetime.timedelta(days=1)
    arrivals = json.loads(dbget("select res_id,res_unique_id,res_guest_status from reservation.res_reservation \
                               where res_arrival='"+str(date)+"'"))
    arrival_start_time = datetime.datetime.now()
    for arrivals_report in arrivals:
        list3.append(arrivals_report['res_unique_id'])
        arrivals_report_update = dbput("update reservation.res_reservation set res_guest_status = 'arrival' \
                               where res_id = '"+str(arrivals_report['res_id'])+"' \
                               and res_unique_id = '"+str(arrivals_report['res_unique_id'])+"' \
                               and res_guest_status not in ('cancel,no show','waitlist') ")
    #print(list3)
    arrival_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Reservation Arrival",
                           "start_time":str(arrival_start_time.strftime("%H:%M:%S")),"end_time":str(arrival_end_time.strftime("%H:%M:%S")),"Iteration": len(list3),"Status":"Completed"})


    #**********************************In-house guest**********************************************
    in_house =  json.loads(dbget(" select * from reservation.res_reservation where res_guest_status='checkin' or res_guest_status='due out'"))
    in_house_start_time = datetime.datetime.now()
    for in_house_report in in_house:
        list4.append(in_house_report['res_unique_id'])
    in_house_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"In-House Guest",
                           "start_time":str(in_house_start_time.strftime("%H:%M:%S")),"end_time":str(in_house_end_time.strftime("%H:%M:%S")),"Iteration": len(list4),"Status":"Completed"})

    #***************************************Room Discrepancy********************************
    '''
    room_discrepancy = json.loads(dbget("select * from room_management.rm_room_list \
                                        where rm_fo_status = 'occupied' and rm_hk_status = 'vacant'"))
    room_disc_start_time = datetime.datetime.now()
    for discrepancy in room_discrepancy:
       dic_pancy.append(discrepancy['rm_room'])
       d['rm_room'] = discrepancy['rm_room']
       d['rm_room_discrepancy'] = 'Skip'
       skip_person = gensql('insert','room_management.rm_room_discrepancy',d)
    sleep_details = json.loads(dbget("select * from room_management.rm_room_list \
                                    where rm_fo_status = 'vacant' and rm_hk_status = 'occupied'"))
    for sleep in sleep_details:
       dic_pancy.append(discrepancy['rm_room'])
       d['rm_room'] = sleep['rm_room']
       d['rm_room_discrepancy'] = 'Sleep'
       sleep_person = gensql('insert','room_management.rm_room_discrepancy',d)
    person_details = json.loads(dbget("select * from room_management.rm_room_list"))
    preson_differ = list(filter(lambda x:x['rm_hk_person']!=x['rm_fo_person'],person_details))
    for preson in preson_differ:
          d['rm_room'] = preson['rm_room']
          d['rm_room_discrepancy'] = 'Person'
          person_differ_details = gensql('insert','room_management.rm_room_discrepancy',d)
    room_disc_end_time = datetime.datetime.now()
    run_additional.append({"Run_additional_procedure":"Room Discrepancies",
                           "start_time":str(room_disc_start_time.strftime("%H:%M:%S")),"end_time":str(room_disc_end_time.strftime("%H:%M:%S")),"Iteration": len(dic_pancy),"Status":"Completed"})
    '''                           
    def serialize(obj):
        if isinstance(obj, datetime.date):
       
               return obj.__str__()

        if isinstance(obj, datetime.time):
               return obj.__str__()
    return (json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':run_additional,'ReturnCode':'RRTS'},indent=4,default=serialize))
def Hotel_END_OF_Day_POST_print_final_report(request):
    #*******************************room cleaning report*******************
    list1,list2 = [],[]
    app_datetime = application_date()
    date = app_datetime[1]
    print(date)
    sql_value = json.loads(dbget("select * from reservation.res_reservation \
	where res_guest_status in('due out','checkin','Checkout') and res_arrival <='"+str(date)+"' and res_depature >= '"+str(date)+"'"))

    for i in sql_value:
        rooms = json.loads(dbget("select * from room_management.rm_room_list \
                              where rm_room = '"+str(i['res_room'])+"'"))
        list1.append({
        "room":i['res_room'],
        "room_type":rooms[0]['rm_room_type'],
        "room_class":rooms[0]['rm_room_class'],
        "room_status":"Dirty"

        })
    list2.append({"Report_Name":"RoomCleaningReport","reportstatus":"filed","room_repport_file":list1})
    #*******************************in-house report**************************
    in_house =  json.loads(dbget(" select * from reservation.res_reservation where\
	res_guest_status='checkin' or res_guest_status='due out' and res_arrival <='"+str(date)+"' and res_depature >='"+str(date)+"'"))
    list2.append({"Report_Name":"IN-houseReport","reportstatus":"filed","room_repport_file":in_house})
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list2,'ReturnCode':'RRTS'},indent=4))
