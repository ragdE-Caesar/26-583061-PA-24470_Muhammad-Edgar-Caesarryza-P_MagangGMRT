import numpy as np
import matplotlib.pyplot as plt


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


def inverse_kinematics(
    x: float,
    y: float,
    first_link_length: float,
    second_link_length: float,
) -> tuple[float, float]:
    """Return one valid joint-angle solution for a planar 2-DoF leg."""
    if first_link_length <= 0 or second_link_length <= 0:
        raise ValueError("Link lengths must be greater than zero.")

    distance = np.sqrt(x**2 + y**2)
    minimum_reach = abs(first_link_length - second_link_length)
    maximum_reach = first_link_length + second_link_length
    if not minimum_reach <= distance <= maximum_reach:
        raise ValueError("The target position is unreachable.")

    cos_angle2 = (
        x**2 + y**2 - first_link_length**2 - second_link_length**2
    ) / (2 * first_link_length * second_link_length)
    angle2 = np.arccos(np.clip(cos_angle2, -1.0, 1.0))

    k1 = first_link_length + second_link_length * np.cos(angle2)
    k2 = second_link_length * np.sin(angle2)
    angle1 = np.arctan2(y, x) - np.arctan2(k2, k1)

    return angle1, angle2


def plot_robot_leg(
    first_joint_angle: float,
    second_joint_angle: float,
    first_link_length: float,
    second_link_length: float,
) -> None:
    """Plot the two links and their joints in the XY plane."""
    first_joint_x = first_link_length * np.cos(first_joint_angle)
    first_joint_y = first_link_length * np.sin(first_joint_angle)
    end_effector_x, end_effector_y = forward_kinematics(
        first_joint_angle,
        second_joint_angle,
        first_link_length,
        second_link_length,
    )

    plt.plot(
        [0, first_joint_x],
        [0, first_joint_y],
        "o-",
        label="Femur",
    )
    plt.plot(
        [first_joint_x, end_effector_x],
        [first_joint_y, end_effector_y],
        "o-",
        label="Tibia",
    )
    plt.scatter(end_effector_x, end_effector_y, marker="x", label="End-effector")
    plt.title("2-DoF Robotic Leg Forward Kinematics")
    plt.xlabel("X Position (cm)")
    plt.ylabel("Y Position (cm)")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


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
    plot_robot_leg(
        first_angle,
        second_angle,
        first_link_length,
        second_link_length,
    )


if __name__ == "__main__":
    main()
