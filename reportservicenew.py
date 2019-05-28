from sqlwrapper import *
from collections import defaultdict
def room_no_report(request):
    print("success")
    d= request.json
#-----------------------Room based Report-------------------------------------------------#
    hkrequest = json.loads(dbget("select room_no, count(*) from hk_requests \
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and business_id ='"+d['business_id']+"' group by room_no"))
    
    
    fdrequest = json.loads(dbget("select room_no, count(*) from  fd_requests  \
	 where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and business_id ='"+d['business_id']+"' group by room_no"))

   
    fbrequest = json.loads(dbget("select room_no, count(*) from fb_requests \
	  where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and business_id ='"+d['business_id']+"' group by room_no"))

    laundry_request = json.loads(dbget("select room_no,count(*) from ldry_request where date(request_time)\
                                         between '"+d['datefrom']+"' and '"+d['dateto']+"' and business_id= '"+d['business_id']+"' group by room_no"))
    final_request=hkrequest+fdrequest+fbrequest+laundry_request
    c = defaultdict(int)
    for s in final_request:
                        c[s['room_no']] += s['count']
    finals = [{'room_no': k ,'Count': v} for k,v in c.items()]
    print("mohannnnnnnnnnnnnnnnnnnnnnnnnnnnn")
#-------------------------department_report---------------------------#
    fbrequest1 = json.loads(dbget("select hotel_department.dept_name as department ,count(*) from fb_requests \
                                  join fb_collection on fb_collection.fbcollection_id = fb_requests.fbcollection_id\
                                  join foodandbeverage_items on foodandbeverage_items.fbitem_id=fb_collection.fbitem_id\
                                  join food_category on food_category.foodcateg_id = foodandbeverage_items.foodcategory_id \
                                  join hotel_department on hotel_department.dept_id=foodandbeverage_items.dept_id where \
                                  date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and \
                                  fb_requests.business_id ='"+d['business_id']+"' group by hotel_department.dept_name"))

    hk_request1=json.loads(dbget("select housekeeping_category.hkcateg_name as department,count(*) from hk_requests\
      join housekeeping_items on housekeeping_items.hkitem_id = hk_requests.hkitem_id\
      join housekeeping_category on housekeeping_category.hkcateg_id = housekeeping_items.hkitemcateg_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and hk_requests.business_id ='"+d['business_id']+"'\
      group by housekeeping_category.hkcateg_name"))

    fd_request1=json.loads(dbget("select fdcategory.fdcategory_name as department,count(*) from fd_requests\
      join frontdesk_items on frontdesk_items.fditem_id = fd_requests.fditem_id\
      join fdcategory on fdcategory.fdcategory_id = frontdesk_items.fdcategory_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and \
      fd_requests.business_id ='"+d['business_id']+"' group by fdcategory.fdcategory_name"))

    laundry_request1 = json.loads(dbget("select hotel_department.dept_name as department ,count(*) from ldry_request \
                                  join ldry_collection on ldry_collection.ldrycollection_id = ldry_request.ldrycollect_id\
                                  join laundry_items on laundry_items.ldryitem_id=ldry_collection.ldryitem_id\
                                  join laundry_category on laundry_category.ldrycateg_id = laundry_items.ldrycateg_id \
                                  join hotel_department on hotel_department.dept_id=laundry_items.dept_id where \
                                  date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and \
                                  ldry_request.business_id ='"+d['business_id']+"' group by hotel_department.dept_name"))
      
    
    dept_final=hk_request1+fbrequest1+fd_request1+laundry_request1
    
