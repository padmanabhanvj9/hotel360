import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_BBL_GET_SELECT_BusinessBlockSearch():

    s = json.loads(dbget("select   pf_company_profile.pf_account,block_room.block_room_id,block_room.res_type_id,block_room.cutoff_date,block_room.cutoff_days, \
			  block_room.inventory_control_id,block_room.ratecode_id,block_room.print_rate,block_room.suppress_rate,\
			  block_room.packages,block_room.trace_code,block_room.follow_date,\
			  business_block_definite.*,\
			  block_business_details.business_details_id,block_business_details.res_method_id,block_business_details.payments_id,\
			  block_business_details.rooming_list_duedate,block_business_details.arrivaltime,block_business_details.depaturetime,\
			  block_business_details.commission,block_business_details.total_rooms_perday,\
			  block_catering.attendess_id,block_catering.guranteed,block_catering.item_discount_perc,block_catering.attenders,\
			  block_catering.info_board,block_catering.contract_no,block_catering.onsite_name,block_catering.followup_date,\
			  block_cancel_catering.catering_cancel_id,block_cancel_catering.catering_cancel_no,block_cancel_catering.catering_reason_id,\
			  block_cancel_catering.catering_comments,block_cancel_catering.room_cancel_no,block_cancel_catering.room_cancel_reason,\
			  block_cancel_catering.room_cancel_comments,block_cancel_catering.room_cancel_destination,\
			  block_meeting.block_meeting_id,block_meeting.meeting_space,block_meeting.meeting_space_type_id,\
			  block_meeting.attendess,\
			  reservation.market.marketgroup_description,\
                          reservation.res_source.sourcedescription,\
                          reservation.origin.origindescription,\
			  reservation.restype.restype_description,\
			  business_block.block_status.status,\
			  business_block.block_type.block_type,\
			  business_block.inventory_control.inventory_control,\
			  revenue_management.ratecode.rate_description,\
			  reservation.payment.payment_description,\
			  catering_reason_id, reservation.cancel_reason.reason reason_one, room_cancel_reason,(select reservation.cancel_reason.reason from reservation.cancel_reason where reservation.cancel_reason.id = business_block.block_cancel_catering.room_cancel_reason) as reason_two,\
                          business_block.meeting_space_type.size_type\
                          from business_block.business_block_definite \
			  left join reservation.market on reservation.market.id = business_block_definite.market_id \
			  left join reservation.res_source on reservation.res_source.id = business_block_definite.source_id \
			  left join reservation.origin on reservation.origin.id = business_block_definite.origin_id \
			  left join business_block.block_status on business_block.block_status.id = business_block_definite.block_status_id \
			  left join business_block.block_type on business_block.block_type.id = business_block_definite.block_type \
                          left join business_block.block_room on block_room.block_id = business_block_definite.block_id \
			  left join reservation.restype on restype.id = block_room.res_type_id\
			  left join profile.pf_company_profile on pf_company_profile.pf_id = business_block_definite.pf_id \
			  left join business_block.inventory_control on inventory_control.inventory_control_id = block_room.inventory_control_id \
                          left join revenue_management.ratecode on revenue_management.ratecode.ratecode_id = block_room.ratecode_id \
			  left join business_block.block_business_details on block_business_details.block_id = business_block_definite.block_id \
			  left join reservation.payment on reservation.payment.id = block_business_details.payments_id  \
			  left join business_block.block_catering on business_block.block_catering.block_id = business_block_definite.block_id \
			  left join business_block.block_cancel_catering on business_block.block_cancel_catering.block_id = business_block_definite.block_id \
			  left join reservation.cancel_reason on reservation.cancel_reason.id = business_block.block_cancel_catering.catering_reason_id  \
			  left join business_block.block_meeting on block_meeting.block_id = business_block_definite.block_id \
			  left join business_block.meeting_space_type on meeting_space_type.id = block_meeting.meeting_space_type_id  "))
    print(s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
   

