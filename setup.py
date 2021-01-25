# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : mao
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xt-date-utils",
    version="0.0.1",
    author="Maoxinteng",
    author_email="1214403402@qq.com",
    description="A Tool For Processing Time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mxtadmin/date-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese(Simplified)",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.7"
)
