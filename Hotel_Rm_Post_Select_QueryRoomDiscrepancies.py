from sqlwrapper import gensql,dbfetch,dbget,dbput
import json

def hotel_rm_post_select_queryroomdiscrepancies(request):
    d, e= {},{}
    room_discrepancy = json.loads(dbget("select * from room_management.rm_room_list \
                                        where rm_fo_status = 'occupied' and rm_hk_status = 'vacant'"))
    print(room_discrepancy)
    if len(room_discrepancy) is not None:
        for discrepancy in room_discrepancy:
           
           d['rm_room'] = discrepancy['rm_room']
           e['rm_room_discrepancy'] = 'Skip'
           skip_person = gensql('update','room_management.rm_room_list',e,d)
    else:
        pass
       
    sleep_details = json.loads(dbget("select * from room_management.rm_room_list \
                                    where rm_fo_status = 'vacant' and rm_hk_status = 'occupied'"))
    c,s={},{}
    if len(sleep_details) is not None:
        
        for sleep in sleep_details:
          
           s['rm_room'] = sleep['rm_room']
           c['rm_room_discrepancy'] = 'Sleep'
           sleep_person = gensql('update','room_management.rm_room_discrepancy',c,s)
    else:
        pass
    
    person_details = json.loads(dbget("select * from room_management.rm_room_list"))
    preson_differ = list(filter(lambda x:x['rm_hk_person']!=x['rm_fo_person'],person_details))
    a,b={},{}
    print(preson_differ)
    if len(preson_differ) is not None:
        for preson in preson_differ:
              a['rm_room'] = preson['rm_room']
              b['rm_room_discrepancy'] = 'Person'
              person_differ_details = gensql('update','room_management.rm_room_list',b,a)
    else:
        pass
    
   

    sql = json.loads(dbget('select * from  room_management.rm_room_list order by rm_room'))
    #print(sql)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))
