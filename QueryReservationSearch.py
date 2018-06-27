from sqlwrapper import gensql, dbget
import json


def QueryReservationSearch():
   
    sql_value = gensql('select','reservation.res_reservation','*')
    #sql_value = dbget("select * from reservation.res_reservation full join profile.pf_individual_profile \
     #     on reservation.res_reservation.pf_id =  profile.pf_individual_profile.pf_id \
      #    full join profile.pf_company_profile on reservation.res_reservation.pf_id = profile.pf_company_profile.pf_id")  
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
