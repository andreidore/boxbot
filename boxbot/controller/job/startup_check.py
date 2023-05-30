import py_trees
import py_trees.console as console


class VerifyBatteryTask(py_trees.behaviour.Behaviour):
    index = 0

    def setup(self):
        # self.name = "VerifyBatteryTask"
        self.index = 0
        return True

    def initialise(self):
        console.banner("VerifyBatteryTask:  Initialising...")

    def update(self):
        console.banner("VerifyBatteryTask:  Running...")
        self.index += 1
        if self.index == 10:
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        console.banner("VerifyBatteryTask:  Terminating...")


class VerifyVisionTask(py_trees.behaviour.Behaviour):

    def setup(self) -> bool:
        self.name = "VerifyVisionTask"
        return True

    def initialise(self) -> None:
        console.banner("VerifyVisionTask:  Initialising...")

    def update(self) -> py_trees.common.Status:
        console.banner("VerifyVisionTask:  Running...")
        return py_trees.common.Status.SUCCESS

    def terminate(self, new_status):
        console.banner("VerifyVisionTask:  Terminating...")


startup_check_root = py_trees.composites.Sequence("Sequence", memory=True)

startup_check_root.add_child(VerifyBatteryTask(name="VerifyBatteryTask"))
startup_check_root.add_child(VerifyVisionTask(name="VerifyVisionTask"))

startup_check = py_trees.trees.BehaviourTree(startup_check_root)
