# workshop_ros2

## Ubuntu 導入
参考サイト <br>
①Windows_VedrtualBox　https://qiita.com/pyon_kiti_jp/items/0be8ac17439abf418e48 <br>
②Windows VMware　https://qiita.com/iwa_gino/items/11aaffa9e49f2fc423d0 <br>
③Mac VMware　https://www.softantenna.com/wp/tips/ubuntu-18-04-vmware-fusion/ <br>
その他, WSLなどお好みで！ <br>

## Ubuntu 20.04にROS2(ros2-dashing) 導入
ー参照先 : https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html <br>
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

<br>
導入はおすすめしませんが、WindowsやMacの人は下のURLから <br>
https://docs.ros.org/en/foxy/Installation.html <br>
<br>
Ubuntuが18.04の人はDashingを入れるのがおすすめです <br>
https://docs.ros.org/en/dashing/Installation/Ubuntu-Install-Debians.html <br>
<br>

### 導入の確認
端末を2つ開き, それそれで以下を実行 <br>
>source /opt/ros/foxy/setup.bash <br>
>ros2 run demo_nodes_cpp talker <br>

>source /opt/ros/foxy/setup.bash <br>
>ros2 run demo_nodes_py listener <br>
<br>
それぞれの端末で <br>
[INFO] [talker]: Publishing: 'Hello World: #1' <br>
[INFO] [listener]: I heard: [Hello World: #1 <br>
みたいな感じで表示されてればたぶん大丈夫です！ <br>

## Git 導入
端末で以下の手順を実行 <br>
>sudo apt install git <br>

## ROS2導入 ーWindows or Macー (Option)
①公式_Windows　https://index.ros.org/doc/ros2/Installation/Dashing/Windows-Development-Setup/ <br>
②公式_Mac　https://index.ros.org/doc/ros2/Installation/Dashing/macOS-Install-Binary/ <br>

## Workshop

### 準備
ディレクトリ作成 <br>
>mkdir -p ~/workshop_ws/src <br>
  
もとのリポジトリと同じものを複製する <br>
>cd ~/workshop_ws/src <br>
>git clone https://github.com/yutabashi/workshop_ros2 <br>
  
ビルドに使うcolconもインストール <br>
>sudo apt install python3-colcon-common-extensions <br>
  
ビルド <br>
>colcon build <br>



### パッケージの作成
指定なし <br>
>ros2 pkg create <package_name> <br>
  
Pythonファイル作成 <br>
>ros2 pkg create --build-type ament_python <package_name> <br>
  
C++ファイル作成 <br>
>ros2 pkg create --build-type ament_cmake <package_name> <br>
  


### 「colcon build」コマンド
すべてのパッケージをビルド <br>
>colcon build <br>
  
特定のパッケージをビルド <br>
>colcon build --package-select <pakcage_name> <br>


### 「node」コマンド
起動中のNodeを確認する <br>
>ros2 node list <br>
  

### 「msg」コマンド
全メッセージファイルの確認 <br>
>ros2 msg list <br>
  
特定パッケージ内のmsg確認 <br>
>ros2 msg pakcage <package_name> <br>
  
メッセージ型の内容を確認 <br>
>ros2 msg show <msg_path/msg_name> <br>
  


### 「topic」コマンド
Nodeが利用しているTopicを表示 <br>
>ros2 topic list <br>
  
Topic内容の表示 <br>
>ros2 topic echo <Topic_name> <br>
  

### 「srv」コマンド
全サービスファイルの確認 <br>
>ros2 srv list <br>
  
特定のパッケージ内のサービスファイル確認 <br>
>ros2 srv pakcage <srv_path/srv_name> <br>
  

### rqt_graphの起動
>rqt_graph <br>
  


### workshop_task
#### step0
ROS2のアクティベート <br>
>source /opt/ros/dashing/setup.bash <br>
  
自分で作成したROS2パッケージのアクティベート <br>
>source ~/workshop_ws/install/local_setup.bash <br>
#### step1
>ros2 run python_pubsub nakanishi_ros2 <br>
>ros2 run python_pubsub itabashi_ros2 <br>

#### step2
>ros2 run cpp_pubsub talker <br>
>ros2 run python_pubsub itabashi_ros2 <br>

#### step3
>ros2 run py_srvcli client 1 2 <br>
>ros2 run py_srvcli service  <br>

#### step4
>ros2 run practice_ros2 hoge <br>
>ros2 run practice_ros2 hoge2 <br>
