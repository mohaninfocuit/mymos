from sqlwrapper import *
from Fetch_Current_Datetime import *
import json

def Add_Guest_Details(request):
    d = request.json
    print(d)
    r_count = json.loads(dbget("select count(*) from guest_details where room_no='"+str(d['room_no'])+"'\
                                and checkout is null"))
    if r_count[0]['count'] == 0:
       d.update({'checkin':str(application_datetime())})
       gensql('insert','guest_details',d)
       dbput("update hotel_rooms set roomstatus_id='1' where room_no='"+str(d['room_no'])+"' \
              and business_id='"+str(d['business_id'])+"' ")
       
       return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                          "Status": "Success","StatusCode": "200"},indent = 4)    
       
    else:
        return json.dumps({"Return": "Room '"+str(d['room_no'])+"' Occupied","ReturnCode": "RO","Status": "Success",
                           "StatusCode": "200"},indent = 4)
        
    
def Edit_Guest_Details(request):
    d = request.json
    print(d)
    y = {k:v for k,v in d.items() if v != '' if k in ('guest_id','business_id')}
    x = {k:v for k,v in d.items() if v != '' if k not in ('guest_id','business_id')}
    gensql('update','guest_details',x,y)
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                          "Status": "Success","StatusCode": "200"},indent = 4)    
       


def Checkout_Guest(request):
    y = request.json
    print(y)

    dbput("update guest_details  set  checkout='"+str(application_datetime())+"'  where  \
           guest_id='"+str(y['guest_id'])+"' and room_no='"+str(y['room_no'])+"' and \
           business_id='"+str(y['business_id'])+"'; \
           update hotel_rooms set roomstatus_id='2' where room_no='"+str(y['room_no'])+"' \
           and business_id='"+str(y['business_id'])+"';")

    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                          "Status": "Success","StatusCode": "200"},indent = 4)    
           

def Query_Guest_Details(request):
    d = request.json
    print(d)
    gus_details = json.loads(dbget("select * from guest_details where business_id='"+str(d['business_id'])+"'\
                                    order by checkin_date "))
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS",
                       "Returnvalue":gus_details},indent=2)
