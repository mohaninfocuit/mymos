from Fetch_Current_Datetime import *
from sqlwrapper import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from apscheduler.schedulers.blocking import BlockingScheduler
#sched = BlockingScheduler()
def sendemailadmin(get_employee,msges):
                 #email = ['infocuit.daisy@gmail.com','infocuit.aravindh@gmail.com']
                 name = "daisy"
                 print("message",msges)
                 message = "hotels"
                 conf_no = "343243245"
                 hotel_name = "SMARTMO"
                 arrival = "mar 3"
                 depature = "mar 4"
                 room_type ="delux"
                 id1 = "324"
                 book_date = "2019-02-13"
                 #print("daisy","infocuit.aravindh@gmail.com",type(email),"eruma suhutup","98789098","mar 2","mar 3", "delux")
                 sender = "infocuit.testing@gmail.com"
                 ids = id1
                 for i in get_employee:

                      receiver = i['email_id']
                      #print(sender,type(sender),receiver,type(receiver))
                      subject = "Hotel Booking"
                      msg = MIMEMultipart()
                      msg['from'] = sender
                      msg['to'] = receiver
                      msg['subject'] = msges
                      print(ids)
                      html = """\
                      <!DOCTYPE html>
                      <html>
                      <head>
                      <meta charset="utf-8">
                      </head>
                      <body>
                      <dl>
                      <dt>
                      <pre>
               
                      
                      <font size="4" color="black">Dear """+name+""",</font>
                      <font size="4" color="black">      We are delighted that you have selected our """""" On behalf of the entire team at the 
                  ,extend you a very welcome and trust stay with us will be both enjoyable and comfortable
                    offers a selection of business services and facilities.which are detailed in the booklet,
                   placed on the writing table in your room.Should you require any assistance or have any specific
                   requirements,please do not hesitate to contact me extension(999).</font>
                       </pre>
                 <pre>
                      <font size="4" color="blue">Confirmation Number: """+conf_no+"""</font>
                      <font size="4" color="blue">Arrival Date: """+arrival+"""</font>
                      <font size="4" color="blue">Depature Date: """+depature+"""</font>
                      <font size="4" color="blue">Room Type: """+room_type+"""</font>
                     

                      <font size="4" color="black">With best regards / Yours sincerely,</font>
                      <font size="4" color="black">Hotel Manager</font></pre>
                        
                      </dl>        
                      </body>
                      </html>
                      """

                      msg.attach(MIMEText(html,'html'))
                      
                      gmailuser = 'infocuit.testing@gmail.com'
                      password = 'infocuit@123'
                      server = smtplib.SMTP('smtp.gmail.com',587)
                      server.starttls()
                      server.login(gmailuser,password)
                      text = msg.as_string()
                      server.sendmail(sender,receiver,text)
                      print ("the message has been sent successfully")
                      server.quit()

