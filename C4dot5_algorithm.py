#kütüphaneler
from tkinter import *
from tkinter import filedialog
from math import *
from tkinter.ttk import Combobox


#global değişkenler


#global değişkenler
file_path=""
record_path=""
listem=[]
metin=""
basliklar=[]
veriler=[]
devamEt=0
sorgu=0

#pencere oluşturma
root= Tk()
root.title("ID3 algoritması")
root.geometry("300x400")
app=Frame(root)
app.grid()

#label ekleme
label = Label(app,text="Lütfen .arff dosyasını seçmek için butona tıklayınız.")
label.grid()

#birinci butonun fonksiyonu
def button1_Basildi():
    root2=Tk()
    root2.withdraw()
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Arff Files", "*.arff"),("All files", "*.*")))
    ArffdanVeriCek(file_path)
    global combo
    basliklar.append("Hepsi")
    combo["values"]=basliklar
    combo.current(basliklar.__len__()-1)

    numeric2string()



def button2_Basildi():
  if(basliklar[basliklar.__len__()-2] == combo.get()):
      return
  elif(combo.get() != "Hepsi" and combo.get()):
      indis=basliklar.index(combo.get())
      donen=Hesapla(indis)
      label3["text"]="\n\nKazanc["+combo.get()+"]="+str(round(donen,4))

  else:
    metin=""
    for i in range(0,basliklar.__len__()-2):
        donen=Hesapla(i)
        metin+="\n\nKazanc["+basliklar[i]+"]="+str(round(donen,4))+"\n"
        label3["text"]=metin






#birinci butonu tanımlama
button1=Button(app,text="Dosya Seç",command=button1_Basildi)
button1.grid()



#label ekleme
label2 = Label(app,text="Hangi nitelikler için kazanç hesaplansın ?")
label2.grid()

#combo boxımızı oluşturma
combo=Combobox(app,height=5,width=15)
combo.grid()

#ikinci butonu tanımlama
button2=Button(app,text="Algoritmayı Uygula",command=button2_Basildi)
button2.grid()

#label ekleme
label3 = Label(app,text="")
label3.grid()

def  ArffdanVeriCek(file_path):
    global metin

    global devamEt

    #excel dosyasını file olarak açma
    with open(file_path) as f:
        #exceldeki her bir satıra erişme
        for g in(f.readlines()):
            #eğer data kısmına geldiysek
            if(devamEt == 1):
                gecici=g.split(",")
                gecici[gecici.__len__()-1]=gecici[gecici.__len__()-1].replace("\n","")
                veriler.append(gecici)
            #sütun isimlerini bulunduran kısmı bulmak için
            if(g.lower().__contains__("@attribute")):
                gecici=g.split(" ")
                basliklar.append(gecici[1])
            #data yazısını görünce devamEt= true yaptık
            if(g.lower().__contains__("@data") == 1):
                devamEt=1

def numeric2string():
    # sadece sayı olan verilerin indislerini bulma
    indisler = []
    for i in range(0, len(veriler[0])):
        if (veriler[0][i].isdigit() == 1):
            indisler.append(i)

    # C4.5 algoritmasına özgün işlemlerin yapıldığı kısım

    # sayısal verilerin birer adet listeye yazımı
    siralancak_veriler = []
    ortalamalar = []
    for indis in indisler:
        for i in range(0, veriler.__len__()):
            if (siralancak_veriler.__contains__(veriler[i][indis]) != 1):
                siralancak_veriler.append(veriler[i][indis])
        toplam = 0
        for veri in siralancak_veriler:
            toplam += int(veri)
        ortalama = round(toplam / siralancak_veriler.__len__())
        ortalamalar.append(ortalama)

    # sayısal verilerin ortalamadan buyuk yada kucuk olmasına gore metine çevirme
    for j in range(0,veriler.__len__()):
        for i in range(0, indisler.__len__()):
            if (int(veriler[j][indisler[i]]) <= int(ortalamalar[i])):
                veriler[j][indisler[i]] = "kucuk"
            else:
                veriler[j][indisler[i]] = "buyuk"



