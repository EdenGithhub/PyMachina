from setuptools import setup, find_packages

setup(
    name='PyMachina',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'colorama',
        'pyfiglet',
        'rich',
        'click',
        'tqdm',
        'pillow',
        'hexdump',
    ],
    python_requires='>=3.7',
    author='Adam Alcander et Eden',
    author_email="aeden6877@gmail.com"
    description='Analyze, decode, and visualize binary machine code (.exe) with colors and sockets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EdenGithhub/PyMachina',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
)
