import random
import math

import rclpy
from rclpy.node import Node

from my_messages.msg import CoordinateXY
from my_messages.srv import CalcDistance


class Hoge(Node):
    def __init__(self):
        super().__init__('hoge')

        self.pub = self.create_publisher(CoordinateXY, 'hoge')
        self.msg = CoordinateXY()
        
        timer_period = 0.25
        self.timer = self.create_timer(timer_period, self._pub_callback)

        self.srv = self.create_service(CalcDistance, 'hoge_service', self._calc_distance)


    def _pub_callback(self):
        self.msg.x, self.msg.y  = [random.randrange(10) for i in range(2)]
        
        self.pub.publish(self.msg)
        self.get_logger().info('Publish XY: ({}, {})'.format(self.msg.x, self.msg.y))

    def _calc_distance(self, req, res):
        res.distance = math.sqrt(float(req.x) ** 2 + float(req.y) ** 2)

        self.get_logger().info('distance: %f' % res.distance)
        return res
    


def main(args = None):
    rclpy.init(args=args)
    hoge = Hoge()
    rclpy.spin(hoge)
    hoge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
