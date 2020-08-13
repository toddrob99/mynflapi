import setuptools
from nflapi import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nflapi",
    version=version.VERSION,
    author="Todd Roberts",
    author_email="todd@toddrob.com",
    description="Python Wrapper for NFL API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toddrob99/nflapi",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
