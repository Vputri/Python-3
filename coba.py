def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

for i in range(11):
    print "%2d ! = %d" % (i, faktorial(i))
