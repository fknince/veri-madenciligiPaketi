#kütüphaneler
from tkinter import *
from tkinter import filedialog
import xlrd
import ctypes


#global değişkenler
file_path=""
record_path=""
metin="@relation"
ekstra=""
baslik=""


#pencere oluşturma
root= Tk()
root.title("xls - arff çevirici")
root.geometry("265x100")
app=Frame(root)
app.grid()

#label ekleme
label = Label(app,text="Lütfen xls dosyasını seçmek için butona tıklayınız.")
label.grid()

#birinci butonun fonksiyonu
def button1_Basildi():
    root2=Tk()
    root2.withdraw()
    global file_path
    file_path = filedialog.askopenfilename(filetypes = (("Excel files", "*.xls")   ,("Excel files", "*.xlt")

                                                   ))

#ikinci butonun fonksiyonu
def button2_Basildi():
    global label
    exceldenVeriCek()
    sorgu=ctypes.windll.user32.MessageBoxW(0, "Dosyanın kayıt edileceği klasörü seçmek için 'Tamam' tuşuna basınız.", "Klasör Seçimi",0)
    if(sorgu == 1 ):
        root2 = Tk()
        root2.withdraw()
        global record_path
        record_path = filedialog.askdirectory()+"/"+baslik+".arff"

        file1 = open(record_path, "w")

        file1.write(metin)
        file1.close()


        label=Label(app,text="İşlem Tamamlandı",fg="green")
        label.grid()

#birinci butonu tanımlama
button1=Button(app,text="Dosya Seç",command=button1_Basildi)
button1.grid()

#ikinci butonu tanımlama
button2=Button(app,text="Dönüştür",command=button2_Basildi)
button2.grid()

#excelden veri çekme ve ana işlemler
def exceldenVeriCek():
#fonksiyonun içine global değişkenleri alma
 global metin
 global ekstra
 global baslik
 #local değişkenler
 ifadeler="{"
 Stringler=[]
 dizi=file_path.split(".")[0].split("/")
 baslik=dizi[len(dizi)-1]
 metin+=" "+baslik+"\n\n"
 #excele bağlanma
 book=xlrd.open_workbook(file_path)
 work_sheet=book.sheet_by_index(0)

#tüm sütunlara ulaşma
 for colindex in range(work_sheet.ncols):
     #eğer verinin tipi String ise

     if ((work_sheet.cell(1, colindex).ctype == 1) ):

        #her bir satırdaki farklı stringi geçici diziye atama
        for rowindex in range(work_sheet.nrows):
            if (rowindex != 0):
                if ((Stringler.__contains__(work_sheet.cell(rowindex, colindex).value) != 1)):
                    Stringler.append(work_sheet.cell(rowindex, colindex).value)
        #dizideki elemanları stringe yazdırma
        for i in range(0, Stringler.__len__()):
            if (i != Stringler.__len__() - 1):
                ifadeler += Stringler.__getitem__(i) + ","
            else:
                ifadeler += Stringler.__getitem__(i) + "}"
        #diziyi boşaltma
        del Stringler[:]
        # metini güncelleme
        metin += "@ATTRIBUTE " + work_sheet.cell(0, colindex).value + " " + ifadeler + "\n"
        # ifadeleri sıfırlama
        ifadeler = "{"
     #eğer verinin tipi numeric ise
     elif ((work_sheet.cell(1, colindex).ctype == 2)):
         metin += "@ATTRIBUTE " + work_sheet.cell(0, colindex).value + " numeric\n"



 metin+="\n@DATA\n"

 maxRow=-1
 maxCol=-1

 for indexRow in range (work_sheet.nrows):
     maxRow=indexRow

 for indexCol in range (work_sheet.ncols):
     maxCol=indexCol

 for rowindex in range(work_sheet.nrows):
     for colindex in range(work_sheet.ncols):
         if(rowindex !=0):
             if(colindex != maxCol):
                if(work_sheet.cell(rowindex,colindex).ctype == 2):
                    sayi=int(work_sheet.cell(rowindex,colindex).value)
                    metin+=str(sayi)+","
                elif(work_sheet.cell(rowindex,colindex).ctype == 1):
                    metin += str(work_sheet.cell(rowindex, colindex).value) + ","

             else:
                  if (work_sheet.cell(rowindex, colindex).ctype == 2):
                      sayi = int(work_sheet.cell(rowindex, colindex).value)
                      metin += str(sayi) + "\n"
                  elif (work_sheet.cell(rowindex, colindex).ctype == 1):
                      metin += str(work_sheet.cell(rowindex, colindex).value) + "\n"








root.mainloop()
