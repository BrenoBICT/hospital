import heapq

# -------------------------
# Função para determinar prioridade a partir do sintoma
# -------------------------
def prioridade_por_sintoma(sintoma):
    sintoma = sintoma.lower()

    # Mapeamento simples de sintomas para prioridade (1 a 5)
    prioridades = {
        'dor no peito': 5,
        'parada respiratória': 5,
        'sangramento intenso': 5,
        'perda de consciência': 5,
        'fratura exposta': 4,
        'dificuldade para respirar': 4,
        'queimadura grave': 4,
        'febre alta': 3,
        'dor abdominal': 3,
        'corte': 2,
        'tosse': 1,
        'dor de cabeça': 1,
        'náusea': 1,
    }

    for chave in prioridades:
        if chave in sintoma:
            return prioridades[chave]
    return None

# -------------------------
# Adicionar paciente no heap (fila de prioridade)
# -------------------------
def adicionar_paciente(fila, nome, prioridade):
    # prioridade negativa porque heapq é min-heap
    heapq.heappush(fila, (-prioridade, nome))

# -------------------------
# Chamar próximo paciente
# -------------------------
def chamar_paciente(fila, historico):
    if not fila:
        print("Nenhum paciente na fila.")
        return
    prioridade, nome = heapq.heappop(fila)
    prioridade = -prioridade  # converte de volta para positivo
    print(f"Chamando paciente: {nome} (Prioridade: {prioridade})")
    historico.append((prioridade, nome))

# -------------------------
# Imprimir fila (recursivo) sem alterar o heap original
# -------------------------
def imprimir_fila_recursiva(fila, index=0):
    if index >= len(fila):
        return
    prioridade, nome = fila[index]
    print(f"{index+1}. {nome} (Prioridade: {-prioridade})")
    imprimir_fila_recursiva(fila, index+1)

# -------------------------
# Histórico (pilha)
# -------------------------
def imprimir_historico(historico):
    if not historico:
        print("Nenhum paciente foi atendido ainda.")
        return
    print("Histórico de pacientes atendidos (mais recente primeiro):")
    for i in range(len(historico)-1, -1, -1):
        prioridade, nome = historico[i]
        print(f"{len(historico)-i}. {nome} (Prioridade: {prioridade})")

# -------------------------
# Menu principal
# -------------------------
def menu():
    fila = []       # heap de pacientes
    historico = []  # pilha de histórico
    while True:
        print("\n--- Sistema de Atendimento Hospitalar ---")
        print("1. Adicionar paciente")
        print("2. Chamar próximo paciente")
        print("3. Mostrar fila de espera")
        print("4. Mostrar histórico de atendimento")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do paciente: ")
            sintoma = input("Sintoma principal do paciente: ")
            prioridade = prioridade_por_sintoma(sintoma)
            if prioridade is None:
                print("Sintoma não reconhecido. Informe a prioridade manualmente.")
                while True:
                    try:
                        prioridade = int(input("Prioridade (1=baixa, 5=alta): "))
                        if 1 <= prioridade <= 5:
                            break
                        else:
                            print("Prioridade deve ser entre 1 e 5.")
                    except:
                        print("Digite um número válido.")
            else:
                print(f"Prioridade definida automaticamente como {prioridade} para o sintoma '{sintoma}'.")
            adicionar_paciente(fila, nome, prioridade)
            print(f"Paciente {nome} adicionado com prioridade {prioridade}.")

        elif escolha == '2':
            chamar_paciente(fila, historico)

        elif escolha == '3':
            if not fila:
                print("Fila vazia.")
            else:
                print("Fila de espera (ordenada por prioridade):")
                # O heap mantém a ordem internamente, mas para mostrar ordenado precisamos criar uma cópia
                fila_temp = sorted(fila, reverse=False)
                imprimir_fila_recursiva(fila_temp)

        elif escolha == '4':
            imprimir_historico(historico)

        elif escolha == '5':
            print("Encerrando sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")

# -------------------------
if __name__ == "__main__":
    menu()
