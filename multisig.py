from keys import gerar_chave, salvar_chaves_em_hex
import hashlib

chaves_publicas = []
chaves_privadas = []

# Gerar as 3 chaves para cada utilizador
for i in range(3):
    priv, pub = gerar_chave()

    chaves_publicas.append(pub)
    chaves_privadas.append(priv)

    print(f"Utilizador {i+1}")

    print("Privada: ", priv.to_string().hex())
    print("Pública: ", pub.to_string().hex())
    print("")

def criar_transacao(destino, valor):
    mensagem = f"Enviar {valor} moedas para {destino}"
    return mensagem.encode('utf-8')  # precisamos de bytes para assinar

def assinar_transacao(mensagem_bytes, chave_privada):
    return chave_privada.sign(mensagem_bytes)

def verificar_assinatura(mensagem_bytes, assinatura, chave_publica):
    try:
        return chave_publica.verify(assinatura, mensagem_bytes)
    except:
        return False
    

# Criar transação simulada
mensagem = criar_transacao("ABC123", 10)
print("Transação:", mensagem.decode())

assinaturas = []
assinantes = [0, 2]  

for i in assinantes:
    assinatura = assinar_transacao(mensagem, chaves_privadas[i])
    assinaturas.append((assinatura, chaves_publicas[i]))
    print(f"Utilizador {i+1} assinou a transação.")

# Verificar as assinaturas
assinaturas_validas = 0
for assinatura, chave_pub in assinaturas:
    if verificar_assinatura(mensagem, assinatura, chave_pub):
        assinaturas_validas += 1

print(f"\nAssinaturas válidas: {assinaturas_validas}")

if assinaturas_validas >= 2:
    print("✅ Transação aprovada (2 de 3 assinaram)")
else:
    print("❌ Transação rejeitada (assinaturas insuficientes)")
