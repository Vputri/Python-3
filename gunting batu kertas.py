import time
import random

from datetime import datetime
sekarang=datetime.now()
hari=sekarang.day
bulan=sekarang.month
tahun=sekarang.year
jam=sekarang.hour
menit=sekarang.minute
detik=sekarang.second
print ''
print '                                                  Tanggal : {}/{}/{}'.format(hari,bulan,tahun)
print "                                                  Jam     : {}:{}:{}".format(jam,menit,detik)
print
print "    ======================================================================="
print
print("            SELAMAT DATANG DI PERMAINAN GUNTING BATU KERTAS");

def menu():
    Skor_Pemain = 0
    Skor_Komputer = 0
    Pilihan_Komputer = ["batu","kertas","gunting"]
    komp_pilih = random.choice(Pilihan_Komputer)
    print
    print "    ======================================================================="
    print
    pemain_pilih = raw_input("    Silahkan masukkan pilih anda [gunting/batu/kertas]: " )
    print
    wait = time.sleep
    if pemain_pilih == "batu" and komp_pilih == "gunting":
        print ("    Anda memilih " + pemain_pilih)
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        wait(1)
        print
        print ("    Selamat Anda menang !")
        Skor_Pemain += 1
        print   
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
        print
    elif pemain_pilih == "gunting" and komp_pilih == "batu":
        wait(.5)
        print ("    Anda memilih " + pemain_pilih)
        print ("    Komputer memilih " + komp_pilih)
        wait(1)
        print
        print ("    Anda Kalah")
        Skor_Komputer += 1
        print      
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
        print
    elif pemain_pilih == "kertas" and komp_pilih == "batu":
        wait(.5)
        print ("    Anda memilih " + pemain_pilih)
        print ("    Komputer memilih " + komp_pilih)
        print
        wait(1)
        print ("    Selamat Anda menang")
        Skor_Pemain += 1
        print
    elif pemain_pilih == "batu" and komp_pilih == "kertas":
        print ("    Anda memilih " + pemain_pilih)
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        print
        wait(1)
        print ('    Anda Kalah')     
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
        print
    elif pemain_pilih == "batu" and komp_pilih == "batu":
        print("    Anda memilih " + pemain_pilih)
        wait(.5)
        print("    Komputer memilih " + komp_pilih)
        print
        wait(1)
        print ('    Seri')
        print      
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
        print
    elif pemain_pilih == "kertas" and komp_pilih == "gunting":
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        print("    Anda memilih " + pemain_pilih)
        print
        wait(1)
        print ("    Anda Kalah")
        Skor_Komputer += 1
        print
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
        print
    elif pemain_pilih == "kertas" and komp_pilih == "kertas":
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        print ("    Anda memilih " + pemain_pilih)
        print
        wait(1)
        print ("    Seri")
        print
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
    elif pemain_pilih == "gunting" and komp_pilih == "kertas":
        print ("    Anda memilih " + pemain_pilih)
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        print
        wait(1)
        print ("    Anda menang")
        Skor_Pemain += 1
        print
        print ("    Skor anda: " + str(Skor_Pemain))
        print ("    Skor Komputer: " + str(Skor_Komputer))
    elif pemain_pilih == "gunting" and komp_pilih == "gunting":
        print("    Anda memilih " + pemain_pilih)
        wait(.5)
        print ("    Komputer memilih " + komp_pilih)
        print
        wait(1)
        print ("    Seri")
        print
        print "    Skor anda: " + str(Skor_Pemain)
        print "    Skor Komputer: " + str(Skor_Komputer)
    else:
        wait(.5)
        print ("    Input yang anda masukkan tidak cocok dengan pilihan yang ada !")
        pilihan()
    print
    print "    ======================================================================="
        
def pilihan():
    print
    pilih = raw_input("    Apakah anda ingin bermain lagi (Y/N): ")
    print
    if pilih in ('y','Y'):
        menu()
        pilihan()
    elif pilih in ('n','N'):
        exit()
    else:
        print
        print("    Oops I didn\'t understand your input, input Y/N")
        pilihan()

menu()
pilihan()
