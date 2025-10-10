# 🏫 Portal Escolar  

Bem-vindo ao **Portal Escolar**, um projeto acadêmico desenvolvido por **Gabriel Túlio**, **César Lopes** com o objetivo de criar um sistema web funcional e acessível para escolas.  
O projeto foi construído com foco em **aprendizado prático**, utilizando **HTML, CSS, JavaScript, PHP, Python e MySQL** para integrar front-end, back-end e banco de dados.

---

## 🎯 Objetivo do Projeto  

O **Portal Escolar** visa facilitar a comunicação e o gerenciamento entre **alunos, professores e administração escolar**, oferecendo um ambiente digital completo com avisos, notícias, perfis e contato direto com a escola.

---

## 🧩 Estrutura do Sistema  

O portal é dividido em várias páginas, cada uma com sua função:

- 🏠 **Página Inicial** — avisos e destaques da escola  
- 👩‍🏫 **Professores** — nomes, disciplinas e e-mails  
- 📰 **Notícias** — cards com imagem, título e resumo  
- 📸 **Galeria** — fotos de eventos e atividades escolares  
- 📞 **Contato** — formulário simples com nome, mensagem e botão “Enviar”  
- 🔐 **Login** — acesso de **alunos, professores e administração**

---

## ⚙️ Tecnologias Utilizadas  

| Tecnologia | Função Principal | Documentação |
|-------------|------------------|--------------|
| **HTML5** | Estrutura das páginas | [HTML MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTML) |
| **CSS3** | Estilização e layout responsivo | [CSS MDN](https://developer.mozilla.org/pt-BR/docs/Web/CSS) |
| **JavaScript** | Interatividade e comportamento dinâmico | [JavaScript MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) |
| **PHP** | Processamento no servidor, login e integração com o banco | [PHP Manual](https://www.php.net/manual/pt_BR/) |
| **Python** | Scripts de automação e prototipagem do banco de dados | [Python Docs](https://docs.python.org/pt-br/3/) |
| **MySQL** | Armazenamento de usuários, notícias e dados escolares | [MySQL Docs](https://dev.mysql.com/doc/) |

---

## 📱 Ferramentas de Desenvolvimento  

O desenvolvimento é feito principalmente em dispositivos móveis e no ambiente escolar:

- **📲 Termux** — servidor PHP e MySQL local no Android  
- **💻 Acode** — editor de código leve para HTML, CSS, JS e PHP  
- **🐍 Pydroid 3 / QPython** — para scripts Python auxiliares  
- **🖥️ PC da Escola** — para testes, ajustes e apresentações

---

## 👤 Login de Exemplo  

Para testes locais:

| Tipo de Usuário | Login | Senha |
|------------------|--------|--------|
| 👩‍🏫 Professor | `userprof` | `123456` |
| 🧑‍🎓 Aluno | `useraluno` | `12345` |

O sistema identifica o tipo de usuário e redireciona para a área correta (perfil do aluno ou professor).

---

## 🧱 Estrutura de Pastas  
portal-escolar/
├── index.html
├── login.html
├── professores.html
├── noticias.html
├── galeria.html
├── contato.html
├── css/
│ └── style.css
├── js/
│ └── script.js
├── php/
│ ├── login.php
│ └── conexao.php
├── python/
│ ├── init_db.py
│ └── backup_data.py
└── img/
└── (imagens da escola, professores e eventos)
