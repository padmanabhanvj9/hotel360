
#Input Param: Null
#OutputParam: Null
#Purpose: This root file pass the parameters value to another file  
#Date: 13/03/18
#Author: Daisy

from flask import Flask,request, jsonify

#</------profile webservice-----------/>
from UpdateIndividualProfile import UpdateIndividualProfile
from UpdateCompanyProfile import UpdateCompanyProfile
from QueryProfileRecord import QueryProfileAcitivitylog
from QueryProfileRecord import QueryNegotiatedRate
from UpdateNegotiatedRate import UpdateNegotiatedRate
from UpdateProfileNotes import UpdateProfileNotes
from QueryProfileRecord import QueryProfileNotes
from UpdateProfilePreferencenew import UpdateProfilePreferencenew
from UpdateProfilePreference import UpdateProfilePreference
from UpdateProfileCreditcard import UpdateProfileCreditcard
from DeleteProfileRecord import DeleteProfileRecord
from QueryProfileRecord import QueryProfilePreference
from UpdateProfileCreditcardRecord import UpdateProfileCreditcardRecord
from UpdateProfileRecord import UpdateProfileRecord
from QueryProfileRecord import QueryProfileCreditcard
from UpdateProfileNotesRecord import UpdateProfileNotesRecord
from UpdateProfileNegotiatedRateRecord import UpdateProfileNegotiatedRateRecord
from MergeProfile import MergeProfile
from QueryProfileRecordAll import QueryProfileRecordAll
from profilesearch import QueryProfileSearch
from QueryProfileHistory import QueryProfileHistoryRecord
from QueryProfileHistory import QueryProfileStatistics
from QueryProfileHistory import QueryProfileFutureRecord
#delete service
from DeleteProfileRecordAll import DeleteProfileCreditCard
from DeleteProfileRecordAll import DeleteProfileNegotiate
from DeleteProfileRecordAll import DeleteProfileNotes
from DeleteProfileRecordAll import DeleteProfilePreference
#dropdown select
from profilecity import profilecity
from profilecity import profilelanguage
from profilecity import profilecountry
from profilecity import profilestate
from profilecity import profilepostalcode
from profilecity import profilevip 
from profilecity import profilenationality
from profilecity import profilecurrency
from profilecity import profilecommunication
from profilecity import profilepftype
from profilecity import profileratecode
from profilecity import profilenotetype
from profilecity import profilepreferencegroup
from profilecity import profilepreferencevalue
#dropdown insert
from profileinsertvalue import profilecity_insert
from profileinsertvalue import profilelanguage_insert
from profileinsertvalue import profilecountry_insert
from profileinsertvalue import profilestate_insert
from profileinsertvalue import profilepostalcode_insert
from profileinsertvalue import profilevip_insert
from profileinsertvalue import profilenationality_insert
from profileinsertvalue import profilecurrency_insert
from profileinsertvalue import profilecommunication_insert
from profileinsertvalue import profilepftype_insert
from profileinsertvalue import profileratecode_insert
from profileinsertvalue import profilenotetype_insert
from profileinsertvalue import profilepreferencegroup_insert
from profileinsertvalue import profilepreferencevalue_insert

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
from HOTEL_RES_GET_SELECT_QueryDepositrule import HOTEL_RES_GET_SELECT_QueryDepositrule
from HOTEL_RES_GET_SELECT_RoomUnassign import HOTEL_RES_GET_SELECT_RoomUnassign
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Insert_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Post_Update_UpdateGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestPrivileges import Hotel_RES_Get_Select_QueryGuestPrivileges
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Insert_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Post_Update_UpdateGuestTraces
from Hotel_RES_Post_Insert_UpdateGuestTraces import Hotel_RES_Get_Select_QueryGuestTraces
from HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation import HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation
from Hotel_RES_Post_Select_Queryreservation import hotel_res_post_select_queryreservation
from QueryReservationSearch import QueryReservationSearch
from HOTEL_RES_POST_SELECT_QueryHistoryReservation import QueryHistoryReservation
from HOTEL_RES_GET_SELECT_QueryFixedRateReservation import HOTEL_RES_GET_SELECT_QueryFixedRateReservation

from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Restype
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Alertarea
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Alertcode
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Origin
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Source
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Payment
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Market
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Department
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_Transaction_code
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_depositrule
from HOTEL_RES_GET_SELECT_QueryReservationValue import Hotel_RES_GET_SELECT_CancelReason

from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_RestypeInsert
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Alertarea
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Alertcode
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Origin
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Source
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Payment
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Market
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Department
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Transaction_code
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_Depositrule
from HOTEL_RES_POST_INSERT_InsertReservationValue import Hotel_RES_POST_INSERT_CancelReason

