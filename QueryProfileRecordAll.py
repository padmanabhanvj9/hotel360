from sqlwrapper import gensql,dbget
import json
def query(sql,pval):
        query = ""
        for k,v in pval.items():
                if v != '':
                   if len(query) == 0:
                      query += " where "
                   else:
                      query += " and " 
                   query += ""+k+" = '"+v+"' "
                   
        sql += query
        print(sql)
        db_res = (dbget(sql))
        return(db_res)
    
def QueryProfileRecordAll(request):
    pval = request.json['val']
    print(pval)
    ptype = request.json['type']
    print(ptype)
    sql = 'select * from profile.pf_individual_profile'
    sql1 = 'select * from profile.pf_company_profile'
    for k,v in ptype.items():
        if v == 'individual':
            return query(sql,pval)
        elif v == 'all':
            data = query(sql,pval)
            data += query(sql1,pval)
            return(data)
        else:
            return query(sql1,pval)        
    #return("done")
