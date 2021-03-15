from os import system, name
import time
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #GNU Linux,Unix dll.
    else: 
        _ = system('clear')
clear()
num=input("Silahkan Masukkan Desimal Disini:")
bin=0
divisionControl=int(num)

total= []
##Error 
if(int(num)<0):
    print("Ini Bukan Angka Positif.\n")

#kalkulasi
for i in range(1,99):
    bin = int(divisionControl)%2
    divisionControl = int(divisionControl)//2
    if(int(divisionControl)==0):
        break
    total.append(str(bin))

total.reverse()
#Output
clear()
print("Input Desimalnya Adalah ", num)
print("Hasil Binernya Adalah")
print("1",end="",sep="")
for i in total:
    print(str(i),sep="",end="")
print()
time.sleep(6)
exec(open('KonversiBiner.py').read())