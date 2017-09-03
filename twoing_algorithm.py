#kütüphaneler
from tkinter import *
from tkinter import filedialog
from math import *
from tkinter.ttk import Combobox
import decimal


#global değişkenler


#global değişkenler
file_path=""
record_path=""
listem=[]
metin=""
basliklar=[]
basliklarCopy=[]
farkli_veriler=[]
uygunlukSonuclari=[]
veriler=[]
toplamVeri=0
devamEt=0
sorgu=0

#pencere oluşturma
root= Tk()
root.title("Twoing algoritması")
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
    global basliklarCopy
    file_path = filedialog.askopenfilename(filetypes=(("Arff Files", "*.arff"),("All files", "*.*")))
    ArffdanVeriCek(file_path)
    global combo
    global toplamVeri
    basliklarCopy=basliklar[:]
    for i in range(0,basliklarCopy.__len__()):
        if(veriler[1][i].isdigit() == 1):
            basliklarCopy.pop(i)
    basliklarCopy.pop(basliklarCopy.__len__()-1)
    basliklarCopy.append("Hepsi")
    combo["values"]=basliklarCopy
    combo.current(basliklarCopy.__len__()-1)
    toplamVeri=veriler.__len__()





def button2_Basildi():
  global uygunlukSonuclari
  global basliklarCopy
  if(combo.get() != "Hepsi" and combo.get()):
      indis = basliklar.index(combo.get())
      del uygunlukSonuclari[:]

      Hesapla(indis)

      #labela sonucu yazdırma
      metin = "\n\n\n"
      for i in range(0, len(uygunlukSonuclari)):
              metin+="- - - - - - - - Aday Bölünme #"+str(i+1)+" - - - - - - - -\nTSol = "+str(uygunlukSonuclari[i][0])+"\n" \
                "TSag = "+str(uygunlukSonuclari[i][1])+"\n" \
                "Uygunluk Ölçütü = "+str(uygunlukSonuclari[i][2])+"\n"
      label3["text"] = metin




  else:
    del uygunlukSonuclari[:]
    sayi=1
    metin = "\n\n\n"
    for i in range(0,basliklarCopy.__len__()-1):
        Hesapla(basliklar.index(basliklarCopy[i]))

        for i in range(0, len(uygunlukSonuclari)):
            metin += "- - - - - - - - Aday Bölünme #" + str(sayi) + " - - - - - - - -\nTSol = " + str(
            uygunlukSonuclari[i][0]) + "\n" \
                                       "TSag = " + str(uygunlukSonuclari[i][1]) + "\n" \
                                                                                  "Uygunluk Ölçütü = " + str(
            uygunlukSonuclari[i][2]) + "\n"
            sayi += 1
        del uygunlukSonuclari[:]


    # pencere oluşturma
    root_ilave = Tk()
    root_ilave.title("Tüm Uygunluk Ölçütleri")
    root_ilave.geometry("300x800")
    app2 = Frame(root_ilave)
    app2.grid()

    # label ekleme
    label_ilave = Label(app2, text=metin)
    label_ilave.grid()

    root_ilave.mainloop()










#birinci butonu tanımlama
button1=Button(app,text="Dosya Seç",command=button1_Basildi)
button1.grid()



#label ekleme
label2 = Label(app,text="Hangi nitelikler için uygunluk hesaplansın ?")
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



def Hesapla(indis):
    global farkli_veriler
    del farkli_veriler[:]
    #secilen sütuna dair farklı değerleri belirleme ( örneğin gelir sütunu için -> (normal,büyük,küçük) )
    for veri in veriler:
        if(farkli_veriler.__contains__(veri[indis]) != 1):
            farkli_veriler.append(veri[indis])

    #Tsol ve Tsag atamasının yapıldığı recursive fonksiyonu çağırıyoruz
    anaIslemler(0,indis)






