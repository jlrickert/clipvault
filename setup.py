import os
import re
import sys

from setuptools import find_packages, setup

min_version = (3, 6)
if sys.version_info < (3, 6):
    raise Exception("Clipvault requires Python %s,%s or higher" % min_version)

version_file = os.path.join(
    os.path.dirname(__file__), 'clipvault', '__init__.py')
with open(version_file, 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'",
        re.S
    ).match(f.read()).group(1)

readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(readme_file, 'r') as f:
    readme = f.read()

setup(
    name='clipvault',
    version=version,
    description="a more secure way to manage passwords",
    long_description=readme,
    author="Jared Rickert",
    author_email="jaredrickert52@gmail.com",
    url='https://github.com/jlrickert/clipvault/',
    include_package_data=True,
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    install_requires=[
        'keyring==10.4.0',
        'pyperclip==1.5.27',
        'rfc3987==1.3.7',
    ] + (['secretstorage==2.3.1'] if "linux" in sys.platform else []),
    entry_points={
        'console_scripts': [
            'snag = clipvault.cmd:snag',
            'vault = clipvault.cmd:vault',
        ],
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
