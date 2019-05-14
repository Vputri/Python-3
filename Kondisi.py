def menu():
    print '                                  Menu Makanan'
    print ''
    print '                               =================== '
    print '                              |     PILIHAN :     |'
    print '                              |                   |'
    print '                              | 1.Nasi Goreng     |'
    print '                              | 2.Nasi Rames      |'
    print '                              | 3.Sop Iga         |'
    print '                              | 4.Gado-Gado       |'
    print '                              |                   |'
    print '                               ==================='
    print ''

    x = (raw_input("Masukkan Pilihan (1-4) : "))
    print ''
    if x == "1":
        print 'Menu pilihan anda adalah Nasi Goreng'
    elif x == "2":
        print 'Menu pilihan anda adalah Nasi Rames'
    elif x == "3":
        print 'Menu pilihan anda adalah Sop Iga'
    elif x == "4":
        print 'Menu pilihan anda adalah Gado-Gado'
    else:
        print 'Pilihan Tidak Ada'
        print ''
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print 'Syntaks eror'
                

menu()
