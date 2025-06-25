# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyMachina",
    version="1.0.0",
    author="Eden Simamora",
    author_email="aeden6877@gmail.com",
    description="A binary analysis toolkit for EXE, BIN, HEX, and Arduino machine code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EdenGithhub/PyMachina",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Software Development :: Debuggers",
        "Topic :: System :: Archiving :: Packaging"
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy",
        "matplotlib",
        "colorama",
        "pyfiglet",
        "hexdump",
        "rich",
        "click",
        "tqdm",
        "Pillow"
    ],
    entry_points={
        'console_scripts': [
            'pymachina=core:main',
        ],
    },
    include_package_data=True,
    zip_safe=False
)
