from sqlwrapper import *
import random
def Insert_Hotel_Department(request):
    d=  request.json
    check_item = json.loads(dbget("select count(*) from hotel_department \
                                     where business_id='"+str(d['business_id'])+"' and dept_name= '"+str(d['dept_name'].title())+"'"))
    if check_item[0]['count'] == 0:
        d.update({'dept_id': (str(d['dept_name'][:3]) +str(random.randint(1000,3000))).lower(),'dept_name':d['dept_name'].title()})
        gensql('insert','hotel_department',d)
        return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        return json.dumps({"Return": "Record Already Inserted","ReturnCode": "RAI","Status": "Success","StatusCode": "200"},indent = 4)

def pdate_Department_Login(request):
    d = request.json
    details = json.loads(dbget("select * from hotel_details where business_id = '"+str(d['business_id'])+"'"))
    if d['loginstatus_id'] == 1:
        b={k : v for k,v in d.items() if k in ('loginstatus_id')}
        c={ k : v for k,v in d.items() if k in('dept_id','business_id')}
        sql=gensql('update','hotel_department',b,c)
        return json.dumps({"Return": "Login Successfully","ReturnValue":details,"ReturnCode": "LS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        b={k : v for k,v in d.items() if k in ('loginstatus_id')}
        c={ k : v for k,v in d.items() if k in('dept_id','business_id')}
        sql=gensql('update','hotel_department',b,c)
        return json.dumps({"Return": "LogOut Successfully","ReturnCode": "LOS","Status": "Success","StatusCode": "200"},indent = 4)

def Update_Hotel_Department(request):
    d = request.json

    b={k : v for k,v in d.items() if k in ('dept_image','dept_password')}
    c={ k : v for k,v in d.items() if k in('dept_id','business_id')}
    sql=gensql('update','hotel_department',b,c)
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent = 4)
    

def Select_Hotel_Department(request):
    d = request.json
    rooms = json.loads(dbget("select h.dept_id,h.dept_name,h.dept_image,h.dept_password,h.loginstatus_id,h.business_id,l.loginstatus\
    from hotel_department h join login_status l on h.loginstatus_id = l.loginstatus_id\
    where h.business_id = '"+str(d['business_id'])+"'"))
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS","Returnvalue":rooms,"Status": "Success","StatusCode": "200"},indent = 4)

