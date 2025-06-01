from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
#    define_livox_frame = Node(
#            package = 'tf2_ros',
#            executable = 'static_transform_publisher',
#            name = 'define_livox_frame',
#            namespace = '',
#            output = 'screen',
#            arguments = [
#                '--x', '0.1012', '--y', '0', '--z', '0.177',
#                '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
#                '--frame-id', 'base_link', '--child-frame-id', 'livox_frame',
#                ],
#            )

#    define_robot_frame = Node(
#            package = 'tf2_ros',
#            executable = 'static_transform_publisher',
#            name = 'define_robot_frame',
#            namespace = '',
#            output = 'screen',
#            arguments = [
#                '--x', '0.1012', '--y', '0', '--z', '0.177',
#                '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
#                '--frame-id', 'odom', '--child-frame-id', 'base_link',
#                ],
#            )

    lidar_tf = Node(
	name='lidar_tf',
	package='tf2_ros',
	executable='static_transform_publisher',
	arguments=['0', '0', '0', '0', '0.390731', '0', '0.920505','lidar_base','lidar_link']
    )
    lidarbase_tf = Node(
	name='lidar_tf',
	package='tf2_ros',
	executable='static_transform_publisher',
	arguments=['0.2', '0.15', '0', '0', '0', '0', '0','base_link','lidar_base']

    pc2_to_scan = Node(
        package='pointcloud_to_laserscan',
        executable='pointcloud_to_laserscan_node',
        name='pointcloud_to_laserscan',
        remappings=[('cloud_in', '/livox/lidar'),
                    ('scan', '/scan')],
        parameters=[{
            'target_frame': 'lidar_base',
            'transform_tolerance': 0.01,
            'min_height': -0.5,
            'max_height': 0.1,
            'angle_min': -2.50, # -3.1415,
            'angle_max': 2.50, # 3.1415,
            'angle_increment': 0.0087,  # M_PI/360.0
            'scan_time': 0.3333,
            'range_min': 0.3,
            'range_max': 100.0,
            'use_inf': True,
            'inf_epsilon': 1.0
        }],
        output='screen',
    )

    ld = LaunchDescription()
#    ld.add_action(define_livox_frame)
#    ld.add_action(define_robot_frame)
    ld.add_action(lidar_tf)
    ld.add_action(lidarbase_tf)
    ld.add_action(pc2_to_scan)

    return ld
