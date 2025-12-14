# SAEPD - Sistema de Acompanhamento Escolar para Pais e Docentes

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)]()
[![Licença](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)]()

## 🎓 Informações do Projeto

| Instituição | Disciplina | Professor |
| :--- | :--- | :--- |
| **UFCA** | **[ADS0013] Projeto Integrado II** | Allysson Araújo |

## 📝 Descrição do Projeto

O **SAEPD** é um **Produto Mínimo Viável (MVP)** desenvolvido para **melhorar a comunicação** e o acompanhamento da vida acadêmica do aluno, fornecendo uma plataforma organizada e segura para pais/responsáveis.

### 🛠️ Arquitetura e Engenharia de Software

O sistema está sendo desenvolvido em **Python**, seguindo uma arquitetura robusta baseada em **Programação Orientada a Objetos (POO)** e separação de responsabilidades (Camadas de Serviço).

**Princípios de POO Aplicados:**

1.  **Abstração e Herança:** O sistema é fundado na classe abstrata `Usuario` (definida em `usuario_base.py`), que estabelece um contrato de métodos obrigatórios (Polimorfismo) para todos os perfis (`Professor`, `PaiResponsavel`, `Administrador`).
2.  **Polimorfismo:** Todas as classes de usuário implementam o método `apresentar_painel()`, mas com lógicas e interfaces específicas para cada perfil.
3.  **Encapsulamento:** Atributos sensíveis (como senha e IDs) são protegidos com acesso controlado (métodos *getters* ou propriedades `@property`).

**Hierarquia de Classes Principal:**
O diagrama a seguir ilustra a fundação da arquitetura, mostrando a herança da classe base `Usuario` e suas conexões.


## 👥 Divisão de Trabalho e Contribuições (Grupo - UFCA)

O trabalho foi dividido em três grandes módulos. **A responsabilidade é definida pelas tarefas**, e os membros devem preencher seu nome e matrícula ao assumirem o módulo.

| Integrante | Matrícula | Módulo de Responsabilidade | Contribuições Principais | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Ilma Rodrigues V. A.** | 2025015455 | **Estrutura Base / Documentação** | `README.md`, Classe Abstrata `Usuario`, Estrutura Inicial | **Concluída** |
| **[Membro 2]** | [Matrícula] | **Módulo de Comunicação** | `Mensagem`, Repositório e Serviço de Mensagens | Pendente |
| **Gyan Carlos Mateus de Oliveira** | 2025015339 | **Módulo de Perfis** | Implementação da classe `Professor` e Repositório de Perfis | Em Progresso |
| **[Membro 4]** | [Matrícula] | **Módulo de Perfis** | Implementação da classe `Administrador` e Serviço de Autenticação (`AuthService`) | Pendente |
| **[Membro 5]** | [Matrícula] | **Módulo Acadêmico** | Classes `Turma`, `Nota`, `Frequencia` e seus Repositórios | Pendente |
| **[Membro 6]** | [Matrícula] | **Módulo Acadêmico / Principal** | Classes `Aluno`, `PaiResponsavel` e `main.py` (Lógica de Execução) | Pendente |


## ⚙️ Como Executar o Projeto (Getting Started)

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Instalação
```bash
# 1. Clonar o repositório
git clone [https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git](https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git)
cd projetointegrado-POO-SAEPD
