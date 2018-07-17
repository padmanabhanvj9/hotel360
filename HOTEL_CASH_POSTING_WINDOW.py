from flask import Flask,request
import json
from sqlwrapper import gensql
import datetime
app = Flask(__name__)
@app.route("/cashiering_posting_window",methods=['POST'])

def index():
    d = request.json
    print(d)
    gensql('insert','cashiering.posting_window',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent=4))

if __name__ == "__main__":
         app.run(host="192.168.1.4",port=5000)
