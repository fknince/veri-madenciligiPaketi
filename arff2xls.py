#kütüphaneler
from tkinter import *
from tkinter import filedialog
import xlwt
import ctypes

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
root.title("arff - xls çevirici")
root.geometry("265x100")
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


def button2_Basildi():
    global file_path
    global sorgu
    #arff dosyasından veri çekme fonksiyonu
    gecici=ArffdanVeriCek(file_path)
    #devam etmek için tamam'a tıkla bildirimi veren komut
    sorgu = ctypes.windll.user32.MessageBoxW(0, "Dosyanın kayıt edileceği klasörü seçmek için 'Tamam' tuşuna basınız.",

                                           "Klasör Seçimi", 0)
    #baslik ismini bulma
    dizi = file_path.split(".")[0].split("/")
    baslik = dizi[len(dizi) - 1]
    #eğer tamam basıldıysa
    if (sorgu == 1):
        #dosya yolu seçme
        root2 = Tk()
        root2.withdraw()
        global record_path
        record_path = filedialog.askdirectory() + "/" +"Converted-"+ baslik+".xls"

        #excel oluşturma ve veri yazma komutları
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(baslik)

        #ilk önce ilk satır yani başlıkları ekleme
        for i in range(0,basliklar.__len__()):
            sheet.write(0,i,basliklar.__getitem__(i))
        #verileri ekleme
        for i in range(0,veriler.__len__()):
            for j in range(0,len(veriler[i])):
                sheet.write(i+1,j,veriler[i][j])
        #excel dosyasını belirtilen adrese ve isimle kaydetme
        workbook.save(record_path)


        #işlemin gerçekleştiğine dair labela yazı yazdırma
        label = Label(app, text="İşlem Tamamlandı", fg="green")
        label.grid()




#birinci butonu tanımlama
button1=Button(app,text="Dosya Seç",command=button1_Basildi)
button1.grid()

#ikinci butonu tanımlama
button2=Button(app,text="Dönüştür",command=button2_Basildi)
button2.grid()

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






root.mainloop()
