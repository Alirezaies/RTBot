import setuptools

with open('README.md', 'r') as fh:
    long_desc = fh.read()

setuptools.setup(
    name='RTBot',
    version='0.0.0',
    scripts=['app'],
    author='Mohammad Sadegh Alirezaie',
    author_email='alirezaie@sadegh.io',
    author_website='https://sadegh.io',
    description='Radio Tonight Bot',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/AlirezaieS/RTBot',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
