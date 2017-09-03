# kütüphaneler
from tkinter import *
from tkinter import filedialog
from math import *
from tkinter.ttk import Combobox

# global değişkenler


# global değişkenler
file_path = ""
record_path = ""
listem = []
metin = ""
basliklar = []
veriler = []
devamEt = 0
sorgu = 0

# pencere oluşturma
root = Tk()
root.title("Linear Regression Algoritması")
root.geometry("300x400")
app = Frame(root)
app.grid()

# label ekleme
label = Label(app, text="Lütfen .arff dosyasını seçmek için butona tıklayınız.")
label.grid()


# birinci butonun fonksiyonu
def button1_Basildi():
    root2 = Tk()
    root2.withdraw()
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Arff Files", "*.arff"), ("All files", "*.*")))
    ArffdanVeriCek(file_path)



def button2_Basildi():
    label3["text"] = Hesapla()




# birinci butonu tanımlama
button1 = Button(app, text="Dosya Seç", command=button1_Basildi)
button1.grid()




# ikinci butonu tanımlama
button2 = Button(app, text="Algoritmayı Uygula", command=button2_Basildi)
button2.grid()

# label ekleme
label3 = Label(app, text="")
label3.grid()


def ArffdanVeriCek(file_path):
    global metin

    global devamEt

    # excel dosyasını file olarak açma
    with open(file_path) as f:
        # exceldeki her bir satıra erişme
        for g in (f.readlines()):
            # eğer data kısmına geldiysek
            if (devamEt == 1):
                gecici = g.split(",")
                gecici[gecici.__len__() - 1] = gecici[gecici.__len__() - 1].replace("\n", "")
                veriler.append(gecici)
            # sütun isimlerini bulunduran kısmı bulmak için
            if (g.lower().__contains__("@attribute")):
                gecici = g.split(" ")
                basliklar.append(gecici[1])
            # data yazısını görünce devamEt= true yaptık
            if (g.lower().__contains__("@data") == 1):
                devamEt = 1




def Hesapla():
    n=veriler.__len__()

    #Y ortalaması hesabı
    ortalama_y=0
    for i in range(0, veriler.__len__()):
        ortalama_y+=float(veriler[i][1])
    ortalama_y=ortalama_y/n

    #∑XiYi  bulan kod
    veri1=0
    carpim=1
    for i in range(0,veriler.__len__()):
        for veri in veriler[i]:
            carpim*=float(veri)
        veri1+=carpim
        carpim = 1

    # ∑Xi  bulan kod
    veri2 = 0
    for i in range(0, veriler.__len__()):
        veri2+=float(veriler[i][0])

    # ∑Yi  bulan kod
    veri3=0
    for i in range(0, veriler.__len__()):
        veri3+=float(veriler[i][1])

    # ∑Xi²  bulan kod
    veri4=0
    for i in range(0, veriler.__len__()):
        veri4+=pow(float(veriler[i][0]),2)


    #a1 hesaplama
    a1=((n*veri1)-(veri2*veri3))/((n*veri4)-pow(veri2,2))

    #a0 hesaplama
    a0= (veri3/n)-((a1*veri2)/n)

    #Sr  hesabı ( reel değer )
    Sr=0
    for i in range(0,veriler.__len__()):
        Sr+=pow((float(veriler[i][1])-a0-(a1*float(veriler[i][0]))),2)

    #St hesabı ( true değer )
    St=0
    for i in range(0, veriler.__len__()):
        St+=pow((float(veriler[i][1])-ortalama_y),2)

    #r² ( belirsizlik katsayısı ) hesabı
    r_kare=(St-Sr)/St

    return "\n\n\n\n\na0 = "+str(a0)+"\na1= "+str(a1)+"\nE = y-"+str(a0)+"-"+str(a1)+"x\nSr = "+str(Sr)+"\nSt = "+str(St)+\
           "\nr²(belirsizlik katsayısı) = "+str(r_kare)




root.mainloop()

















