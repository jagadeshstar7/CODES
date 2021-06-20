from bs4 import BeautifulSoup
import requests
import pandas as pd
url="http://www.estesparkweather.net/archive_reports.php?date=200901"
zoo = requests.get(url)
soup = BeautifulSoup(zoo.text,'lxml')
#print(soup.h1.string)
extracted_text=[]
for i in soup.find_all("td"):
    #print(i.get_text())
    extracted_text.append(i.get_text())
df=pd.DataFrame(extracted_text,columns=["Data"])#converting list to dataframe
#dxl=df.to_csv("n.csv")

extracted_text=extracted_text[:1210]
#sam=[]
#for i in extracted_text:#extracting data which starts with Jan
#    if i.startswith("Jan"):
#        i=i.replace("Average and Extremes","")
#        
#    
#        
#        sam.append(i)
#    else:
#        pass


#Average_temperature=[]
#for i in df:
#    if i.startswith("Average temperature"):
#        Average_temperature.append(df[df.index(i)+1])
#    else:
#        pass

#Extracting the columns
    columns=[]
    for i in extracted_text[:38]:
        if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall"):
            columns.append(i)
        else:
            pass
    
#removing jan
d1=[]
for i in extracted_text[:39]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d1.append(i)
 

d2=[]
for i in extracted_text[39:78]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d2.append(i)
   

d3=[]
for i in extracted_text[78:117]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d3.append(i)
      

d4=[]
for i in extracted_text[117:156]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d4.append(i)
 

d5=[]
for i in extracted_text[156:195]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d5.append(i)


d6=[]
for i in extracted_text[195:234]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d6.append(i)
 

d7=[]
for i in extracted_text[234:273]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d7.append(i)


d8=[]
for i in extracted_text[273:312]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d8.append(i)


d9=[]
for i in extracted_text[312:351]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d9.append(i)


d10=[]
for i in extracted_text[351:390]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d10.append(i)

d11=[]
for i in extracted_text[390:429]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d11.append(i)


d12=[]
for i in extracted_text[429:468]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d12.append(i)
 

d13=[]
for i in extracted_text[468:507]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d13.append(i)
 

d14=[]
for i in extracted_text[507:546]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d14.append(i)
 

d15=[]
for i in extracted_text[546:585]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d15.append(i)
 

d16=[]
for i in extracted_text[585:624]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d16.append(i)


d17=[]
for i in extracted_text[624:663]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d17.append(i)



d18=[]
for i in extracted_text[663:702]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d18.append(i)
 


d19=[]
for i in extracted_text[702:741]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d19.append(i)
 

d20=[]
for i in extracted_text[741:780]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d20.append(i)
  

d21=[]
for i in extracted_text[780:819]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d21.append(i)
  

d22=[]
for i in extracted_text[819:858]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d22.append(i)
  

d23=[]
for i in extracted_text[858:897]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d23.append(i)


d24=[]
for i in extracted_text[897:936]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d24.append(i)
  

d25=[]
for i in extracted_text[936:975]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d25.append(i)


d26=[]
for i in extracted_text[975:1014]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d26.append(i)



d27=[]
for i in extracted_text[1014:1053]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d27.append(i)


d28=[]
for i in extracted_text[1053:1092]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d28.append(i)
  

d29=[]
for i in extracted_text[1092:1131]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d29.append(i)


d30=[]
for i in extracted_text[1131:1170]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d30.append(i)
  

d31=[]
for i in extracted_text[1170:]:
    if i.startswith("Average") or i.startswith("Minimum") or i.startswith("Maximum") or i.startswith("Rainfall") or i.startswith("Jan"):
        pass
    else:
        d31.append(i)
 



jack=pd.DataFrame(columns=columns)
jack.loc["Jan 1"]=d1
jack.loc["Jan 2"]=d2
jack.loc["Jan 3"]=d3
jack.loc["Jan 4"]=d4
jack.loc["Jan 5"]=d5
jack.loc["Jan 6"]=d6
jack.loc["Jan 7"]=d7
jack.loc["Jan 8"]=d8
jack.loc["Jan 9"]=d9
jack.loc["Jan 10"]=d10
jack.loc["Jan 11"]=d11
jack.loc["Jan 12"]=d12
jack.loc["Jan 13"]=d13
jack.loc["Jan 14"]=d14
jack.loc["Jan 15"]=d15
jack.loc["Jan 16"]=d16
jack.loc["Jan 17"]=d17
jack.loc["Jan 18"]=d18
jack.loc["Jan 19"]=d19
jack.loc["Jan 20"]=d20
jack.loc["Jan 21"]=d21
jack.loc["Jan 22"]=d22
jack.loc["Jan 23"]=d23
jack.loc["Jan 24"]=d24
jack.loc["Jan 25"]=d25
jack.loc["Jan 26"]=d26
jack.loc["Jan 27"]=d27
jack.loc["Jan 28"]=d28
jack.loc["Jan 29"]=d29
jack.loc["Jan 30"]=d30
jack.loc["Jan 31"]=d31
Req_DF=jack#Final Data Frame
Req_DF.insert(0,"yyyy-mm-dd",["2021-01-01","2021-01-02","2021-01-03","2021-01-04","2021-01-05","2021-01-06","2021-01-07","2021-01-08","2021-01-09","2021-01-10","2021-01-11","2021-01-12","2021-01-13","2021-01-14","2021-01-15","2021-01-16","2021-01-17","2021-01-18","2021-01-19","2021-01-20","2021-01-21","2021-01-22","2021-01-23","2021-01-24","2021-01-25","2021-01-26","2021-01-27","2021-01-28","2021-01-29","2021-01-30","2021-01-31"])
Req_DF=Req_DF.set_index("yyyy-mm-dd")





