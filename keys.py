from ecdsa import SigningKey, SECP256k1
import binascii


def gerar_chave():
    chave_privada = SigningKey.generate(curve=SECP256k1)
    chave_publica = chave_privada.get_verifying_key()
    return chave_privada, chave_publica

def salvar_chaves_em_hex(chave_privada, chave_publica):
    return {
        'privada_hex': chave_privada.to_string().hex(),
        'publica_hex': chave_publica.to_string().hex()
    }

# Teste
if __name__ == "__main__":
    priv, pub = gerar_chave()
    hex_keys = salvar_chaves_em_hex(priv, pub)

    print(hex_keys)

    print("Chave privada:", hex_keys['privada_hex'])
    print("Chave pública:", hex_keys['publica_hex'])
