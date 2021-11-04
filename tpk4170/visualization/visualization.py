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
import numpy as np
import ipywidgets
from pythreejs import Object3D
from tpk4170.visualization.viewer import Viewer
from tpk4170.models import Grid, Ball, ur5, Axes
from tpk4170.models import kr6r900sixx as kr6
from transformations import quaternion_from_euler


class Visualizer:
    def __init__(
        self,
        base_link,
        link_1,
        link_2,
        link_3,
        link_4,
        link_5,
        link_6,
        fk,
        interact=False,
    ):
        self.viewer = Viewer()
        self.grid = Grid()
        self.viewer.add(self.grid)

        self.base_link = base_link
        self.link_1 = link_1
        self.link_2 = link_2
        self.link_3 = link_3
        self.link_4 = link_4
        self.link_5 = link_5
        self.link_6 = link_6

        self.viewer.add(self.base_link)
        self.viewer.add(self.link_1)
        self.viewer.add(self.link_2)
        self.viewer.add(self.link_3)
        self.viewer.add(self.link_4)
        self.viewer.add(self.link_5)
        self.viewer.add(self.link_6)

        self._fk = fk

        if interact:
            self.interact()

        self.show(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))

    def show(self, q, show_trajectory=False):
        T01, T02, T03, T04, T05, T06 = self._fk(q)

        print(T06)
        self.link_1(T01)
        self.link_2(T02)
        self.link_3(T03)
        self.link_4(T04)
        self.link_5(T05)
        self.link_6(T06)

        if show_trajectory:
            ball = Ball(color="white", radius=0.01)
            ball.position = T06[:3, 3].tolist()
            self.viewer.add(ball)

    def interact(self):
        def f(q1, q2, q3, q4, q5, q6):
            q = np.array([q1, q2, q3, q4, q5, q6])
            self.show(q)

        ipywidgets.interact(
            f,
            q1=(np.deg2rad(-180), np.deg2rad(180)),
            q2=(np.deg2rad(-180), np.deg2rad(180)),
            q3=(np.deg2rad(-180), np.deg2rad(180)),
            q4=(np.deg2rad(-180), np.deg2rad(180)),
            q5=(np.deg2rad(-180), np.deg2rad(180)),
            q6=(np.deg2rad(-180), np.deg2rad(180)),
        )


class Kr6R900SixxVisualizer:
    def __init__(self):
        self._viewer = Viewer()
        self._grid = Grid()
        self._viewer.add(self._grid)

        base_link = kr6.BaseLink()
        link1 = kr6.Link1()
        link2 = kr6.Link2()
        link3 = kr6.Link3()
        link4 = kr6.Link4()
        link5 = kr6.Link5()
        link6 = kr6.Link6()
        ee_link = Axes(0.1)

        joint1 = Object3D()
        joint1.position = (0.0, 0.0, 0.4)
        joint2 = Object3D()
        joint2.position = (0.025, 0.0, 0.0)
        joint3 = Object3D()
        joint3.position = (0.455, 0.0, 0.0)
        joint4 = Object3D()
        joint4.position = (0.0, 0.0, 0.035)
        joint5 = Object3D()
        joint5.position = (0.42, 0.0, 0.0)
        joint6 = Object3D()
        joint6.position = (0.08, 0.0, 0.0)

        ee_joint = Object3D()

        base_link.add(joint1)
        joint1.add(link1)
        link1.add(joint2)
        joint2.add(link2)
        link2.add(joint3)
        joint3.add(link3)
        link3.add(joint4)
        joint4.add(link4)
        link4.add(joint5)
        joint5.add(link5)
        link5.add(joint6)
        joint6.add(link6)
        link6.add(ee_joint)
        ee_joint.add(ee_link)

        self._joints = [joint1, joint2, joint3, joint4, joint5, joint6]
        self._offsets = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self._axes = np.array(
            [
                [0.0, 0.0, -1.0],
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                [-1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [-1.0, 0.0, 0.0],
            ]
        )

        self.theta = np.zeros(6)

        self._robot = base_link
        self._viewer.add(self._robot)

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, theta):
        assert len(theta) == 6
        self._theta = theta
        for th, joint, offset, axes in zip(
            theta, self._joints, self._offsets, self._axes
        ):
            joint.quaternion = tuple( 
                np.roll(quaternion_from_euler(*((th + offset) * axes)), -1)
            )

    def interact(self):
        def f(q1, q2, q3, q4, q5, q6):
            q = np.array([q1, q2, q3, q4, q5, q6])
            self.theta = q

        ipywidgets.interact(
            f,
            q1=(np.deg2rad(-170), np.deg2rad(170)),
            q2=(np.deg2rad(-190), np.deg2rad(45)),
            q3=(np.deg2rad(-120), np.deg2rad(156)),
            q4=(np.deg2rad(-185), np.deg2rad(185)),
            q5=(np.deg2rad(-120), np.deg2rad(120)),
            q6=(np.deg2rad(-350), np.deg2rad(350)),
        )


