import site
from pythreejs import Object3D, AxesHelper
import numpy as np

from tpk4170.models import ColladaMesh
from tpk4170.utils.transformations import quaternion_from_matrix

dae_path = site.USER_BASE + '/share/tpk4170/models/ur5/visual/'

class Link(Object3D):
    def __init__(self):
        Object3D.__init__(self)

    def __call__(self, trf):
        self.quaternion = quaternion_from_matrix(trf).tolist()
        self.position = (trf[:3, 3]).tolist()

class BaseLink(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'base.dae')
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link1(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'shoulder.dae')
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link2(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'upperarm.dae')
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link3(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'forearm.dae')
        self.mesh = mesh
        # mesh.rotateX(np.pi/2)
        # mesh.position = (0.39225, 0., -0.1197+0.13585)
        # mesh.rotateY(-np.pi/2)
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link4(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'wrist1.dae')
        # mesh.position = (0.0, -0.10915 + (-0.1197+0.13585), 0)
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link5(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'wrist2.dae')
        # mesh.position = (0.0, 0.09465, 0)
        # mesh.rotateX(np.pi/2)
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)


class Link6(Link):
    def __init__(self):
        Object3D.__init__(self)
        mesh = ColladaMesh(dae_path + 'wrist3.dae')
        # mesh.position = (0.0, 0.0, -0.0823)
        # mesh.rotateX(np.pi/2)
        self.mesh = mesh
        self.add(mesh)
        axes = AxesHelper(size=0.1)
        self.add(axes)
