'''
ノード"nakanishi_ros2"からのトピックである"topic", ノード"hoge"からのトピックである"hoge"を受け取り,
3つの値を座標と仮定し原点から3点までのユークリッド距離を求めた後, この距離情報をトピック名'enshu'としてpublishしてください

独自メッセージを作成する場合
編集するファイル→このファイル
　　　　　　　　　my_messages/CmakeLists.txt, my_messages/msgにDistance.msgファイル作成, 
std_msg.msg の Float64などを使用する場合
編集するファイル→このファイル

'''


import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from my_messages.msg import CoordinateXY, Distance


class Enshu(Node):
    def __init__(self):
        super().__init__('enshu')
        pass

        #self.sub = ***
        #self.sub = ***
        #self.pub = ***

    def _topic_callback(self, msg):
        pass
        
       
    def _hoge_distance(self, msg):
        pass




def main(args = None):
    rclpy.init(args=args)
    enshu = Enshu()
    rclpy.spin(enshu)
    enshu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()