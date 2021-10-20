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
import sys

import numpy as np
from pythreejs import AxesHelper, Object3D
from tpk4170.models import ColladaMesh
from transformations import quaternion_from_matrix

_DAE_PATH = sys.prefix + "/share/tpk4170/models/ur5/visual/"


class Link(Object3D):
    def __init__(self):
        Object3D.__init__(self)

    def __call__(self, trf):
        self.quaternion = np.roll(quaternion_from_matrix(trf), 1).tolist()
        self.position = (trf[:3, 3]).tolist()


class BaseLink(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "base.dae")
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link1(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "shoulder.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link2(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "upperarm.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link3(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "forearm.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link4(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "wrist1.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link5(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "wrist2.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link6(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(_DAE_PATH + "wrist3.dae")
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)
