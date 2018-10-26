from sqlwrapper import gensql,dbget,dbput
import json
from flask import Flask,request, jsonify
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def AMAZON_RESERVATION_LAMBDA_LEX(request):
    d = {}
    arrivalsdate = request.args.get('arrival')
    depaturedate = request.args.get('depature')
    #arrivalsdate = request.json['arrival']
    #depaturedate = request.json['depature']
    d['arrival']  = arrivalsdate
    d['depature']  = depaturedate
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    #reservation = {'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}], sort_keys=True, indent=4))
def amazon_insert(request):
    d = {}
    arrivalsdate = request.json['arrival']
    depaturedate = request.json['depature']
    d['arrival']  = arrivalsdate
    d['depature']  = depaturedate
    d['roomtype'] = 'KNGN'
    d['adults'] = 2
    d['child'] = 4
    d['guestname'] = 'daisy'
    d['phone'] = '9698689999'
    d['email'] = 'veroni@gmail.com'
    sql_value = gensql('insert','amazonlex.reservation',d)
    #reservation = {'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}], sort_keys=True, indent=4))
def CheckConfirmation(request):
    no = request.json['confirmation_number']
    print(no)
    no = "PMS"+no
    c_no = b_id = json.loads(dbget("select count(*) from reservation.res_reservation where \
                                    res_confnumber= '"+no+"' "))
    print(c_no[0]['count'],type(c_no[0]['count']))
    if c_no[0]['count'] != 0 : 
       return(json.dumps({"ServiceStatus":"Success","Return_code":"Valid"}))
    else:
       return(json.dumps({"ServiceStatus":"Success","Return_code":"Invalid"}))
def checkinguest(request):
    
        confir = request.json['confirmation_number']
        confir = "PMS"+confir
        mobile = request.json['mobile']
        #phone = request.json['mobile']
        RES_Log_Date = datetime.datetime.utcnow().date()
        print(RES_Log_Date)
        RES_Log_Date = str(RES_Log_Date)
        psql = json.loads(dbget("select res_arrival from reservation.res_reservation where res_confnumber = '"+confir+"' and pf_mobileno = '"+mobile+"'"))
        print(psql)
        #today_arrival = psql[0]['res_arrival']
        if RES_Log_Date == psql[0]['res_arrival']:
            sql = dbput("update reservation.res_reservation set res_guest_status = 'checkin' where res_confnumber = '"+confir+"'")
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'checkin success','ReturnCode':'Valid'}, sort_keys=True, indent=4))
   
        else:
              return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Checkin a Today Guest arrivals only','ReturnCode':'Invalid'}, sort_keys=True, indent=4))

        #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Please say valid mobile number','ReturnCode':'Invalid'}, sort_keys=True, indent=4))
   
def Checkroom(request):
        confir = request.json['confirmation_number']
        confir = "PMS"+confir
        room = request.json['Room']
        c_no = b_id = json.loads(dbget("select count(*) from reservation.res_reservation where \
                                    res_confnumber= '"+confir+"' and res_room = '"+room+"' "))
        if c_no[0]['count'] != 0 : 
          return(json.dumps({"StatusCode":"Success","Return_code":"Valid"}))
        else:
          return(json.dumps({"StatusCode":"Failure","Return_code":"Invalid"}))

def sendemailani(name,email,message,conf_no,arrival,depature,room_type,room,msg_sub):
     print(name,email,message,conf_no,arrival,depature,room_type,room,msg_sub)
     sender = "infocuit.daisy@gmail.com"
     RES_Log_Date = datetime.datetime.utcnow().date()
     print(RES_Log_Date)
     
     for i in email:

          receiver = i
          #print(sender,type(sender),receiver,type(receiver))
          subject = "Kconnect24/7 service"
          msg = MIMEMultipart()
          msg['from'] = sender
          msg['to'] = receiver
          msg['subject'] = subject
        
   
          hotel_name = "smartmo"
          Address = "21,first street,chennai"
          mobile_no = "9988776655"
          email_no = "hotelsmart@gmail.com"
          html = """\
          <!DOCTYPE html>
          <html>
          <head>
          <meta charset="utf-8">
          </head>
          <body>
          <dl>
          <dt>
          <pre>
          <font size="4" color="black">"""+hotel_name+""",</font>
          <font size="4" color="black">"""+Address+""",</font>
          <font size="4" color="black">"""+mobile_no+""",</font>
          <font size="4" color="black">"""+email_no+""".</font>
          
          
          <font size="4" color="black">Dear """+name+""",</font>
          <font size="4" color="black">    Echodot received a request from the customer on """+str(RES_Log_Date)+""" regarding """+msg_sub+""".
          Please send someone to resolve the issue.</font>
          
         
           </pre>
     <pre>
          <font size="4" color="blue">Room Number: """+room+"""</font>
          <font size="4" color="blue">Room Type: """+room_type+"""</font>
          <font size="4" color="blue">Confirmation Number: """+conf_no+"""</font>
          <font size="4" color="blue">Arrival Date: """+arrival+"""</font>
          <font size="4" color="blue">Depature Date: """+depature+"""</font>
         
          

          <font size="4" color="black">With best regards / Yours sincerely,</font>
          <font size="4" color="black">Echodot Assistant</font></pre>
            
          </dl>        
          </body>
          </html>
          """

          msg.attach(MIMEText(html,'html'))
          
          gmailuser = 'infocuit.daisy@gmail.com'
          password = 'justinveroni'
          server = smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login(gmailuser,password)
          text = msg.as_string()
          server.sendmail(sender,receiver,text)
          print ("the message has been sent successfully")
          server.quit()
     return(json.dumps({'Return': 'Message Send Successfully',"Return_Code":"MSS","Status": "Success","Status_Code": "200"}, sort_keys=True, indent=4))



def callexternalapi(request):
     phone = request.json['confirmation_number']
     d = {}
     d['res_confnumber'] = "PMS"+phone
     result = json.loads(gensql('select','reservation.res_reservation','*',d))
     re = result[0]
     print(re,type(re))     
     name = "Hotelier"
     #email = ['r.ahamed@konnect247.com','i.sidhanee@konnect247.com','jazizahmed@gmail.com','infocuit.daisy@gmail.com']
     email = ['infocuit.daisy@gmail.com','infocuit.banupriya@gmail.com']
     message = "Kconnect24/7"
     conf_no = phone
     #hotel_name = "SMARTMO"
     arrival = re['res_arrival']
     depature = re['res_depature']
     room_type = re['res_room_type']
     msg_sub = request.json['msg']
     room = request.json['Room']
     return sendemailani(name,email,message,conf_no,arrival,depature,room_type,room,msg_sub)

