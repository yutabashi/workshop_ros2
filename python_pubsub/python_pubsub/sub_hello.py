## ROS2パッケージのインポート
import rclpy
from rclpy.node import Node

## 今回使用するROS2標準搭載のmsg型
from std_msgs.msg import String


class MinimalSubscriber(Node):

    ## コンストラクタ
    def __init__(self):
        ## ノードの初期化
        super().__init__('minimal_subscriber')

        ## subscriberの宣言, (msg型, 受信するtopic名, 受信した場合に実行される関数名, (バッファサイズ：デフォルトは10))
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        ## ROS2で使用できる独自のPrint、標準出力
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    ## rclpyの初期化
    rclpy.init(args=args)

    ## インスタンス生成
    minimal_subscriber = MinimalSubscriber()

    ## プロセス終了まで処理の繰り返し
    rclpy.spin(minimal_subscriber)

    ## 終了処理
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
