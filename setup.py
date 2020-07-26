from setuptools import setup, find_packages

import os
import dhwani

VERSION = dhwani.__version__
HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="dhwani",
    version=VERSION,
    description="English to Indic language phonetic conversion engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ndyashas/Dhwani",
    license="Apache License, Version 2.0",
    author="Yashas ND",
    author_email="ndyashas@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Text Processing",
    ],
    install_requires=["PyYAML>=5.3<6"],
    packages=find_packages(),
    include_package_data=True,
    keywords=["Indic", "Phonetic", "Dhwani"],
)
