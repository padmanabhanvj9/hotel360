
#Input Param: Null
#OutputParam: Null
#Purpose: This root file pass the parameters value to another file  
#Date: 13/03/18
#Author: Daisy

from flask import Flask,request, jsonify

#</------profile webservice-----------/>
from UpdateIndividualProfile import UpdateIndividualProfile
from UpdateCompanyProfile import UpdateCompanyProfile
from UpdateProfileNotes import UpdateProfileNotes
from UpdateProfilePreference import UpdateProfilePreference
from UpdateProfileCreditcard import UpdateProfileCreditcard
from UpdateNegotiatedRate import UpdateNegotiatedRate
from DeleteProfileRecord import DeleteProfileRecord
from QueryNegotiatedRate import QueryNegotiatedRate
from QueryProfileRecord import QueryNegotiatedRate
from QueryProfileRecord import QueryProfileNotes
from QueryProfileRecord import QueryProfilePreference
from QueryProfileRecord import QueryProfileAcitivitylog
from UpdateProfileRecord import UpdateProfileRecordIndividual
from UpdateProfileRecord import UpdateProfileRecordCompany
from MergeProfile import MergeProfile
from UpdateProfilePreferencenew import UpdateProfilePreferencenew
from UpdateProfileNotesRecord import UpdateProfileNotesRecord
from UpdateProfileNegotiatedRateRecord import UpdateProfileNegotiatedRateRecord
from QueryProfileRecord import QueryProfileCreditcard
from UpdateProfileCreditcardRecord import UpdateProfileCreditcardRecord
from QueryProfileRecordAll import QueryProfileRecordAll
#</------profile webservice-------------------/>

#</--------------reservation webservice---------/>
from HOTEL_RES_POST_INSERT_UpdateNewReservation import HOTEL_RES_POST_INSERT_UpdateNewReservation
from HOTEL_RES_POST_UPDATE_UpdateReservation import HOTEL_RES_POST_UPDATE_UpdateReservation
from HOTEL_RES_POST_INSERT_UpdateFixedRateReservation import HOTEL_RES_POST_INSERT_UpdateFixedRateReservation
from HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation import HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation
from HOTEL_RES_POST_INSERT_WaitlistReservation import HOTEL_RES_POST_INSERT_WaitlistReservation
from HOTEL_RES_GET_SELECT_QueryWaitlistReservation import HOTEL_RES_GET_SELECT_QueryWaitlistReservation
from HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation import HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation
from HOTEL_RES_POST_INSERT_UpdateAlertReservation import HOTEL_RES_POST_INSERT_UpdateAlertReservation
from HOTEL_RES_GET_SELECT_QueryAlertReservation import HOTEL_RES_GET_SELECT_QueryAlertReservation
from HOTEL_RES_POST_UPDATE_UpdateReservationAlert import HOTEL_RES_POST_UPDATE_UpdateReservationAlert
from Hotel_RES_Get_Select_QueryReservationActivitylog import Hotel_RES_Get_Select_QueryReservationActivitylog
from Hotel_RES_Post_Insert_UpdateFixedChargesReservation import Hotel_RES_Post_Insert_UpdateFixedChargesReservation
from HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation import HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation
from HOTEL_RES_GET_SELECT_QueryFixedChargesReservation import HOTEL_RES_GET_SELECT_QueryFixedChargesReservation
from HOTEL_RES_POST_INSERT_UpdateDeposit import HOTEL_RES_POST_INSERT_UpdateDeposit
from HOTEL_RES_POST_UPDATE_UpdateDeposit import HOTEL_RES_POST_UPDATE_UpdateDeposit
from HOTEL_RES_GET_SELECT_QueryDeposit import HOTEL_RES_GET_SELECT_QueryDeposit
from HOTEL_RES_GET_SELECT_RoomUnassign import HOTEL_RES_GET_SELECT_RoomUnassign
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Insert_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Update_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Get_Select_QueryGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Insert_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Update_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Get_Select_QueryGuestTraces
from HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation import HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation
from Hotel_RES_Post_Select_Queryreservation import hotel_res_post_select_queryreservation
#</--------------reservation webservice---------/>
#<-------------------Frontdesk------------------>
from HOTEL_FD_POST_INSERT_UpdateQueueRreservation import HOTEL_FD_POST_INSERT_UpdateQueueRreservation
from HOTEL_FD_GET_SELECT_QueryQueueReservation import HOTEL_FD_GET_SELECT_QueryQueueReservation
#<--------------------------------------------------->
#<---------------Room management------------------------->
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroomlist
from Hotel_RM_Post_Update_Updateroomstatus import hotel_rm_post_update_updateroomstatus
from Hotel_RM_Post_Select_Queryhousekeepinglist import hotel_rm_post_select_queryhousekeepinglist
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroomcondition
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateoutoforderservice
from Hotel_RM_Post_Select_Queryoutoforderservice import hotel_rm_post_select_queryoutoforderservice
from Hotel_RM_Post_Insert_Updateroom import hotel_rm_post_insert_updateroommaintenance
from Hotel_RM_Post_Select_Queryroommaintenance import hotel_rm_post_select_queryroommaintenance
from Hotel_RM_Post_Update_Updateroomdiscrepancies import hotel_rm_post_update_updateroomdiscrepancies

