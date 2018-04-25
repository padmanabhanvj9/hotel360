#Input Params: business_id
#OutputParams: business_id, business_mobile, business_first_name, business_last_name, doj
#Purpose: It received input parameters from root file as STRING and passed those parameters to DB wrapper as dictionary/List,
#DB wrapper execute the sql query and return values back to this function.
#Created Date:13/03/2018
#Modified Date: 
#Author:Aravinth 



# import packages required for this program 
import json
import datetime

from sqlwrapper import gensql
from flask import Flask,request, jsonify



# Below function is called from the root file 
def Template_Get_String():
     # syntax for get and assign the value from business_id 
     business_id = request.args['business_id']  
     # call gensql for connect DB and execute the query
     d = {} # define dictionary 
     s = [] # define list
     s = ['business_id','business_mobile','business_first_name','business_last_name','doj']
     d['business_id']= business_id

     #Include buisness logic before calling Sql Query(Optional)
     
     #gensql('insert','table_name',d) # eg: insert into table_name  (business_id)  values ('?') 
     sql_value = gensql('select','test',s,d) # eg: select * from table_name  where  business_id='?'  
     #gensql('update','table_name',d,e) # eg: update NextIDs  set  business_id='?'  where  b_id='?'

     #Include buisness logic after Sql Query

     # finally return the value from DB_Wrapper
     return(sql_value)

    
