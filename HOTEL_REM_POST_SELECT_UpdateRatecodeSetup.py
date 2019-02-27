from sqlwrapper import gensql, dbget, dbput
import datetime
import json
def HOTEL_REM_POST_SELECT_UpdateRatecodeSetup(request):
    
    d = request.json
    print(d)
    
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.*,\
                                res_source.*,\
                                ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id  \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id \
                                join reservation.market on ratecode_setup.market_id = market.id \
                                join reservation.res_source on ratecode_setup.source_id = res_source.id \
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id \
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = rate_components.components_id \
                                join revenue_management.tranction_details on ratecode_setup.transaction_details_id = \
                                tranction_details.tranction_detail_id where ratecode.ratecode_id='"+str(d['ratecode_id'])+"' "))
    
    #print("records   ",records,"len",len(records))
    
    for cords in records:
        
      cords['rooms'] = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                        room_type.id,room_type.type\
                                        from revenue_management.rooms_selected join room_management.room_type on \
                                        rooms_selected.room_type_id = room_type.id where\
                                        rooms_selected.rooms_id='"+str(cords['rooms_id'])+"' "))
      
      #print("records   ",records,"len",len(records)) 
    
    
      cords['packages'] = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             package_code.package_code,package_code.package_code_id\
                             from revenue_management.packages_selected\
                             join packages.package_code on packages_selected.package_code_id =  \
                             package_code.package_code_id  where packages_selected.packages_id='"+str(cords['packages_id'])+"'"))

      rate_details = json.loads(dbget("select * from revenue_management.rate_details \
                                       where ratecode_id='"+str(cords['ratecode_id'])+"'"))

      #print("rate_details  ",rate_details, len(rate_details))
      no = 0
      for rate in rate_details:
          print("rate",rate)
          get_detail_rate = json.loads(dbget("SELECT rates_all.rates_id, rates_all.ratecode_id, \
                                              rates_all.rate_details_id, season_code.*, rates_all.rate_date,\
                                              rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                                              rates_all.four_adult_rate, rates_all.extra_adult_rate,rates_all.one_child_rate,rates_all.two_child_rate,\
                                              rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                                              rate_tier.* from revenue_management.rates_all join \
                                              revenue_management.season_code on \
                                              rates_all.season_code_id = season_code.season_code_id join \
                                              revenue_management.rate_tier on \
                                              rates_all.rate_tier_id = rate_tier.rate_tier_id \
                                              where rates_all.ratecode_id='"+str(rate['ratecode_id'])+"' and \
                                              rates_all.rate_details_id='"+str(rate['rate_details_id'])+"'  "))

          print("-----------------------------------")
          #print("get_detail_rate", get_detail_rate,len(get_detail_rate))
          
          if len(get_detail_rate) != 0:
             detail_rate = get_detail_rate[no]
             #print("detail_rate", detail_rate)
             if  detail_rate['rate_tier_id'] != 0:
                 detail_rate['packages_id'] = 0
          #print("rateof", detail_rate,type(detail_rate))
          
          
              
             x = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                                           room_type.id as roomid,room_type.type as roomstype\
                                                           from revenue_management.rooms_selected  join room_management.room_type on \
                                                           rooms_selected.room_type_id = room_type.id \
                                                          where rooms_selected.rooms_id='"+str(detail_rate['rooms_id'])+"' "))
             rate['rooms'] = x
              
              
             y = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                                package_code.package_code,package_code.package_code_id\
                                from revenue_management.packages_selected\
                                join packages.package_code on packages_selected.package_code_id =  \
                                package_code.package_code_id  where \
                                packages_selected.packages_id='"+str(detail_rate['packages_id'])+"'"))
          
             rate['packages'] = y

             z = json.loads(dbget("select * from revenue_management.rate_days where \
                                   rate_details_id='"+str(rate['rate_details_id'])+"' "))
             

             detail_rate['rooms'] = x
             detail_rate['packages'] = y
             detail_rate['days'] = z
             
             rate['advanced_details'] = detail_rate

          #no=len(get_detail_rate)-1
      cords['rate_details'] = rate_details        

    return(json.dumps({"records":records,"return_code":"RRS","message":"Record Retrived Successfully"},indent=4))


