from typing import List


class State:
    """Clasa de bază pentru stări"""

    def __init__(self, fsm):
        self.fsm = fsm
        self.numbers = fsm.numbers

    def process(self):
        """Metodă abstractă pentru procesarea stării"""
        raise NotImplementedError

    def remove_and_print(self, index):
        """Șterge și afișează elementul din listă"""
        removed = self.numbers.pop(index)
        print(f"{self.__class__.__name__}: Șters element {removed}")
        print(f"Lista actuală: {self.numbers}")


class S0State(State):
    """Starea inițială - verifică lista"""

    def process(self):
        if not self.numbers:
            print("S0: Lista este goală. Programul se termină.")
            self.fsm.running = False
        else:
            print("S0: Lista are elemente. Trecem la S1")
            self.fsm.state = self.fsm.s1


class S1State(State):
    """Starea care șterge primul element par"""

    def process(self):
        for i, num in enumerate(self.numbers):
            if num % 2 == 0:
                self.remove_and_print(i)
                print("S1: Trecem la S2")
                self.fsm.state = self.fsm.s2
                return

        print("S1: Nu s-au găsit elemente pare. Trecem la S2")
        self.fsm.state = self.fsm.s2


class S2State(State):
    """Starea care șterge primul element impar"""

    def process(self):
        for i, num in enumerate(self.numbers):
            if num % 2 != 0:
                self.remove_and_print(i)
                print("S2: Trecem la S0")
                self.fsm.state = self.fsm.s0
                return

        print("S2: Nu s-au găsit elemente impare. Trecem la S0")
        self.fsm.state = self.fsm.s0


class FiniteStateMachine:
    """Automatul finit cu 3 stări"""

    def __init__(self, numbers: List[int]):
        self.numbers = numbers.copy()
        self.running = True

        # Inițializare stări
        self.s0 = S0State(self)
        self.s1 = S1State(self)
        self.s2 = S2State(self)

        self.state = self.s0  # Starea inițială

    def run(self):
        """Rulează automatul până când lista este goală"""
        print(f"Lista inițială: {self.numbers}")
        while self.running:
            self.state.process()


# Exemplu de utilizare
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fsm = FiniteStateMachine(numbers)
    fsm.run()