def Hesapla(indis):

    eylem_indis = basliklar.__len__() - 2

    #eylemin farklı durumlarını bir listeye atma
    listem_durumlar_eylem = []
    for i in range(0, veriler.__len__()):
        if (listem_durumlar_eylem.__contains__(veriler[i][eylem_indis]) != 1):
            listem_durumlar_eylem.append(veriler[i][eylem_indis])

    #H(oyun) hesapladığımız kısım
    listem_durumlar_eylemSonuclar=[]

    for durumlar in listem_durumlar_eylem:
        gecici = 0
        for  i  in range(0,veriler.__len__()):

            if(veriler[i][eylem_indis] == durumlar):
                gecici+=1
        listem_durumlar_eylemSonuclar.append(gecici)



    toplam=0
    for lde in listem_durumlar_eylemSonuclar:
        toplam+=lde

    Heylem=0
    for lde in listem_durumlar_eylemSonuclar:
        Heylem+=(lde/toplam)*((log(lde/toplam))/(log(2)))
    Heylem=-1*Heylem




    #H(seçilen nitelik,Oyun) hesabını yaptığımız kısım

    #örneğin seçilen Hava niteliği ise  farklı  bütün durumları bulan kod ( Rüzgarlı,Bulutlu,Yağmurlu)
    listem_durumlar=[]
    for i in range (0,veriler.__len__()):
        if(listem_durumlar.__contains__(veriler[i][indis]) != 1):
            listem_durumlar.append(veriler[i][indis])



    #H(secilen,oyun) hesabı
    listem_durumAdetleri=[]
    for durum in listem_durumlar:
        gecici=0
        for veri in veriler:
            if(veri.__contains__(durum)):
                gecici+=1
        listem_durumAdetleri.append(gecici)

    toplam_durumSayisi=veriler.__len__()





    #H(nitelik = durum) hesaplama örneğin H(Hava = yağmurlu)

    #lazım olcak listeleri hazırlama

    listem_durumEntropileri=[]

    gecici=[]
    for t in range(0,listem_durumlar.__len__()):


        gecici[:]=[]
        # içinde eylem durumu adeti kadar sıfır olan dizi liste oluşturdur örneğin oyun için evet ve hayır için 2 tane sıfır
        for k in range(0, listem_durumlar_eylem.__len__()):
            gecici.append(0)
        for i in range(0,veriler.__len__()):

            if(veriler[i][indis] == listem_durumlar[t] ):

                for j in range(0,listem_durumlar_eylem.__len__()):

                    if(veriler[i][eylem_indis] == listem_durumlar_eylem[j]):

                        gecici[j]+=1

        listem_durumEntropileri.append(gecici[:]) #boktan hatanın olduğu kısım düzelten şey ise = gecici[:] yapmak



    #toplamları hesaplayan
    toplamlar = []
    toplam = 0
    # her bir durum entropilwein toplamını bulan kısım örneğin hava güneşli için evet ve hayır saysının toplamı
    for eleman in listem_durumEntropileri:
        for elemanlar in eleman:
            toplam += elemanlar
        toplamlar.append(toplam)
        toplam = 0


    #matematiksel işlemlerin yapıldığı kısım
    listem_durumSonuclari=[]
    for i in range(0,listem_durumlar.__len__()):
        sonuc=0
        for elemanlar in listem_durumEntropileri[i]:
            if(elemanlar/toplamlar[i] != 0):
                sonuc+=((elemanlar/toplamlar[i])*(log(elemanlar/toplamlar[i]))/log(2))
        listem_durumSonuclari.append((-1*sonuc))








    #H(secilen,oyun) matematiksel hesabı
    sonuc=0
    for i in range(0,listem_durumlar.__len__()):
        sonuc+=((listem_durumAdetleri[i]/toplam_durumSayisi)*listem_durumSonuclari[i])


    #Kazanç(secilen,oyun) matematiksel hesabı = H(oyun) - H(secilen,oyun)
    donecek=Heylem-sonuc
    return donecek












root.mainloop()

