#@sched.scheduled_job('interval', seconds=30)
def Foodandbeverage_Reminder(request):
   print("foodandbeverage")
   string,string1,esca_string,esca_string1 = '','','',''
   today_date = application_datetime().strftime('%Y-%m-%d')
   today_datetime = datetime.datetime.strptime(application_datetime().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
   #print("today_datetime", today_datetime, type(today_datetime))
   query_reminder_count = json.loads(dbget("select * from fb_requests r where date(request_time)='"+str(today_date)+"' and r.ticketstatus_id=1"))
   #print(query_reminder_count)
   if len(query_reminder_count) != 0:        
    for query_reminder in query_reminder_count:
           initial = datetime.datetime.strptime(query_reminder['request_time'], "%Y-%m-%d %H:%M:%S")
           #print('initial',initial, type(initial))
           current  = today_datetime - initial
           #print(current)
           minutes = int(current.seconds % 3600 / 60.0)
           #print("minutes",minutes)
           if 10 <= minutes < 20 :
               
                if query_reminder['reminder_count'] ==0:
                   if len(string) == 0:
                       string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   print("ticket_no",string)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 1"
                   var = sendemailadmin(get_employee,message)
           elif 20 <= minutes < 30 :
               if query_reminder['reminder_count'] ==1:
                   if len(string1) == 0:
                       string1  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   print("ticket_no",string1)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 2"
                   var = sendemailadmin(get_employee,message)
           elif 30 <= minutes < 40 :
               if query_reminder['escalation_count'] == 0:
                   if len(esca_string) == 0:
                       esca_string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       esca_string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message= "escalation 1"
                   var = sendemailadmin(get_employee,message)
                           
                
           elif 40 >= minutes  :
              if query_reminder['escalation_count'] == 1:
                if len(esca_string1) == 0:
                       esca_string1  = "'"+str(query_reminder['ticket_no'])+"'"
                else:
                       esca_string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                get_employee = json.loads(dbget("select * from hotel_details"))
                message = "escalation 2"
                var = sendemailadmin(get_employee,message)
                 
           else:
               pass
    if len(string) == 0:
             pass
    else:
             dbput("update fb_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string)+")")
             string = ''
    if len(string1) ==0:
        pass
    else:
        dbput("update fb_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string1)+")")
        string1 = ''
    if len(esca_string) == 0:
        pass
    else:
        
      dbput("update fb_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string)+")")
      esca_string = ''
    if len(esca_string1) == 0:
        pass
    else:
        
      dbput("update fb_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string1)+")")
      esca_string1  = ''
              
         #print(current.strftime('%M'), type(current.strftime('%M')))
   else:
           pass
   return json.dumps({"Return":"Success"})
  #House keeping
#@sched.scheduled_job('interval', seconds=30)        
def Housekeeping_Reminder(request):
   print("housekeeping")
   string,string1,esca_string,esca_string1 = '','','',''
   today_date = application_datetime().strftime('%Y-%m-%d')
   today_datetime = datetime.datetime.strptime(application_datetime().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
  # print("today_datetime", today_datetime, type(today_datetime))
   query_reminder_count = json.loads(dbget("select * from hk_requests r where date(request_time)='"+str(today_date)+"' and r.ticketstatus_id=1"))
   #print(query_reminder_count)
   if len(query_reminder_count) != 0:        
    for query_reminder in query_reminder_count:
           initial = datetime.datetime.strptime(query_reminder['request_time'], "%Y-%m-%d %H:%M:%S")
           #print('initial',initial, type(initial))
           current  = today_datetime - initial
          # print(current)
           minutes = int(current.seconds % 3600 / 60.0)
           #print("minutes",minutes)
           if 10 <= minutes < 20 :
               
                if query_reminder['reminder_count'] ==0:
                   if len(string) == 0:
                       string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   #print("ticket_no",string)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 1"
                   var = sendemailadmin(get_employee,message)
           elif 20 <= minutes < 30 :
               if query_reminder['reminder_count'] ==1:
                   if len(string1) == 0:
                       string1  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   #print("ticket_no",string1)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 2"
                   var = sendemailadmin(get_employee,message)
           elif 30 <= minutes < 40 :
               if query_reminder['escalation_count'] == 0:
                   if len(esca_string) == 0:
                       esca_string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       esca_string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message= "escalation 1"
                   var = sendemailadmin(get_employee,message)
                           
                
           elif 40 >= minutes  :
              if query_reminder['escalation_count'] == 1:
                if len(esca_string1) == 0:
                       esca_string1  = "'"+str(query_reminder['ticket_no'])+"'"
                else:
                       esca_string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                get_employee = json.loads(dbget("select * from hotel_details"))
                message = "escalation 2"
                var = sendemailadmin(get_employee,message)
                 
           else:
               pass
    if len(string) == 0:
             pass
    else:
             dbput("update hk_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string)+")")
             string = ''
    if len(string1) ==0:
        pass
    else:
        dbput("update hk_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string1)+")")
        string1 = ''
    if len(esca_string) == 0:
        pass
    else:
        
      dbput("update hk_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string)+")")
      esca_string = ''
    if len(esca_string1) == 0:
        pass
    else:
        
      dbput("update hk_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string1)+")")
      esca_string1  = ''
              
         #print(current.strftime('%M'), type(current.strftime('%M')))
   else:
           pass
   return json.dumps({"Return":"Success"})
    
#Front Desk
#@sched.scheduled_job('interval', seconds=30)
def Frontdesk_Reminder(request):
   print("front desk")
   string,string1,esca_string,esca_string1 = '','','',''
   today_date = application_datetime().strftime('%Y-%m-%d')
   today_datetime = datetime.datetime.strptime(application_datetime().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
   #print("today_datetime", today_datetime, type(today_datetime))
   query_reminder_count = json.loads(dbget("select * from fd_requests r where date(request_time)='"+str(today_date)+"' and r.ticketstatus_id=1"))
   #print(query_reminder_count)
   if len(query_reminder_count) != 0:        
    for query_reminder in query_reminder_count:
           initial = datetime.datetime.strptime(query_reminder['request_time'], "%Y-%m-%d %H:%M:%S")
           #print('initial',initial, type(initial))
           current  = today_datetime - initial
           print(current)
           minutes = int(current.seconds % 3600 / 60.0)
           #print("minutes",minutes)
           if 10 <= minutes < 20 :
               
                if query_reminder['reminder_count'] ==0:
                   if len(string) == 0:
                       string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                  # print("ticket_no",string)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 1"
                   var = sendemailadmin(get_employee,message)
           elif 20 <= minutes < 30 :
               if query_reminder['reminder_count'] ==1:
                   if len(string1) == 0:
                       string1  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   #print("ticket_no",string1)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 2"
                   var = sendemailadmin(get_employee,message)
           elif 30 <= minutes < 40 :
               if query_reminder['escalation_count'] == 0:
                   if len(esca_string) == 0:
                       esca_string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       esca_string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message= "escalation 1"
                   var = sendemailadmin(get_employee,message)
                           
                
           elif 40 >= minutes  :
              if query_reminder['escalation_count'] == 1:
                if len(esca_string1) == 0:
                       esca_string1  = "'"+str(query_reminder['ticket_no'])+"'"
                else:
                       esca_string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                get_employee = json.loads(dbget("select * from hotel_details"))
                message = "escalation 2"
                var = sendemailadmin(get_employee,message)
                 
           else:
               pass
    if len(string) == 0:
             pass
    else:
             dbput("update fd_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string)+")")
             string = ''
    if len(string1) ==0:
        pass
    else:
        dbput("update fd_requests set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string1)+")")
        string1 = ''
    if len(esca_string) == 0:
        pass
    else:
        
      dbput("update fd_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string)+")")
      esca_string = ''
    if len(esca_string1) == 0:
        pass
    else:
        
      dbput("update fd_requests set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string1)+")")
      esca_string1  = ''
              
         #print(current.strftime('%M'), type(current.strftime('%M')))
   else:
           pass
       
   return json.dumps({"Return":"Success"})
#sched.start()

def Laundry_Reminder(request):
   print("Laundry")
   string,string1,esca_string,esca_string1 = '','','',''
   today_date = application_datetime().strftime('%Y-%m-%d')
   today_datetime = datetime.datetime.strptime(application_datetime().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
   #print("today_datetime", today_datetime, type(today_datetime))
   query_reminder_count = json.loads(dbget("select * from ldry_request r where date(request_time)='"+str(today_date)+"' and r.ticketstatus_id=1"))
   #print(query_reminder_count)
   if len(query_reminder_count) != 0:        
    for query_reminder in query_reminder_count:
           initial = datetime.datetime.strptime(query_reminder['request_time'], "%Y-%m-%d %H:%M:%S")
           #print('initial',initial, type(initial))
           current  = today_datetime - initial
           print(current)
           minutes = int(current.seconds % 3600 / 60.0)
           #print("minutes",minutes)
           if 10 <= minutes < 20 :
               
                if query_reminder['reminder_count'] ==0:
                   if len(string) == 0:
                       string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                  # print("ticket_no",string)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 1"
                   var = sendemailadmin(get_employee,message)
           elif 20 <= minutes < 30 :
               if query_reminder['reminder_count'] ==1:
                   if len(string1) == 0:
                       string1  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   #print("ticket_no",string1)
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message = "reminder 2"
                   var = sendemailadmin(get_employee,message)
           elif 30 <= minutes < 40 :
               if query_reminder['escalation_count'] == 0:
                   if len(esca_string) == 0:
                       esca_string  = "'"+str(query_reminder['ticket_no'])+"'"
                   else:
                       esca_string += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                   get_employee = json.loads(dbget("select * from hotel_details"))
                     
                   message= "escalation 1"
                   var = sendemailadmin(get_employee,message)
                           
                
           elif 40 >= minutes  :
              if query_reminder['escalation_count'] == 1:
                if len(esca_string1) == 0:
                       esca_string1  = "'"+str(query_reminder['ticket_no'])+"'"
                else:
                       esca_string1 += ',' +"'"+str(query_reminder['ticket_no'])+"'"
                get_employee = json.loads(dbget("select * from hotel_details"))
                message = "escalation 2"
                var = sendemailadmin(get_employee,message)
                 
           else:
               pass
    if len(string) == 0:
             pass
    else:
             dbput("update ldry_request set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string)+")")
             string = ''
    if len(string1) ==0:
        pass
    else:
        dbput("update ldry_request set reminder_count = reminder_count+'1'  where ticket_no in ("+str(string1)+")")
        string1 = ''
    if len(esca_string) == 0:
        pass
    else:
        
      dbput("update ldry_request set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string)+")")
      esca_string = ''
    if len(esca_string1) == 0:
        pass
    else:
        
      dbput("update ldry_request set escalation_count = escalation_count+'1'  where ticket_no in( "+str(esca_string1)+")")
      esca_string1  = ''
              
         #print(current.strftime('%M'), type(current.strftime('%M')))
   else:
           pass
       
   return json.dumps({"Return":"Success"})
#sched.start()

