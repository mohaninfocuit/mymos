from sqlwrapper import *
import random


def Insert_Housekeeping_Item(request):
    d = request.json
    check_item = json.loads(dbget("select count(*) from housekeeping_items \
                                     where business_id='"+str(d['business_id'])+"' and hkitem_name= '"+str(d['hkitem_name'].title())+"'"))
    if check_item[0]['count'] == 0:
        d.update({'hkitem_id': (str(d['hkitem_name'][:3]) +str(random.randint(100,300))).lower(),'hkitem_name':d['hkitem_name'].title()})
        gensql('insert','housekeeping_items',d)
        return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        return json.dumps({"Return": "Record Already Inserted ","ReturnCode": "RAI","Status": "Success","StatusCode": "200"},indent = 4)

def Select_Housekeeping_Item(request):
    d= request.json
    output = json.loads(dbget("select housekeeping_items.*, housekeeping_category.hkcateg_name,\
                    housekeeping_category.hkcateg_image\
                    from housekeeping_items join  housekeeping_category on \
                    housekeeping_items.hkitemcateg_id=housekeeping_category.hkcateg_id where housekeeping_items.business_id='"+str(d['business_id'])+"' "))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":output},indent=4))

def Update_Housekeeping_Item(request):
    d= request.json
    b={k : v for k,v in d.items() if k in ('hkitem_image','hkitem_name','hkitemcateg_id')}
    c={ k : v for k,v in d.items() if k in('business_id','hkitem_id')}
    sql=gensql('update','housekeeping_items',b,c)
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent = 4)
    

