import sys
import tty
import termios

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray


class ArmTeleop(Node):

    def __init__(self):
        super().__init__('arm_teleop')

        self.publisher_ = self.create_publisher(
            Float64MultiArray,
            '/arm_controller/commands',
            10
        )

        # Starting torque
        self.torque = 40.0

        self.get_logger().info('''
========================================
        ROBOT ARM TORQUE TELEOP
========================================

Joint Controls:

1 / q  -> Joint 1 + / -
2 / w  -> Joint 2 + / -
3 / e  -> Joint 3 + / -
4 / r  -> Joint 4 + / -
5 / t  -> Joint 5 + / -
6 / y  -> Joint 6 + / -

+  -> Increase torque by 10
-  -> Decrease torque by 10

x  -> Stop all joints
c  -> Exit teleop

CTRL+C -> Force Exit

========================================
''')

    def get_key(self):

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return key

    def publish_effort(self, efforts):

        msg = Float64MultiArray()
        msg.data = efforts

        self.publisher_.publish(msg)

        print("\n--------------------------------")
        print(f"Current Torque : {self.torque}")
        print(f"Published      : {efforts}")
        print("--------------------------------")

    def run(self):

        while rclpy.ok():

            key = self.get_key()

            efforts = [0.0] * 6

            # Increase torque
            if key == '+':

                self.torque += 10.0

                print(f"\nTorque Increased -> {self.torque}")

                continue

            # Decrease torque
            elif key == '-':

                self.torque = max(0.0, self.torque - 10.0)

                print(f"\nTorque Decreased -> {self.torque}")

                continue

            # Stop all joints
            elif key == 'x':

                self.publish_effort([0.0] * 6)

                print("\nAll joints stopped")

                continue

            # Exit teleop
            elif key == 'c':

                self.publish_effort([0.0] * 6)

                print("\nExiting teleop...")

                break

            # Joint 1
            elif key == '1':
                efforts[0] = self.torque

            elif key == 'q':
                efforts[0] = -self.torque

            # Joint 2
            elif key == '2':
                efforts[1] = self.torque

            elif key == 'w':
                efforts[1] = -self.torque

            # Joint 3
            elif key == '3':
                efforts[2] = self.torque

            elif key == 'e':
                efforts[2] = -self.torque

            # Joint 4
            elif key == '4':
                efforts[3] = self.torque

            elif key == 'r':
                efforts[3] = -self.torque

            # Joint 5
            elif key == '5':
                efforts[4] = self.torque

            elif key == 't':
                efforts[4] = -self.torque

            # Joint 6
            elif key == '6':
                efforts[5] = self.torque

            elif key == 'y':
                efforts[5] = -self.torque

            else:
                continue

            self.publish_effort(efforts)


def main(args=None):

    rclpy.init(args=args)

    node = ArmTeleop()

    try:
        node.run()

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()