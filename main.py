from emailVer import hibpEmailVerification

while True:

    email = input("Digite seu e-mail: ").upper()

    if "@" in email:
        if "." in email[-5:]:
            try:
                result = hibpEmailVerification(email)
                if type(result) is list:
                    print("Infelizmente encontramos evidências que seu e-mail apareceu no vazamento dos seguintes sites/aplicativos: \n")
                    for item in result:
                        print(f"{item['Name']}")
                else:
                    print(result)
            except Exception as e:
                print(f"{e}")
        else:
            print("Insira um e-mail com a finalização válida! (ex: .com/.uol/.fr")
    else:
        print("Insira um e-mail válido!")

    restart = input("\nDeseja pesquisar outro e-mail? (Digite \'S\' para continuar ou qualquer outra tecla para finalizar.) \n")

    if restart == 'S':
        pass
    else:
        break