#----------------------------remainder_count_report---------------------------------------#  
    hkrequest2 = json.loads(dbget("select housekeeping_category.hkcateg_name as department,\
    (select count(reminder_count) as reminder_one from hk_requests where reminder_count=1),\
    (select count(reminder_count) as reminder_two from hk_requests where reminder_count=2)\
    from hk_requests\
    join housekeeping_items on housekeeping_items.hkitem_id = hk_requests.hkitem_id\
    join housekeeping_category on housekeeping_category.hkcateg_id = housekeeping_items.hkitemcateg_id\
    where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and\
    hk_requests.business_id ='"+d['business_id']+"'\
    group by housekeeping_category.hkcateg_name"))
    print(hkrequest2,'')

    fb_request2= json.loads(dbget("select hotel_department.dept_name as department,\
    (select count(reminder_count) as reminder_one from fb_requests where reminder_count=1),\
    (select count(reminder_count) as reminder_two from fb_requests where reminder_count=2)\
    from fb_requests\
     join fb_collection on fb_collection.fbcollection_id = fb_requests.fbcollection_id\
    join foodandbeverage_items on foodandbeverage_items.fbitem_id=fb_collection.fbitem_id\
    join hotel_department on hotel_department.dept_id=foodandbeverage_items.dept_id\
     where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and fb_requests.business_id ='"+d['business_id']+"'\
     group by hotel_department.dept_name"))\

    fd_request2=json.loads(dbget("select fdcategory.fdcategory_name as department,\
    (select count(reminder_count) as reminder_one from fd_requests where reminder_count=1),\
    (select count(reminder_count) as reminder_two from fd_requests where reminder_count=2) from fd_requests\
      join frontdesk_items on frontdesk_items.fditem_id = fd_requests.fditem_id\
      join fdcategory on fdcategory.fdcategory_id = frontdesk_items.fdcategory_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' \
      and fd_requests.business_id ='"+d['business_id']+"' group by fdcategory.fdcategory_name"))

    
    
    laundry_request2 = json.loads(dbget("select hotel_department.dept_name as department,\
    (select count(reminder_count) as reminder_one from ldry_request where reminder_count=1),\
    (select count(reminder_count) as reminder_two from ldry_request where reminder_count=2) from ldry_request\
    join ldry_collection on ldry_collection.ldrycollection_id = ldry_request.ldrycollect_id\
    join laundry_items on laundry_items.ldryitem_id=ldry_collection.ldryitem_id\
    join hotel_department on hotel_department.dept_id=laundry_items.dept_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' \
      and ldry_request.business_id ='"+d['business_id']+"' group by  hotel_department.dept_name"))

    remainder_report=hkrequest2+fb_request2+fd_request2+laundry_request2

#-----------------------Escalation_based_report---------------------#
    
    hkrequest3 = json.loads(dbget("select housekeeping_category.hkcateg_name as department,\
    (select count(escalation_count) as escalation_one from hk_requests where escalation_count=1),\
    (select count(escalation_count) as escalation_two from hk_requests where escalation_count=2)\
    from hk_requests\
    join housekeeping_items on housekeeping_items.hkitem_id = hk_requests.hkitem_id\
    join housekeeping_category on housekeeping_category.hkcateg_id = housekeeping_items.hkitemcateg_id\
    where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and\
    hk_requests.business_id ='"+d['business_id']+"'\
    group by housekeeping_category.hkcateg_name"))
    print(hkrequest2,'')

    fb_request3= json.loads(dbget("select hotel_department.dept_name as department,\
    (select count(escalation_count) as escalation_one from fb_requests where escalation_count=1),\
    (select count(escalation_count) as escalation_two from fb_requests where escalation_count=2)\
    from fb_requests\
    join fb_collection on fb_collection.fbcollection_id = fb_requests.fbcollection_id\
    join foodandbeverage_items on foodandbeverage_items.fbitem_id=fb_collection.fbitem_id\
    join hotel_department on hotel_department.dept_id=foodandbeverage_items.dept_id\
     where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' and fb_requests.business_id ='"+d['business_id']+"'\
     group by hotel_department.dept_name"))

    fd_request3=json.loads(dbget("select fdcategory.fdcategory_name as department,\
    (select count(reminder_count) as reminder_one from fd_requests where reminder_count=1),\
    (select count(reminder_count) as reminder_two from fd_requests where reminder_count=2) from fd_requests\
      join frontdesk_items on frontdesk_items.fditem_id = fd_requests.fditem_id\
      join fdcategory on fdcategory.fdcategory_id = frontdesk_items.fdcategory_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' \
      and fd_requests.business_id ='"+d['business_id']+"' group by fdcategory.fdcategory_name"))

    laundry_request3 = json.loads(dbget("select hotel_department.dept_name as department,\
    (select count(escalation_count) as escalation_one from ldry_request where escalation_count=1),\
    (select count(escalation_count) as escalation_two from ldry_request where escalation_count=2) from ldry_request\
    join ldry_collection on ldry_collection.ldrycollection_id = ldry_request.ldrycollect_id\
    join laundry_items on laundry_items.ldryitem_id=ldry_collection.ldryitem_id\
    join hotel_department on hotel_department.dept_id=laundry_items.dept_id\
      where date(request_time) between '"+d['datefrom']+"' and '"+d['dateto']+"' \
      and ldry_request.business_id ='"+d['business_id']+"' group by hotel_department.dept_name"))

    esclation=fd_request3+fb_request3+hkrequest3+laundry_request3
    


    return (json.dumps({"Return": "Record Retrived Successfully",
                        "ReturnCode": "RRS",
                        "Room_based_report":finals,
                        "Department_based_report":dept_final,
                        "Remainder_based_report":remainder_report,
                        "Escalation_based_report":esclation,
                        "Status": "Success","StatusCode": "200"},indent=4))
   
#---------------------------department based request count----------------------#

 #------------------------------device based report-----------------------------#
 
    

