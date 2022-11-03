username = 'vd'

password = '6363'

userInput = input("Masukkan Username?\n")

if userInput == username:
    a=input("Masukkan Password?\n")   
    if a == password:
        print("Selamat Datang Ini Informasi Tentang Komputermu!")
        import socket
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        print("NAMA KOMPUTER:"+hostname)
        print("IP KOMPUTER:"+IPAddr)
    else:
        print("Password dan Username SALAH.")
else:
    print("Password dan Username SALAH.")