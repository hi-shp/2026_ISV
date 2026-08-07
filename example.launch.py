cd example
mkdir launch
cat << 'EOF' > launch/example.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_pubsub',
            namespace='',
            executable='listener',
            name='listener'
        ),
        Node(
            package='py_pubsub',
            namespace='',
            executable='talker',
            name='talker'
        ),
    ])
EOF
