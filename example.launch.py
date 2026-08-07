cat << 'EOF' > launch/example.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='example',
            namespace='',
            executable='listener',
            name='listener'
        ),
        Node(
            package='example',
            namespace='',
            executable='talker',
            name='talker'
        ),
    ])
EOF
