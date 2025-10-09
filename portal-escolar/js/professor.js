// js/professor.js - Sistema do Professor
class SistemaProfessor {
    constructor() {
        this.turmas = [];
        this.alunos = [];
        this.resumos = [];
        this.iniciar();
    }

    async iniciar() {
        await this.carregarDadosProfessor();
        this.carregarTurmas();
        this.atualizarSelectsTurmas();
    }

    async carregarDadosProfessor() {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        document.getElementById('nomeProfessor').textContent = `Bem-vindo, ${user.nome}`;
    }

    async carregarTurmas() {
        // Simular carregamento de turmas do banco
        this.turmas = [
            { id: 1, nome: '9º Ano A', disciplina: 'Matemática', alunos: 25 },
            { id: 2, nome: '9º Ano B', disciplina: 'Matemática', alunos: 28 }
        ];
        
        this.exibirTurmas();
    }

    exibirTurmas() {
        const container = document.getElementById('lista-turmas');
        container.innerHTML = '';

        this.turmas.forEach(turma => {
            const card = document.createElement('div');
            card.className = 'turma-card';
            card.innerHTML = `
                <h4>${turma.nome} - ${turma.disciplina}</h4>
                <p>👥 ${turma.alunos} alunos</p>
                <button class="btn" onclick="sistemaProfessor.verAlunosTurma(${turma.id})">
                    👀 Ver Alunos
                </button>
            `;
            container.appendChild(card);
        });
    }

    atualizarSelectsTurmas() {
        const selects = [
            'select-turma-notas',
            'select-turma-faltas', 
            'select-turma-resumo'
        ];

        selects.forEach(selectId => {
            const select = document.getElementById(selectId);
            select.innerHTML = '<option value="">Selecione uma turma</option>';
            
            this.turmas.forEach(turma => {
                const option = document.createElement('option');
                option.value = turma.id;
                option.textContent = `${turma.nome} - ${turma.disciplina}`;
                select.appendChild(option);
            });
        });
    }

    async verAlunosTurma(turmaId) {
        // Simular carregamento de alunos
        this.alunos = [
            { id: 1, nome: 'João Silva', notas: [8.5, 7.8, 9.2], faltas: 2 },
            { id: 2, nome: 'Maria Santos', notas: [9.0, 8.5, 8.8], faltas: 0 }
        ];

        let html = '<h4>Lista de Alunos</h4><div class="alunos-lista">';
        
        this.alunos.forEach(aluno => {
            const media = aluno.notas.reduce((a, b) => a + b, 0) / aluno.notas.length;
            html += `
                <div class="aluno-item">
                    <div>
                        <strong>${aluno.nome}</strong><br>
                        <small>Média: ${media.toFixed(1)} | Faltas: ${aluno.faltas}</small>
                    </div>
                    <div>
                        <button class="btn" onclick="sistemaProfessor.lancarNotaAluno(${aluno.id})">
                            📊 Notas
                        </button>
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
        document.getElementById('minhas-turmas').innerHTML = `<h3>Alunos da Turma</h3>${html}`;
    }

    async salvarResumo() {
        const turmaId = document.getElementById('select-turma-resumo').value;
        const unidade = document.getElementById('unidade-resumo').value;
        const titulo = document.getElementById('titulo-resumo').value;
        const conteudo = document.getElementById('conteudo-resumo').value;

        if (!turmaId || !titulo || !conteudo) {
            alert('Preencha todos os campos!');
            return;
        }

        const resumo = {
            id: Date.now(),
            turmaId: parseInt(turmaId),
            unidade: parseInt(unidade),
            titulo: titulo,
            conteudo: conteudo,
            data: new Date().toLocaleDateString()
        };

        // Salvar no localStorage (substituir por API depois)
        let resumos = JSON.parse(localStorage.getItem('resumos_aula') || '[]');
        resumos.push(resumo);
        localStorage.setItem('resumos_aula', JSON.stringify(resumos));

        alert('Resumo salvo com sucesso!');
        this.carregarResumos();
        
        // Limpar formulário
        document.getElementById('titulo-resumo').value = '';
        document.getElementById('conteudo-resumo').value = '';
    }

    carregarResumos() {
        const resumos = JSON.parse(localStorage.getItem('resumos_aula') || '[]');
        const container = document.getElementById('lista-resumos');
        
        container.innerHTML = '';
        
        resumos.forEach(resumo => {
            const turma = this.turmas.find(t => t.id === resumo.turmaId);
            const div = document.createElement('div');
            div.className = 'resumo-assunto';
            div.innerHTML = `
                <h4>${resumo.titulo} - Unidade ${resumo.unidade}</h4>
                <p><strong>Turma:</strong> ${turma ? turma.nome : 'N/A'}</p>
                <p>${resumo.conteudo}</p>
                <small>Publicado em: ${resumo.data}</small>
            `;
            container.appendChild(div);
        });
    }
}

// Funções globais para as abas
function mostrarAba(abaId) {
    // Esconder todas as abas
    document.querySelectorAll('.conteudo-aba').forEach(aba => {
        aba.classList.remove('ativa');
    });
    document.querySelectorAll('.aba').forEach(aba => {
        aba.classList.remove('ativa');
    });

    // Mostrar aba selecionada
    document.getElementById(abaId).classList.add('ativa');
    event.target.classList.add('ativa');

    // Carregar conteúdo específico se necessário
    if (abaId === 'resumos') {
        sistemaProfessor.carregarResumos();
    }
}

// Inicializar sistema
const sistemaProfessor = new SistemaProfessor();