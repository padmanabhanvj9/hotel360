from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_SELECT_UpdateRatecodeSetup(request):
    d = request.json
    print(d)
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.market_id,\
                                market.market_code,source.source_id,\
                                source.source_code_description,ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id \
                                from revenue_management.ratecode_setup \
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id\
                                join revenue_management.market on ratecode_setup.market_id = market.market_id\
                                join revenue_management.source on ratecode_setup.source_id = source.source_id\
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id\
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = \
                                rate_components.components_id where rateheader_id="+str(d['rateheader_id'])+" "))
    print(records[0]['rooms_id'])
    rec1 = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id, room_type.room_type_id,room_type.room_type \
                             from revenue_management.rooms_selected join revenue_management.room_type on \
                             rooms_selected.room_type_id = room_type.room_type_id \
                             where rooms_id ="+str(records[0]['rooms_id'])+""))
    records.append({"room_types":rec1})
    #print(records[0]['packages_id'])
    rec2 = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             packages_codes.package_code,packages_codes.package_code_id\
                             from revenue_management.packages_selected\
                             join revenue_management.packages_codes on packages_selected.package_code_id =  \
                             packages_codes.package_code_id where packages_id="+str(records[0]['packages_id'])+" "))
    records.append({"packages":rec2})
    return(json.dumps({"Return": records,"Status": "Success","StatusCode": "200"},indent=4))
