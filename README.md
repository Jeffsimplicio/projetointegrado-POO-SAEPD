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
O diagrama a seguir ilustra a fundação da arquitetura, mostrando a herança da classe base `Usuario`.


## 👥 Divisão de Trabalho e Contribuições (Grupo - UFCA)

O trabalho foi dividido em blocos de responsabilidade, utilizando os princípios de coesão e baixo acoplamento para a modularidade do projeto.

| Integrante | Matrícula | Contribuições Principais | Status |
| :--- | :--- | :--- | :--- |
| **Ilma Rodrigues Vieira Azevedo (Você)** | 2025015455 | **Documentação, Estrutura Base e Módulo de Comunicação:** `README.md`, Classe Abstrata `Usuario`, e o Módulo de Mensagens (`mensagem.py`, `messaging_service.py`). | **PR Aberto** |
| **Gyan Carlos Mateus de Oliveira** | 2025015339 | **Entidades e Perfil Docente:** Classes `Aluno`, `Turma`, Repositórios Acadêmicos e a implementação da classe `Professor`. | Em Progresso |
| **Jose Nataniel Gomes Pereira** | 2025015698 | **Núcleo, Serviços e Perfil Responsável:** Classes `Administrador`, Serviços de Autenticação (`AuthService`), Lógica Acadêmica (`AcademicService`) e a implementação da classe `PaiResponsavel`. | Em Progresso |

## ⚙️ Como Executar o Projeto (Getting Started)

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Instalação
```bash
# 1. Clonar o repositório
git clone [https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git](https://github.com/Jeffsimplicio/projetointegrado-POO-SAEPD.git)
cd projetointegrado-POO-SAEPD
