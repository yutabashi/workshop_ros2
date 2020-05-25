from setuptools import setup

package_name = 'python_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules = [
        'python_pubsub.pub_hello',
        'python_pubsub.sub_hello',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='frege',
    maintainer_email='ginmenu@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nakanishi_ros2 = python_pubsub.pub_hello:main',
            'itabashi_ros2 = python_pubsub.sub_hello:main',
        ],
    },
)
