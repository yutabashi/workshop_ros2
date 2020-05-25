## ROS2パッケージのインポート
import rclpy
from rclpy.node import Node

## 今回使用するROS2標準搭載のmsg型
from std_msgs.msg import String


class MinimalPublisher(Node):

    ## コンストラクタ
    def __init__(self):
        ## ノードの初期化
        super().__init__('minimal_publisher')

        ## publisherの宣言 (msg型, 送信するtopic名, (バッファサイズ：デフォルトは10))
        self.publisher_ = self.create_publisher(String, 'topic', 10)

        ## タイマーセット. 今回は, 0.5秒毎に "timer_callback"が呼び出されるように設定
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0

    def timer_callback(self):
        ## msgのオブジェクトを作成
        msg = String()

        ## String.msgのdata変数に値を代入
        msg.data = str(self.i)

        ## トピックを送信
        self.publisher_.publish(msg)

        ## ROS2で使用できる独自のPrint、標準出力
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    ## rclpyの初期化
    rclpy.init(args=args)

    ## インスタンス生成
    minimal_publisher = MinimalPublisher()

    ## プロセス終了まで処理の繰り返し
    rclpy.spin(minimal_publisher)

    ## 終了処理
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
