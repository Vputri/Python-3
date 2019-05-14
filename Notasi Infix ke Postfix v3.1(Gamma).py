def infixToPostfix(infixexpr):
    tingkatan_operator = {
        "^":4,
        "*":3,
        "/":3,
        "+":2,
        "-":2,
        "(":1
    }

    huruf = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    angka = "0123456789"
    operator = "+-/*^"

    operator_stack = []
    operator_stack1 = []
    operator_stack2 = []
    top_stack = []
    postfix_list = []

    def stack():
        print ("    Top     : ",top_stack)
        print ("    Stack   : ",operator_stack1)
        print ("    Stack   : ",operator_stack2)
        print ("    Output  : ",postfix_list)
        print ()

    for token in infixexpr:
          
        if token == "(":
            operator_stack.append(token)
            postfix_list.append(" ")
            top_stack.append(operator_stack[-1])
            if len(operator_stack) > 1:
                operator_stack1.append(operator_stack[-2])
            else :
                operator_stack1.append(" ")
            if len(operator_stack) > 2:
                operator_stack2.append(operator_stack[-3])
            else :
                operator_stack2.append(" ")
                
        elif token in huruf or token in angka:
            postfix_list.append(token)
            top_stack.append(operator_stack[-1])
            if len(operator_stack) > 1:
                operator_stack1.append(operator_stack[-2])
            else :
                operator_stack1.append(" ")
            if len(operator_stack) > 2:
                operator_stack2.append(operator_stack[-3])
            else :
                operator_stack2.append(" ")
                
        elif token in operator:
            if (len(operator_stack) == 0) or (tingkatan_operator[token] > tingkatan_operator[operator_stack[-1]]):
                operator_stack.append(token)
                postfix_list.append(" ")
                if len(operator_stack) != 0:
                    top_stack.append(operator_stack[-1])
                else :
                    top_stack = []
                if len(operator_stack) > 1:
                    operator_stack1.append(operator_stack[-2])
                else :
                    operator_stack1.append(" ")
                if len(operator_stack) > 2:
                    operator_stack2.append(operator_stack[-3])
                else :
                    operator_stack2.append(" ")
                
            elif (len(operator_stack) > 1) and (tingkatan_operator[token] <= tingkatan_operator[operator_stack[-1]]):
                postfix_list.append(operator_stack.pop())
                operator_stack.append(token)
                if len(operator_stack) != 0:
                    top_stack.append(operator_stack[-1])
                else :
                    top_stack = []
                if len(operator_stack) > 1:
                    operator_stack1.append(operator_stack[-2])
                else :
                    operator_stack1.append(" ")
                if len(operator_stack) > 2:
                    operator_stack2.append(operator_stack[-3])
                else :
                    operator_stack2.append(" ")
                    
        elif token == ")":
            topToken = operator_stack.pop()
            while topToken != "(":
                postfix_list.append(topToken)
                topToken = operator_stack.pop()
            if len(operator_stack) != 0:
                top_stack.append(operator_stack[-1])
            else :
                top_stack.append(" ")
            if len(operator_stack) > 1:
                operator_stack1.append(operator_stack[-2])
            else :
                operator_stack1.append(" ")
            if len(operator_stack) > 2:
                operator_stack2.append(operator_stack[-3])
            else :
                operator_stack2.append(" ")
                
        elif token == ";":
            topToken = operator_stack.pop()
            if token != ')':
                postfix_list.append(topToken)
            if len(operator_stack) > 1:
                operator_stack1.append(operator_stack[-2])
            else :
                operator_stack1.append(" ")
            
        else :
            while (len(operator_stack)!=0 ) and (tingkatan_operator[operator_stack[-1]] >= tingkatan_operator[token]):
                  postfix_list.append(operator_stack.pop())
            operator_stack.append(token)

    while (len(operator_stack)!=0 ):
        postfix_list.append(operator_stack.pop())
        
    stack()
    return "".join(postfix_list)

print ("                          |------------------------|")
print ("                          |PROGRAM INFIX KE POSTFIX|")
print ("                          |------------------------|")
print ()

def menu():
    penutup = ";"
    infix1 = (input("    Masukan Notasi infix : "))
    print()
    
    infix = list(infix1.replace(" ",""))
    print ("    Diamati : ",infix)
    
    Postfix = infixToPostfix(infix)
    "".join(Postfix)
    print("    Postfix dari",infix1,"Adalah",Postfix)
    print()
    n = input("    Apakah anda ingin memilih lagi(Y/N): ")
    if n in ["Y","y"]:
        print()
        menu()
    elif n in ["N","n"]:
        exit()

menu()