#<------------------------------------------------------------------->
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#Review , include comment
#Post Method to invoke JSON POST Request
#<------profile route ---->
@app.route("/")
def index():
   return "welcome to smartmo"
@app.route("/Profile/UpdateIndividualProfile",methods = ['POST'])

def CreateProfile():
   return UpdateIndividualProfile(request)

@app.route("/Profile/UpdateCompanyProfile",methods = ['POST'])
def CreateCompanyProfile():
   return UpdateCompanyProfile(request)

@app.route("/Profile/UpdateProfileNotes", methods=['POST'])
def ProfileNotes():
   return UpdateProfileNotes(request)

@app.route("/Profile/UpdateProfilePreference",methods=['POST'])
def UpdateGuestPreference():
   return UpdateProfilePreference(request)

@app.route("/Profile/UpdateProfileCreditcard", methods=['POST'])
def Updateprofilecreditcard():
   return UpdateProfileCreditcard(request)

@app.route("/Profile/UpdateNegotiatedRate",methods=['POST'])
def CreateNegotiatedRate():
   return UpdateNegotiatedRate(request)
@app.route("/Profile/UpdateProfileRecordIndividual",methods=['POST'])
def updateIndividual():
   return UpdateProfileRecordIndividual()
@app.route("/Profile/UpdateProfileRecordCompany",methods=['POST'])
def updatecompany():
   return UpdateProfileRecordCompany()

@app.route("/Profile/DeleteProfileRecord",methods=['GET'])
def deleteprofile():
   return DeleteProfileRecord()
@app.route("/Profile/QueryNegotiatedRate",methods=['GET'])
def querynegotiatedrate():
   return QueryNegotiatedRate()
@app.route("/Profile/QueryProfileNotes",methods=['GET'])
def querynotes():
   return QueryProfileNotes()
@app.route("/Profile/QueryProfilePreference",methods=['GET'])
def profilepreference():
   return QueryProfilePreference()
@app.route("/Profile/QueryProfileAcitivitylog",methods=['GET'])
def queryprofilelog():
   return QueryProfileAcitivitylog()

@app.route("/Profile/UpdateProfilePreferencenew",methods=['POST'])
def newprofilepreference():
   return UpdateProfilePreferencenew(request)
@app.route("/Profile/UpdateProfileNotesRecord",methods=['POST'])
def updateprofilenotes():
   return UpdateProfileNotesRecord(request)
@app.route("/Profile/UpdateProfileNegotiatedRateRecord",methods=['POST'])
def updatenegotiatedrate():
   return UpdateProfileNegotiatedRateRecord(request)
@app.route("/Profile/QueryProfileCreditcard",methods=['GET'])
def querycreditcard():
   return QueryProfileCreditcard()
@app.route("/Profile/UpdateProfileCreditcardRecord",methods=['POST'])
def updatecreditcard():
   return UpdateProfileCreditcardRecord(request)


@app.route("/profile/MergeProfile",methods=['POST'])
def mergeprofilerecord():
   return MergeProfile(request)
@app.route("/profile/QueryProfileRecordAll",methods=['POST'])
def queryallrecord():
   return QueryProfileRecordAll(request)
#</----------------------/>
#</----------------reservation route--------->
@app.route("/Hotel_RES_Post_Insert_UpdateFixedChargesReservation",methods=['POST'])
def insertfixedcharges():
    return Hotel_RES_Post_Insert_UpdateFixedChargesReservation(request)

@app.route("/HOTEL_RES_POST_INSERT_UpdateNewReservation",methods=['POST'])
def CreateNewReservation():
    return HOTEL_RES_POST_INSERT_UpdateNewReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateReservation",methods=['post'])
def UpdateReservation():
    return HOTEL_RES_POST_UPDATE_UpdateReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateFixedRateReservation",methods=['POST'])
def insertfixedrate():
    return HOTEL_RES_POST_INSERT_UpdateFixedRateReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation",methods=['POST'])
def updatefixedrate():
    return HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_WaitlistReservation",methods=['POST'])
def waitlistreservation():
    return HOTEL_RES_POST_INSERT_WaitlistReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryWaitlistReservation",methods=['GET'])
def queryWaitlistReservation():
    return HOTEL_RES_GET_SELECT_QueryWaitlistReservation()
@app.route("/HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation",methods=['POST'])
def updatewaitlistreservation():
    return HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateAlertReservation",methods=['POST'])
