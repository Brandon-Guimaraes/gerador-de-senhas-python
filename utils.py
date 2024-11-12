import random
import string

lowercase_letters = string.ascii_lowercase  # letras minúsculas
uppercase_letters = string.ascii_uppercase  # letras maiúsculas
digits = string.digits                      # dígitos de 0 a 9
special_characters = string.punctuation     # caracteres especiais (!, @, #, etc.)

def generate_secure_password(length=12, use_upper=True, use_digits=True, use_special=True):
    available_characters = lowercase_letters
    password = []

    if use_upper:
        password.append(random.choice(uppercase_letters))
        available_characters += uppercase_letters
    if use_digits:
        password.append(random.choice(digits))
        available_characters += digits
    if use_special:
        password.append(random.choice(special_characters))
        available_characters += special_characters

    # Completar o restante da senha
    password += [random.choice(available_characters) for _ in range(length - len(password))]
    random.shuffle(password)  # Embaralhar para misturar os caracteres iniciais
    return ''.join(password)

# Função para mostrar o menu e capturar as opções do usuário
def user_menu():
    print("Bem-vindo ao Gerador de Senhas Seguras!\n")
    
    # Captura o comprimento da senha
    while True:
        try:
            length = int(input("Digite o comprimento da senha desejada (ex: 12): "))
            if length < 4:
                print("A senha deve ter pelo menos 4 caracteres.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    # Pergunta se o usuário deseja incluir letras maiúsculas
    use_upper = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'

    # Pergunta se o usuário deseja incluir dígitos
    use_digits = input("Incluir dígitos? (s/n): ").strip().lower() == 's'

    # Pergunta se o usuário deseja incluir caracteres especiais
    use_special = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    # Gerar a senha com as preferências do usuário
    password = generate_secure_password(length, use_upper, use_digits, use_special)
    print("\nSenha Gerada:", password)