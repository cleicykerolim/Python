from random import choice
#Random éum modulo utilizado em python para gerar numeros pseudo-aleatorios.
#Ou seja, ele seleciona elementos de uma lista de forma aleatoria e exibe o
#seu resultado embaralhado........... O choice ou random.choice retorna "um" elemento
#da sequencia sorteada.

# inicialmente não temos vitorias
jogador_vitorias = 0
comp_vitorias = 0

#definindo funcao para o jogador executar em tela
def opcao_jogador():
# escolha do jogador
    esc_jogador = input("Escolha uma cor: verde, amarelo, azul ou vermelho? ")
    # verifica se a escolha do jogador está dentro da lista
    if esc_jogador in ["Verde", "VERDE", "verde"]:
        esc_jogador = "verde"
    elif esc_jogador in ["Amarelo", "AMARELO", "amarelo"]:
        esc_jogador = "amarelo"
    elif esc_jogador in ["Azul", "AZUL", "azul"]:
        esc_jogador = "azul"
    elif esc_jogador in ["Vermelho", "VERMELHO", "vermelho"]:
        esc_jogador = "vermelho"
    else:
        print("Opcao invalida. Tente novamente!")
        # chama novamente a funcao
        opcao_jogador()
    #se o jogador digitou corretamente, ele retorna o valor da funcao
    return esc_jogador

# definindo funcao para a maquina gerar aleatoriamente uma cor por rodada
def opcao_computador():
    esc_computador = choice(["verde", "amarelo", "azul", "vermelho"])
    return esc_computador

while True:

    print("--------")

    # é preciso chamar as funcoes para executa-las
    esc_computador = opcao_computador()
    esc_jogador = opcao_jogador()

    print("--------")

    # jogador sempre ganha nessa condicao
    if (esc_jogador == "verde") and (esc_computador == "verde") or (esc_jogador == "amarelo") and (esc_computador == "amarelo") or (esc_jogador == "azul") and (esc_computador == "azul") or (esc_jogador == "vermelho") and (esc_computador == "vermelho"):
        print(f"Voce escolheu {esc_jogador} e a maquina escolheu {esc_computador}. Resultado = Voce acertou :)")
        # conta o numero de vezes que o jogador ganhou
        jogador_vitorias = jogador_vitorias + 1
    else:
        print(f"Voce escolheu {esc_jogador} e a maquina escolheu {esc_computador}. Resultado = Voce errou :(")
        # conta o numero de vezes que a maquina ganhou
        comp_vitorias += 1

    print("--------")

    print(f"vitorias do jogador: {jogador_vitorias}")
    print(f"vitorias da maquina: {comp_vitorias}")

    print("--------")

    esc_jogador = input("Voce quer jogar novamente (s/n)")
    if esc_jogador in ["SIM", "Sim", "sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "Nao", "nao", "n", "N"]:
        break
    # print(f"rodadas: {esc_computador}")
    else:
        break

