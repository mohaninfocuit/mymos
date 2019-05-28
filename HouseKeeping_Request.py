from sqlwrapper import *
import re
from Fetch_Current_Datetime import *

def Raise_HK_Request(request):

   d=request.json
   
   current_datetime=application_datetime()
   ticket_no = str(current_datetime.strftime("%Y-%m-%d%H:%M:%S"))+str(d['room_no'])+'hou1024'+str(d['hkitem_id'])

   d.update({'reminder_count':0,'escalation_count':0,
             'ticketstatus_id':1,'request_time':str(current_datetime.strftime("%Y-%m-%d %H:%M:%S")),
             'ticket_no':re.sub("-|:","",ticket_no)})
   gensql('insert','hk_requests',d)
   
   return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent = 4)


def Close_HK_Request(request):
   d=request.json
   dbput("update hk_requests set ticketstatus_id='2' \
         where ticket_no='"+str(d['ticket_no'])+"'")
   return json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS","Status": "Success",
                      "StatusCode": "200"},indent = 4)  


def Query_Hk_Request(request):

   d=request.json

   records = json.loads(dbget("select hk_requests.ticket_no,ticket_status.*,hk_requests.room_no,\
                               hk_requests.reminder_count,hk_requests.escalation_count,hk_requests.request_time,\
                               hk_requests.business_id,housekeeping_items.hkitem_id,housekeeping_items.hkitem_name,\
                               housekeeping_items.hkitem_image,housekeeping_items.dept_id, \
	                       housekeeping_category.hkcateg_id, housekeeping_category.hkcateg_name,\
	                       housekeeping_category.hkcateg_image from hk_requests\
	                       join ticket_status on hk_requests.ticketstatus_id = ticket_status.ticketstatus_id\
	                       join housekeeping_items on hk_requests.hkitem_id = housekeeping_items.hkitem_id\
	                       join housekeeping_category on housekeeping_items.hkitemcateg_id = \
	                       housekeeping_category.hkcateg_id \
	                       where hk_requests.business_id='"+str(d['business_id'])+"' and \
                               housekeeping_items.business_id='"+str(d['business_id'])+"' \
	                       and housekeeping_category.business_id='"+str(d['business_id'])+"' "))
   
   return json.dumps({"Return": "Record Retrived Successfully","ReturnCode": "RRS",
                      "Returnvalue":records,"Status": "Success","StatusCode": "200"},indent = 4)    
