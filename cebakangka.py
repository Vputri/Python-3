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
print ''
print("            SELAMAT DATANG DI PERMAINAN TEBAK ANGKA");
print
    
def menu():
    namaku = raw_input("   Input your name: ");
    print
    angka = random.randint(1,30)
    print ("   Coba tebak angka antara 1-30");
    print
    tebak = raw_input("   Masukan angka: ");
    print
    if tebak == angka:
        print ("   Good Job, "+nama+ "Tebakan Anda benar");
    else:
        print ("   Maaf Tebakan Anda Salah");
        print
        n = raw_input("   Apakah anda ingin bermain lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
menu()
