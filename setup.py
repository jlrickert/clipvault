import os
import re
import sys

from setuptools import find_packages, setup

min_version = (3, 6)
if sys.version_info < (3, 6):
    raise Exception("Siam requires Python %s,%s or higher" % min_version)

version_file = os.path.join(os.path.dirname(__file__), 'snagvault', '__init__.py')
with open(version_file, 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'",
        re.S
    ).match(f.read()).group(1)

readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(readme_file, 'r') as f:
    readme = f.read()

setup(
    name='snagvault',
    version=version,
    description="a more secure way to manage passwords",
    long_description=readme,
    author="Jared Rickert",
    author_email="jaredrickert52@gmail.com",
    url='https://github.com/jlrickert/snagvault/',
    include_package_data=True,
    packages=find_packages('snagvault'),
    package_dir={'': 'snagvault'},
    setup_requires=['pytest-runner'],
    install_requires=[
        'keyring==10.4.0',
        'secretstorage==2.3.1',
    ],
    entry_points={
        'console_scripts': ['snag = snagvault.__main__:main'],
    },
    tests_require=['pytest>=2.5.2'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database :: Front-Ends",
        "Operating System :: OS Independent",
    ],
    platforms='any',
    zip_safe=False)
