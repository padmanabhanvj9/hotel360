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

    sql_value = gensql('select','profile.postalcode','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilevip():

    sql_value = gensql('select','profile.vip','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilenationality():

    sql_value = gensql('select','profile.nationality','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profilecurrency():

    sql_value = gensql('select','profile.currency','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilecommunication():

    sql_value = gensql('select','profile.communication','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilepftype():

    sql_value = gensql('select','profile.profiletype','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
    
def profileratecode():

    sql_value = gensql('select','profile.ratecode','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilenotetype():

    sql_value = gensql('select','profile.notetype','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    
def profilepreferencegroup():
 
    sql_value = gensql('select','profile.preferencegroup','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))

def profilepreferencevalue():

    sql_value = gensql('select','profile.preference','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
def Title():

    sql_value = gensql('select','profile.title','*')
    result = json.loads(sql_value)
    print(result)
    return (json.dumps({'Status': 'Success', 'StatusCode': '200', 'ReturnValue': result , 'ReturnCode': 'RRTS'}, indent=4))
    

