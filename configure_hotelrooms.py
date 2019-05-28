from sqlwrapper import *
import random

def Insert_Hotel_room(request):
    check_item = json.loads(dbget("select count(*) from hotel_rooms \
                                     where business_id='"+str(d['business_id'])+"' and room_no= '"+str(d['room_no'].title())+"'"))
    if check_item[0]['count'] == 0:
        d=  request.json
        gensql('insert','hotel_rooms',d)
        return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        return json.dumps({"Return": "Record Already Inserted","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)

def Select_Hotel_Room(request):
    d = request.json
    rooms = json.loads(dbget("select h.room_no,h.roomtype_id,h.price,h.business_id,h.roomstatus_id,h.room_password,h.loginstatus_id,\
    r.roomtype_name,r.roomtype_image,\
    s.roomstatus,l.loginstatus\
    from hotel_rooms h \
    join room_type r on h.roomtype_id = r.roomtype_id \
    join room_status s on h.roomstatus_id = s.roomstatus_id\
    join login_status l on h.loginstatus_id = l.loginstatus_id\
    where h.business_id = '"+str(d['business_id'])+"'"))
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS","ReturnValue":rooms,"Status": "Success","StatusCode": "200"},indent = 4)


def Update_Room_Login(request):
    d = request.json
    b={k : v for k,v in d.items() if k in ('loginstatus_id')}
    c={ k : v for k,v in d.items() if k in('business_id','room_no')}
    sql=gensql('update','hotel_rooms',b,c)
    print("status",sql)
    return json.dumps({"Return": "Room Login Successfully","ReturnCode": "RLS","Status": "Success","StatusCode": "200"},indent = 4)
