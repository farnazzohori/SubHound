import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["Sh4z0"]
mycol = mydb["Domian"]

def Get_Scope():
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sh4z0"]
    mycol = mydb["Scope"]
    mydoc = mycol.find([])
    domain_arrey=[]
    for i in mydoc:
        domain_arrey.append(i["Domian"])
    return domain_arrey


def subfinder_func(_domain):
        subs = os.popen("subfinder -d {}  -silent".format(_domain)).read().split("\n") #> result.txt
        for sub in subs:
            new_line = sub.strip()
            if new_line != "":
                inserter(new_line)
        return subs

def finding(domian):
    myquery = { "domian": {"$regex": domian } }
    mydoc = mycol.find(myquery)
    i = 0
    for x in mydoc:
        i += 1
    if not(i==0):
        return 1
    else:
        return 0      
    
def inserter(add_domian):
    subs = subfinder_func(add_domian)
    for i in range(0, len(subs)):  
        new_lines = str(subs[i]).replace("\n", "").strip()
        if new_lines == "":
            continue
        if not(finding(new_lines) == 0):
            pass
        else:
            print(new_lines)
            mydict = { "domian": new_lines ,"timestamp":str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) }   
            x = mycol.insert_one(mydict)
                
                

Scope_Domain = Get_Scope()
for i in Scope_Domain:
    inserter(str(i))