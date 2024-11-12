# Gerador de Senhas Seguras

Este é um projeto simples em Python que gera senhas seguras e personalizáveis. Ele permite que o usuário escolha o comprimento da senha e o tipo de caracteres a serem incluídos, como letras maiúsculas, dígitos e caracteres especiais.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:


- **`utils.py`**: Contém todas as funções para gerar uma senha segura com as opções desejadas.
- **`main.py`**: O ponto de entrada para rodar o programa. Ele importa funções de `utils.py` e exibe um menu para o usuário definir suas preferências de senha.

## Pré-requisitos

- Python 3.6 ou superior

## Instalação

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/gerador-de-senhas.git
    cd gerador-de-senhas
    ```

2. Certifique-se de que você tem o Python instalado. Para verificar, execute:

    ```bash
    python --version
    ```

## Uso

1. No terminal, navegue até o diretório do projeto.
2. Execute o script `main.py` para iniciar o gerador de senhas:

    ```bash
    python main.py
    ```

3. O programa exibirá um menu interativo onde você poderá definir:
   - O comprimento da senha desejada.
   - Se deseja incluir letras maiúsculas.
   - Se deseja incluir dígitos.
   - Se deseja incluir caracteres especiais.

### Exemplo de Execução

```plaintext
Bem-vindo ao Gerador de Senhas Seguras!

Digite o comprimento da senha desejada (ex: 12): 16
Incluir letras maiúsculas? (s/n): s
Incluir dígitos? (s/n): s
Incluir caracteres especiais? (s/n): n

Senha Gerada: X3qfY6hsUzme7tDl
