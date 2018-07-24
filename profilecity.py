from sqlwrapper import gensql
import json
def profilecity():
    s = ['city']
    sql_value = gensql('select','profile.city',s)
    result = json.loads(sql_value)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def profilelanguage():
    s = ['language']
    sql_value = gensql('select','profile.language',s)
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilecountry():
    s = ['country']
    sql_value = gensql('select','profile.country',s)
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilestate():
    s = ['state']
    sql_value = gensql('select','profile.state',s)
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilepostalcode():

    sql_value = gensql('select','profile.postalcode','postalcode')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilevip():

    sql_value = gensql('select','profile.vip','vipguest')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilenationality():

    sql_value = gensql('select','profile.nationality','nationality')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilecurrency():

    sql_value = gensql('select','profile.currency','currency,currency_description')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilecommunication():

    sql_value = gensql('select','profile.communication','commtype,commtype_description')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilepftype():

    sql_value = gensql('select','profile.profiletype','profiletype')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profileratecode():

    sql_value = gensql('select','profile.ratecode','ratecode')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilenotetype():

    sql_value = gensql('select','profile.notetype','notetype')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilepreferencegroup():
 
    sql_value = gensql('select','profile.preferencegroup','prefernecegroup,preferencegroup_desc')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))

def profilepreferencevalue():

    sql_value = gensql('select','profile.preference','preference,preference_description')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
def Title():

    sql_value = gensql('select','profile.title','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    

