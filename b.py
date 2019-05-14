def kubus():
    print "1. LUAS KUBUS"
    s = raw_input("   Masukkan Panjang Sisi Kubus    : ")
    L = int(s)**2
    print "   Jadi, Luas Kubus adalah ",L

def Balok():
    print "2. LUAS BALOK"
    p = raw_input("   Masukkan Panjang Balok    : ")
    l = raw_input("   Masukkan Lebar Balok      : ")
    t = raw_input("   Masukkan Tinggi Balok     : ")
    L = 2*(int(p)*int(l)+int(p)*int(t)+int(l)*int(t))
    print "   Jadi, Luas Kubus adalah ",L

def lingkaran():
    print "3. LUAS LINGKARAN"
    r = raw_input("   Masukkan Panjang Jari-Jari Lingkaran   : ")
    L = 3.14*int(r)**2
    print "   Jadi, Luas Kubus adalah ",L
    
print "         LUAS BANGUN RUANG DAN BANGUN DATAR"
print
kubus()
print
Balok()
print
lingkaran()
