from sqlwrapper import *


def Insert_Hotel_Faq(request):
    d=request.json
    #d['faq_question']= d['faq_question'].strip('""')
    #d['faq_question'] = '"{}"'.format(d['faq_question'])
    #d['faq_answer']= d['faq_answer'].strip('""')
    #d['faq_answer'] = '"{}"'.format(d['faq_answer'])
    print(d)
    gensql('insert','hotel_faq',d)
    return json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS","Status": "Success","StatusCode": "200"},indent = 4)


def Select_Hotel_Faq(request):
    d=request.json
    d1 = json.loads(gensql('select','hotel_faq','*',d))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))

def Delete_Hotel_Faq(request):
    d1=request.json['hotel_faq_id']
    d2=request.json['business_id']
    dbput("delete from hotel_faq where hotel_faq_id ='"+d1+"'and business_id='"+d2+"'")
    return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
