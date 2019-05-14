#Cetak top dan stack
print_stack = []
output = []

def infixToPostfix(infixexpr):
    # menyimpan nilai tingkatan operator di dictionari python
    tingkatan_operator = {
        "^":4,
        "*":3,
        "/":3,
        "+":2,
        "-":2,
        "(":1
    }
    
    # inisialisasi stack kosong
    operator_stack = []

    huruf = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    angka = "0123456789"
    operator = "+-/*^"

    def stack():
        stack2 = []
        for i in operator_stack:
            stack2.append(i)
        print_stack.append(stack2)

    #looping token pada infix inputan yang telah ubah menjadi list token
    for token in infixexpr:

        #Jika token alfabet atau angka maka token akan dimasukkan ke postfixlist
        if token in huruf or token in angka:
            output.append(token)
            stack()

        #Jika token = ( maka akan dimasukkan ke operator_stack
        elif token == '(':
            operator_stack.append(token)
            output.append("")
            stack()

        
        elif token in operator:
            if (len(operator_stack)==0 ) or (tingkatan_operator[token] > tingkatan_operator[operator_stack[-1]]):
                operator_stack.append(token)
                output.append("")
                stack()

            elif (tingkatan_operator[operator_stack[-1]] >= tingkatan_operator[token]):
                output.append(operator_stack.pop())
                operator_stack.append(token)
                stack()
                    
        #Jika token = ) maka operator_stack yang ada di dalam operator stack akan di dikeluarkan semua sampe ketemu ( dan akan dimasukkan ke postfixlist
        elif token == ')':
            topToken = operator_stack.pop()
            while topToken != '(':
                output.append(topToken)
                topToken = operator_stack.pop()
            else:
                topToken
            stack()


       #Jika token = ; maka operator_stack yang ada di dalam operator stack akan di dikeluarkan semua kecuali )
        elif token == ';':
            topToken = operator_stack.pop()
            if token != ')':
                output.append(topToken)
                stack()
                
        #jika operator_stack tdk kosong dan tingkatan operator yang paling terakhir didlm operator stack derajatnya >= tingkatan operator yang dicek
        # maka akan dimasukkan ke dalam postfix dan juga akan dikeluarkan dari operator stack sampe operator stack kosong
        # setelah operator_stack kosong maka token operator saat ini akan dimasukkan ke output
        else:
            while (len(operator_stack)!=0 ) and (tingkatan_operator[operator_stack[-1]] >= tingkatan_operator[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
            stack()
            
    # untuk isi operator_stack tdk kosong maka akan dimasukkan ke dalam postfix dan juga akan dikeluarkan dari operator stack sampe operator stack kosong
    while (len(operator_stack)!=0 ):
        output.append(operator_stack.pop())
        stack()

    # menggabungkan output menjadi string
    return "".join(output)

print '                PROGRAM INFIX KE POSTFIX'
print

def menu():
    #menginput notasi infix
    infix1 = (raw_input('   Masukkan notasi infix : '))
    print
    
    #mengubah notasi infix menjadi list dan membuang spasi
    infix = list(infix1.replace(" ", ""))

    # megubah infix menjadi postfix
    postfix = infixToPostfix(infix)
    print "   Postfix dari ",infix1," adalah ",postfix
    print
    
    # print
    # print "top   :",
    # for i in print_top:
    #     print "| "+i+" |",
    n=0
    m=-1
    b=0
    st = ["   Diamati:","   Top    :","   Stack  :","   Output :"]
    print st[0],
    for i in infix1:
        print i+" |",
    print "\n"
    print st[1],
    while b < len(print_stack)-1:
        try:
            print print_stack[b][m]+" |",
        except IndexError:
            print "  |",
        b+=1
    b=0
    m=-2
    max_len = max([len(i) for i in print_stack])
    print "\n"
    print st[2],
    while b < len(print_stack) and m * -1 <= max_len:
        if n <= len(print_stack)-2:
            try:
                print print_stack[b][m]+" |",
            except IndexError:
                print "  |",
            n+=1
            b+=1
        else:
            b=0
            n=0
            m-=1
            print "\n",
            print " "*len(st[2]),
    print "\n"+st[3],
    for i in output:
        if len(i) == 0:
            print "  |",
        else:
            print i+" |",
    print
    del print_stack[:]
    del output[:]
    
    def ulang():
        n = raw_input("\n   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
        else:
            print "\n   Maaf Anda Salah Input"
            ulang()
    ulang()
menu()
