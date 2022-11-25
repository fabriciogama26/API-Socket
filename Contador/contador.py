import threading

class Contador():
    '''
    Classe Contador
    '''

    def __init__(self, nthreads, maxcont):
        '''
        Construtor
        '''
        self._cont = 0
        self._maxcont = maxcont
        self._threadPool = []
        self._nthreads = nthreads
        self._lock = threading.Lock()

    def incremento(self):
        '''
        Método que realiza o incremento da variável _cont
        '''
        n = 0

        self._lock.acquire()
        while n < self._maxcont:
            self._cont += 1
            n += 1
        self._lock.release()
       
    def run(self):
        '''
        Método que realiza a execução das múltiplas threads
        '''
        for t in range(0,self._nthreads):
            self._threadPool.append(threading.Thread(target = self.incremento))
            self._threadPool[t].start()

        for th in self._threadPool:
            th.join()

        print(f'Resultado obtido: {self._cont} | Resultado esperado: {self._nthreads * self._maxcont}')