// Menu Mobile
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenu = document.querySelector('.mobile-menu');
    const nav = document.querySelector('nav ul');
    
    if (mobileMenu) {
        mobileMenu.addEventListener('click', function() {
            nav.classList.toggle('show');
        });
    }
    
    // Verificar autenticação
    checkAuthStatus();
    
    // Carregar dados dinâmicos
    loadDynamicContent();
});

// Verificar status de autenticação
function checkAuthStatus() {
    const user = localStorage.getItem('currentUser');
    const loginBtn = document.querySelector('.login-btn');
    
    if (user && loginBtn) {
        const userData = JSON.parse(user);
        loginBtn.textContent = `Olá, ${userData.nome}`;
        loginBtn.href = userData.tipo === 'aluno' ? 'area_restrita_aluno.html' : 'area_restrita_professor.html';
        
        // Adicionar botão de logout
        const logoutBtn = document.createElement('a');
        logoutBtn.href = '#';
        logoutBtn.textContent = 'Sair';
        logoutBtn.className = 'logout-btn';
        logoutBtn.style.marginLeft = '1rem';
        logoutBtn.style.background = 'var(--accent-color)';
        logoutBtn.style.padding = '0.5rem 1rem';
        logoutBtn.style.borderRadius = 'var(--border-radius)';
        logoutBtn.style.color = 'white';
        logoutBtn.style.textDecoration = 'none';
        
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            localStorage.removeItem('currentUser');
            window.location.href = 'index.html';
        });
        
        loginBtn.parentNode.appendChild(logoutBtn);
    }
}

// Carregar conteúdo dinâmico
function loadDynamicContent() {
    // Simular carregamento de dados do backend
    setTimeout(() => {
        // Atualizar contador de notificações se estiver na área restrita
        const notificationBadge = document.querySelector('.notificacao');
        if (notificationBadge) {
            notificationBadge.textContent = '3';
        }
    }, 1000);
}

// Sistema de login (simulado)
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    
    // Simular verificação no backend
    const users = [
        { id: 1, email: 'aluno@escola.com', senha: '123456', nome: 'João Silva', tipo: 'aluno' },
        { id: 2, email: 'professor@escola.com', senha: '123456', nome: 'Maria Santos', tipo: 'professor' }
    ];
    
    const user = users.find(u => u.email === email && u.senha === senha);
    
    if (user) {
        // Salvar usuário no localStorage (simulando sessão)
        localStorage.setItem('currentUser', JSON.stringify(user));
        
        // Redirecionar para área apropriada
        if (user.tipo === 'aluno') {
            window.location.href = 'area_restrita_aluno.html';
        } else {
            window.location.href = 'area_restrita_professor.html';
        }
    } else {
        alert('Email ou senha incorretos!');
    }
}

// Formulário de contato
function handleContact(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const mensagem = document.getElementById('mensagem').value;
    
    // Simular envio para backend
    console.log('Mensagem enviada:', { nome, email, mensagem });
    
    alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
    event.target.reset();
}
// js/main.js - ATUALIZADO COM CONTROLE DE ACESSO

// Verificar autenticação e redirecionar
function checkAuthAndRedirect() {
    const user = localStorage.getItem('currentUser');
    const currentPage = window.location.pathname;
    
    // Páginas que requerem autenticação
    const protectedPages = [
        'area_restrita_aluno.html',
        'area_restrita_professor.html',
        'professores.html',
        'noticias.html',
        'galeria.html',
        'contato.html',
        'logica.html'
    ];
    
    const isProtectedPage = protectedPages.some(page => currentPage.includes(page));
    
    if (isProtectedPage && !user) {
        window.location.href = 'login.html';
        return false;
    }
    
    return true;
}

// Menu baseado no tipo de usuário
function updateMenuBasedOnUserType() {
    const user = localStorage.getItem('currentUser');
    const nav = document.querySelector('nav ul');
    
    if (!nav) return;
    
    if (!user) {
        // Usuário não logado - menu limitado
        nav.innerHTML = `
            <li><a href="index.html">Início</a></li>
            <li><a href="login.html" class="login-btn">Login</a></li>
        `;
    } else {
        const userData = JSON.parse(user);
        
        if (userData.tipo === 'aluno') {
            nav.innerHTML = `
                <li><a href="index.html">Início</a></li>
                <li><a href="area_restrita_aluno.html">Minha Área</a></li>
                <li><a href="noticias.html">Notícias</a></li>
                <li><a href="logica.html">Exercícios</a></li>
                <li><a href="#" onclick="logout()" class="login-btn">Sair</a></li>
            `;
        } else if (userData.tipo === 'professor') {
            nav.innerHTML = `
                <li><a href="index.html">Início</a></li>
                <li><a href="area_restrita_professor.html">Minha Área</a></li>
                <li><a href="professores.html">Professores</a></li>
                <li><a href="noticias.html">Notícias</a></li>
                <li><a href="galeria.html">Galeria</a></li>
                <li><a href="contato.html">Contato</a></li>
                <li><a href="logica.html">Exercícios</a></li>
                <li><a href="#" onclick="logout()" class="login-btn">Sair</a></li>
            `;
        }
    }
}

// Logout
function logout() {
    localStorage.removeItem('currentUser');
    window.location.href = 'index.html';
}

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    checkAuthAndRedirect();
    updateMenuBasedOnUserType();
    // ... resto do código do menu mobile
});