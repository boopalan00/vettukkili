from bs4 import BeautifulSoup as bs

def vuln_place(url,content,pl,DB_check):
    forms =  bs(content, "lxml").find_all("form")
    L = []
    for form in forms:
        A = form.attrs.get("action").lower() 
        M = form.attrs.get("method").lower() 
        D = {}
        if M == "post" or M == "get":
            for _ in form.find_all("input"):
                if _.get("type") == 'submit':
                    D[_.get("name")] = _.get("value") 
                elif 'hidden' == _.get("type"): 
                    D[_.get("name")] = _.get("value") 
                else:
                    D[_.get("name")] = CHECK_DB(url,_.get("name"),pl,DB_check,)
            if form.find_all("select"):
                for s in form.find_all("select"):
                    print(s)

        L.append([reverse_url(url)+A , D])
    return L
        