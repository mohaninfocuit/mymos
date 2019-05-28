from sqlwrapper import *
def test_Data(request):
    d=  request.json
    gensql('insert','contacts',d)
    return("data_Inserted")
    
