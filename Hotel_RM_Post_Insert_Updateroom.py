from sqlwrapper import gensql
import json

def hotel_rm_post_insert_updateroomlist(request):
    d = request.json
    print(gensql('insert','room_management.RM_Room_List',d))
    return("success")
def hotel_rm_post_insert_updateroomcondition(request):
    d = request.json
    print(gensql('insert','room_management.RM_Room_Condition',d))
    return("success")
def hotel_rm_post_insert_updateoutoforderservice(request):
    d = request.json
    print(gensql('insert','room_management.RM_Room_Mainteanance',d))
    return("success")
def hotel_rm_post_insert_updateroommaintenance(request):
    d = request.json
    d['rm_resolvedon'] = 'unresolved' 
    print(gensql('insert','room_management.RM_Room_Mainteanance_Acitivity_Log',d))
    return("success")



