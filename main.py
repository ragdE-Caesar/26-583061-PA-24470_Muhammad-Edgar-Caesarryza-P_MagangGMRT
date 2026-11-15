import numpy as np


def forward_kinematics(
    first_joint_angle: float,
    second_joint_angle: float,
    first_link_length: float,
    second_link_length: float,
) -> tuple[float, float]:
    """Return the end-effector coordinates for a planar 2-DoF leg."""
    x = first_link_length * np.cos(first_joint_angle)
    x += second_link_length * np.cos(first_joint_angle + second_joint_angle)

    y = first_link_length * np.sin(first_joint_angle)
    y += second_link_length * np.sin(first_joint_angle + second_joint_angle)

    return x, y


def main() -> None:
    print("Forward Kinematics for a 2-DoF Robotic Leg")
    first_angle_degrees = float(
        input("Angle of the first joint (theta1) in degrees: ")
    )
    second_angle_degrees = float(
        input("Angle of the second joint (theta2) in degrees: ")
    )
    first_link_length = float(input("Length of the first link (l1): "))
    second_link_length = float(input("Length of the second link (l2): "))

    first_angle = np.radians(first_angle_degrees)
    second_angle = np.radians(second_angle_degrees)
    x, y = forward_kinematics(
        first_angle,
        second_angle,
        first_link_length,
        second_link_length,
    )

    print(f"The end effector is at position ({x:.4f}, {y:.4f})")


if __name__ == "__main__":
    main()
