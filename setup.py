import setuptools
import platform

os_type = platform.system()

# check the platform and raise an error if OS is not Linux.
if os_type != 'Linux':
    raise OSError('Error: This Package Can Only Be Installed On Linux.')

with open('README.md', 'r') as fh:
    long_desc = fh.read()

setuptools.setup(
    name='RTBot',
    version='0.0.0',
    scripts=['RadioTonight'],
    author='Mohammad Sadegh Alirezaie',
    author_email='alirezaie@sadegh.io',
    description='Radio Tonight Bot',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/AlirezaieS/RTBot',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)  ",
         "Operating System :: POSIX :: Linux",
         "Development Status :: 1 - Planning",

    ],
    install_requires=[
        'python-telegram-bot>11'
    ]
)
