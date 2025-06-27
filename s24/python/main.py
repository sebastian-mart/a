import threading
from typing import List


class State:
    """Clasa de bază pentru stări"""

    def __init__(self, fsm):
        self.fsm = fsm
        self.numbers = fsm.numbers

    def process(self):
        """Metodă abstractă pentru procesarea stării"""
        raise NotImplementedError



class S0State(State):
    """Starea inițială - verifică lista"""

    def process(self):
        self.fsm.lock.acquire()
        try:
            if not self.numbers:
                print("S0: Lista este goală. Programul se termină.")
                self.fsm.running = False
                return False
            else:
                print("S0: Lista are elemente. Trecem la S1")
                self.fsm.current_state = "s1"
                return True
        finally:
            self.fsm.lock.release()


class S1State(State):
    """Starea care șterge primul element par"""

    def process(self):
        self.fsm.lock.acquire()
        try:
            for i, num in enumerate(self.numbers):
                if num % 2 == 0:
                    removed = self.numbers.pop(i)
                    print(f"Șters element {removed}")
                    print(f"Lista actuală: {self.numbers}")
                    print("S1: Trecem la S2")
                    self.fsm.current_state = "s2"
                    return True

            print("S1: Nu s-au găsit elemente pare. Trecem la S2")
            self.fsm.current_state = "s2"
            return True
        finally:
            self.fsm.lock.release()


class S2State(State):
    """Starea care șterge primul element impar"""

    def process(self):
        self.fsm.lock.acquire()
        try:
            for i, num in enumerate(self.numbers):
                if num % 2 != 0:
                    removed = self.numbers.pop(i)
                    print(f"Șters element {removed}")
                    print(f"Lista actuală: {self.numbers}")
                    print("S2: Trecem la S0")
                    self.fsm.current_state = "s0"
                    return True

            print("S2: Nu s-au găsit elemente impare. Trecem la S0")
            self.fsm.current_state = "s0"
            return True
        finally:
            self.fsm.lock.release()


class FiniteStateMachine:
    """Automatul finit cu thread-uri dedicate pentru fiecare stare"""

    def __init__(self, numbers: List[int]):
        self.numbers = numbers.copy()
        self.running = True
        self.lock = threading.RLock()
        self.current_state = "s0"

        # Inițializare stări
        self.state0 = S0State(self)
        self.state1 = S1State(self)
        self.state2 = S2State(self)

        # Creare thread-uri dedicate pentru fiecare stare
        self.thread0 = threading.Thread(target=self.run_state, args=(self.state0,))
        self.thread1 = threading.Thread(target=self.run_state, args=(self.state1,))
        self.thread2 = threading.Thread(target=self.run_state, args=(self.state2,))

    def run_state(self, state: State):
        """Funcția executată de fiecare thread (fără with)"""
        while self.running:
            self.lock.acquire()
            try:
                should_continue = state.process()
                if not should_continue:
                    break
            finally:
                self.lock.release()


    def start(self):
        """Pornește toate thread-urile"""
        print(f"Lista inițială: {self.numbers}")
        self.thread0.start()
        self.thread1.start()
        self.thread2.start()

    def wait_for_completion(self):

        # Așteaptă terminarea thread-urilor
        self.thread0.join()
        self.thread1.join()
        self.thread2.join()

        print("Program terminat")


# Exemplu de utilizare
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fsm = FiniteStateMachine(numbers)
    fsm.start()
    fsm.wait_for_completion()