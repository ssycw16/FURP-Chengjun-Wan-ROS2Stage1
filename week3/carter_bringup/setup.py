from glob import glob
import os

from setuptools import setup

package_name = 'carter_bringup'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml')),
        (os.path.join('share', package_name, 'urdf'),
         glob('urdf/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Carter differential drive bringup and control lab',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'square_trajectory = carter_bringup.square_trajectory:main',
            'rotate_in_place = carter_bringup.rotate_in_place:main',
            'cmd_vel_watchdog = carter_bringup.cmd_vel_watchdog:main',
            'check_odom_tf = carter_bringup.check_odom_tf:main',
        ],
    },
)
