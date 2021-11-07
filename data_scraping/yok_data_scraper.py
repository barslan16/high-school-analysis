
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import xlsxwriter
import os
import pandas as pd


empty_url='https://yokatlas.yok.gov.tr/'


#available year
Y18="2018/"
Y19="2019/"
Y20=""
years=[Y20,Y19,Y18]

#sleep time
m=0.1


#selenium parser
#chrome driver needs to be installed on your computer
def newparser(link):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("phantomjs-1.9.2-windows/chromedriver.exe", options=options)
    driver.implicitly_wait(1)
    driver.get(link)
    more_buttons = driver.find_elements_by_class_name("moreLink")
    for x in range(len(more_buttons)):
        if more_buttons[x].is_displayed():
            driver.execute_script("arguments[0].click();", more_buttons[x])
            time.sleep(m)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup



# gives the codes of universities
filedest='university_codes.xlsx'

#there are four types university:
    #Devlet = State, 
    #Vakıf = Private, 
    #Kıbrıs = Northern Cyprus Turkish Republic, 
    #Yurdışı = Abroad

typeofuni=["DEVLET","VAKIF","KIBRIS","YURTDIŞI"]


#Each university has a code


devletuni = pd.read_excel(filedest, sheet_name='Devlet')
#State universities codes
devletunikod=devletuni['Üniversite Kodu'].tolist()
#State universities names
devletuniadi=devletuni['Üniversite'].tolist()

vakifuni = pd.read_excel(filedest, sheet_name='Vakıf')
vakifunikod=vakifuni['Üniversite Kodu'].tolist()
vakifuniadi=vakifuni['Üniversite'].tolist()

kibrisuni = pd.read_excel(filedest, sheet_name='Kıbrıs')
kibrisunikod=kibrisuni['Üniversite Kodu'].tolist()
kibrisuniadi=kibrisuni['Üniversite'].tolist()

yurtdisiuni = pd.read_excel(filedest, sheet_name='Yurtdışı')
yurtdisiunikod=yurtdisiuni['Üniversite Kodu'].tolist()
yurtdisiuniadi=yurtdisiuni['Üniversite'].tolist()


unikods=[devletunikod,vakifunikod,kibrisunikod,yurtdisiunikod]
uniadi=[devletuniadi,vakifuniadi,kibrisuniadi,yurtdisiuniadi]


p=0

