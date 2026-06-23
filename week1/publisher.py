import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        # 创建话题，话题名/chatter，消息类型String，队列长度10
        self.pub = self.create_publisher(String, "/chatter", 10)
        self.timer_period = 0.5
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Week1 ROS2 Message: {self.count}"
        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
