from msilib.schema import MsiAssembly
from turtle import st
from bs4 import BeautifulSoup
import time,csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r=requests.get(START_URL)
#print("hello")
headers=["Proper name","Distance","Mass","Radius"]
star_data = []
final_star_data=[]
final_star_data_new =[]

def scrape():
    
    
    soup = BeautifulSoup(r.content, "html.parser")
    for row in soup.find_all("tr"):
        temp_list = []
        for index,td_tag in enumerate(row.find_all("td")):
            if index==1 :
                #for index,td_tag in enumerate(row):
                # print(index)
                # print(td_tag.text)
                temp_list.append(td_tag.text)
            else :
                temp_list.append(td_tag.text)
        star_data.append(temp_list)

    
    #print(temp_list)
    
        #     else:
        #         try:
        #             temp_list.append(td_tag.contents[0])
        #         except:
        #             temp_list.append("")
        # star_data.append(temp_list)
        # print(star_data)
# with open("scrapper_2.csv", "w") as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(headers)
#     csvwriter.writerows(star_data)

def remove_extra_columns() :
    for row in star_data :
        #print(row)
        del row[:1]
        #print(row)
        del row[1:2]
        #print(row)
        del row[2:3]
        #print(row)
        del row[4:5]
        #print(row)
        final_star_data.append(row)
    #print(final_star_data)

def scrape_more_data() :
    page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
    soup = BeautifulSoup(page.text,"html.parser")
    temp_list=[]
    star_table= soup.find_all("table")
    table_rows = star_table[5].find_all("tr")

    star_name=[]
    radius=[]
    mass=[]
    distance=[]

    for td_tag in table_rows:
        temp_array=[td_tag.text]
        temp_list.append(temp_array)
    
    del temp_list[:1]
    #print(temp_list)

    star_data_sorted=[]

    for row in temp_list:
        star_data_element=[element.replace("\n",",") for element in row]
        star_data_element=star_data_element[0].split(",")
        star_data_sorted.append(star_data_element)
        
    for row in star_data_sorted:
        star_name.append(row[1])
        radius.append(row[9])
        mass.append(row[8])
        distance.append(row[6])
    #print(distance)

    temp_dict={"Star Name":star_name,"Distance":distance,"Mass":mass,"Radius":radius}
    df = pd.DataFrame(temp_dict)
    #print(df)
    df.to_csv("stars_data.csv",index=False)

scrape_more_data()
# remove_extra_columns()

# for index,data in enumerate(final_star_data) :
#     new_star_data_element=final_star_data[index]
#     new_star_data_element=new_star_data_element[:]
#     new_star_data_element=[element.replace("\n","") for element in new_star_data_element]
#     #final_star_data=[]
#     #print(new_star_data_element)
#     final_star_data_new.append(new_star_data_element)

for row in final_star_data:
    row = [element.replace("\n","")for element in row]
    final_star_data_new.append(row)
#print(final_star_data)

# with open("star_data.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(final_star_data_new)
