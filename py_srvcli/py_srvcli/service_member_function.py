## ROS2パッケージのインポート
import rclpy
from rclpy.node import Node

## 今回使用するROS2標準搭載のservice型
from example_interfaces.srv import AddTwoInts


class MinimalService(Node):

    ## コンストラクタ
    def __init__(self):
        ## ノードの初期化
        super().__init__('minimal_service')

        ## serverの宣言 (sevice型, service名, 要求を受信した場合に実行される関数名)
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        ## 受け取ったデータの合計を計算
        response.sum = request.a + request.b
        
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        ## 返信
        return response


def main(args=None):
    ## rclpyの初期化
    rclpy.init(args=args)

    ## インスタンス生成
    minimal_service = MinimalService()

    ## プロセス終了までノード処理の繰り返し
    rclpy.spin(minimal_service)

    ## 終了処理
    minimal_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()