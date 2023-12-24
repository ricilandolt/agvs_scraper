from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
import numpy as np
import re 

df = pd.read_csv("AGVS_Mitglieder.csv")

# get team / about sub pages 
for i,website in enumerate(df["Webseite"]):
    if website != "" and not pd.isna(website):
        site = "http://"+website
        try :
            r = requests.get(site)
            soup = bs(r.content, "lxml")
        except:
            continue
        subsite = np.nan
        for a in soup.find_all("a"):
            try :
                 currentsite = a["href"] 
            except: 
                currentsite = np.nan
            if isinstance(currentsite,str):
                if "team" in  currentsite: 
                    print(currentsite)
                    subsite = currentsite
                    break
                elif "ueber" in currentsite :
                    subsite = currentsite
        if not pd.isna(subsite) and not subsite.startswith("http") :
            if subsite.startswith("/"):
                subsite = website+subsite
            else : 
                subsite = website+"/"+subsite
        df.loc[i,"TeamSubsite"] = subsite
df.to_csv("subsites.csv", index = False)

# get email adresses from team / about pages

liste = []
email_liste = []
for website in df[~df["TeamSubsite"].isnull()]["TeamSubsite"]:
    if not website.startswith("http"):
        try :
            r = requests.get("http://"+website)
            soup = bs(r.content,"lxml")
            for link in soup.findAll('a'):
                link_extracted = link.get('href')
                if link_extracted and link_extracted.startswith("mailto:"):
                    email_liste.append(link_extracted.split("mailto:")[1])
        except: 
            pass
    else: 
        try: 
            r = requests.get(website)
            soup = bs(r.content,"lxml")
            for link in soup.findAll('a'):
                link_extracted = link.get('href')
                if link_extracted and link_extracted.startswith("mailto:"):
                    email_liste.append(link_extracted.split("mailto:")[1])
        except:
            pass
email_liste.extend(df["E-Mail"])
extended_email_list = list(set(email_liste))    
extended_email_list = [email for email in extended_email_list if isinstance(email, str) and "@" in email ]
extended_email_list =list(map(lambda x : x.split("?")[0] ,extended_email_list))
shorter_list = [email for email in extended_email_list if not re.findall("amag", email) and not re.findall("emilfrey", email)]
pd.DataFrame(shorter_list,columns =["E-Mail"]).to_csv("email_liste_short.csv",index=False)
pd.DataFrame(extended_email_list,columns =["E-Mail"]).to_csv("email_liste.csv",index=False)


    

   