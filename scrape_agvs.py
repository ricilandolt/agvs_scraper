from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
import numpy as np

agvs_members = pd.DataFrame()
url = "https://www.agvs-upsa.ch/de/verband/mitgliederverzeichnis/liste"
while url != "":
    print(url)
    time.sleep(1)
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    webels = soup.select(".field-content")[:-3]
    textels = [el.text for el in webels]
    text_list = np.array_split(textels, np.ceil(len(textels)/15))
    df = pd.DataFrame(text_list)
    agvs_members = pd.concat([agvs_members,df])
    if soup.select("li.pager__item.pager__item--next"):
        url = "https://www.agvs-upsa.ch" + soup.select("li.pager__item.pager__item--next")[0].find("a")["href"]
    else : 
        url = ""

agvs_members.columns= ["Name_MitgliedNr","Name", "Bezeichnung","Bezeichnung 2","Strasse","PLZ","Ortschaft","Postfach","Telefon","Fax","E-Mail","Webseite", "Sektion", "Kanton","AECzertifiziert"]
agvs_members.to_csv("AGVS_Mitglieder.csv", index = False)