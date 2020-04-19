import unittest
from vwapp_eda.stack import Stack


class StackTestCase(unittest.TestCase):
    """
    Casos de teste do projeto pilha.
    """

    def setUp(self):
        """
        Método executado a cada teste.
        """

        self.stack = Stack()

    def tearDown(self):
        """
        Método executado após cada teste.
        """

        pass

    def test_push(self):
        """
        Teste para o caso de sucesso!.
        """

        self.assertEqual(self.stack.length, 0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.length, 3)

if __name__ == '__main__':
    unittest.main()