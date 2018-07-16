from sqlwrapper import gensql, dbget
import datetime
import json
def HOTEL_REM_POST_SELECT_QueryRatecode(request):
  res_arrival = request.json['res_arrival']
  sql_value = dbget("select ratecode_setup.*, ratecode.rate_code, room_type.type, rate_details.*, currency.currency from revenue_management.ratecode_setup left join revenue_management.ratecode \
                 on revenue_management.ratecode_setup.ratecode_id = revenue_management.ratecode.ratecode_id left join room_management.room_type \
                 on room_management.room_type.id = revenue_management.ratecode_setup.roomtype_id left join revenue_management.currency \
                 on revenue_management.currency.transaction_currency_id = revenue_management.ratecode_setup.transaction_currency_id left join revenue_management.rate_details \
                 on revenue_management.rate_details.ratecode_id = revenue_management.ratecode_setup.ratecode_id where '"+res_arrival+"' between rate_details.start_date and  rate_details.end_date")
  sqlvalue = json.loads(sql_value)
  return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sqlvalue  ,'ReturnCode':'RRTS'},indent=4))
