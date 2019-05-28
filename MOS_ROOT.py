from flask import Flask,request
from flask_cors import CORS


app = Flask(__name__) #here i set environment varible for flask framework web application
CORS(app)
#-----------------------Configuration-------------------
from Signup_Details import *
from Frontdesk_Request import *
from Raise_Front_Desk_Request import *
from GuestDetails import *
from HouseKeeping_Request import *
from room_configuration import *
from hotel_contact import *
from housekeeping_configuration import *
from reportservicenew import*

from configure_hotelrooms import *
from configure_hotelDepartment import *
from configure_foodandbeverage import *
from configure_laundry import *
from Configure_Hotelfaq import *
from Raise_Foodandbeverage_Request import *
from Reminder_Escalation import *
from Raise_Laundry_Request import *
from Query_all_department_categories import*
#below i set path for web application

@app.route("/",methods=['GET','POST'])
def mos_index():
    return "Hello mos Manager"

#@TOS.route("/<string:name>",methods=['GET','POST'])
#def pass_param(name):
   # return (name)
#-----------hotel signup details--------------

@app.route("/Hotel_Signup_Details",methods=['POST'])
def sigupdetail():
    return Hotel_Signup_Details(request)


@app.route("/Query_Hotel_Signup_Details",methods=['GET'])
def querysigupdetail():
    return Query_Hotel_Signup_Details(request)
#-----------------------Front Desk Items--------------#

@app.route("/Configure_Front_Desk_Items",methods=['POST'])
def frontdeskservice():
    return Configure_Front_Desk_Items(request)

@app.route("/Update_Front_Desk_Items",methods=['POST'])
def updatefrontdeskitems():
    return Update_Front_Desk_Items(request)

@app.route("/Select_Front_Desk_Items",methods=['POST'])
def selectfrontdeskitems():
    return Select_Front_Desk_Items(request)

#----------------configuration----------#

@app.route("/Update_Roomtype",methods=['POST'])
def updateroomtype():
    return Update_Roomtype(request)

@app.route("/Insert_Roomtype",methods=['POST'])
def insertroomtype():
    return Insert_Roomtype(request)

@app.route("/Select_Room_Type",methods=['POST'])
def selectroomtype():
   return Select_Room_Type(request)

@app.route("/Insert_Contact_Number",methods=['POST'])
def insertcontactnumber():
    return Insert_Contact_Number(request)

@app.route("/Select_Contact_Number",methods=['POST'])
def selectcontactnumber():
    return Select_Contact_Number(request)

@app.route("/Delete_Contact_Number",methods=['POST'])
def deletecontactnumber():
    return Delete_Contact_Number(request)
#-----------------House Keeping Items-----------------#
@app.route("/Insert_Housekeeping_Item",methods=['POST'])
def housekeepingitem():
   return Insert_Housekeeping_Item(request)

@app.route("/Select_Housekeeping_Item",methods=['POST'])
def selecthousekeepingitem():
   return Select_Housekeeping_Item(request)

@app.route("/Update_Housekeeping_Item",methods=['POST'])
def updatehousekeepingitem():
   return Update_Housekeeping_Item(request)
#configure hotel rooms*******************************

@app.route("/Insert_Hotel_room",methods=['POST'])
def inserthotelroom():
    return Insert_Hotel_room(request)

@app.route("/Select_Hotel_Room",methods=['POST'])
def selecthotelroom():
    return Select_Hotel_Room(request)

@app.route("/Update_Room_Login",methods=['POST'])
def updatehotelrooms():
    return Update_Room_Login(request)

#****************department***************

@app.route("/Insert_Hotel_Department",methods=['POST'])
def hotel_department():
    return Insert_Hotel_Department(request)

@app.route("/Update_Department_Login",methods=['POST'])
def update_department():
    return pdate_Department_Login(request)

@app.route("/Update_Hotel_Department",methods=['POST'])
def update_departments():
    return Update_Hotel_Department(request)

@app.route("/Select_Hotel_Department",methods=['POST'])
def select_department():
    return Select_Hotel_Department(request)
#configure food and beverage******************************
@app.route("/Foodandbeverage_Items",methods=['POST'])
def conf_foodandbeverage():
    return Foodandbeverage_Items(request)

@app.route("/Select_Foodandbeverage_Items",methods=['POST'])
def select_foodandbeverage():
    return Select_Foodandbeverage_Items(request)

@app.route("/Update_Foodandbeverage_Items",methods=['POST'])
def update_foodandbeverage():
    return Update_Foodandbeverage_Items(request)

@app.route("/Configure_Laundry_Items",methods=['POST'])
def conf_laundry():
    return Configure_Laundry_Items(request)

