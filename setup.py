#!/usr/bin/env python

# Copyright 2021 Norwegian University of Science and Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name="tpk4170",
    version="2021",
    description="Python modules for the course TPK4170 Robotics at NTNU ",
    author="Lars Tingelstad",
    author_email="lars.tingelstad@ntnu.no",
    url="",
    download_url="https://github.com/tingelst/tpk4170-robotics/archive/master.zip",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.15.0",
        "matplotlib>=3.0.0",
        "pycollada>=0.4.1",
        "pythreejs>=2.0.0",
        "jupyter-client==7.0.6",
        "sympy",
        "transformations",
        "modern_robotics",
    ],
    data_files=[
        (
            "share/tpk4170/models/ur5/visual",
            [
                "tpk4170/models/ur5/visual/base.dae",
                "tpk4170/models/ur5/visual/forearm.dae",
                "tpk4170/models/ur5/visual/shoulder.dae",
                "tpk4170/models/ur5/visual/upperarm.dae",
                "tpk4170/models/ur5/visual/wrist1.dae",
                "tpk4170/models/ur5/visual/wrist2.dae",
                "tpk4170/models/ur5/visual/wrist3.dae",
            ],
        ),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
