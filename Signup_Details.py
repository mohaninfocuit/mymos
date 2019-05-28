from sqlwrapper import *
import random
def Hotel_Signup_Details(request):
    
    d=request.json
    d['business_id'] = (str(d['hotel_name'][:3]) + str(d['branch'][:3])+str(random.randint(1000,3000))).lower()
    print(d['business_id'])
    d.update({"hotel_name":d['hotel_name'].title(),"country":d['country'].title(),"htl_state":d['htl_state'].title(),"branch":d['branch'].title()})
    
    gensql('insert','hotel_details',d)
    return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)
def Query_Hotel_Signup_Details(request):
    
  
    details = json.loads(dbget("select * from hotel_details"))
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS","Returnvalue":details,"Status": "Success","StatusCode": "200"},indent = 4)
