print "Ketikkan Control C atau -1 untuk keluar"
number = 1
while number != -1:
    print ''
    try:
        number = int(raw_input("Masukan angka   : "))
        print "Anda memasukan  :",number
    except ValueError:
        print "Bukan angka bilangan integer atau float!"
