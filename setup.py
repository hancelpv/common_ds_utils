import pathlib
import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="common_ds_utils",
    version="1.0.0",
    description="Utilies for Data Science Projects",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hancelpv/common_ds_utils",
    author="Hancel PV",
    author_email="hancelpv@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["sklearn", "pandas", "numpy"],
    python_requires='>=3.6'
)