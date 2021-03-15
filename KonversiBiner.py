from os import system, name
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #GNU Linux,Unix dll.
    else: 
        _ = system('clear')
clear()

print("Selamat Datang di Konversi Biner. Aplikasi Ini Bisa Mengonversi Biner ke Desimal atau Sebaliknya.")
print("Dibuat Oleh Hervin FM aka QueenAgella")
print("Silahkan Pilih Opsi Dibawah\n")
print("{} {} {}".format("(1)Biner ke Desimal |", "(2)Desimal ke Biner |", "(3)Keluar\n"))
ValSelectionM=int(input("Pilih Nomor Untuk Memulai:\nUSER>>"))
if(ValSelectionM==1):
    exec(open('biner.py').read())
else:
    if(ValSelectionM==2):
        exec(open('desimal.py').read())
    else:
        if(ValSelectionM==3):
            exit()
        else:
            ##Error handler
            if(ValSelectionM>3):
                print("Nomor Tidak Ditemukan. Pilih Nomor dari Tabel.")
                exec(open('KonversiBiner.py').read())#Restart
            else:
                if(ValSelectionM<1):
                    print("Nomor Tidak Ditemukan. Pilih Nomor dari Tabel.")
                    exec(open('KonversiBiner.py').read())#Restart
            