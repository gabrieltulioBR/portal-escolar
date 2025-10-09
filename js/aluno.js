// js/aluno.js - Sistema do Aluno
class SistemaAluno {
    constructor() {
        this.notas = [];
        this.faltas = [];
        this.resumos = [];
        this.iniciar();
    }

    async iniciar() {
        await this.carregarDadosAluno();
        this.carregarNotas();
        this.carregarFrequencia();
        this.carregarResumos();
    }

    async carregarDadosAluno() {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        document.getElementById('nomeAluno').textContent = `Bem-vindo, ${user.nome}`;
    }

    async carregarNotas() {
        // Simular dados do banco
        this.notas = [
            { materia: 'Matemática', bim1: 8.5, bim2: 7.8, bim3: 9.2, bim4: null },
            { materia: 'Português', bim1: 7.2, bim2: 8.1, bim3: 8.5, bim4: null },
            { materia: 'Ciências', bim1: 9.0, bim2: 8.7, bim3: 9.1, bim4: null }
        ];

        this.exibirNotas();
        this.calcularMedias();
    }

    exibirNotas() {
        const tbody = document.getElementById('tabela-notas');
        tbody.innerHTML = '';

        this.notas.forEach(nota => {
            const notasValidas = [nota.bim1, nota.bim2, nota.bim3, nota.bim4].filter(n => n !== null);
            const media = notasValidas.length > 0 ? 
                (notasValidas.reduce((a, b) => a + b, 0) / notasValidas.length).toFixed(1) : '-';

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${nota.materia}</td>
                <td>${nota.bim1 || '-'}</td>
                <td>${nota.bim2 || '-'}</td>
                <td>${nota.bim3 || '-'}</td>
                <td>${nota.bim4 || '-'}</td>
                <td><strong>${media}</strong></td>
            `;
            tbody.appendChild(tr);
        });
    }

    calcularMedias() {
        const todasNotas = this.notas.flatMap(nota => 
            [nota.bim1, nota.bim2, nota.bim3, nota.bim4].filter(n => n !== null)
        );

        if (todasNotas.length > 0) {
            const mediaGeral = (todasNotas.reduce((a, b) => a + b, 0) / todasNotas.length).toFixed(1);
            document.getElementById('media-geral').textContent = mediaGeral;
            
            // Definir situação
            const situacao = mediaGeral >= 6 ? 'Aprovado' : mediaGeral >= 4 ? 'Recuperação' : 'Reprovado';
            const cor = mediaGeral >= 6 ? '#27ae60' : mediaGeral >= 4 ? '#f39c12' : '#e74c3c';
            
            document.getElementById('situacao-aluno').innerHTML = 
                `<span style="color: ${cor}; font-weight: bold">${situacao}</span>`;
        }
    }

    async carregarFrequencia() {
        // Simular dados
        this.faltas = 5;
        const totalAulas = 80;
        const frequencia = ((totalAulas - this.faltas) / totalAulas * 100).toFixed(1);

        document.getElementById('total-faltas').textContent = this.faltas;
        document.getElementById('total-aulas').textContent = totalAulas;
        document.getElementById('percentual-frequencia').textContent = frequencia;

        // Gráfico simples de frequência
        document.getElementById('grafico-frequencia').innerHTML = `
            <div style="background: #ecf0f1; height: 20px; border-radius: 10px; margin: 10px 0;">
                <div style="background: #3498db; height: 100%; width: ${frequencia}%; border-radius: 10px;"></div>
            </div>
        `;
    }

    async carregarResumos() {
        const resumos = JSON.parse(localStorage.getItem('resumos_aula') || '[]');
        const container = document.getElementById('lista-resumos-aluno');
        
        container.innerHTML = '';

        if (resumos.length === 0) {
            container.innerHTML = '<p>Nenhum resumo disponível no momento.</p>';
            return;
        }

        resumos.forEach(resumo => {
            const card = document.createElement('div');
            card.className = 'resumo-card';
            card.innerHTML = `
                <h4>${resumo.titulo}</h4>
                <p><strong>Unidade ${resumo.unidade}</strong></p>
                <p>${resumo.conteudo.substring(0, 150)}...</p>
                <small>Publicado em: ${resumo.data}</small>
            `;
            container.appendChild(card);
        });
    }
}

// Inicializar sistema
const sistemaAluno = new SistemaAluno();