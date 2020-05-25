import sys

## ROS2パッケージのインポート
import rclpy
from rclpy.node import Node

## 今回使用するROS2標準搭載のservice型
from example_interfaces.srv import AddTwoInts


class MinimalClientAsync(Node):

    ## コンストラクタ
    def __init__(self):
        ## ノードの初期化
        super().__init__('minimal_client_async')

        ## clientの宣言 (service型, service名)
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        ## serviceのオブジェクトを作成
        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])

        ## 変数a, bを送信
        self.future = self.cli.call_async(self.req)


def main(args=None):
    ## rclpyの初期化
    rclpy.init(args=args)

    ## インスタンス生成, 関数実行
    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    ## ノードが実行中ならばwhileループ開始
    while rclpy.ok():
        ## ノードの処理を一回呼び出し
        rclpy.spin_once(minimal_client)
        
        ## serverからの応答があるか確認
        if minimal_client.future.done():
            ## 例外処理
            try:
                ## serverからの結果を取得
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                ## 取得した結果を表示
                minimal_client.get_logger().info(
                    'Result of add_two_ints: for %d + %d = %d' %
                    (minimal_client.req.a, minimal_client.req.b, response.sum))
            break

    ## 終了処理
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
