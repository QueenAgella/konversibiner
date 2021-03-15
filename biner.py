from os import system, name
import time
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #Linux,Unix dll.
    else: 
        _ = system('clear')
clear()
BinM= (input("Silahkan Masukkan Biner Disini:"))
numplus=0
total=0
OUBinM=[]

##Error 
if(int(BinM)<0):
    print("Ini Bukan Biner.")
    exit()

#nomor mundur
lenBin= len(BinM)
while lenBin > 0: 
    OUBinM+=BinM[ lenBin-1]
    lenBin= lenBin-1

#Kalkulasi
for number in OUBinM:
    y=2**numplus
    x=int(number)*y
    total=total+x
    numplus+=1
#Output
clear()
print("Hasil Konversi Desimalnya Adalah ")
print(total)
time.sleep(6)
exec(open('KonversiBiner.py').read())
