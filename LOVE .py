print("  🍓 𝑺𝑹𝑰𝑱𝑨 🍓")


for r in range(6):
    for c in range(7):
        if r==0 and c%3!=0 or r==1 and c%3==0 or r-c==2 or r+c==8:
           print('💚', end='')      
        else:
               print(" ",end=" ")
    print()

for k in range(10):
    for l in range(10):
        if k==0 and l==0 or k==0 and l==5:
            print('I', end='')
        elif k==1 and l==1 or k==1 and l==2:
            print('LOVE', end=' ')
        elif k==3 and l==2:
            print('YOU',end=' ')
        else:
            print('  ',end=" ")
    print()
    

