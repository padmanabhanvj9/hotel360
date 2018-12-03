from sqlwrapper import gensql
import datetime
import json
def HOTEL_RES_POST_UPDATE_UpdateFixedChargesReservation(request):

    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if k in ('Res_id')}
    e = { k : v for k,v in d.items() if v != '' if  k not in  ('Res_id','fixed_charges_id')}
    f = { k : v for k,v in d.items() if  k == 'Fixed_Charges_Begin_Date' and v != '' if k == 'Fixed_Charges_End_Date' and v != ''}
    print(f)
    #Fixed_Charges_Begin_Date = d.get('Fixed_Charges_Begin_Date')
    #print(Fixed_Charges_Begin_Date)
    
    #Fixed_Charges_End_Date = d.get('Fixed_Charges_End_Date')
    #print(Fixed_Charges_End_Date)
    #if Fixed_Charges_Begin_Date == '' or Fixed_Charges_End_Date == '':
    #    sql_value = gensql('update','reservation.res_fixed_charges',e,a)
    #    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    print(a,e)
    s = ['RES_Arrival','RES_Depature','PF_Firstname','PF_Mobileno','RES_Nights']
    sql_value = gensql('select','reservation.res_reservation',s,a)
    sql_value = json.loads(sql_value)
    print(sql_value,type(sql_value))
    data = sql_value[0]
    arrival = data['res_arrival']
    depature = data['res_depature']
    print(arrival,depature,type(arrival))
    arr_date = datetime.datetime.strptime(arrival, '%Y-%m-%d').date()
    dep_date = datetime.datetime.strptime(depature, '%Y-%m-%d').date()
    print(arr_date,dep_date,type(arr_date))
    data1 = d.get('Fixed_Charges_Begin_Date')
    data2 = d.get('Fixed_Charges_End_Date')
    charges_begin_date = datetime.datetime.strptime(data1, '%Y-%m-%d').date()
    charges_end_date = datetime.datetime.strptime(data2, '%Y-%m-%d').date()
    print(charges_begin_date,charges_end_date,type(charges_end_date))
    a = { k : v for k,v in d.items() if k in ('Res_id','fixed_charges_id')}
    if charges_begin_date >= arr_date and charges_end_date  <= dep_date and arr_date <= charges_end_date:
       sql_value = gensql('update','reservation.res_fixed_charges',e,a)
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'please enter valid date','ReturnCode':'PEVD'}, sort_keys=True, indent=4))
    #elif charges_begin_date <= arr_date and charges_end_date  >= dep_date :
    #    sql_value = gensql('update','reservation.res_fixed_charges',e,a)
    #    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'please enter valid date','ReturnCode':'PEVD'}, sort_keys=True, indent=4))

    
