import sys
from pythreejs import Object3D, AxesHelper
import numpy as np

from tpk4170.models import ColladaMesh
from transformations import quaternion_from_matrix


class KR6R900sixx:
    def __init__(self):
        pass


class Link(Object3D):
    def __init__(self):
        Object3D.__init__(self)

    def __call__(self, trf):
        self.quaternion = np.roll(quaternion_from_matrix(trf), 1).tolist()
        self.position = (trf[:3, 3]).tolist()


dae_path = sys.prefix + "/share/tpk4170/models/kr6r900sixx/visual/"


class BaseLink(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + "base_link.dae", scale=0.001)
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link1(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_1.dae", scale=0.001)
        self.mesh = mesh
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link2(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_2.dae", scale=0.001)
        mesh.rotateY(np.pi/2)
        self.mesh = mesh
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link3(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_3.dae", scale=0.001)
        mesh.position = (-0.025, 0.0, 0.0)
        self.mesh = mesh
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link4(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_4.dae", scale=0.001)
        self.mesh = mesh
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link5(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_5.dae", scale=0.001)
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)


class Link6(Link):
    def __init__(self):
        Link.__init__(self)
        mesh = ColladaMesh(dae_path + "link_6.dae", scale=0.001)
        self.mesh = mesh
        self.add(mesh)
        # axes = AxesHelper(size=0.1)
        # self.add(axes)
