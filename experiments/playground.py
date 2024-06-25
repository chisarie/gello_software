from polymetis import RobotInterface, GripperInterface

robot = RobotInterface(
    ip_address="172.16.0.2",
)

gripper = GripperInterface(
    ip_address="localhost",
)

# example usages
gripper_state = gripper.get_state()
gripper.goto(width=0.01, speed=0.05)
gripper.grasp(speed=0.05, force=0.1)