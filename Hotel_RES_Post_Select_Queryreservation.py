from sqlwrapper import gensql,dbget,dbfetch
import json

def pfdict(pf,query):
    if len(query) == 0:
        query += " where "
    else:
        query += " and "      
    for key,values in pf.items():
      names = ''  
      if values != '':           
        if key == 'pf_type':  
           if values == 'individual':
             data = dbfetch('select pf_firstname from profile.pf_individual_profile')
             print(data)
             
             for i in data:
                 if len(names) == 0:
                    names += "'"+i+"'"
                 else:
                    names += ','+"'"+i+"'"
           else:
             data = dbfetch('select pf_firstname from profile.pf_company_profile')
             print(data)
             for i in data:
                 if len(names) == 0:
                    names += "'"+i+"'"
                 else:
                    names += ','+"'"+i+"'"    
        if key == 'pf_country':              
            data = dbfetch("select pf_firstname from profile.pf_individual_profile where pf_individual_country = '"+values+"' ")
            print(data)
            data1 = dbfetch("select pf_firstname from profile.pf_company_profile where pf_company_country = '"+values+"' ")
            for i in data :
                 if len(names) == 0:
                    names += "'"+i+"'"
                 else:
                    names += ','+"'"+i+"'"
            for i in data1 :
                 if len(names) == 0:
                    names += "'"+i+"'"
                 else:
                    names += ','+"'"+i+"'"                  
    query += "pf_firstname in ("+names+")"
    return(query)
def hotel_res_post_select_queryreservation(request):
    global query
    query = ""           
    res,d,e = request.json['res'],{},{}
    pf = request.json['pf']
    print(len(pf))
    sql = 'select * from reservation.res_reservation'
    
    for name,val in res.items():
      if val != '':      
        if len(query) == 0:
           query += " where "
        else:
           query += " and " 
        if val != '':
           query += ""+name+" = "+val+" "
    print(sql+query)
    if len(pf) != 2:
        query = pfdict(pf,query)
        print(query)
    print(sql+query)
    return(dbget(sql+query))

