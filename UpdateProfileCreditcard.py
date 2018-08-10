from sqlwrapper import gensql,dbget
import json

def UpdateProfileCreditcard(request):
    d = request.json
    #print(d)
    gensql('insert','profile.pf_creditcard',d)
    sql_value = json.loads(dbget("select cc_id from profile.pf_creditcard \
                                   where pf_creditcard_no='"+d['PF_Creditcard_No']+"' \
                                   and pf_expiration_date='"+d['PF_Expiration_Date']+"' and res_id='"+d['res_id']+"' "))
    #print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Return_value':sql_value[0]['cc_id'],'ReturnCode':'RIS'}, sort_keys=True, indent=4))


def UpdateProfileCreditcardnew(request):
    d = request.json
    #print(d)
    gensql('insert','profile.pf_creditcard',d)
    sql_value = json.loads(dbget("select cc_id from profile.pf_creditcard \
                                   where pf_creditcard_no='"+d['PF_Creditcard_No']+"' \
                                   and pf_expiration_date='"+d['PF_Expiration_Date']+"' "))
    #print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Return_value':sql_value[0]['cc_id'],'ReturnCode':'RIS'}, sort_keys=True, indent=4))
   
