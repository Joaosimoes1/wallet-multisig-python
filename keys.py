from ecdsa import SigningKey, SECP256k1
import os


def gerar_chave():
    chave_privada = SigningKey.generate(curve=SECP256k1)
    chave_publica = chave_privada.get_verifying_key()
    return chave_privada, chave_publica

def salvar_chaves(nome, priv, pub, pasta='storage'):
    if not os.path.exists(pasta):
        os.makedir(storage)

    with open(os.path.join(pasta, f"{nome}_priv.key"), "wb") as f:
        f.write(priv.to_string())
    with open(os.path.join(pasta, f"{nome}_pub.key"), "wb") as f:
        f.write(pub.to_string())

def carregar_chaves(nome, pasta='storage'):
    with open(os.path.join(pasta, f"{nome}_priv.key"), "rb") as f:
        priv = SigningKey.from_string(f.read(), curve=SECP256k1)
    with open(os.path.join(pasta, f"{nome}_pub.key"), "rb") as f:
        pub = VerifyingKey.from_string(f.read(), curve=SECP256k1)
    return priv, pub
