from setuptools import setup, find_packages


setup(
    name='gol',
    packages=['gol'],
    entry_points={
        'console_scripts': [
            'gol=gol:main'
        ]
    }
)

