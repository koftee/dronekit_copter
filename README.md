# dronekit_copter
#gazebo,ardupilot ve ardupilot eklenti kurulumu kurulumu
Gazebo ubuntu kurma

Virtual box indirme
https://www.virtualbox.org/wiki/Downloads

Ubuntu iso dosyası indirme
https://ubuntu.com/download/desktop


#pip kurulumu

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-dev
sudo apt-get install python3-pip

#eğer çoklu indirme çalışmazsa paketleri tek tek indiriniz

ardupilot kurulum

sudo apt-get update
sudo apt-get install git
sudo apt-get install gitk git-gui

#üstteki 3 satır ardupilot deposunu klonlama için git kurulumu

#depo kullandı
git  clone https://github.com/ArduPilot/ardupilot

#gerekli araçların hazır script ile yüklenmesi
Tools/environment_install/install-prereqs-ubuntu.sh -y

ardupilot kurulumu bitti 

#bu paketler tek tek kurulmazsa sudo apt-get install python3-paketadı ->yazarak kurabilirsiniz
sudo apt-get install python3-dev python3-opencv python3-wxgtk3.0 python3-pip python3-matplotlib python3-pygame python3-lxml python3-yaml

#mavproxy kurma
pip install MAVProxy

#Gazebo kurulum
#ubuntu sürümğ 20.04 (Focal Fossa) ise önerilen gazebo sürümü gazebo garden

#gerekli araçların yüklenmesi
sudo apt-get update
sudo apt-get install lsb-release wget gnupg

#gazebo garden indirme
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update

sudo apt-get install gz-garden


#ardupilot gazebo kurma
sudo apt update
sudo apt install libgz-sim7-dev rapidjson-dev

#klasör oluştur ve depoyu kopyala
mkdir -p gz_ws/src && cd gz_ws/src
git clone https://github.com/ArduPilot/ardupilot_gazebo

#plugin kurma
export GZ_VERSION=harmonic
cd ardupilot_gazebo
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4

#gazeboyu configure etme
export GZ_SIM_SYSTEM_PLUGIN_PATH=$HOME/gz_ws/src/ardupilot_gazebo/build:$GZ_SIM_SYSTEM_PLUGIN_PATH
export GZ_SIM_RESOURCE_PATH=$HOME/gz_ws/src/ardupilot_gazebo/models:$HOME/gz_ws/src/ardupilot_gazebo/worlds:$GZ_SIM_RESOURCE_PATH

#garden kurulumu bitti şimdi sıra harmonicte

#pymavlink yüklemesi: MAVLink'in python için yazılmış kütüphanesidir.
pip install pymavlink

#Dronekit kurulumu. Programla yapmak için kullacağımız arayüz bu yazılımdır. Scriptlerimizi bu yazılımın özelliklerini kullanarak yazacağız.
#Hakkında ayrıntılı bilgi için burayı okuyabilirsiniz: https://dronekit-python.readthedocs.io/en/latest/about/overview.html

Kurulum:
pip install dronekit
pip3 install dronekit

#gazebo harmonic kurma
#gerekli araçlar
sudo apt-get update
sudo apt-get install lsb-release wget gnupg

#harmonici indirme

sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install gz-harmonic

#ardupilot gazebo eklentisi kurma kısmı bu kısım içinde aynı


#quadcopter çalıştırma gazebo
gz sim -v4 -r iris_runway.sdf

#ayrı bir terminalde  sitl çalıştırma
sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console
#######################################################################################################################
go.py dosyası verilen 2 konuma giden ve ardından geri dönen bir otonom gidiş kodu
