import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    '''
    Launches multiple instances of the single camera launch file using
    appropriate config files and names as arguments to those launch files.

    Arguments of interest are:
        'node_name':
            Name of the wrapper node.
            (default: 'pylon_ros2_camera_node')

        'camera_id':
            Id of the camera. Used as node namespace.
            (default: 'my_camera')

        'config_file':
            Camera parameters structured in a .yaml file.
            (default: '/home/mcav/pylon_ws/install/pylon_ros2_camera_wrapper/share/pylon_ros2_camera_wrapper/config/default.yaml')
    '''

    camera_launch_descriptions = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(get_package_share_directory('pylon_ros2_camera_wrapper'), 'launch'),
                '/pylon_ros2_camera.launch.py'
            ]),
            launch_arguments={
                'node_name': 'CAM' + str(cam_num),
                'camera_id': 'CAM' + str(cam_num),
                'config_file': [
                    os.path.join(get_package_share_directory('pylon_ros2_camera_wrapper'), 'config'),
                    '/CAM' + str(cam_num) + '.yaml'
                ]
            }.items(),
        ) for cam_num in range(1,7)
    ]

    ld = LaunchDescription(camera_launch_descriptions)

    return ld