for unikod in unikods:
    for sira in range(len(unikod)):
        directory='DATA/'+typeofuni[p]+'/'+str(unikod[sira])
        #check university's file
        if not os.path.exists(directory):
            os.makedirs(directory)
    
        print(uniadi[sira])
    
        #The link of the page where all departments of the university are located
        soup=newparser("https://yokatlas.yok.gov.tr/lisans-univ.php?u="+str(unikod[sira]))
        
        
        #saves all majors' links
        bolumlinkleri=[]
        bolumaciklamalari=[]
        for link in soup.find_all('a', href=True):
            if 'lisans.php' in link['href']:
                print(empty_url+str(link['href']))
                bolumlinkleri.append(empty_url+str(link['href']))
                #print(link.get_text())
                bolumaciklamalari.append(link.get_text())
        
        #link of each major
        for bolumlinki in bolumlinkleri:
            
            #parser
            soupyazici=newparser(bolumlinki)
            
            #allows us to find the printer link on the page
            def yazicilinkibulma(soup,id):
                return soup.find(id=id).find_all('a', href=True)[2]['href']
            
            
            #High Schools Graduated by Students (2020)
            yazıcılinki1=yazicilinkibulma(soupyazici, "c1060") #Yerleşenlerin Mezun Oldukları Liseler (2020) 
            
            #General Information (2020)
            yazıcılinki2=yazicilinkibulma(soupyazici, 'c1000_1') #Genel Bilgiler (2020)
         
            #Profile of Last Student (2020)
            yazıcılinki13=yazicilinkibulma(soupyazici, 'c1070') #Yerleşen Son Kişinin Profili (2020)
            
            #sleep to prevent over request
            time.sleep(m)
            
            
            
            

            def sifirlariyoketme(giris):
                if giris=="---":
                    return int(0)
                else:
                    return int(giris)
            
            #the process is repeated for each year
            for year in years:
                if year=='':
                    writingyear=2020
                    print("2020: "+str(uniadi[sira]))
                elif year=='2019/':
                     writingyear=2019
                     print("2019: "+str(uniadi[sira]))
                elif year=='2018/':
                    writingyear=2018
                    print("2018: "+str(uniadi[sira]))
                
                #create new file, add required columns
                workbook = xlsxwriter.Workbook('DATA/'+typeofuni[p]+'/'+str(unikod[sira])+"/"+str(writingyear)+"_"+str(yazıcılinki1[19:28]) + ".xlsx")
                
                
                
                #High Schools Graduated by Students (2020)
                newworksheet1 = workbook.add_worksheet("Mezun Oldukları Liseler")
                row = 0
                
                #add columns' names
                newworksheet1.write_string(row, 0, "Lise") 
                newworksheet1.write_string(row, 1, "Toplam")            
                newworksheet1.write_string(row, 2, "Liseden Yeni Mezun")
                newworksheet1.write_string(row, 3, "Önceki Mezun")
                
                time.sleep(m)
                
                soup1=newparser(empty_url+year+yazıcılinki1)
                veri=[]
                row = 1
                #check program
                if len(soup1.findAll("td", {"class": "thb small"}))==0:
                    print("finds nothing")
                    time.sleep(5)
                if len(soup1.findAll("td", {"class": "thb small"}))==0:
                    print("finds nothing"")
                else:
                    for i in range(len(soup1.findAll("td", {"class": "thb small"}))):
                        if i==0:
                            okul="TOPLAM"
                        else:
                            okul=soup1.findAll("td", {"class": "thb small"})[i-1].get_text()
                        newworksheet1.write_string(row,0 , okul)
                        newworksheet1.write_number(row,1 , sifirlariyoketme(soup1.findAll("td", {"class": "text-center"})[3*i].get_text()))
                        newworksheet1.write_number(row,2 , sifirlariyoketme(soup1.findAll("td", {"class": "text-center"})[3*i+1].get_text()))
                        newworksheet1.write_number(row,3 , sifirlariyoketme(soup1.findAll("td", {"class": "text-center"})[3*i+2].get_text()))
                        #print(okul,soup1.findAll("td", {"class": "text-center"})[3*i].get_text(),soup1.findAll("td", {"class": "text-center"})[3*i+1].get_text(),soup1.findAll("td", {"class": "text-center"})[3*i+2].get_text())
                        row+=1
                    
                    newworksheet2 = workbook.add_worksheet("Son Yerleşen Profili")
                    row=0
                
                    newworksheet2.write_string(row, 0, "Açıklama") 
                    newworksheet2.write_string(row, 1, "Bilgi")            
                    time.sleep(m)
                    
                    #Profile of Last Student (2020)
                    soup2=newparser(empty_url+year+yazıcılinki13)
                    row=1
                    
                    deger = soup2.find_all(align='center')
                    isim = soup2.find_all(class_='thb vert-align')
                    
                    for i in range(len(isim)):
                        
                        newworksheet2.write_string(row,0 ,isim[i].get_text())
                        newworksheet2.write_string(row,1 ,deger[i+1].get_text())
                        row+=1
                    
                    
                    #General Information (2020)

                    newworksheet3 = workbook.add_worksheet("Genel Bilgiler")
                    row=0
                
                    newworksheet3.write_string(row, 0, "Açıklama") 
                    newworksheet3.write_string(row, 1, "Bilgi")
                    newworksheet3.write_string(1, 0, "Bölüm")
                    time.sleep(m)
                    soup3=newparser(empty_url+year+yazıcılinki2)
                    
                    isim = soup3.find_all(class_='thb text-left')
                    deger = soup3.find_all(class_='text-center vert-align')
                    bolum_adi = soup3.find_all(class_='thb text-center')
                    if len(bolum_adi)==0:
                        pass
                    else:
                        print(bolum_adi[0].get_text())
                        newworksheet3.write_string(1, 1, str(bolum_adi[0].get_text()))
                    row=2
                    for i in range(len(isim)):
                
                        newworksheet3.write_string(row,0 ,isim[i].get_text())
                        newworksheet3.write_string(row,1 ,deger[i].get_text())
                
                        row+=1
                    
                    
                workbook.close()
                time.sleep(m)
    p+=1      
                
#available data for further analysis             
"""    
yazıcılinki3=yazicilinkibulma(soup, "c1000_2") #Kontenjan, Yerleşme ve Kayıt İstatistikleri (2020)

yazıcılinki4=yazicilinkibulma(soup, "c1010") #Yerleşenlerin Cinsiyet Dağılımı (2020)

yazıcılinki5=yazicilinkibulma(soup, 'c1020ab')#Yerleşenlerin Geldikleri Coğrafi Bölgeler (2020)

yazıcılinki6=yazicilinkibulma(soup, 'c1020c') #Yerleşenlerin Geldikleri İller

yazıcılinki7=yazicilinkibulma(soup, 'c1030a') #Yerleşenlerin Öğrenim Durumu (2020)

yazıcılinki8=yazicilinkibulma(soup, 'c1030b') #Yerleşenlerin Liseden Mezuniyet Yılları (2020)

yazıcılinki9=yazicilinkibulma(soup, 'c1050b') #Yerleşenlerin Mezun Oldukları Lise Alanları (2020)

yazıcılinki10=yazicilinkibulma(soup, 'c1050a') #Yerleşenlerin Mezun Oldukları Lise Grubu / Tipleri (2020

yazıcılinki11=yazicilinkibulma(soup, 'c1030c') #Yerleşen Okul Birincileri (2020)

yazıcılinki12=yazicilinkibulma(soup, 'c1000_3') #Taban Puan ve Başarı Sırası İstatistikleri (2020)

yazıcılinki14=yazicilinkibulma(soup, 'c1210a') #Yerleşenlerin YKS Net Ortalamaları (2020)

yazıcılinki15=yazicilinkibulma(soup, 'c1220') #Yerleşenlerin YKS Puanları (2020)

yazıcılinki16=yazicilinkibulma(soup, 'c1230') #Yerleşenlerin YKS Başarı Sıraları (2020)

yazıcılinki17=yazicilinkibulma(soup, 'c1080') #Ülke Genelinde Tercih Edilme İstatistikleri (2020)

yazıcılinki18=yazicilinkibulma(soup, 'c1040') #Yerleşenler Ortalama Kaçıncı Tercihlerine Yerleşti ? (2020)

yazıcılinki19=yazicilinkibulma(soup, 'c1300') #Yerleşenlerin Tercih Eğilimleri - Genel (2020)

yazıcılinki20=yazicilinkibulma(soup, 'c1310') #Yerleşenlerin Tercih Eğilimleri - Üniversite Türleri (2020)

yazıcılinki21=yazicilinkibulma(soup, 'c1320') #Yerleşenlerin Tercih Eğilimleri - Üniversiteler (2020)

yazıcılinki22=yazicilinkibulma(soup, 'c1330') #Yerleşenlerin Tercih Eğilimleri - İller (2020)

yazıcılinki23=yazicilinkibulma(soup, 'c1340a') #Yerleşenlerin Tercih Eğilimleri - Aynı/Farklı Program (2020)

yazıcılinki24=yazicilinkibulma(soup, 'c1340b') #Yerleşenlerin Tercih Eğilimleri - Programlar (Meslekler) (2020)

yazıcılinki25=yazicilinkibulma(soup, 'c1110') #Yerleşme Koşulları (2020 YKS)

yazıcılinki26=yazicilinkibulma(soup, 'c2050') #Öğretim Üyesi Sayısı ve Unvan Dağılımı

yazıcılinki27=yazicilinkibulma(soup, 'c2010') #Kayıtlı Öğrenci Sayısı

yazıcılinki28=yazicilinkibulma(soup, 'c2030') #Programdan Mezun Olan Öğrenci Sayıları

yazıcılinki29=yazicilinkibulma(soup, 'c2040') #Değişim Programı ile Giden/Gelen Öğrenci Sayıları

yazıcılinki30=yazicilinkibulma(soup, 'c2060') #Yatay Geçiş ile Gelen/Giden Öğrenci Sayıları
"""  