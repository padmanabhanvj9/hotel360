
#Input Param: Null
#OutputParam: Null
#Purpose: This root file pass the parameters value to another file  
#Date: 13/03/18
#Author: Daisy

from flask import Flask,request, jsonify

#Review
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
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#Review , include comment
#Post Method to invoke JSON POST Request
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

@app.route("/Profile/QueryProfileRecordALL",methods=['POST'])
def queryallrecord():
   return QueryProfileRecordALL()
@app.route("/profile/MergeProfile",methods=['POST'])
def mergeprofilerecord():
   return MergeProfile(request)
@app.route("/profile/QueryProfileRecordAll",methods=['POST'])
def queryallrecord():
   return QueryProfileRecordAll(request)
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="192.168.99.1",port=5000)
   
