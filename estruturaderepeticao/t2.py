while True:
    usuario = input("👤 Digite seu nome de usuário: ")
    senha = input("🔑 Digite sua senha: ")

    if senha == usuario:
        print("❌ Senha inválida! A senha não pode ser igual ao nome de usuário. Tente novamente.\n")
    else:
        print("✅ Login aceito! Bem-vindo(a),", usuario)
        break