class Ur5Visualizer:
    def __init__(self):
        self._viewer = Viewer()
        self._grid = Grid()
        self._viewer.add(self._grid)

        base_link = ur5.BaseLink()
        link1 = ur5.Link1()
        link2 = ur5.Link2()
        link3 = ur5.Link3()
        link4 = ur5.Link4()
        link5 = ur5.Link5()
        link6 = ur5.Link6()
        ee_link = Axes(0.1)

        joint1 = Object3D()
        joint1.position = (0.0, 0.0, 0.089159)
        joint2 = Object3D()
        joint2.position = (0.0, 0.13585, 0.0)
        joint3 = Object3D()
        joint3.position = (0.0, -0.1197, 0.425)
        joint4 = Object3D()
        joint4.position = (0.0, 0.0, 0.39225)
        joint5 = Object3D()
        joint5.position = (0.0, 0.093, 0.0)
        joint6 = Object3D()
        joint6.position = (0.0, 0.0, 0.09465)

        ee_joint = Object3D()
        ee_joint.position = (0.0, 0.0823, 0.0)
        ee_joint.rotateX(-np.pi / 2)

        base_link.add(joint1)
        joint1.add(link1)
        link1.add(joint2)
        joint2.add(link2)
        link2.add(joint3)
        joint3.add(link3)
        link3.add(joint4)
        joint4.add(link4)
        link4.add(joint5)
        joint5.add(link5)
        link5.add(joint6)
        joint6.add(link6)
        link6.add(ee_joint)
        ee_joint.add(ee_link)

        self._joints = [joint1, joint2, joint3, joint4, joint5, joint6]
        self._offsets = np.array([0.0, np.pi / 2, 0.0, np.pi / 2, 0.0, 0.0])
        self._axes = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.0, 1.0, 0.0],
            ]
        )

        self.theta = np.zeros(6)

        self._robot = base_link
        self._viewer.add(self._robot)

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, theta):
        assert len(theta) == 6
        self._theta = theta
        for th, joint, offset, axes in zip(
            theta, self._joints, self._offsets, self._axes
        ):
            joint.quaternion = tuple(
                np.roll(quaternion_from_euler(*((th + offset) * axes)), -1)
            )

    def interact(self):
        def f(q1, q2, q3, q4, q5, q6):
            q = np.array([q1, q2, q3, q4, q5, q6])
            self.theta = q

        ipywidgets.interact(
            f,
            q1=(np.deg2rad(-180), np.deg2rad(180)),
            q2=(np.deg2rad(-180), np.deg2rad(180)),
            q3=(np.deg2rad(-180), np.deg2rad(180)),
            q4=(np.deg2rad(-180), np.deg2rad(180)),
            q5=(np.deg2rad(-180), np.deg2rad(180)),
            q6=(np.deg2rad(-180), np.deg2rad(180)),
        )
