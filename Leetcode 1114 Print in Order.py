# 2025/01/10
class Foo:
    def __init__(self):
        self.lock1 = True
        self.lock2 = True

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1 = False


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            if not self.lock1:
                # printSecond() outputs "second". Do not change or remove this line.
                printSecond()
                self.lock2 = False
                break

    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
        # printThird() outputs "third". Do not change or remove this line.
            if not self.lock1 and not self.lock2:
                printThird()
                break
