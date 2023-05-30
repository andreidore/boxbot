from typing import Optional


class State:

    def __init__(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, fsm: Optional["FiniteStateMachine"]):
        pass


class FiniteStateMachine:
    def __init__(self, init_state: State):

        print("Init FSM")
        self.current_state = init_state
        self.new_state = None
        self.needToTrigger = True

    def update(self):

        if self.needToTrigger:
            self.current_state.enter()
            self.needToTrigger = False

        if self.new_state is not None:
            self.current_state.exit()
            self.current_state = self.new_state
            self.current_state.enter()
            self.new_state = None

        self.current_state.update(self)

    def transition_to(self, new_state: State):
        self.new_state = new_state
