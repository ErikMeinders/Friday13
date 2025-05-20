from setuptools import setup, find_packages

with open("README_PACKAGE.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="find_repeat",
    version="0.1.0",
    author="Erik Meinders",
    author_email="erik@easytouch.nl",
    description="A utility for finding repeating patterns in sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErikMeinders/Friday13",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)