def HOTEL_REM_POST_SELECT_SelectRatesetupAll(request):
    
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.*,\
                                res_source.*,\
                                ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id  \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id \
                                join reservation.market on ratecode_setup.market_id = market.id \
                                join reservation.res_source on ratecode_setup.source_id = res_source.id \
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id \
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = rate_components.components_id \
                                join revenue_management.tranction_details on ratecode_setup.transaction_details_id = \
                                tranction_details.tranction_detail_id "))
    
    #print("records   ",records,"len",len(records))
    
    for cords in records:
        
      cords['rooms'] = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                        room_type.id,room_type.type\
                                        from revenue_management.rooms_selected join room_management.room_type on \
                                        rooms_selected.room_type_id = room_type.id where\
                                        rooms_selected.rooms_id='"+str(cords['rooms_id'])+"' "))
      
      #print("records   ",records,"len",len(records)) 
    
    
      cords['packages'] = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             package_code.package_code,package_code.package_code_id\
                             from revenue_management.packages_selected\
                             join packages.package_code on packages_selected.package_code_id =  \
                             package_code.package_code_id  where packages_selected.packages_id='"+str(cords['packages_id'])+"'"))

      rate_details = json.loads(dbget("select * from revenue_management.rate_details \
                                       where ratecode_id='"+str(cords['ratecode_id'])+"'"))

      #print("rate_details  ",rate_details, len(rate_details))
      no = 0   
      for rate in rate_details:
          #print("rate",rate)
          get_detail_rate = json.loads(dbget("SELECT rates_all.rates_id, rates_all.ratecode_id, \
                                              rates_all.rate_details_id, season_code.*, rates_all.rate_date,\
                                              rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                                              rates_all.four_adult_rate, rates_all.extra_adult_rate, rates_all.one_child_rate,rates_all.two_child_rate,\
                                              rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                                              rate_tier.* from revenue_management.rates_all join \
                                              revenue_management.season_code on \
                                              rates_all.season_code_id = season_code.season_code_id join \
                                              revenue_management.rate_tier on \
                                              rates_all.rate_tier_id = rate_tier.rate_tier_id \
                                              where rates_all.ratecode_id='"+str(rate['ratecode_id'])+"' and \
                                              rates_all.rate_details_id='"+str(rate['rate_details_id'])+"'  "))
          if len(get_detail_rate) != 0:
             detail_rate = get_detail_rate[0] 
             #print("rateof", detail_rate,type(detail_rate))
             if  detail_rate['rate_tier_id'] != 0:
                 detail_rate['packages_id'] = 0
          
              
             x = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                                           room_type.id as roomid,room_type.type as roomstype\
                                                           from revenue_management.rooms_selected  join room_management.room_type on \
                                                           rooms_selected.room_type_id = room_type.id \
                                                          where rooms_selected.rooms_id='"+str(detail_rate['rooms_id'])+"' "))
             rate['rooms'] = x
              
              
             y = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                                package_code.package_code,package_code.package_code_id\
                                from revenue_management.packages_selected\
                                join packages.package_code on packages_selected.package_code_id =  \
                                package_code.package_code_id  where \
                                packages_selected.packages_id='"+str(detail_rate['packages_id'])+"'"))
          
             rate['packages'] = y

             z = json.loads(dbget("select * from revenue_management.rate_days where \
                                   rate_details_id='"+str(rate['rate_details_id'])+"' "))

             detail_rate['rooms'] = x
             detail_rate['packages'] = y
             detail_rate['days'] = z
             rate['advanced_details'] = detail_rate

          #no+=1
      cords['rate_details'] = rate_details        

    return(json.dumps({"records":records,"return_code":"RRS","message":"Record Retrived Successfully"},indent=4))


