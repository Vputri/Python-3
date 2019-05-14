def mengulang():
    print
    n = raw_input("   Apakah anda ingin mengulang lagi(Y/N): ")
    if n in ["Y", "y"]:
        print ''
        menu()
    elif n in ["N", "n"]:
        exit()
    else:
        print
        print 'Maaf Anda salah mengiput'
        print
        n = raw_input("   Apakah anda ingin mengulang lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        
def menu():
    print
    print "                               TEMPERATURE CONVERT"
    print
    print "  ========================================================================="
    print "  |                                  PILIHAN :                            |"
    print "  |                                                                       |"
    print "  |                               1.Celcius    (C)                        |"
    print "  |                               2.Fahrenheit (F)                        |"
    print "  |                               3.Reamur     (R)                        |"
    print "  |                               4.Kelvin     (K)                        |"
    print "  |                                                                       |"
    print "  ========================================================================="
    print
    
    x = raw_input("   Dari (C/F/R/K)              : ")
    print
    if x in ["C", "c"]:
        x = raw_input("   Ke (F/R/K)                  : ")
        print
        if x in ["F", "f"]:
            C = raw_input("   Masukkan Derajat Celcius    : ")
            print
            F = (int(C) * 9 / 5) + 32
            print "   F = (9/5 x C)+32"
            print "     = (9/5 x",C,") + 32"
            print "     =",F
            mengulang()
        if x in ["R", "r"]:
            C = raw_input("   Masukkan Derajat Celcius    : ")
            print
            R = int(C) * 4 / 5
            print "   R = 4/5 x C"
            print "     = 4/5 x",C
            print "     =",R
            mengulang()
        if x in ["K", "k"]:
            C = raw_input("   Masukkan Derajat Celcius    : ")
            print
            K = int(C) + 273
            print "   K = C + 273"
            print "     =",C," + 273"
            print "     =",K
            mengulang()
        else :
            print '   Maaf Pilihan Anda Tidak Ada'
            mengulang()   

    if x in ["F", "f"]:
        x = raw_input("   Ke (C/R/K)                  : ")
        print
        if x in ["C", "c"]:
            F = raw_input("   Masukkan Derajat Fahrenheit : ")
            print
            C = (int(F) - 32) * 5 / 9
            print "   C = 5/9 * (",F,"- 32)"
            print "     =",C
            mengulang()
        if x in ["R", "r"]:
            F = raw_input("   Masukkan Derajat Fahrenheit : ")
            print
            R = (int(F) - 32) * 4 / 9
            print "   R = 4/9 * (",F," - 32)"
            print "     =",R
            mengulang()
        if x in ["K", "k"]:
            F = raw_input("   Masukkan Derajat Fahrenheit : ")
            print
            K = ((int(F) - 32) * 5 / 9) +273
            print "   K = (5/9 * (",F," - 32)) + 273"
            print "     =",K
            mengulang()
        else :
            print '   Maaf Pilihan Anda Tidak Ada'
            mengulang() 
                
    if x in ["R", "r"]:
        x = raw_input("   Ke (C/F/K)                  : ")
        print
        if x in ["C", "c"]:
            R = raw_input("   Masukkan Derajat Reamur     : ")
            print
            C = (int(R) * 5 / 4)
            print "   C = 5/4 x",R
            print "     =",C
            mengulang()
        if x in ["F", "f"]:
            R = raw_input("   Masukkan Derajat Reamur     : ")
            print
            F = (int(R) * 9 / 4) + 32
            print "   F = (9/4 x",R,") + 32"
            print "     =",F
            mengulang()
        if x in ["K", "k"]:
            R = raw_input("   Masukkan Derajat Reamur     : ")
            print
            K = (int(R) * 5 / 4)+ 273
            print "   K = (5/4 x",R,") + 32"
            print "     =",K
            mengulang()
        else :
            print '   Maaf Pilihan Anda Tidak Ada'
            mengulang() 

    if x in ["K", "k"]:
        x = raw_input("   Ke (C/F/R)                  : ")
        print
        if x in ["C", "c"]:
            K = raw_input("   Masukkan Derajat Kelvin     : ")
            print
            C = int(K) - 273
            print "   C =",K,'-273'
            print "     =",C
            mengulang()
        if x in ["R", "r"]:
            K = raw_input("   Masukkan Derajat Kelvin     : ")
            print
            R = (int(K) - 273) * 4 / 5
            print "   R = 4/5 * (",K,"- 273)"
            print "     =",R
            mengulang()
        if x in ["F", "f"]:
            K = raw_input("   Masukkan Derajat Kelvin     : ")
            print
            F = ((int(K) - 273) * 9 / 5) + 32
            print "   F = (9/5 * (",K,"- 273)) + 32"
            print "     =",F
            mengulang()
        else :
            print '   Maaf Pilihan Anda Tidak Ada'
        mengulang() 
        
    else :
        print '   Maaf Pilihan Anda Tidak Ada'
        mengulang()
            
menu()
