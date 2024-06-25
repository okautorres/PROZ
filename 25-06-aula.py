def inicio():
    
    resp = "SIM"
    while(resp.upper() == "SIM"):
        
        print("Escolha a opção: \n")
        print("1 - Quantidade de caracteres")
        print("2 - Quantidade de palavras ")
        print("0 - Sair \n")
        
        liberado = False
        
        while(not liberado):
            opcao = int(input())
            if opcao == 1:
                print("Digite a palavra: ")
                palavra = input()
                nospace = palavra.replace(" ", "")
                caracteres(nospace)
                resp = input("Deseja continuar ? Se sim, digite (sim)")
                break
            elif opcao == 2:
                print("Digite as palavras: ")
                palavras = input()
                qtpalavras(palavras)
                resp = input("Deseja continuar ? Se sim, digite (sim)")
                break
            elif opcao == 0:
                print("Fechando sistema")
                exit()
    
def caracteres(palavra):
   print("A quantidade de caracteres é:" + str(len(palavra)))
   
def qtpalavras(palavras):
    qt = palavras.split()
    print("A quantidade de palavras é:" + str(len(qt)))

inicio()