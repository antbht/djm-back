from setuptools import setup, find_packages

import djm_back

setup(
    name=djm_back.__package__,
    version=djm_back.__version__,
    description=('Dejamobile Take Home - Backend API'),
    author='Antoine BUHOT',
    author_mail='buhot.a@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['unit_tests',]),
    install_requires=[
        "falcon>=2.0.0",
        "gunicorn>=20.0.4",
        "requests>=2.24.0"
    ],
    entry_points={
        'console_scripts': [
            'djm-back = djm_back.__main__:main'
        ]
    }
)