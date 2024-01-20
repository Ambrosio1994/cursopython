path = "c:\\Users\\diham\\Curso Python\\main\\main.txt"

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        mensagem = f'{msg} ({self.__class__.__name__})'
        with open(path, 'w') as arquivo:
            arquivo.write(mensagem)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('erro')
    lp.log_sucess('sucesso')
    lf = LogFileMixin()
    lf.log_error('erro')
    lf.log_sucess('sucesso')