# 🏥 Sistema de Atendimento Hospitalar — Fila de Prioridade com Heap

Este projeto implementa um sistema de atendimento hospitalar no **terminal**, onde os pacientes são atendidos conforme a **gravidade do caso** e não pela ordem de chegada.  
A prioridade é determinada automaticamente com base no sintoma informado ou pode ser definida manualmente.  

O código foi desenvolvido em **Python** usando conceitos aprendidos na disciplina de **Algoritmos e Estruturas de Dados I**, incluindo:
- **Heap** (`heapq`) para implementar fila de prioridade
- **Pilha** para armazenar histórico de pacientes atendidos
- **Recursão** para exibir a fila
- Estruturas de dados básicas e lógica condicional

---

## 📌 Tabela de sintomas e prioridades

| Sintoma                     | Prioridade |
|-----------------------------|------------|
| dor no peito                | 5 |
| parada respiratória         | 5 |
| sangramento intenso         | 5 |
| perda de consciência        | 5 |
| fratura exposta             | 4 |
| dificuldade para respirar   | 4 |
| queimadura grave            | 4 |
| febre alta                  | 3 |
| dor abdominal               | 3 |
| corte                       | 2 |
| tosse                       | 1 |
| dor de cabeça               | 1 |
| náusea                      | 1 |

> Sintomas não listados solicitam ao usuário informar manualmente a prioridade.

---

## ▶ Como executar o programa

### 1️⃣ Pré-requisitos
- Ter **Python 3** instalado no computador.

### 2️⃣ Baixar o código
Baixe o arquivo `hospital.py` ou clone o repositório no GitHub:
```bash
git clone https://github.com/BrenoBICT/hospital

Ao executar, você verá:
--- Sistema de Atendimento Hospitalar ---
1. Adicionar paciente
2. Chamar próximo paciente
3. Mostrar fila de espera
4. Mostrar histórico de atendimento
5. Sair
Escolha uma opção:
Funções do menu:

Adicionar paciente → Informe nome e sintoma; prioridade será calculada automaticamente ou manualmente.

Chamar próximo paciente → Remove o paciente mais urgente da fila e o envia para o histórico.

Mostrar fila de espera → Lista pacientes por gravidade (mais graves primeiro).

Mostrar histórico de atendimento → Lista pacientes já atendidos, em ordem reversa.

Sair → Fecha o programa.