from Hotel_RES_POST_SELECT_QueryFutureReservation import ProfileFutureReservation
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
from Hotel_Rm_Post_Select_QueryRoomList import hotel_rm_post_select_queryroomlist
from Hotel_Rm_Post_Select_QueryRoomCondition import hotel_rm_post_select_queryroomcondition
from Hotel_Rm_Post_Update_UpdateRoomCondition import hotel_rm_post_update_updateroomcondition


from RoomManagementDropdown import select_roomstatus
from RoomManagementDropdown import select_class
from RoomManagementDropdown import select_condition
from RoomManagementDropdown import select_hkstatus_code
from RoomManagementDropdown import select_room_type
from RoomManagementDropdown import select_room_no
from RoomManagementDropdown import select_discription
from RoomManagementDropdown import select_servicestatus_code
from RoomManagementDropdown import select_turndownstatus


#insert

from RoomManagementDropdownInsert import insert_roomstatus
from RoomManagementDropdownInsert import insert_class
from RoomManagementDropdownInsert import insert_condition
from RoomManagementDropdownInsert import insert_hkstatus_code
from RoomManagementDropdownInsert import insert_room_type
from RoomManagementDropdownInsert import insert_room_no
from RoomManagementDropdownInsert import insert_room_discription
from RoomManagementDropdownInsert import insert_servicestatus_code
from RoomManagementDropdownInsert import insert_turndownstatus
#<------------------------------------------------------------------->
#<---------------------------------amazonlex---------->
from AMAZON_RESERVATION_LAMBDA_LEX import AMAZON_RESERVATION_LAMBDA_LEX
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

@app.route("/Profile/QueryProfileAcitivitylog",methods=['POST'])
def queryprofilelog():
   return QueryProfileAcitivitylog(request)

@app.route("/Profile/QueryNegotiatedRate",methods=['POST'])
def querynegotiatedrate():
   return QueryNegotiatedRate(request)

@app.route("/Profile/UpdateNegotiatedRate",methods=['POST'])
def InsertNegotiatedRate():
   return UpdateNegotiatedRate(request)

@app.route("/Profile/UpdateProfileNotes", methods=['POST'])
def ProfileNotes():
   return UpdateProfileNotes(request)

@app.route("/Profile/QueryProfileNotes",methods=['POST'])
def querynotes():
   return QueryProfileNotes(request)

@app.route("/Profile/UpdateProfilePreferencenew",methods=['POST'])
def newprofilepreference():
   return UpdateProfilePreferencenew(request)

@app.route("/Profile/UpdateProfilePreference",methods=['POST'])
def UpdateGuestPreference():
   return UpdateProfilePreference(request)

@app.route("/Profile/UpdateProfileCreditcard", methods=['POST'])
def Updateprofilecreditcard():
   return UpdateProfileCreditcard(request)

@app.route("/Profile/DeleteProfileRecord",methods=['POST'])
def deleteprofile():
   return DeleteProfileRecord(request)

@app.route("/Profile/QueryProfilePreference",methods=['POST'])
def profilepreference():
   return QueryProfilePreference(request)

@app.route("/Profile/UpdateProfileCreditcardRecord",methods=['POST'])
def updatecreditcard():
   return UpdateProfileCreditcardRecord(request)

@app.route("/Profile/UpdateProfileRecord",methods=['POST'])
def updateIndividual():
   return UpdateProfileRecord(request)

@app.route("/Profile/QueryProfileCreditcard",methods=['POST'])
def querycreditcard():
   return QueryProfileCreditcard(request)

@app.route("/Profile/UpdateProfileNotesRecord",methods=['POST'])
def updateprofilenotes():
   return UpdateProfileNotesRecord(request)

@app.route("/Profile/UpdateProfileNegotiatedRateRecord",methods=['POST'])
def updatenegotiatedrate():
   return UpdateProfileNegotiatedRateRecord(request)

@app.route("/profile/MergeProfile",methods=['POST'])
def mergeprofilerecord():
   return MergeProfile(request)
@app.route("/profile/QueryProfileRecordAll",methods=['POST'])
def queryallrecord():
   return QueryProfileRecordAll(request)

@app.route("/Profile/QueryProfileSearch",methods=['GET'])
def ProfileSearch():
   return QueryProfileSearch(request)

@app.route("/Profile/QueryProfileHistory",methods=['POST'])
def QueryProfileHistory():
   return QueryProfileHistoryRecord(request)

@app.route("/Profile/QueryProfileStatistics",methods=['POST'])
def QueryProfileStatisticsRecord():
   return QueryProfileStatistics(request)

