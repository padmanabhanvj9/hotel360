from sqlwrapper import gensql
import json
def profilecity_insert(request):
    d = request.json
   
    sql_value = gensql('insert','profile.city',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'},indent=4))
def profilelanguage_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.language',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profilecountry_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.country',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profilestate_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.state',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profilepostalcode_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.postalcode',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profilevip_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.vip',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def profilenationality_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.nationality',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profilecurrency_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.currency',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def profilecommunication_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.communication',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def profilepftype_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.profiletype',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
    
def profileratecode_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.ratecode',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def profilenotetype_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.notetype',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def profilepreferencegroup_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.preferencegroup',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def profilepreferencevalue_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.preference',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
def Title_insert(request):
    d = request.json
    sql_value = gensql('insert','profile.title',d)
    
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    

