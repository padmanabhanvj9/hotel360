from sqlwrapper import gensql

import json

def QueryProfileSearch(request):
    
  
    sql_value = gensql('select','profile.pf_company_profile','*')
    sql_value1 = json.loads(sql_value)
    #print(sql_value1)

    
    sql_value = gensql('select','profile.pf_individual_profile','*')
    sql_value2 = json.loads(sql_value)
    #print(sql_value2)
    result = []
    result = sql_value1 + sql_value2
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