def anaIslemler(kullanilanIndis,indis):
    global farkli_veriler
    global uygunlukSonuclari
    if(kullanilanIndis < farkli_veriler.__len__()):
        TSol = []
        Tsag = []

        del TSol[:]
        del Tsag[:]

        for i in range(0, farkli_veriler.__len__()):
            if (i == kullanilanIndis):
                TSol.append(farkli_veriler[i])
            else:
                Tsag.append(farkli_veriler[i])

        # Tsol kayıt sayısının hesabı
        Tsol_adet = 0
        for veri in veriler:
            if (veri[indis] == TSol[0]):
                Tsol_adet += 1
        # Tsağ kayıt sayısının hesabı
        Tsag_adet = 0
        for veri in veriler:
            for eleman in Tsag:
                if (eleman == veri[indis]):
                    Tsag_adet += 1

        #Psol ve Psağ hesabı
        global toplamVeri
        PSol=Tsol_adet/toplamVeri
        PSag=Tsag_adet/toplamVeri

        #Eylemin şartlarını belirleme örneğin Memnuniyet için Evet yada Hayır
        eylem_sartlar =[]

        del eylem_sartlar[:]

        for veri in veriler:
            if(eylem_sartlar.__contains__(veri[veri.__len__()-1])!= 1):
                eylem_sartlar.append(veri[veri.__len__()-1])

        #Eylemin şartlarının Tsol ve Tsaga göre adetlerinin hesabı
        Tsol_Sartlar=[]
        Tsag_Sartlar=[]

        del Tsol_Sartlar[:]
        del Tsag_Sartlar[:]

        #dizilerin içini kolaylık olması açısından farklı şart sayısı kadar sıfırla doldurma
        for i in range(eylem_sartlar.__len__()):
            Tsol_Sartlar.append(0)
            Tsag_Sartlar.append(0)

        #Eylemin şartlarının Tsol ve Tsaga göre adetlerinin hesap işlemleri

        #Tsol için
        for veri in veriler:
            for tsol in TSol:
                if(tsol == veri[indis]):
                    for i in range (0,eylem_sartlar.__len__()):
                        if(veri[veri.__len__()-1] == eylem_sartlar[i]):
                            Tsol_Sartlar[i]+=1

        #Tsag için
        for veri in veriler:
            for tsag in Tsag:
                if (tsag == veri[indis]):
                    for i in range(0, eylem_sartlar.__len__()):
                        if (veri[veri.__len__() - 1] == eylem_sartlar[i]):
                            Tsag_Sartlar[i] += 1

        #P(sart/Tsol) hesabı
        P_Tsol_Sartlar=[]

        del P_Tsol_Sartlar[:]
        toplam=0

        for ts in Tsol_Sartlar:
            toplam+=ts


        for ts in Tsol_Sartlar:
            P_Tsol_Sartlar.append(ts/toplam)


        # P(sart/Tsag) hesabı
        P_Tsag_Sartlar = []

        del P_Tsag_Sartlar[:]
        toplam = 0
        for ts in Tsag_Sartlar:
            toplam += ts
        for ts in Tsag_Sartlar:
            P_Tsag_Sartlar.append(ts / toplam)

        #uygunluk formülünde toplam işareti olan kısmının yapımı ∑P(j/tsol)-P(j/tsag) kısmı
        doncek=0
        for i in range(0,P_Tsol_Sartlar.__len__()):
            doncek+=(fabs(P_Tsol_Sartlar[i]-P_Tsag_Sartlar[i]))

        uygunluk=2*PSol*PSag*doncek
        yuvarlanmis_uygunluk=decimal.Decimal(uygunluk)
        deger=yuvarlanmis_uygunluk.__float__()


        gecicidizi=[TSol,Tsag,round(deger,2)]
        uygunlukSonuclari=uygunlukSonuclari[:]
        uygunlukSonuclari.append(gecicidizi)

        kullanilanIndis+=1
        return anaIslemler(kullanilanIndis,indis)


    else:
            return





















root.mainloop()

















