from setuptools import setup

setup(
    name='fyyur',
    packages=['fyyur'],
    include_package_data=True,
    install_requires=[
        'flask',
        'babel',
        'pandas',
        'python-dateutil',
        'flask-moment',
        'flask-wtf'
    ],
)