def HOTEL_REM_POST_SELECT_GetRatecodeSetup(ids):
    
    print("ids in getratecode",ids)
    
    records = json.loads(dbget("select ratecode_setup.rateheader_id, ratecode.ratecode_id,ratecode.rate_code,\
                                ratecode.rate_description,ratecategory.rate_category,ratecategory.rate_category_decription,\
                                ratecategory.ratecategory_id,ratecategory.rate_class,\
                                ratecode_setup.begin_sell_date,ratecode_setup.end_sell_date,market.*,\
                                res_source.*,\
                                ratecode_setup.display_sequence,sell_control.*,rate_components.*,\
                                ratecode_setup.rooms_id,ratecode_setup.packages_id,tranction_details.*\
                                from revenue_management.ratecode_setup\
                                join revenue_management.ratecode on ratecode_setup.ratecode_id = ratecode.ratecode_id  \
                                join revenue_management.ratecategory on ratecode.rate_category_id = ratecategory.ratecategory_id \
                                join reservation.market on ratecode_setup.market_id = market.id \
                                join reservation.res_source on ratecode_setup.source_id = res_source.id \
                                join revenue_management.sell_control on ratecode_setup.sell_control_id = sell_control.sell_id \
                                join revenue_management.rate_components on ratecode_setup.rate_components_id = rate_components.components_id \
                                join revenue_management.tranction_details on ratecode_setup.transaction_details_id = \
                                tranction_details.tranction_detail_id where ratecode.ratecode_id in ("+str(ids)+") "))
    
    print("records","len: ",len(records))
    
    for cords in records:
        
      cords['rooms'] = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                        room_type.id,room_type.type\
                                        from revenue_management.rooms_selected join room_management.room_type on \
                                        rooms_selected.room_type_id = room_type.id where\
                                        rooms_selected.rooms_id='"+str(cords['rooms_id'])+"' "))
      
      #print("records   ",records,"len",len(records)) 
    
    
      cords['packages'] = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                             package_code.package_code,package_code.package_code_id\
                             from revenue_management.packages_selected\
                             join packages.package_code on packages_selected.package_code_id =  \
                             package_code.package_code_id  where packages_selected.packages_id='"+str(cords['packages_id'])+"'"))

      rate_details = json.loads(dbget("select * from revenue_management.rate_details \
                                       where ratecode_id='"+str(cords['ratecode_id'])+"'"))

      #print("rate_details  ",rate_details, len(rate_details))
      no = 0
      for rate in rate_details:
          #print("rate",rate)
          get_detail_rate = json.loads(dbget("SELECT rates_all.rates_id, rates_all.ratecode_id, \
                                              rates_all.rate_details_id, season_code.*, rates_all.rate_date,\
                                              rates_all.one_adult_rate, rates_all.two_adult_rate, rates_all.three_adult_rate,\
                                              rates_all.four_adult_rate, rates_all.extra_adult_rate,rates_all.one_child_rate,rates_all.two_child_rate,\
                                              rates_all.extra_child_rate, rates_all.rooms_id, rates_all.packages_id,\
                                              rate_tier.* from revenue_management.rates_all join \
                                              revenue_management.season_code on \
                                              rates_all.season_code_id = season_code.season_code_id join \
                                              revenue_management.rate_tier on \
                                              rates_all.rate_tier_id = rate_tier.rate_tier_id \
                                              where rates_all.ratecode_id='"+str(rate['ratecode_id'])+"' and \
                                              rates_all.rate_details_id='"+str(rate['rate_details_id'])+"'  "))

          print("-----------------------------------")
          #print("get_detail_rate", get_detail_rate,len(get_detail_rate))
          
          if len(get_detail_rate) != 0:
             detail_rate = get_detail_rate[no]
             if  detail_rate['rate_tier_id'] != 0:
                 detail_rate['packages_id'] = 0
          #print("rateof", detail_rate,type(detail_rate))
          
          
              
             x = json.loads(dbget("select rooms_selected.rooms_selected_id,rooms_selected.rooms_id,\
                                                           room_type.id as roomid,room_type.type as roomstype\
                                                           from revenue_management.rooms_selected  join room_management.room_type on \
                                                           rooms_selected.room_type_id = room_type.id \
                                                          where rooms_selected.rooms_id='"+str(detail_rate['rooms_id'])+"' "))
             rate['rooms'] = x
              
              
             y = json.loads(dbget("select packages_selected.packages_selected_id,packages_selected.packages_id,\
                                package_code.package_code,package_code.package_code_id\
                                from revenue_management.packages_selected\
                                join packages.package_code on packages_selected.package_code_id =  \
                                package_code.package_code_id  where \
                                packages_selected.packages_id='"+str(detail_rate['packages_id'])+"'"))
          
             rate['packages'] = y

             z = json.loads(dbget("select * from revenue_management.rate_days where \
                                   rate_details_id='"+str(rate['rate_details_id'])+"' "))
             

             detail_rate['rooms'] = x
             detail_rate['packages'] = y
             detail_rate['days'] = z
             
             rate['advanced_details'] = detail_rate

          #no+=1
      cords['rate_details'] = rate_details        

    return(json.dumps({"records":records,"return_code":"RRS","message":"Record Retrived Successfully"},indent=4))
