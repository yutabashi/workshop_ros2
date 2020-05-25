import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

from rclpy.executors import MultiThreadedExecutor

from my_messages.msg import CoordinateXY
from my_messages.srv import CalcDistance


class Hoge2(Node):
    def __init__(self):
        super().__init__('hoge2')

        self.sub = self.create_subscription(CoordinateXY, 'hoge', self._sub_callback)
        self.pub = self.create_publisher(Point, 'hoge2')
        self.pub2 = self.create_publisher(Point, 'hoge3')

        self.cli = self.create_client(CalcDistance, 'hoge_service')

        self.pub_msg = Point()
        self.req = CalcDistance.Request()
        self.i = 0

    def _sub_callback(self, sub_msg):
        self.pub_msg.x, self.pub_msg.y = float(sub_msg.x), float(sub_msg.y)
        
        self.pub.publish(self.pub_msg)
        self.pub2.publish(self.pub_msg)
        self.get_logger().info('Publish XY: ({}, {})'.format(self.pub_msg.x, self.pub_msg.y))

        self.i += 1
        self._calc_distance()
        
       
    def _calc_distance(self):
        if self.i % 5 == 0:
            self.req.x, self.req.y = int(self.pub_msg.x), int(self.pub_msg.y)
            self.cli.call_async(self.req)


            '''
            client側にpub/subのような同期処理がある場合, spinループ内で応答待ち処理を書くべきではない
            必要なら, spin_onceで強引に実装 or Actionのような非同期の1対1通信を使用する
            '''


def main(args = None):
    rclpy.init(args=args)
    hoge2 = Hoge2()
    rclpy.spin(hoge2)
    hoge2.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
