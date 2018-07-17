from flask import Flask,request
import json
from sqlwrapper import gensql,dbget
import datetime
app = Flask(__name__)
@app.route("/cashiering_billing_currency_selectid",methods=['POST'])

def index():

       res_id = request.json['res_id']
       s = dbget("select * from cashiering.billing_post where res_id="+res_id+" ")
       print(s)
       return s

if __name__ == "__main__":
         app.run(host="192.168.1.4",port=5000)



   

