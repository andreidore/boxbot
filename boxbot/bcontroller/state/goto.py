
from boxbot.fsm.fsm import State, FiniteStateMachine


class GotoState(State):
    index = 0

    def enter(self):
        print("GotoState: enter")

    def exit(self):
        print("GotoState: exit")

    def update(self, fsm: FiniteStateMachine):
        print("GotoState: update")
        self.index += 1

        if self.index == 10:
            from boxbot.bcontroller.state.idle import IdleState
            fsm.transition_to(IdleState())
