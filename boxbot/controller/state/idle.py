import boxbot.controller.state
from boxbot.fsm.fsm import State, FiniteStateMachine


class IdleState(State):
    index = 0

    def enter(self):
        print("IdleState: enter")

    def exit(self):
        print("IdleState: exit")

    def update(self, fsm: FiniteStateMachine):
        self.index += 1

        if self.index == 10:
            fsm.transition_to(boxbot.controller.state.goto.GotoState())
