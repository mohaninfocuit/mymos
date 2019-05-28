from sqlwrapper import *
import random


def Configure_Front_Desk_Items(request):
    d = request.json
    print(d)
    check_item = json.loads(dbget("select count(*) from frontdesk_items \
                                     where business_id='"+str(d['business_id'])+"' and fditem_names= '"+str(d['fditem_names'].title())+"'"))
    if check_item[0]['count'] == 0:
        '''
        get_category = json.loads(dbget("select count(*) from fdcategory \
                                         where business_id='"+str(d['business_id'])+"' and fdcategory_name = '"+str(d['fdcategory_name'].title())+"'"))
        if d['fdcategory_name'] != '':
            if get_category[0]['count'] == 0:
                s={"fdcategory_id":(d['fdcategory_name'][:3]+str(random.randint(1000,3000))).lower(),
                   "fdcategory_name":d['fdcategory_name'].title(),
                   "fdcategory_image":d['fdcategory_image'],
                   "business_id":d['business_id']}
                s = {k:v for k,v in s.items() if v!= ""}
                gensql('insert','fdcategory',s)

                
                
                d.update({'fditem_id': (d['fditem_names'][:3]+str(random.randint(1000,3000))).lower(),"fdcategory_id":s['fdcategory_id'],"fditem_names":d['fditem_names'].title()})
                d = {k:v for k,v in d.items() if v!= "" if k not in ('fdcategory_name','fdcategory_image')}
                gensql('insert','',d)
        else:
        '''
        d.update({'fditem_id':(d['fditem_names'][:3]+str(random.randint(1000,3000))).lower(),"fditem_names":d['fditem_names'].title()})
        d = {k:v for k,v in d.items() if v!= "" }
        gensql('insert','frontdesk_items',d)
        #return json.dumps({"Retun":d},indent=4)

        return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        return json.dumps({"Return": "Record Already Inserted","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)

def Update_Front_Desk_Items(request):
    d = request.json
    d['fditem_names']=d['fditem_names'].title()
   
    s={k:v for k,v in d.items() if v != "" if k in ('fditem_names','fditem_image','fdcategory_id')}
    
    z={k:v for k,v in d.items() if v != "" if k in ('fditem_id','business_id')}
    
    gensql('update','frontdesk_items',s,z)
    print(s)
    '''

    e={k:v for k,v in d.items() if v != "" if k in ('fdcategory_name','fdcategory_image')}
   
    print(e)
    f={k:v for k,v in d.items() if v != "" if k in ('fdcategory_id','business_id')}
    if not e:
        pass
    else:
        gensql('update','fdcategory',e,f)
    '''
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent = 4)
def Select_Front_Desk_Items(request):
    d = request.json
    output = json.loads(dbget("select fdcategory.fdcategory_id,fdcategory.fdcategory_name,fdcategory.fdcategory_image,frontdesk_items.fditem_id,\
                               frontdesk_items.fditem_names,frontdesk_items.fditem_image,\
                               frontdesk_items.dept_id fdcategory,hotel_department.dept_name,hotel_department.dept_image from frontdesk_items \
                               join  fdcategory on frontdesk_items.fdcategory_id=fdcategory.fdcategory_id \
                               join  hotel_department on frontdesk_items.dept_id=hotel_department.dept_id\
                               where frontdesk_items.business_id='"+str(d['business_id'])+"'"))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":output},indent=4))

