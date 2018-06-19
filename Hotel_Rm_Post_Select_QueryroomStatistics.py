from sqlwrapper import dbget
import json

def hotel_rm_post_select_queryroomstatistics(request):
    sql = 'select * from room_management.RM_Room_List order by rm_room'
    #print(sql)      
    db_res = json.loads(dbget(sql))
    #print(db_res,type(db_res),len(db_res))
    Total_Rooms,Total_Clean,Total_Dirty,Total_Inspected,Total_oo,Total_os = len(db_res),0,0,0,0,0
    nres_clean,nres_dirty,nres_insp,nres_os  = 0,0,0,0
    res_clean,res_dirty,res_insp,res_os = 0,0,0,0

    for i in db_res:
        status = i['rm_room_status']
        res_status = i['rm_reservation_status']
        if status == 'dirty':
            Total_Dirty += 1
            if res_status == 'not_reserved':
                nres_dirty += 1
            else :
                res_dirty += 1
        elif status == 'inspected':
            Total_Inspected += 1
            
            if res_status == 'not_reserved':
                nres_insp += 1
            else :
                res_insp += 1            
        elif status == 'clean':
            Total_Clean += 1
            
            if res_status == 'not_reserved':
                nres_clean += 1
            else :
                res_clean += 1            
        elif status == 'oo':
            Total_oo += 1
            
            if res_status == 'not_reserved':
                nres_os += 1
            else :
                res_os += 1            
        elif status == 'os':
            Total_os += 1
            
            if res_status == 'not_reserved':
                nres_os += 1
            else :
                res_os += 1
                
    print(Total_Dirty,Total_Inspected,Total_Clean,Total_oo,Total_os)
    print(nres_clean,nres_dirty,nres_insp,nres_os)
    print(res_clean,res_dirty,res_insp,res_os)
    d={}
    d['Total_Rooms'],d['Total_Dirty'],d['Total_Inspected'],d['Total_Clean'],d['Total_oo'],d['Total_os'] = Total_Rooms,Total_Dirty,Total_Inspected,Total_Clean,Total_oo,Total_os
    d['nres_clean'],d['nres_dirty'],d['nres_insp'],d['nres_os'] = nres_clean,nres_dirty,nres_insp,nres_os
    d['res_clean'],d['res_dirty'],d['res_insp'],d['res_os'] = res_clean,nres_dirty,res_insp,res_os
    print(d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':d  ,'ReturnCode':'RRTS'},indent=4))