@app.route("/Profile/QueryFutureReservation",methods=['POST'])
def QueryProfileFuture():
   return QueryProfileFutureRecord(request)

#delete
@app.route("/Profile/DeleteProfileCreditcard",methods=['POST'])
def DeleteProfileCreditcard():
   return DeleteProfileCreditCard(request)

@app.route("/Profile/DeleteProfileNegotiate",methods=['POST'])
def DeleteProfileNegotiatedRate():
   return DeleteProfileNegotiate(request)

@app.route("/Profile/DeleteProfileNotes",methods=['POST'])
def DeleteProfileNote():
   return DeleteProfileNotes(request)

@app.route("/Profile/DeleteProfilePreference",methods=['POST'])
def DeleteProfilePreferences():
   return DeleteProfilePreference(request)

# select profile dropdown
@app.route("/Profile/profilecity",methods=['GET'])
def cityvalue():
   return profilecity()
@app.route("/Profile/profilelanguage",methods=['GET'])
def languagevalue():
   return profilelanguage()
@app.route("/Profile/profilecountry",methods=['GET'])
def countryvalue():
   return profilecountry()
@app.route("/Profile/profilestate", methods=['GET'])
def statevalue():
   return profilestate()
@app.route("/Profile/profilepostalcode",methods=['GET'])
def postalcodevalue():
   return profilepostalcode()
@app.route("/Profile/profilevip",methods=['GET'])
def profilevivalue():
   return profilevip()
@app.route("/Profile/profilenationality",methods=['GET'])
def profilenationalityvalue():
   return profilenationality()
@app.route("/Profile/profilecurrency",methods=['GET'])
def profilecurrencyvalue():
   return profilecurrency()
@app.route("/Profile/profilecommunication",methods=['GET'])
def profilecommunicationvalue():
   return profilecommunication()
@app.route("/Profile/profilepftype",methods=['GET'])
def profilepftypevalue():
   return profilepftype()
@app.route("/Profile/profileratecode",methods=['GET'])
def profileratecodevalue():
   return profileratecode()
@app.route("/Profile/profilenotetype",methods=['GET'])
def profilenotetypevalue():
   return profilenotetype()
@app.route("/Profile/profilepreferencegroup",methods=['GET'])
def profilepreferencegroupvalue():
   return profilepreferencegroup()
@app.route("/Profile/profilepreferencevalue",methods=['GET'])
def profilepreferencevalues():
   return profilepreferencevalue()
