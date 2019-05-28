from sqlwrapper import *
import random
import collections
def Configure_Laundry_Items(request):
    d = request.json
    #print(d)
    list1 = [] 
    d["dept_id"]="lau1997"
    d['ldryitem_id']=d['ldryitem_name'][:3]+str(random.randint(1000,3000)).lower()
    get_category = json.loads(dbget("select count(*) from laundry_category \
                                     where business_id='"+str(d['business_id'])+"' and ldrycateg_name = '"+str(d['ldrycateg_name'].title())+"'"))
    print(get_category)
    
    if len(d["faqs"]) !=0:
        for item in d['faqs']:
            list1.append(tuple((d['ldryitem_id'],item['faqquestion'].replace("'",'"'),item['faqanswer'].replace("'",'"'),d['business_id'])))
        values = ', '.join(map(str, list1))
        print("dddddddddddddddddddddd",values)
        dbput("INSERT INTO  laundry_faqs (ldryitem_id, faqquestion, faqanswer,business_id)VALUES {}".format(values))
      
    if get_category[0]['count'] == 0:
        s={"ldrycateg_id":(d['ldrycateg_name'][:3]+str(random.randint(1000,3000))).lower(),
           "ldrycateg_name":d['ldrycateg_name'].title(),
           "ldrycateg_image":d['ldrycateg_image'],
           "business_id":d['business_id']}
        s = {k:v for k,v in s.items() if v!= ""}
        catogory = gensql('insert','laundry_category',s)
        #print("if_catogory",catogory)
        
        d.update({"ldrycateg_id":str(s['ldrycateg_id']),"ldryitem_name":d['ldryitem_name'].title()})
        d = {k:v for k,v in d.items() if v!= "" if k not in ('ldrycateg_name','ldrycateg_image','faqs')}
        insert_item = gensql('insert','laundry_items',d)
        #print("if_insert item:",insert_item)
    else:
        print("ssssssssssssssssssssssssssssssss")
        d.update({"ldrycateg_id":str(d['ldrycateg_id']),"ldryitem_name":d['ldryitem_name'].title()})
        d = {k:v for k,v in d.items() if v!= "" if k not in ('ldrycateg_name','ldrycateg_image','faqs')}
        insert_item = gensql('insert','laundry_items',d)
        #print("else_insert item:",insert_item)
    
    #return json.dumps({"Retun":d},indent=4)

    return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)


def Select_Laundry_Items(request):
    d = request.json
    finals,list1=[],[]
    lau_items = json.loads(dbget("select laundry_category.ldrycateg_name,laundry_category.ldrycateg_image,laundry_items.* \
                                from laundry_items\
                                join laundry_category on laundry_category.ldrycateg_id = laundry_items.ldrycateg_id\
                                where laundry_items.business_id='"+d['business_id']+"'"))
    lau_question = json.loads(dbget("select * from laundry_faqs where business_id='"+d['business_id']+"'"))
    #category = [items['ldrycateg_name'] for items in lau_items]
    #print(list(set(category)))
    for ldry in lau_items:
        
        ldry['faqs']=[lau_qu for lau_qu in lau_question if ldry['ldryitem_id']==lau_qu['ldryitem_id']]
    grouped = collections.defaultdict(list)
    for item in lau_items:
        grouped[item['ldrycateg_name']].append(item)

    print(grouped)
    for model, group in grouped.items():
    #print
    #print model
    #pprint(group, width=150)
       finals.append({"ldrycateg_name":model,"laundry_items":group})
    
    return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS","ReturnValue":finals,"Status": "Success","StatusCode": "200"},indent = 4)


def Update_Laundry_Items(request):
    d = request.json
    d.update({'ldrycateg_name':d['ldrycateg_name'].title(),"ldryitem_name":d['ldryitem_name'].title()})
    print(d) 

    b={k : v for k,v in d.items() if k in ('ldrycateg_name','ldrycateg_image')}
    c={ k : v for k,v in d.items() if k in('ldrycateg_id','business_id')}
    sql=gensql('update','laundry_category',b,c)
    
    b={k : v for k,v in d.items() if k in ('ldryitem_name','ldrycateg_id','ldryitem_description','price')}
    c={ k : v for k,v in d.items() if k in('ldryitem_id','business_id')}
    sql=gensql('update','laundry_items',b,c)
    return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success","StatusCode": "200"},indent = 4)       
