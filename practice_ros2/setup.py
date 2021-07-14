from setuptools import setup

package_name = 'practice_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
     py_modules = [
        'practice_ros2.hoge',
        'practice_ros2.hoge2',
        'practice_ros2.enshu',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yutabashi',
    maintainer_email='yutabashi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hoge = practice_ros2.hoge:main',
            'hoge2 = practice_ros2.hoge2:main',
            'enshu = practice_ros2.enshu:main',
        ],
    },
)
