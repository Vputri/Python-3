def menu():
    print
    print "                               TEMPERATURE CONVERT"
    print ""
    print "======================================================================="
    print "|                                  PILIHAN :                          |"
    print "|                                                                     |"
    print "|                               1.Celcius                             |"
    print "|                               2.Fahrenheit                          |"
    print "|                               3.Reamur                              |"
    print "|                               4.Kelvin                              |"
    print "|                                                                     |"
    print "======================================================================="
    print ""
    
    x = raw_input("   Masukkan Pilihan (C/F/R/K)   : ")
    print ""
    if x in ["C", "c"]:
        C = raw_input("   Masukkan Derajat Celcius     : ")
        F = (int(C) * 9 / 5) + 32
        R = int(C) * 4 / 5
        K = int(C) + 273
        print ""
        print "   F = (9/5 x",C,") + 32"
        print "     =",F
        print ""
        print "   R = 4/5 x",C
        print "     =",R
        print ""
        print "   K =",C," + 273"
        print "     =",K
        print ""
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print ''
            print "   Maaf anda salah menginput"
            print ''
            n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
            if n in ["Y", "y"]:
                print ''
                menu()
            elif n in ["N", "n"]:
                exit()
                
    elif x in ["F", "f"]:
        F = raw_input("   Masukkan Derajat Fahrenheit  : ")
        C = (int(F) - 32) * 5 / 9
        R = (int(F) - 32) * 4 / 9
        K = ((int(F) - 32) * 5 / 9) +273
        print ""
        print "   C = 5/9 * (",F,"- 32)"
        print "     =",C
        print ""
        print "   R = 4/9 * (",F," - 32)"
        print "     =",R
        print ""
        print "   K = (5/9 * (",F," - 32)) + 273"
        print "     =",K
        print ""
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print ''
            print "   Maaf anda salah menginput"
            print ''
            n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
            if n in ["Y", "y"]:
                print ''
                menu()
            elif n in ["N", "n"]:
                exit()
                
    elif x in ["R", "r"]:
        R = raw_input("   Masukkan Derajat Reamur      : ")
        C = (int(R) * 5 / 4)
        F = (int(R) * 9 / 4) + 32
        K = (int(R) * 5 / 4)+ 273
        print ""
        print "   C = 5/4 x",R
        print "     =",C
        print ""
        print "   F = (9/4 x",R,") + 32"
        print "     =",F
        print ""
        print "   K = (5/4 x",R,") + 32"
        print "     =",K
        print ""
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print ''
            print "   Maaf anda salah menginput"
            print ''
            n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
            if n in ["Y", "y"]:
                print ''
                menu()
            elif n in ["N", "n"]:
                exit()
                
    elif x in ["K", "k"]:
        K = raw_input("   Masukkan Derajat Kelvin      : ")
        C = int(K) - 273
        R = (int(K) - 273) * 4 / 5
        F = ((int(K) - 273) * 9 / 5) + 32
        print ""
        print "    C =",K,'-273'
        print "      =",C
        print ""
        print "    R = 4/5 * (",K,"- 273)"
        print "      =",R
        print ""
        print "    F = (9/5 * (",K,"- 273)) + 32"
        print "      =",F
        print ""
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print ''
            print "   Maaf anda salah menginput"
            print ''
            n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
            if n in ["Y", "y"]:
                print ''
                menu()
            elif n in ["N", "n"]:
                exit()
                
    else:
        print "   Maaf anda salah menginput"
        print ''
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print ''
            print "   Maaf anda salah menginput"
            print ''
            n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
            if n in ["Y", "y"]:
                print ''
                menu()
            elif n in ["N", "n"]:
                exit()
            
menu()
