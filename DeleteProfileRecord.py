from sqlwrapper import gensql,dbput
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def DeleteProfileRecord():
   #con = psycopg2.connect(user='akvwghpxnyalss',password='bc0080c7c0f0b55e162582666cf6b39227c6160e2759dbb0d7f28d58190952cd',host='ec2-54-235-146-184.compute-1.amazonaws.com',port='5432',database='dfbvc8j8egd076')
   #cur = con.cursor()
                   
   PF_Firstname = request.args['PF_Firstname']
   PF_Mobileno = request.args['PF_Mobileno']
   PF_Type = request.args['PF_Type']

   if PF_Type == 'individual':
      
      if request.args.get('PF_Firstname')and request.args.get('PF_Mobileno') and request.args.get('PF_Type'):

         sql = ("delete from profile.pf_individual_profile where PF_Firstname = '"+PF_Firstname+"' and PF_Mobileno = "+PF_Mobileno+" and PF_Type = '"+PF_Type+"'")
         print(sql)             
         #cur.execute(sql)
         dbput(sql)
         #con.commit()
       
         return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

   else :
 
        sql = ("delete from profile.pf_company_profile where PF_Firstname = '"+PF_Firstname+"' and PF_Mobileno = "+PF_Mobileno+" and PF_Type = '"+PF_Type+"' ")
        print(sql)   
        dbput(sql)
     
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))


