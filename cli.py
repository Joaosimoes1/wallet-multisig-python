from keys import gerar_chave, salvar_chaves, carregar_chaves
from ecdsa import BadSignatureError
import os

def criar_e_assinar_transacao():
    destino = input("Destino da transação: ")
    valor = input("Valor da transação: ")
    mensagem = f"Enviar {valor} moedas para {destino}".encode('utf-8')

    assinaturas_validas = 0

    for i in range(3):
        nome = input(f"Nome do usuário que vai assinar ({i+1}/3 ou ENTER para pular): ")
        if nome == "":
            continue
        try:
            priv, pub = carregar_chaves(nome)
            assinatura = priv.sign(mensagem)
            pub.verify(assinatura, mensagem)
            assinaturas_validas += 1
            print(f"✔️  Assinatura de {nome} válida.")
        except (FileNotFoundError, BadSignatureError):
            print(f"❌  Assinatura de {nome} inválida ou chave não encontrada.")

    print(f"\nTotal de assinaturas válidas: {assinaturas_validas}")
    if assinaturas_validas >= 2:
        print("✅ Transação Aprovada (2 de 3 assinaram)")
    else:
        print("❌ Transação Rejeitada (assinaturas insuficientes)")

while True:
        print("\n=== Carteira Multisig (2 de 3) ===")
        print("1. Criar novo par de chaves")
        print("2. Listar chaves salvas")
        print("3. Criar e assinar transação")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do usuário (ex: user1): ")
            priv, pub = gerar_chave()
            salvar_chaves(nome, priv, pub)
            print(f"✔️  Chaves salvas como {nome}_priv.key e {nome}_pub.key.")
        
        elif escolha == "2":
            arquivos = os.listdir("storage")
            print("\nChaves encontradas:")
            for f in arquivos:
                print(" -", f)
        
        elif escolha == "3":
            criar_e_assinar_transacao()
        
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

