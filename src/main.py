import os
from matplotlib import pyplot as plt

from SofaScene import *
from SofaScene.utils._sofa_share import SOFA_SHARE_MESH


"""
This is a very simple python scene for a SOFA simulation
It prints the position of a cube's node
"""


def main():
    root = RootNode()
    root + DefaultAnimationLoop()

    share = ga.Tree(os.getenv("SOFA_ROOT")).parent / "src/share/mesh"
    cube = share / SOFA_SHARE_MESH.cube_obj

    node = root.add_child("cube")
    node + Solvers()
    node + Topology(cube, scale=20, translation=[0, 20, 0])
    node + MechanicalObject(name="cube_dof")
    node + TriangleFEMForceField(youngModulus=1e5, poissonRatio=0.3)
    node.add_visual(color="azure")

    root.print()
    sofa = RunSofa(root, BaseSOFAParams(dt=1e-2, n=10), Controller)
    sofa.run()

    print(sofa.controller.data.df)
    sofa.controller.plot()



class Controller(BaseSOFAController):
    def init(self):
        self.l = Link(self.find(name="cube_dof"), "position")

    def after_init(self):
        self.x0 = self.get(self.l)
        log.info(f"shape of MechanicalObject position t=0: {self.x0.shape}")

    def before_animate(self):
        pass

    def after_animate(self):
        self.data.add(x4=self.get(self.l)[4, 0])

    def plot(self):
        df = self.data.df
        with ga.SPlot(fname="x_pos.png"):
            fig, ax = plt.subplots()
            ga.despine(fig)
            ax.scatter(df["t"], df["x4"], marker="x", label="x[4]")
            ax.set_xlabel("time [s]")
            ax.set_ylabel("$x$ position of point 4")
            ax.legend()
            fig.tight_layout()
        x = str(ga.fTree(__file__)/'x_pos.png')
        log.info(f"Image generated to {x!r}")
        


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = ga.get_logger()

    main()
