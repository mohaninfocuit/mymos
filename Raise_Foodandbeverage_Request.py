from sqlwrapper import *
import re
from Fetch_Current_Datetime import *
def Raise_Foodandbeverage_Request(request):
    d=request.json
    list1 = []
    order_no = json.loads(dbget("SELECT array_to_string(ARRAY(SELECT chr((48 + round(random() * 9)) :: integer) \
                                FROM generate_series(1,10)), '');"))
    print(order_no)
    for item in d['food_items']:
        list1.append(tuple((order_no[0]['array_to_string'],item['fbitem_id'],item['quantity'])))
    values = ', '.join(map(str, list1))
    dbput("INSERT INTO  fb_collection (fbcollection_id, fbitem_id, quantity)VALUES {}".format(values))
                
    current_datetime=application_datetime()
    ticket_no = str(current_datetime.strftime("%Y-%m-%d%H:%M:%S"))+str(d['room_no'])+'foo2106'+str(order_no[0]['array_to_string'])
    
    d.update({'reminder_count':0,'escalation_count':0,
              'ticketstatus_id':1,'request_time':str(current_datetime.strftime("%Y-%m-%d %H:%M:%S")),
              'ticket_no':re.sub("-|:","",ticket_no),'fbcollection_id':order_no[0]['array_to_string'],'fbitem_count':d['fbitem_count'],'total_amount':d['total_amount']})
    print(d)
    d={k:v for k,v in d.items() if k not in ('food_items')}
    gensql('insert','fb_requests',d)
    return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)

    
    
def Close_Foodandbeverage_Request(request):
    
    
    d=request.json
    dbput("update fb_requests set ticketstatus_id='2' where ticket_no='"+str(d['ticket_no'])+"'")
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent = 4)

def Query_Foodandbeverage_Request(request):
    
    d=request.json
    list1,finals = [],[]
    details = json.loads(dbget("select f.item_name,fc.quantity,f.item_description,f.price,f.item_image,\
               f.item_createdon,f.dept_id,c.*,t.*,s.*,r.* from fb_requests r\
    join fb_collection fc on fc.fbcollection_id = r.fbcollection_id\
    join foodandbeverage_items f  on fc.fbitem_id = f.fbitem_id\
    join food_category c on f.foodcategory_id = c.foodcateg_id\
    join foodtype t on f.foodtype_id = t.foodtype_id\
    join todayspecial s on f.todayspecial_id = s.todayspecial_id\
    where r.business_id='"+str(d['business_id'])+"' "))
    
    for detail in details:
        if detail['ticket_no'] not in list1:
            #print(list1)
            list1.append(detail['ticket_no'])
            finals.append({"ticket_no":detail['ticket_no'],"food_items":[]})
    for final in finals:
        for detail in details:
            if detail['ticket_no'] == final['ticket_no']:
                final['food_items'].append(detail)
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS","Returnvalue":finals,"Status": "Success","StatusCode": "200"},indent = 4)



