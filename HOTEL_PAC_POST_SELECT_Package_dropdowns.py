from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_PAC_POST_SELECT_Forecastgroup(request):
    d = request.json
    x = json.loads(dbget("select * from packages.forecast_group"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Transactioncode(request):
    d = request.json
    x = json.loads(dbget("select * from packages.transaction_details"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Postingrhythm(request):
    d = request.json
    x = json.loads(dbget("select * from packages.posting_rhythm"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Calculaterule(request):
    d = request.json
    x = json.loads(dbget("select * from packages.calculate_rule"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Iteminventory(request):
    d = request.json
    x = json.loads(dbget("select * from packages.item_inventory"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Packages(request):
    d = request.json
    x = json.loads(dbget("SELECT package_code_id, package_code,forecast_group.*,short_description, description,transaction_details.*,\
                   currency.*,attributes_id,posting_rhythm.*,calculate_rule.*, valid_time_from, valid_time_to, sell_separate, post_next_day,\
                   package_code.item_inventory_selected_id,package_code.alternates_selected_id \
                   FROM packages.package_code join packages.forecast_group on package_code.forecast_code_id = forecast_group.forecast_group_id\
                   join packages.transaction_details on package_code.transaction_code_id = transaction_details.transaction_code_id\
                   join profile.currency on package_code.currency_id = currency.id\
                   join packages.posting_rhythm on package_code.posting_rhythm_id = posting_rhythm.posting_rhythm_id\
                   join packages.calculate_rule on package_code.calculate_rule_id = calculate_rule.calculate_rule_id\
                   where package_code.package_code_id="+str(d['package_code_id'])+" "))
    #print(x,len(x))
    x1,x2 = [],[]
    if len(x) == 1 :
      x1 = json.loads(dbget("select item_inventory_selected_id,item_id,item_inventory.* from packages.item_inventory_selected join\
                   packages.item_inventory on item_inventory_selected.item_inventory_id = item_inventory.item_inventory_id\
                   where item_id = "+str(x[0]['item_inventory_selected_id'])+" "))
      x2 = json.loads(dbget("SELECT alternate_selected.alternates_selected_id, alternate_id, package_code.package_code_id, package_code.package_code\
	           FROM packages.alternate_selected join packages.package_code on package_code.alternates_selected_id = \
	           alternate_selected.alternate_id where \
	           alternate_selected.alternate_id = "+str(x[0]['alternates_selected_id'])+" "))
    y = json.loads(dbget("select packages_details_id,package_code_id,start_date,end_date,price,allowance,season_code.*\
                  from packages.package_details join revenue_management.season_code on package_details.season_code_id =\
                  season_code.season_code_id where package_code_id="+str(d['package_code_id'])+""))

    return(json.dumps({"Package_header":x,"item_inventory":x1,"alternates":x2,"Package_details":y,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_PAC_POST_SELECT_Packages_All(request):
    d = request.json
    x = json.loads(dbget("select package_code_id,package_code,short_description,sell_separate,currency.* \
                   FROM packages.package_code join  profile.currency on package_code.currency_id = currency.id"))
    return(json.dumps({"Return_values":x,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))


def HOTEL_PAC_POST_SELECT_PackagesTrasnactioncode(request):
    today_date =datetime.datetime.utcnow().date()
    sql_value = json.loads(dbget("select packages.package_code.package_code,packages.package_code.short_description, \
                                    packages.package_details.package_code_id,packages.package_details.price from packages.package_details \
                                    join packages.package_code on packages.package_code.package_code_id =  packages.package_details.package_code_id \
                                    where '"+str(today_date)+"' <= packages.package_details.start_date or '"+str(today_date)+"' >= packages.package_details.end_date"))


    return(json.dumps({"Return_values":sql_value,"Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))
