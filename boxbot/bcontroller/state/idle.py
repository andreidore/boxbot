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
            from boxbot.bcontroller.state.goto import GotoState
            fsm.transition_to(GotoState())
