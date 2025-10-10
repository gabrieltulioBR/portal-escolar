# 🏫 Portal Escolar  

Bem-vindo ao **Portal Escolar**, um projeto acadêmico desenvolvido por **Gabriel Túlio** com o objetivo de criar um sistema web simples e funcional para escolas.  
O projeto foi construído com foco em **acessibilidade, organização e aprendizado prático** nas áreas de **HTML, CSS, JavaScript, PHP e MySQL**.

---

## 🎯 Objetivo do Projeto  

O **Portal Escolar** tem como meta facilitar a comunicação entre **alunos, professores e administração**, centralizando informações em um único ambiente digital.  
Com ele, é possível visualizar **avisos, notícias, professores, eventos** e entrar em contato diretamente com a escola.

---

## 🧩 Estrutura do Sistema  

O portal é dividido em várias páginas, cada uma com sua função específica:

- 🏠 **Página Inicial** — exibe avisos, destaques e novidades da escola.  
- 👩‍🏫 **Professores** — mostra nomes, disciplinas e contatos de cada professor.  
- 📰 **Notícias** — contém cards de notícias com imagem, título e resumo.  
- 📸 **Galeria** — apresenta fotos de eventos e atividades escolares.  
- 📞 **Contato** — formulário simples com nome, mensagem e botão “Enviar”.  
- 🔐 **Login** — sistema de acesso para **alunos, professores e administração**.

---

## ⚙️ Tecnologias Utilizadas  

| Tecnologia | Função Principal | Documentação |
|-------------|------------------|--------------|
| **HTML5** | Estrutura das páginas | [HTML MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTML) |
| **CSS3** | Estilização e layout responsivo | [CSS MDN](https://developer.mozilla.org/pt-BR/docs/Web/CSS) |
| **JavaScript** | Interatividade e comportamento dinâmico | [JavaScript MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) |
| **PHP** | Processamento no servidor e login | [PHP Manual](https://www.php.net/manual/pt_BR/) |
| **MySQL** | Banco de dados (futuro) | [MySQL Docs](https://dev.mysql.com/doc/) |

---

## 📱 Ferramentas de Desenvolvimento  

O projeto está sendo desenvolvido principalmente em dispositivos móveis, utilizando:

- **📲 Termux** — para rodar o servidor PHP localmente.  
- **💻 Acode** — editor de código leve e prático para Android.  
- **🖥️ PC (na escola)** — para testes, ajustes e apresentações.

---

## 👤 Login de Exemplo  

Para testes locais, o sistema conta com dois usuários cadastrados:

| Tipo de Usuário | Login | Senha |
|------------------|--------|--------|
| 👩‍🏫 Professor | `userprof` | `123456` |
| 🧑‍🎓 Aluno | `useraluno` | `12345` |

Após o login, cada tipo de usuário é redirecionado para sua respectiva área.

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
│ └── login.php
└── img/
└── (imagens da escola, professores, eventos)