#<----------------------------------------------------------->

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
@app.route("/HOTEL_RES_GET_SELECT_QueryFixedRateReservation",methods=['POST'])
def Queryfixedrate():
    return HOTEL_RES_GET_SELECT_QueryFixedRateReservation(request)
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
@app.route("/HOTEL_RES_GET_SELECT_QueryAlertReservation",methods=['POST'])
def queryalert():
    return HOTEL_RES_GET_SELECT_QueryAlertReservation(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateReservationAlert",methods=['POST'])
def updatealert():
    return HOTEL_RES_POST_UPDATE_UpdateReservationAlert(request)
@app.route("/Hotel_RES_Get_Select_QueryReservationActivitylog",methods=['GET'])
def queryreservationactivitylog():
    return Hotel_RES_Get_Select_QueryReservationActivitylog()
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def updatefixedcharges():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryFixedChargesReservation",methods=['POST'])
def queryfixedcharges():
    return HOTEL_RES_GET_SELECT_QueryFixedChargesReservation(request)
@app.route("/HOTEL_RES_POST_INSERT_UpdateDeposit",methods=['POST'])
def insertdeposit():
    return HOTEL_RES_POST_INSERT_UpdateDeposit(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateDeposit",methods=['POST'])
def updatedeposit():
    return HOTEL_RES_POST_UPDATE_UpdateDeposit(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryDepositrule",methods=['POST'])
def querydepositrule():
    return HOTEL_RES_GET_SELECT_QueryDepositrule(request)
@app.route("/HOTEL_RES_GET_SELECT_RoomUnassign",methods=['GET'])
def roomunassign():
    return HOTEL_RES_GET_SELECT_RoomUnassign()
@app.route("/Hotel_RES_Post_Insert_UpdateGuestPrivileges",methods=['POST'])
def GuestPrivileges():
    return Hotel_RES_Post_Insert_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestPrivileges",methods=['POST'])
def UpdateGuestPrivileges():
    return Hotel_RES_Post_Update_UpdateGuestPrivileges(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestPrivileges",methods=['POST'])
def SelectGuestPrivileges():
    return Hotel_RES_Get_Select_QueryGuestPrivileges(request)
@app.route("/Hotel_RES_Post_Insert_UpdateGuestTraces",methods=['POST'])
def GuestTraces():
    return Hotel_RES_Post_Insert_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Post_Update_UpdateGuestTraces",methods=['POST'])
def UpdateGuestTraces():
    return Hotel_RES_Post_Update_UpdateGuestTraces(request)
@app.route("/Hotel_RES_Get_Select_QueryGuestTraces",methods=['POST'])
def SelectGuestTraces():
    return Hotel_RES_Get_Select_QueryGuestTraces(request)
@app.route("/HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation",methods=['POST'])
def UpdateFixedChargesReservation():
    return HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request)
@app.route('/Hotel_Res_Post_Select_Queryreservation',methods=['POST'])
def Queryreservation():
   return hotel_res_post_select_queryreservation(request)
@app.route("/HOTEL_RES_GET_SELECT_QueryReservationSearch",methods=['GET'])
def QueryReservationSearchVALY():
    return QueryReservationSearch()
@app.route("/HOTEL_RES_POST_SELECT_QueryHistoryReservation",methods=['POST'])
def QueryHistoryReservationVALUE():
    return QueryHistoryReservation(request)

   
@app.route("/Hotel_RES_POST_INSERT_RestypeInsert",methods=['POST'])
def Hotel_RES_POST_INSERT_RestypeInsertvalue():
    return Hotel_RES_POST_INSERT_RestypeInsert(request)
@app.route("/Hotel_RES_POST_INSERT_Alertarea",methods=['POST'])
def Hotel_RES_POST_INSERT_Alertareava():
    return Hotel_RES_POST_INSERT_Alertarea(request)
@app.route("/Hotel_RES_POST_INSERT_Alertcode",methods=['POST'])
def Hotel_RES_POST_INSERT_Alertcodeva():
    return Hotel_RES_POST_INSERT_Alertcode(request)
@app.route("/Hotel_RES_POST_INSERT_Origin",methods=['POST'])
def Hotel_RES_POST_INSERT_Originva():
    return Hotel_RES_POST_INSERT_Origin(request)
@app.route("/Hotel_RES_POST_INSERT_Source",methods=['POST'])
def Hotel_RES_POST_INSERT_Sourceva():
    return Hotel_RES_POST_INSERT_Source(request)
@app.route("/Hotel_RES_POST_INSERT_Payment",methods=['POST'])
def Hotel_RES_POST_INSERT_Paymentvalue():
   return Hotel_RES_POST_INSERT_Payment(request)
@app.route("/Hotel_RES_POST_INSERT_Market",methods=['POST'])
def Hotel_RES_POST_INSERT_Marketvalue():
   return Hotel_RES_POST_INSERT_Market(request)
@app.route("/Hotel_RES_POST_INSERT_Department",methods=['POST'])
def Hotel_RES_POST_INSERT_Departmentvalt():
   return Hotel_RES_POST_INSERT_Department(request)
@app.route("/Hotel_RES_POST_INSERT_Transaction_code",methods=['POST'])
def Hotel_RES_POST_INSERT_Transaction_codevalue():
   return Hotel_RES_POST_INSERT_Transaction_code(request)
@app.route("/Hotel_RES_POST_INSERT_Depositrule",methods=['POST'])
def Hotel_RES_POST_INSERT_Depositruleva():
   return Hotel_RES_POST_INSERT_Depositrule(request)
@app.route("/Hotel_RES_POST_INSERT_CancelReason",methods=['POST'])
def Hotel_RES_POST_INSERT_CancelReasonval():
   return Hotel_RES_POST_INSERT_CancelReason(request)


@app.route("/Hotel_RES_GET_SELECT_Restype",methods=['GET'])
def Hotel_RES_GET_SELECT_Restype():
    return Hotel_RES_GET_SELECT_Restype()
@app.route("/Hotel_RES_GET_SELECT_Alertarea",methods=['GET'])
def Hotel_RES_GET_SELECT_Alertareavalue():
    return Hotel_RES_GET_SELECT_Alertarea()
@app.route("/Hotel_RES_GET_SELECT_Alertcode",methods=['GET'])
def Hotel_RES_GET_SELECT_Alertcodevalue():
    return Hotel_RES_GET_SELECT_Alertcode()
@app.route("/Hotel_RES_GET_SELECT_Origin",methods=['GET'])
def Hotel_RES_GET_SELECT_Originvalue():
    return Hotel_RES_GET_SELECT_Origin()
@app.route("/Hotel_RES_GET_SELECT_Source",methods=['GET'])
def Hotel_RES_GET_SELECT_Sourceva():
    return Hotel_RES_GET_SELECT_Source()
@app.route("/Hotel_RES_GET_SELECT_Payment",methods=['GET'])
def Hotel_RES_GET_SELECT_Paymentvalur():
   return Hotel_RES_GET_SELECT_Payment()
@app.route("/Hotel_RES_GET_SELECT_Market",methods=['GET'])
def Hotel_RES_GET_SELECT_Marketgads():
   return Hotel_RES_GET_SELECT_Market()
@app.route("/Hotel_RES_GET_SELECT_Department",methods=['GET'])
def Hotel_RES_GET_SELECT_Departmentvalue():
   return Hotel_RES_GET_SELECT_Department()
@app.route("/Hotel_RES_GET_SELECT_Transaction_code",methods=['GET'])
def Hotel_RES_GET_SELECT_Transaction_codevalue():
   return Hotel_RES_GET_SELECT_Transaction_code()
@app.route("/Hotel_RES_GET_SELECT_depositrule",methods=['GET'])
def Hotel_RES_GET_SELECT_depositruledasd():
   return Hotel_RES_GET_SELECT_depositrule()
@app.route("/Hotel_RES_GET_SELECT_CancelReason",methods=['GET'])
def Hotel_RES_GET_SELECT_CancelReasonvalue():
   return Hotel_RES_GET_SELECT_CancelReason()

@app.route("/ProfileFutureReservation",methods=['POST'])
def futurereservation():
    return ProfileFutureReservation(request)
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
@app.route("/Hotel_Rm_Post_Select_QueryRoomList",methods=['POST'])
def QueryRoomList():
   return hotel_rm_post_select_queryroomlist(request)
@app.route("/Hotel_Rm_Post_Select_QueryRoomCondition",methods=['POST'])
def QueryRoomCondition():
   return hotel_rm_post_select_queryroomcondition(request)
@app.route("/Hotel_Rm_Post_Update_UpdateRoomCondition",methods=['POST'])
def UpdateRoomCondition():
   return hotel_rm_post_update_updateroomcondition(request)


@app.route("/Select_RoomStatus",methods=['POST'])
def Select_RoomStatus():
  return select_roomstatus()
@app.route("/Select_Class",methods=['POST'])
def Select_Class():
  return select_class()
@app.route("/Select_Condition",methods=['POST'])
def Select_Condition():
  return select_condition()
@app.route("/Select_Hkstatus_Code",methods=['POST'])
def Select_Hkstatus_Code():
  return select_hkstatus_code()
@app.route("/Select_Room_Type",methods=['POST'])
def Select_Room_Type():
  return select_room_type()
@app.route("/Select_Room_No",methods=['POST'])
def Select_Room_No():
  return select_room_no()
@app.route("/Select_Discription",methods=['POST'])
def Select_Discription():
  return select_discription()
@app.route("/Select_Servicestatus_Code",methods=['POST'])
def Select_Servicestatus_Code():
  return select_servicestatus_code()
@app.route("/Select_Turndownstatus",methods=['POST'])
def Select_Turndownstatus():
  return select_turndownstatus()

#insert
@app.route("/Insert_Roomstatus",methods=['POST'])
def Insert_Roomstatus():
  return insert_roomstatus(request)
@app.route("/Insert_Class",methods=['POST'])
def Insert_Class():
  return insert_class(request)
@app.route("/Insert_Condition",methods=['POST'])
def Insert_Condition():
  return insert_condition(request)
@app.route("/insert_hkstatus_code",methods=['POST'])
def insert_hkstatus_code_value():
  return insert_hkstatus_code(request)
@app.route("/insert_room_type",methods=['POST'])
def insert_room_type_value():
  return insert_room_type(request)
@app.route("/insert_room_no",methods=['POST'])
def insert_room_no_value():
  return insert_room_no(request)
@app.route("/insert_room_discription",methods=['POST'])
def insert_room_discription_value():
  return insert_room_discription(request)
@app.route("/insert_servicestatus_code",methods=['POST'])
def insert_servicestatus_codevalue():
  return insert_servicestatus_code(request)
@app.route("/insert_turndownstatus",methods=['POST'])
def insert_turndownstatus_value():
  return insert_turndownstatus(request)


#<--------------------------------------------------------->
#<--------------amazonlex-------------------------->
@app.route('/AMAZON_RESERVATION_LAMBDA_LEX',methods=['POST'])
def amazonlex():
   return AMAZON_RESERVATION_LAMBDA_LEX(request)
#<----------------------------------------------->
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="192.168.99.1",port=5000)
   
