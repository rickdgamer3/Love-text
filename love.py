def main():
        print("  🍓 CRUSH 🍓")

        for row in range(6):
                for col in range(7):
                        if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8:
                                print('💚', end='')
                        else:
                                print(' ', end=' ')
                print()

        for a in range(10):
                for b in range(10):
                        if a==0 and b==0 or a==0 and b==5:
                                print('I', end= ' ')
                        elif a==1 and b==1 or a==1 and b==2:
                                print('LOVE', end=' ')
                        elif a==3 and b==2:
                                print('YOU',end=' ')
                        else:
                                print('  ',end=' ')
                print()

if __name__ == "__main__":
    main()