def alertreservation():
    return HOTEL_RES_POST_INSERT_UpdateAlertReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryAlertReservation",methods=['GET'])
def queryalert():
    return HOTEL_RES_GET_SELECT_QueryAlertReservation()
@app.route("/HOTEL_RES_POST_UPDATE_UpdateReservationAlert",methods=['POST'])
def updatealert():
    return HOTEL_RES_POST_UPDATE_UpdateReservationAlert(request)
@app.route("/Hotel_RES_Get_Select_QueryReservationActivitylog",methods=['GET'])
def queryreservationactivitylog():
    return Hotel_RES_Get_Select_QueryReservationActivitylog()
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def updatefixedcharges():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryFixedChargesReservation",methods=['GET'])
def queryfixedcharges():
    return HOTEL_RES_GET_SELECT_QueryFixedChargesReservation()
@app.route("/HOTEL_RES_POST_INSERT_UpdateDeposit",methods=['POST'])
def insertdeposit():
    return HOTEL_RES_POST_INSERT_UpdateDeposit(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateDeposit",methods=['POST'])
def updatedeposit():
    return HOTEL_RES_POST_UPDATE_UpdateDeposit(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryDeposit",methods=['GET'])
def querydeposit():
    return HOTEL_RES_GET_SELECT_QueryDeposit()
@app.route("/HOTEL_RES_GET_SELECT_RoomUnassign",methods=['GET'])
def roomunassign():
    return HOTEL_RES_GET_SELECT_RoomUnassign()
@app.route("/Hotel_RES_Post_Insert_UpdateGuestPrivileges",methods=['POST'])
def GuestPrivileges():
    return Hotel_RES_Post_Insert_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestPrivileges",methods=['POST'])
def UpdateGuestPrivileges():
    return Hotel_RES_Post_Update_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestPrivileges",methods=['GET'])
def SelectGuestPrivileges():
    return Hotel_RES_Get_Select_QueryGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Insert_UpdateGuestTraces",methods=['POST'])
def GuestTraces():
    return Hotel_RES_Post_Insert_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestTraces",methods=['POST'])
def UpdateGuestTraces():
    return Hotel_RES_Post_Update_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestTraces",methods=['GET'])
def SelectGuestTraces():
    return Hotel_RES_Get_Select_QueryGuestTraces(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def UpdateFixedChargesReservation():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route('/Hotel_Res_Post_Select_Queryreservation',methods=['POST'])
def Queryreservation():
   return hotel_res_post_select_queryreservation(request)
#</----------------------------/>
#<---------------frontdesk route----------------------->
@app.route("/HOTEL_FD_POST_INSERT_UpdateQueueRreservation",methods=['POST'])
def insertqueue():
    return HOTEL_FD_POST_INSERT_UpdateQueueRreservation(request)
@app.route("/HOTEL_FD_GET_SELECT_QueryQueueReservation",methods=['POST'])
def queryqueue():
    return HOTEL_FD_GET_SELECT_QueryQueueReservation(request)
#<--------------------------------------------->
#<----------------------Room maangement route------------------->
@app.route('/Hotel_Rm_Post_Insert_Updateroomlist',methods=['POST'])
def Updateroomlist():
   return hotel_rm_post_insert_updateroomlist(request)
@app.route('/Hotel_Rm_Post_Update_Updateroomstatus',methods=['GET'])
def Updateroomstatus():
   return hotel_rm_post_update_updateroomstatus(request)
@app.route('/Hotel_Rm_Post_Select_Queryhousekeepinglist',methods=['POST'])
def Queryhousekeepinglist():
   return hotel_rm_post_select_queryhousekeepinglist(request)
@app.route('/Hotel_Rm_Post_Insert_Updateroomcondition',methods=['POST'])
def Updateroomcondition():
   return hotel_rm_post_insert_updateroomcondition(request)
@app.route('/Hotel_Rm_Post_Insert_Updateoutoforderservice',methods=['POST'])
def Updateoutoforderservice():
   return hotel_rm_post_insert_updateoutoforderservice(request)
@app.route('/Hotel_Rm_Post_Select_Queryoutoforderservice',methods=['POST'])
def Queryoutoforderservice ():
   return hotel_rm_post_select_queryoutoforderservice(request)
@app.route('/Hotel_Rm_Post_Insert_Updateroommaintenance',methods=['POST'])
def Updateroommaintenance ():
   return hotel_rm_post_insert_updateroommaintenance(request)
@app.route('/Hotel_Rm_Post_Select_Queryroommaintenance',methods=['GET','POST'])
def Queryroommaintenance():
   return hotel_rm_post_select_queryroommaintenance(request)
@app.route("/hotel_rm_post_update_updateroomdiscrepancies",methods=['POST'])
def updateroomdiscrepancies():
   return hotel_rm_post_update_updateroomdiscrepancies(request)

#<--------------------------------------------------------->
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="192.168.99.1",port=5000)
   
