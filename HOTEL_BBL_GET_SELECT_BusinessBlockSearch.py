import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_BBL_GET_SELECT_BusinessBlockSearch(request):

    s = json.loads(dbget("select business_block.*,business_block_definite.*,  block_room.*, \
                 block_business_details.*, block_catering.*,block_cancel_catering.*, \
                 roomtype_one,room_management.room_type.type typeone ,roomtype_two ,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.business_block.roomtype_two) as typetwo,roomtype_three,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.business_block.roomtype_three) as typethree ,\
                reservation.market.marketgroup_description,\
                reservation.res_source.sourcedescription, \
                reservation.origin.origindescription, \
                reservation.restype.restype_description, \
                revenue_management.ratecode.rate_description, \
                reservation.payment.payment_description, \
                catering_reason_id, reservation.cancel_reason.reason reason_one, room_cancel_reason,(select reservation.cancel_reason.reason from reservation.cancel_reason where reservation.cancel_reason.id = business_block.block_cancel_catering.room_cancel_reason) as reason_two \
                from business_block.business_block \
                join business_block.business_block_definite on business_block_definite.block_id = business_block.block_id \
                join business_block.block_room on block_room.block_id = business_block.block_id \
                join business_block.block_business_details on block_business_details.block_id = business_block.block_id \
                left join business_block.block_catering on block_catering.block_id = business_block.block_id \
                left join business_block.block_cancel_catering on block_cancel_catering.block_id = business_block.block_id \
                join room_management.room_type on room_management.room_type.id = business_block.business_block.roomtype_one \
                join reservation.market on reservation.market.id = business_block_definite.market_id \
                join reservation.res_source on reservation.res_source.id = business_block_definite.source_id \
                join reservation.origin on reservation.origin.id = business_block_definite.origin_id \
                join reservation.restype on reservation.restype.id = block_room.res_type_id \
                join revenue_management.ratecode on revenue_management.ratecode.ratecode_id = block_room.ratecode_id \
                join reservation.payment on reservation.payment.id = block_business_details.payments_id\
                left join reservation.cancel_reason on reservation.cancel_reason.id = business_block.block_cancel_catering.catering_reason_id"))
    print(s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
   

