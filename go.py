import time
import math
from dronekit import connect,VehicleMode,LocationGlobalRelative

cs = "127.0.0.1:14550"
iha = connect(cs,wait_ready=True)

def arm_yuksel(hedef_yukseklik):
    while iha.is_armable == False:
        print("Gerekli şartlar sağlanmadı")
        time.sleep(1)
    print("İha şuanda arm edilebilir")
    iha.mode = VehicleMode("GUIDED")
    while iha.mode != 'GUIDED':
        print("GUIDED moda geçiş yapılıyor")
        time.sleep(1.5)
    print("GUIDED moduna geçildi")
    iha.armed = True
    while iha.armed == False:
        print("İha arm olması bekleniyor")
        time.sleep(1)
    print("İha arm olmuştur")

    iha.simple_takeoff(hedef_yukseklik)

    while iha.location.global_relative_frame.alt <= hedef_yukseklik * 0.94:
        print(f"Şuanki yükseklik {iha.location.global_relative_frame.alt}")
        time.sleep(0.5)

    print("İstenen yüksekliğe erişildi")
arm_yuksel(15)

p1 = LocationGlobalRelative(-35.36228158, 149.16340157,20)
p2 = LocationGlobalRelative(-35.36115344,149.16477199,20)

iha_konum = iha.location.global_relative_frame

def distanceto(kiha,kp):
    distance_lat=kiha.lat - kp.lat
    distance_long=kiha.lon - kp.lon
    dst = math.sqrt((distance_lat*distance_lat) + (distance_long*distance_long)) * 1.113195e5
    return dst
dst1 = distanceto(iha_konum,p1)
iha.simple_goto(p1)

while dst1 >= 0.5:
    iha_konum = iha.location.global_relative_frame
    dst1 = distanceto(iha_konum,p1)
    print(f"nokta 1 e gidiyorum. Kalan mesaafe {dst1} iha konum: {iha_konum} nokta1 {p1}")
    time.sleep(2)

dst2 = distanceto(iha_konum,p2)
iha.simple_goto(p2)

while dst2 >= 0.5:
    dst2 = distanceto(iha_konum,p2)
    iha_konum = iha.location.global_relative_frame
    print(f"nokta 2 ye gidiyorum. Kalan mesafe {dst2} iha konum {iha_konum} nokta2 {p2}")
    time.sleep(2)
homeloc = iha.home_location

dst3 = distanceto(iha_konum,homeloc)
iha.mode = VehicleMode("RTL")
while dst3 >=0.5:
    iha_konum = iha.location.global_relative_frame
    dst3 = distanceto(iha_konum,homeloc)
    print("eve gidiyorum")
    time.sleep(2)

iha.mode = VehicleMode("RTL")
print("ev deyim")

while iha_konum.alt != 0:
    print("iniyorum")
    time.sleep(2)
iha.mode = vehicleMode("LAND")
print("indim")
