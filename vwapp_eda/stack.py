class Stack:
    """
    Pilha de dados em python.

    O novo elemento é sempre inserido no topo da pilha, ou seja, ao final da pilha e a remoção também
    é feita no topo da pilha, ou seja, vai removendo do ultimo elemento até o primeiro elemento da pilha.

    Na pilha o primeiro elemento a ser inserido é o último a ser removido (FILO - First In Last Out)
    """

    def __init__(self):
        """
        Construtor
        """
        
        self.__stack = []
        self.__count = 0
        
    def push(self, element):
        """
        Inserir um elemento no topo pilha
        """
        
        self.__stack.append(element)
        self.__count += 1
        
    def pop(self):
        """
        Remover o elemento do topo da pilha.
        """
        
        if not self.empty:
            self.__stack.pop(self.__count -1)
            self.__count -= 1
        
    def top(self):
        """
        Pegar o ultimo elemento da pilha.
        """
        
        if not self.empty:
            return self.__stack[-1]
    
        return None
    
    @property
    def empty(self):
        """
        Verificar se a pilha ta vazia.
        """
        
        if self.__count == 0:
            return True
        
        return False
    
    @property
    def length(self):
        """
        Retorna o tamanho da pilha
        """

        return self.__count