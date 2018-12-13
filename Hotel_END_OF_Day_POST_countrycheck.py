from sqlwrapper import gensql, dbget
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
