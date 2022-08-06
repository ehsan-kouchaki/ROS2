from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
	package_name = 'my_robot'

	# Set the path to the package, urdf, and rviz:
	pkg_path = get_package_share_path(package_name)
	default_rviz_config_path = pkg_path / 'rviz/urdf.rviz'
	default_urdf_path = pkg_path / 'urdf/walker_nocontrol.urdf.xacro'

	# The alternative way for setting path would be:
	#pkg_path = launch_ros.substitutions.FindPackageShare(package=package_name).find(package_name)
	#default_rviz_config_path = os.path.join(pkg_path, 'rviz/rviz_basic_settings.rviz')
	#default_urdf_path = os.path.join(pkg_path, 'urdf/my_robot_1.urdf')
	
	gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
	                                description='Flag to enable joint_state_publisher_gui')
	model_arg = DeclareLaunchArgument(name='model', default_value=str(default_urdf_path),
	                                  description='Absolute path to robot urdf file')
	rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
	                                 description='Absolute path to rviz config file')
	
	robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),
                                       value_type=str)
                                       
	robot_state_publisher_node = Node(
		package='robot_state_publisher',
		executable='robot_state_publisher',
		parameters=[{'robot_description': robot_description}]
	)

	# Depending on gui parameter, either launch joint_state_publisher or joint_state_publisher_gui
	joint_state_publisher_node = Node(
		package='joint_state_publisher',
		executable='joint_state_publisher',
		condition=UnlessCondition(LaunchConfiguration('gui'))
	)
	joint_state_publisher_gui_node = Node(
		package='joint_state_publisher_gui',
		executable='joint_state_publisher_gui',
		condition=IfCondition(LaunchConfiguration('gui'))
	)

	rviz_node = Node(
		package='rviz2',
		executable='rviz2',
		name='rviz2',
		output='screen',
		arguments=['-d', LaunchConfiguration('rvizconfig')]
	)

	return LaunchDescription([
		gui_arg,
		model_arg,
		rviz_arg,
		joint_state_publisher_node,
		joint_state_publisher_gui_node,
		robot_state_publisher_node,
		rviz_node
	])

    
	   
