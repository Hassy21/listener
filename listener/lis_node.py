import sys
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException


from can_plugins2.msg import Frame


class Listener(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.sub = self.create_subscription(Frame, 'can_tx', self.callback, 10)

    def callback(self, frame):
        self.get_logger().info(f'Subscribe: id= {frame.id}, dlc= {frame.dlc}, data= {frame.data}')


def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.try_shutdown()