from sqlwrapper import gensql, dbget
import json


def QueryReservationSearch():


    sql_value = json.loads(dbget("select pf_individual_profile.pf_firstname as firstname,pf_individual_profile.pf_lastname,\
            pf_individual_profile.pf_language,pf_individual_profile.pf_title,pf_individual_profile.pf_mobileno,pf_individual_profile.pf_individual_vip,\
            pf_company_profile.pf_account, pf_company_profile.pf_type, res_reservation.* from reservation.res_reservation \
	                      left join profile.pf_company_profile on pf_company_profile.pf_id = res_reservation.res_block \
	                      left join profile.pf_individual_profile on pf_individual_profile.pf_id = res_reservation.pf_id where res_room_type not in ('PM')"))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
