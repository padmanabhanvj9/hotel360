from sqlwrapper import gensql, dbget
import json


def QueryReservationSearch():
    #sql_value = dbget("select pf_company_profile.pf_account,res_reservation.* from reservation.res_reservation \
     #          full join profile.pf_company_profile on reservation.res_reservation.pf_id = profile.pf_company_profile.pf_id ")
    sql_value = gensql('select','reservation.res_reservation','*')
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
