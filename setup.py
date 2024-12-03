from setuptools import setup, find_packages

setup(
    name='nix',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nix=nix.cli:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
)
