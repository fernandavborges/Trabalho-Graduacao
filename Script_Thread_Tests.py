import os
from subprocess import Popen, PIPE
import time

if __name__ == "__main__":
    option_test = input("Qual teste será rodado?\n 1. Teste 1 \n 3. Teste 3 \n>> ")
    if(option_test != '1' and option_test != '3'):
        print("Opção inválida!")
        exit()
    print("Será criado o banco de imagens por quartis com 10 imagens por sujeito. Para teste 1 o banco de imagens é criado com 90 sujeitos e para o teste 3 são 73 sujeitos utilizados.\n")

    start_tests = ""
    while(not start_tests.isalnum()):
        start_tests = input("Começar o teste em qual número?\n >>")

    if(int(start_tests) > 30):
        print("São necessários apenas 30 testes.")
        exit()

    tests = range(int(start_tests), 31)

    for test in tests:
        print("Teste ", test, "\n")

        print("Criando o Banco de Imagens...")
        command = ["python3", "BD_Tests.py"]
        process = Popen(command, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True, text=True)

        if(option_test == '1'):
            output, erro = process.communicate(input='1\n3\n90\n10', timeout=None)
            print(erro)
        else:
            output, erro = process.communicate(input='3\n3\n73\n10', timeout=None)
            print(erro)

        print("Rodando a Thread...")
        command = ["python3", "Thread_Tests.py"]
        process = Popen(command, stdin=PIPE, shell=True, text=True)

        time.sleep(5)
        if(option_test == '1'):
            output = process.communicate(input='1\n3\n' + str(test) + '\n1', timeout=None)
            print(output)
        else:
            output = process.communicate(input='3\n3\n' + str(test) + '\n1', timeout=None)
            print(output)

        process.wait()