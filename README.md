# workshop_ros2

## Ubuntu18.04 導入
参考サイト <br>
①Windows_VedrtualBox　https://qiita.com/pyon_kiti_jp/items/0be8ac17439abf418e48 <br>
②Windows VMware　https://qiita.com/iwa_gino/items/11aaffa9e49f2fc423d0 <br>
③Mac VMware　https://www.softantenna.com/wp/tips/ubuntu-18-04-vmware-fusion/ <br>
その他, WSLなどお好みで！ <br>

## ROS2(ros2-dashing) 導入
ー参照 : https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/ <br>
端末で以下の手順を実行 <br>
>sudo locale-gen en_US en_US.UTF-8 <br>
>sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 <br>
>export LANG=en_US.UTF-8 <br>
>sudo apt-get update && sudo apt-get install curl gnupg2 lsb-release <br>
>curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add - <br>
>sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' <br>
>sudo apt-get update <br>
>sudo apt-get install ros-dashing-desktop <br>
>sudo apt install python3-argcomplete <br>
>source /opt/ros/dashing/setup.bash <br>
>echo "source /opt/ros/dashing/setup.bash" >> ~/.bashrc <br>
>source ~/.bashrc <br>
>sudo apt install python3-colcon-common-extensions

### 導入の確認
端末を2つ開き, それそれで以下を実行 <br>
>ros2 run demo_nodes_cpp talker <br>
>ros2 run demo_nodes_py listener <br>
<br>
それぞれの端末で <br>
[INFO] [talker]: Publishing: 'Hello World: #' <br>
[INFO] [listener]: I heard: [Hello World: #] <br>
みたいな感じで表示されてればたぶん大丈夫です！ <br>

## Git 導入
端末で以下の手順を実行 <br>
>sudo apt-get install git <br>

## ROS2導入 ーWindows or Macー (Option)
①公式_Windows　https://index.ros.org/doc/ros2/Installation/Dashing/Windows-Development-Setup/ <br>
②公式_Mac　https://index.ros.org/doc/ros2/Installation/Dashing/macOS-Install-Binary/ <br>
