from setuptools import setup
from mynumber import __version__
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='mynumber',
    version=__version__,
    description="'My Number' validate module",
    long_description=long_description,
    author='haminiku',
    author_email='haminiku1129@gmail.com',
    url='https://github.com/subc/mynumber',
    packages=['mynumber'],
    package_dir={'mynumber': 'mynumber'},
    include_package_data=True,
    install_requires=[],
    license='MIT License',
    zip_safe=False,
    keywords=["'My Number'", "Japan", "My Number system", "mynumber"],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
