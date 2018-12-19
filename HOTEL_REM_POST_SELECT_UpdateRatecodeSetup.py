from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_SELECT_UpdateRatecodeSetup(request):
    d = request.json
    print(d)
    records,rec1,rec2,rec3,rec4,rec5 = [],[],[],[],[],[]

    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.id,\
                                market.marketgroup,market.marketgroup_description,res_source.id,\
                                res_source.sourcecode,res_source.sourcedescription,ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id\
                                join reservation.market on ratecode_setup.market_id = market.id\
                                join reservation.res_source on ratecode_setup.source_id = res_source.id\
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id\
                                join revenue_management.rate_components on ratecode_setup.rate_components_id =\
                                rate_components.components_id join revenue_management.tranction_details on\
                                ratecode_setup.transaction_details_id = tranction_details.tranction_detail_id \
                                where ratecode_setup.ratecode_id="+str(d['ratecode_id'])+" "))
    #print(records[0]['rooms_id'])
    #print(records)
    if len(records) != 0:
      #if rec3[0]['rooms_id'] is not None:
        print("rooms")
        rec1 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where rooms_id ="+str(records[0]['rooms_id'])+""))

    #records.append({"room_types":rec1})
    #print(records[0]['packages_id'])
        #if rec3[0]['packages_id'] is not None:
        print("packages")
        rec2 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id where packages_id="+str(records[0]['packages_id'])+" "))
    #records.append({"packages":rec2})

    rec3 = json.loads(dbget("SELECT rate_details_id, one_adult_amount, two_adult_amount, three_adult_amount,\
                             four_adult_amount, extra_adult_amount, one_child_amount, two_child_amount,\
                             extra_child_amount, start_date, end_date, season_code.*,rate_days.*,rate_details.ratecode_id,\
                             rate_details.rooms_id,rate_details.packages_id, \
                             rate_tier.* FROM revenue_management.rate_details \
                             join revenue_management.season_code on rate_details.season_code_id = \
                             season_code.season_code_id join revenue_management.rate_days on \
                             rate_details.rate_days_id = rate_days.rate_days_id left join revenue_management.rate_tier \
                             on rate_details.rate_tier_id = rate_tier.rate_tier_id where \
                             rate_details.ratecode_id="+str(d['ratecode_id'])+" "))
    print("rec3",rec3)
    if len(rec3) != 0:
      #if rec3[0]['rooms_id'] is not None:

       print("rooms")
       rec4 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where rooms_id ="+str(rec3[0]['rooms_id'])+""))
    #rec3.append({"room_types":rec4})
    #print(records[0]['packages_id'])
       if rec3[0]['packages_id'] is not None:
         print("packages")
         rec5 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id where packages_id="+str(rec3[0]['packages_id'])+" "))
    #rec3.append({"packages":rec5})
    return(json.dumps({"Rate_header":records,"Rate_header_room_types":rec1,"Rate_header_packages":rec2,
                       "Rate_details":rec3,"Rate_details_room_types":rec4,"Rate_details_packages":rec5,
                       "Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_REM_POST_SELECT_SelectRatesetupAll(request):
    records,rec1,rec2,rec3,rec4,rec5 = [],[],[],[],[],[]
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.market_id,\
                                market.market_code,source.source_id,\
                                source.source_code_description,ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id\
                                join revenue_management.market on ratecode_setup.market_id = market.market_id\
                                join revenue_management.source on ratecode_setup.source_id = source.source_id\
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id\
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = rate_components.components_id\
				join revenue_management.tranction_details on ratecode_setup.transaction_details_id = tranction_details.tranction_detail_id "))
    #print(records[0]['rooms_id'])
    if len(records) != 0:

      rec1 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             "))

    #records.append("room_types":rec1)
    #print(records[0]['packages_id'])
      rec2 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id "))
    #records.append("packages":rec2)

    rec3 = json.loads(dbget("SELECT rate_details_id, one_adult_amount, two_adult_amount, three_adult_amount,\
                             four_adult_amount, extra_adult_amount, one_child_amount, two_child_amount,\
                             extra_child_amount, start_date, end_date, season_code.*,rate_days.*,rate_details.ratecode_id,\
                             rate_details.rooms_id,rate_details.packages_id, \
                             rate_tier.* FROM revenue_management.rate_details \
                             join revenue_management.season_code on rate_details.season_code_id = \
                             season_code.season_code_id join revenue_management.rate_days on \
                             rate_details.rate_days_id = rate_days.rate_days_id left join revenue_management.rate_tier \
                             on rate_details.rate_tier_id = rate_tier.rate_tier_id "))
    if len(rec3) != 0:

      rec4 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             "))
    #rec3.append("room_types":rec4)
    #print(records[0]['packages_id'])
      rec5 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id "))
    #rec3.append("packages":rec5)
    return(json.dumps({"Rate_header":records,"Rate_header_room_types":rec1,"Rate_header_packages":rec2,
                       "Rate_details":rec3,"Rate_details_room_types":rec4,"Rate_details_packages":rec5,
                       "Return": "RRS","Status": "Success","StatusCode": "200"},indent=4))
