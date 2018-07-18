from sqlwrapper import gensql, dbget
import datetime
import json
def HOTEL_REM_POST_SELECT_QueryRatecode(request):
  res_arrival = request.json['res_arrival']
  sql_value = dbget("select revenue_management.ratecode_setup.*,revenue_management.rate_details.*, room_management.room_type.*, \
revenue_management.currency.*, revenue_management.ratecategory.*, revenue_management.negotiated_rate.*,revenue_management.season_code.* \
from revenue_management.ratecode_setup join revenue_management.rate_details \
on revenue_management.ratecode_setup.ratecode_id = revenue_management.rate_details.ratecode_id \
join room_management.room_type on revenue_management.ratecode_setup.roomtype_id = room_management.room_type.id \
join revenue_management.currency on revenue_management.ratecode_setup.transaction_currency_id = revenue_management.currency.transaction_currency_id \
join revenue_management.ratecategory on revenue_management.ratecode_setup.rate_category_id = revenue_management.ratecategory.ratecategory_id \
join revenue_management.negotiated_rate on revenue_management.ratecode_setup.ratecode_id = revenue_management.negotiated_rate.negotiated_code_id \
join revenue_management.season_code on revenue_management.rate_details.season_code_id = revenue_management.season_code.season_code_id \
where '"+res_arrival+"' between revenue_management.rate_details.start_date and revenue_management.rate_details.end_date")
  sqlvalue = json.loads(sql_value)
  return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sqlvalue  ,'ReturnCode':'RRTS'},indent=4))
