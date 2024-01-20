import time


def main():
    # Mensagem de entrada
    count = input("Digite um número inteiro para iniciar a contagem regressiva: ")

    # Validação do número
    while not count.isdigit():
        print("Número digitado inválido. Por favor, digite um número inteiro: ")
        count = input("Digite um número inteiro: ")

    # Conversão do número para inteiro
    count = int(count)

    # Contagem regressiva
    while count > 0:
        print(count, end="\r", flush=True)
        time.sleep(
            0.5
        )  # Mude esse valor para alterar a velocidade da contagem de acordo com necessidade.
        count -= 1

    # Quebra de linha
    print()


if __name__ == "__main__":
    main()
