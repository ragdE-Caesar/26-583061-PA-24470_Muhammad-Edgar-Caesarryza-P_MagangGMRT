import numpy as np
import matplotlib.pyplot as plt


def forward_kinematics(
    hip_yaw_angle: float,
    femur_pitch_angle: float,
    tibia_pitch_angle: float,
    first_link_length: float,
    second_link_length: float,
) -> tuple[float, float, float]:
    """Return the 3D end-effector coordinates of a two-link robotic leg."""
    if first_link_length <= 0 or second_link_length <= 0:
        raise ValueError("Link lengths must be greater than zero.")

    femur_x = first_link_length * np.cos(femur_pitch_angle)
    tibia_angle = femur_pitch_angle + tibia_pitch_angle
    radial_reach = femur_x + second_link_length * np.cos(tibia_angle)
    z = (
        first_link_length * np.sin(femur_pitch_angle)
        + second_link_length * np.sin(tibia_angle)
    )
    x = radial_reach * np.cos(hip_yaw_angle)
    y = radial_reach * np.sin(hip_yaw_angle)

    return x, y, z


def plot_robot_leg(
    hip_yaw_angle: float,
    femur_pitch_angle: float,
    tibia_pitch_angle: float,
    first_link_length: float,
    second_link_length: float,
) -> None:
    """Plot the hip, knee, and end-effector in 3D space."""
    knee_radial = first_link_length * np.cos(femur_pitch_angle)
    knee_x = knee_radial * np.cos(hip_yaw_angle)
    knee_y = knee_radial * np.sin(hip_yaw_angle)
    knee_z = first_link_length * np.sin(femur_pitch_angle)
    end_effector_x, end_effector_y, end_effector_z = forward_kinematics(
        hip_yaw_angle,
        femur_pitch_angle,
        tibia_pitch_angle,
        first_link_length,
        second_link_length,
    )

    figure = plt.figure()
    axis = figure.add_subplot(111, projection="3d")
    axis.plot(
        [0, knee_x],
        [0, knee_y],
        [0, knee_z],
        "o-",
        linewidth=3,
        label="Femur",
    )
    axis.plot(
        [knee_x, end_effector_x],
        [knee_y, end_effector_y],
        [knee_z, end_effector_z],
        "o-",
        linewidth=3,
        label="Tibia",
    )
    axis.scatter(
        end_effector_x,
        end_effector_y,
        end_effector_z,
        marker="x",
        s=80,
        label="End-effector",
    )
    axis.scatter(0, 0, 0, marker="o", s=60, color="black", label="Hip")
    axis.set_title("3D Robotic Leg Forward Kinematics")
    axis.set_xlabel("X (cm)")
    axis.set_ylabel("Y (cm)")
    axis.set_zlabel("Z (cm)")
    axis.grid(True)
    axis.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    print("3D Robotic Leg Forward Kinematics")
    first_link_length = float(input("Length of the first link (l1): "))
    second_link_length = float(input("Length of the second link (l2): "))
    if first_link_length <= 0 or second_link_length <= 0:
        print("Link lengths must be greater than zero.")
        return

    hip_yaw_angle = float(input("Hip yaw angle (theta1) in radians: "))
    femur_pitch_angle = float(input("Femur pitch angle (theta2) in radians: "))
    tibia_pitch_angle = float(input("Tibia pitch angle (theta3) in radians: "))

    x, y, z = forward_kinematics(
        hip_yaw_angle,
        femur_pitch_angle,
        tibia_pitch_angle,
        first_link_length,
        second_link_length,
    )

    print(f"The end effector is at position ({x:.4f}, {y:.4f}, {z:.4f}) cm")
    plot_robot_leg(
        hip_yaw_angle,
        femur_pitch_angle,
        tibia_pitch_angle,
        first_link_length,
        second_link_length,
    )


if __name__ == "__main__":
    main()
