from setuptools import setup, find_packages

setup(
    name='filexl',
    version='1.0.2',
    description='CLI tool to list files and export to Excel',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author='Kiarash Gharahgozloo',
    author_email='kiarash.gh@gmail.com',
    url='https://github.com/kiarash-gh/filexl',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'filexl = filexl.cli:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
