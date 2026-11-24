from setuptools import setup, find_packages
from glob import glob
import os

package_name = 'robo_description'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(),

    data_files=[

        # ament
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        # package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # launch
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        # urdf/xacro
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')
        ),

        # rviz
        (
            os.path.join('share', package_name, 'rviz'),
            glob('rviz/*')
        ),

        # config
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*')
        ),

        # worlds
        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*')
        ),

        # meshes
        (
            os.path.join('share', package_name, 'meshes'),
            glob('meshes/*')
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='vishwa',
    maintainer_email='vishwa@todo.todo',

    description='6DOF Robot Arm',
    license='Apache License 2.0',

    tests_require=['pytest'],

    entry_points={
        'console_scripts': [

            'teleop = robo_description.teleop:main',

        ],
    },
)   
