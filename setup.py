from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='facilyst',
    version='0.0.1',
    author='Parthiv Naresh',
    author_email='pppn95@gmail.com',
    description='facilyst is a library that aggregates functions and utilities commonly used in the course of data science and machine learning to facilitate ease of access.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ParthivNaresh/facilyst/',
    python_requires='>=3.8, <4',
    install_requires=open('requirements.txt').readlines(),
    tests_require=open('test-requirements.txt').readlines(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'facilyst = facilyst.__main__:cli'
        ]
    },
)
