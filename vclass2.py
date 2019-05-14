print;
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
print;
print '                         PROGRAM SEGITIGA TERBALIK';
print '                          Vika Putri Ariyanti'
print;

string = ""
y = 1

x = int(input("   Masukkan angka : "))
print ("\n")
no = x

while y <= x:
	
	kol = y
	while kol > 1:
		string = string + "   "
		kol = kol - 1
	
	kiri = 0
	while kiri <= (x - y):
		string = string + " " + str(no) + " "
		kiri = kiri + 1	
	
	kanan = kiri	
	while kanan > 1:
		string = string + " " + str(no) + " "
		kanan = kanan - 1

	string = string + "\n\n"
	y = y + 1
	no = no - 1
print (string)
