from sqlwrapper import gensql,dbget

import json

def QueryProfileSearch(request):
    
  
    sql_value = dbget("	select pf_individual_country as country,pf_individual_state as state,pf_individual_address as address_one,pf_home_address as address_two, \
	                 * from  profile.pf_individual_profile ")
    sql_value1 = json.loads(sql_value)
    #print(sql_value1)

    
    sql_value = dbget("	select pf_company_country as country,pf_company_state as state,pf_company_address as address_one,pf_business_address as address_two,\
	* from  profile.pf_company_profile")
    sql_value2 = json.loads(sql_value)
    #print(sql_value2)
    result = []
    result = sql_value1 + sql_value2
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
