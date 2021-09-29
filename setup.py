import pathlib

import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

import re

def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

project_name = 'common_ds_utils'
# This call to setup() does all the work
setup(
    name="common_ds_utils",
    version=get_property('__version__', project_name),
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
