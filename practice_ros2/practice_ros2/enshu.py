import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from my_messages.msg import CoordinateXY, Distance


class Enshu(Node):
    def __init__(self):
        super().__init__('enshu')

        self.sub = self.create_subscription(String, 'topic', self._topic_callback)
        self.sub2 = self.create_subscription(CoordinateXY, 'hoge', self._hoge_callback)
        self.pub = self.create_publisher(Distance, 'enshu')

        self.msg = Distance()
        self.flag = False
        
    def _topic_callback(self, msg):
        if self.flag:
            self.flag = False
            self.msg.distance = math.sqrt(self.point[0] ** 2 + self.point[1] ** 2 + int(msg.data) ** 2)
            self.pub.publish(self.msg)

            self.get_logger().info('i: {} ,distance: {}'.format(msg.data, self.msg.distance))

    def _hoge_callback(self, msg):
        self.flag = True
        self.point = [msg.x, msg.y]


def main(args = None):
    rclpy.init(args=args)
    enshu = Enshu()
    rclpy.spin(enshu)
    enshu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
