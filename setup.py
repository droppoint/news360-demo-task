"""
news360-demo-task
----------------

Реализация тестового задания для компании Ngenix.

"""
from setuptools import find_packages, setup

install_requires = [
    'click==6.7',
]


setup(
    name='news360-demo-task',
    version='1.0.0',

    description='Реализация тестового задания для компании News360',
    long_description=__doc__,

    url='https://github.com/droppoint/news360-demo-task',

    author='Aleksey Partilov',
    author_email='partilov@gmail.com',

    entry_points={
        'console_scripts': [
            'ndt = news360_demo_task.cli:main',
        ]
    },

    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
        'Private :: Do Not Upload'
    ],

    keywords='News360',
    packages=find_packages(exclude=('tests', 'tests.*')),

    install_requires=install_requires
)
