from abc import ABC, abstractmethod

class TestABC(ABC):
    @abstractmethod
    def setup(self):
        """Метод для підготовки до тесту."""
        pass

    @abstractmethod
    def newtest(self):
        """Метод для виконання тесту."""
        pass

    @abstractmethod
    def teardown(self):
        """Метод для очищення після тесту."""
        pass

class RealTest(TestABC):
    def setup(self):
        print("Підготовка до тесту прикладу")

    def newtest(self):
        print("Виконання тесту прикладу")

    def newtest1(self):
        print("Виконання тесту прикладу")

    def teardown(self):
        print("Очищення після тесту прикладу")


RealTest().setup()
RealTest().newtest()
RealTest().newtest1()
RealTest().teardown()