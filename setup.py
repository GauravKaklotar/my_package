from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    author="Gaurav Kaklotar",
    author_email="gauravkaklotar2003@gmail.com",
    description="A simple example Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GauravKaklotar/my_package",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