@app.route("/Select_Laundry_Items",methods=['POST'])
def select_laundry():
    return Select_Laundry_Items(request)

@app.route("/Update_Laundry_Items",methods=['POST'])
def update_laundry():
    return Update_Laundry_Items(request)

#----------------------------------------------Raise Request

@app.route("/Raise_Front_Desk_Request",methods=['POST'])
def raisefrontoffice():
    return Raise_Front_Desk_Request(request)
@app.route("/Close_Front_Desk_Request",methods=['POST'])
def closefrontoffce():
    return Close_Front_Desk_Request(request)
@app.route("/Query_Front_Desk_Request",methods=['POST'])
def selectfrontoffice():
    return Query_Front_Desk_Request(request)

@app.route("/Raise_Foodandbeverage_Request",methods=['POST'])
def raisefooditem():
    return Raise_Foodandbeverage_Request(request)
@app.route("/Close_Foodandbeverage_Request",methods=['POST'])
def closefooditem():
    return Close_Foodandbeverage_Request(request)
@app.route("/Query_Foodandbeverage_Request",methods=['POST'])
def selectfooditem():
    return Query_Foodandbeverage_Request(request)


#----------GuestDetails-----------------------

@app.route("/Add_Guest_Details",methods=['POST'])
def addguest():
   return Add_Guest_Details(request)
@app.route("/Edit_Guest_Details",methods=['POST'])
def editguest():
   return Edit_Guest_Details(request)
@app.route("/Checkout_Guest",methods=['POST'])
def checkoutguest():
   return Checkout_Guest(request)

@app.route("/Query_Guest_Details",methods=['POST'])
def QueryGuestDetails():
    return Query_Guest_Details(request)

#----------HouseKeeping Reqeust-----------------
@app.route("/Raise_HK_Request",methods=['POST'])
def RaiseHKRequest():
   return Raise_HK_Request(request)

@app.route("/Close_HK_Request",methods=['POST'])
def CloseHKRequest():
   return Close_HK_Request(request)

@app.route("/Query_Hk_Request",methods=['POST'])
def QueryHkRequest():
   return Query_Hk_Request(request)

#--------------------laundry request------------------
@app.route("/Raise_Laundry_Request",methods=['POST'])
def raiselaundryrequest():
   return Raise_Laundry_Request(request)

@app.route("/Close_Laundry_Request",methods=['POST'])
def closelaundryrequest():
   return Close_Laundry_Request(request)

@app.route("/Query_Laundry_Request",methods=['POST'])
def querylaundryrequest():
   return Query_laundry_Request(request)
#-------------------reminder------------#
@app.route("/Foodandbeverage_Reminder",methods=['GET'])
def fooandbev():
   return Foodandbeverage_Reminder(request)

@app.route("/Housekeeping_Reminder",methods=['GET'])
def houkee():
   return Housekeeping_Reminder(request)

@app.route("/Frontdesk_Reminder",methods=['GET'])
def frontdk():
   return Frontdesk_Reminder(request)

@app.route("/Laundry_Reminder",methods=['GET'])
def landry():
   return Laundry_Reminder(request)

#------------------------FAQ------------------------#
@app.route("/Insert_Hotel_Faq",methods=['POST'])
def insert_faq():
   return Insert_Hotel_Faq(request)

@app.route("/Select_Hotel_Faq",methods=['POST'])
def select_faq():
   return Select_Hotel_Faq(request)

@app.route("/Delete_Hotel_Faq",methods=['POST'])
def delete_faq():
   return Delete_Hotel_Faq(request)

#------------Query category---------#

@app.route("/Select_Frontdesk_Category",methods=['POST'])
def select_Frontcate():
   return Select_Frontdesk_Category(request)

@app.route("/Select_Laundry_Category",methods=['POST'])
def select_laundrycate():
   return Select_Laundry_Category(request)

@app.route("/Select_Food_Category",methods=['POST'])
def select_Foodcate():
   return Select_Food_Category(request)

@app.route("/Select_Housekeeping_Category",methods=['POST'])
def select_Hkcate():
   return Select_Housekeeping_Category(request)
#---------------------report------------------------#
@app.route("/Room_report_request",methods=['POST'])
def Room_Report_request():
   return room_no_report(request)

@app.errorhandler(404)
def unhandled_exception(e):
   return(json.dumps({"Return":"page Not Found","Returncode":"404"}))
@app.errorhandler(405)
def unhandled_exception(e):
 return(json.dumps({"Return":"Method Not Allowed","Returncode":"405"}))
	
if __name__ == "__main__":
    #TOS.run(debug=True)
    app.run(host ='192.168.1.21',port =5000)#run web application
