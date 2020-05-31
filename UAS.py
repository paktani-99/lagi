print('Selamat datang di jasa pengitiman paket ANUGRAH','\n')
berat_paket= int(input('berapa berat paket(dlm km): '))
jarak= int(input('berapa jarak pengiriman: '))
durasi_kirim=int(input('berapa lama paket sampai: '))
 
#perhitunganberat 1
if berat_paket == 1:
    if jarak < 25:
        if durasi_kirim <= 1 :
            biaya = 15000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 12000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 8000
            print('biaya ongkir = Rp ',biaya )
    elif jarak < 50:
        if durasi_kirim <= 1 :
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 23000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 19000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 15000
            print('biaya ongkir = Rp ',biaya )
    elif jarak < 150:
        if durasi_kirim <= 1 :
            biaya = 35000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 25000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 20000
            print('biaya ongkir = Rp ',biaya )
    
    elif jarak < 350:
        if durasi_kirim <3:
            biaya = 40000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
#berat2
elif berat_paket > 1:
    if jarak < 25:
        if durasi_kirim <= 1 :
            biaya = 15000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 12000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 8000
            print('biaya ongkir = Rp ',biaya )
    elif jarak < 50:
        if durasi_kirim <= 1 :
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 23000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 19000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 15000
            print('biaya ongkir = Rp ',biaya )
    elif jarak < 150:
        if durasi_kirim <= 1 :
            biaya = 35000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 25000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 20000
            print('biaya ongkir = Rp ',biaya )
    elif jarak < 350:
        if durasi_kirim <3:
            biaya = 40000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <5:
            biaya = 30000
            print('biaya ongkir = Rp ',biaya )
    print ('Rp',int(biaya*1.5))
            
elif berat_paket > 1:
    if jarak < 50:
        if durasi_kirim <= 1 :
            biaya = 33000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <2:
            biaya = 26000
            print('biaya ongkir = Rp ',biaya )
        elif durasi_kirim <3:
            biaya = 20000
            print('biaya ongkir = Rp ',biaya )
    
    

