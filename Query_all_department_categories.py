from sqlwrapper import *
def Select_Frontdesk_Category(request):
    d=request.json
    d1 = json.loads(gensql('select','fdcategory','*',d))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))

def Select_Laundry_Category(request):
    d=request.json
    d1 = json.loads(gensql('select','laundry_category','*',d))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))

def Select_Food_Category(request):
    d=request.json
    d1 = json.loads(gensql('select','Food_category','*',d))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))


def Select_Housekeeping_Category(request):
    d=request.json
    d1 = json.loads(gensql('select','housekeeping_category','*',d))
    return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))

