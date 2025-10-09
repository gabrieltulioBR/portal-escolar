
class SistemaQuestoes {
    constructor() {
        this.questoesAtuais = [];
        this.respostasUsuario = {};
        this.tempoRestante = 30 * 60;
        this.timerInterval = null;
        
        this.inicializar();
    }
    
    inicializar() {
        console.log('✅ Sistema de questões carregado!');
        
        // Conectar botões
        this.conectarEventos();
        
        // Esconder áreas inicialmente
        document.getElementById('areaQuestoes').style.display = 'none';
        document.getElementById('areaResultado').style.display = 'none';
    }
    
    conectarEventos() {
        const gerarBtn = document.getElementById('gerarQuestoes');
        const finalizarBtn = document.getElementById('finalizarSimulado');
        const novoBtn = document.getElementById('novoSimulado');
        
        if (gerarBtn) {
            gerarBtn.addEventListener('click', () => {
                console.log('🎯 Botão clicado!');
                this.gerarSimulado();
            });
        }
        
        if (finalizarBtn) {
            finalizarBtn.addEventListener('click', () => {
                this.finalizarSimulado();
            });
        }
        
        if (novoBtn) {
            novoBtn.addEventListener('click', () => {
                this.reiniciarSimulado();
            });
        }
    }
    
    async gerarSimulado() {
        console.log('🚀 Iniciando geração de simulado...');
        
        const materia = document.getElementById('materia').value;
        const dificuldade = document.getElementById('dificuldade').value;
        const quantidade = parseInt(document.getElementById('quantidade').value);
        
        // Mostrar loading
        this.mostrarLoading(true);
        
        try {
            // Usar API Python para gerar questões
            const api = new QuestoesAPI();
            const questões = await api.gerarQuestoes(materia, dificuldade, quantidade);
            
            this.mostrarLoading(false);
            this.exibirQuestoes(questões, materia, dificuldade, quantidade);
            
        } catch (error) {
            console.error('Erro:', error);
            this.mostrarLoading(false);
            
            // Fallback local
            const questões = this.gerarQuestoesLocais(materia, dificuldade, quantidade);
            this.exibirQuestoes(questões, materia, dificuldade, quantidade);
        }
    }
    
    gerarQuestoesLocais(materia, dificuldade, quantidade) {
        const questoes = [];
        
        for (let i = 0; i < quantidade; i++) {
            const questao = {
                id: Date.now() + i,
                enunciado: `Questão ${i+1} - Exemplo de ${materia} (${dificuldade})`,
                alternativas: [
                    "Alternativa Correta",
                    "Alternativa Incorreta 1", 
                    "Alternativa Incorreta 2",
                    "Alternativa Incorreta 3"
                ],
                resposta_correta: 0,
                tipo: materia,
                dificuldade: dificuldade
            };
            questoes.push(questao);
        }
        
        return questoes;
    }
    
    mostrarLoading(mostrar) {
        const overlay = document.getElementById('loadingOverlay');
        const btn = document.getElementById('gerarQuestoes');
        
        if (overlay) {
            overlay.style.display = mostrar ? 'flex' : 'none';
        }
        
        if (btn) {
            if (mostrar) {
                btn.innerHTML = '⏳ Gerando...';
                btn.disabled = true;
            } else {
                btn.innerHTML = '🚀 Gerar Questões Aleatórias';
                btn.disabled = false;
            }
        }
    }
    
    exibirQuestoes(questoes, materia, dificuldade, quantidade) {
        console.log('📝 Exibindo questões:', questoes.length);
        
        this.questoesAtuais = questoes;
        this.respostasUsuario = {};
        
        // Mostrar área de questões
        const areaQuestoes = document.getElementById('areaQuestoes');
        areaQuestoes.style.display = 'block';
        
        // Atualizar informações
        this.atualizarInfoSimulado(materia, dificuldade, quantidade);
        
        // Gerar HTML das questões
        this.criarListaQuestoes(questoes);
        
        // Iniciar timer
        this.iniciarTimer();
        
        // Scroll para as questões
        areaQuestoes.scrollIntoView({ behavior: 'smooth' });
    }
    
    atualizarInfoSimulado(materia, dificuldade, quantidade) {
        const formatar = {
            matematica: 'Matemática',
            portugues: 'Português', 
            ciencias: 'Ciências',
            historia: 'História',
            geografia: 'Geografia',
            logica: 'Lógica',
            facil: 'Fácil',
            medio: 'Médio',
            dificil: 'Difícil'
        };
        
        document.getElementById('tituloSimulado').textContent = `Simulado de ${formatar[materia]}`;
        document.getElementById('infoMateria').textContent = `Matéria: ${formatar[materia]}`;
        document.getElementById('infoDificuldade').textContent = `Dificuldade: ${formatar[dificuldade]}`;
        document.getElementById('infoQuantidade').textContent = `Questões: ${quantidade}`;
    }
    
    criarListaQuestoes(questoes) {
        const listaQuestoes = document.getElementById('listaQuestoes');
        listaQuestoes.innerHTML = '';
        
        questoes.forEach((questao, index) => {
            const questaoElement = this.criarElementoQuestao(questao, index + 1);
            listaQuestoes.appendChild(questaoElement);
        });
    }
    
    criarElementoQuestao(questao, numero) {
        const div = document.createElement('div');
        div.className = 'questao-item';
        div.innerHTML = `
            <div class="questao-cabecalho">
                <div class="questao-numero">Questão ${numero}</div>
                <div class="questao-dificuldade dificuldade-${questao.dificuldade}">
                    ${questao.dificuldade.charAt(0).toUpperCase() + questao.dificuldade.slice(1)}
                </div>
            </div>
            
            <div class="questao-enunciado">${questao.enunciado}</div>
            
            <div class="questao-alternativas">
                ${questao.alternativas.map((alt, idx) => `
                    <div class="alternativa" onclick="sistemaQuestoes.selecionarAlternativa(${questao.id}, ${idx})">
                        <input type="radio" name="questao_${questao.id}" id="alt_${questao.id}_${idx}">
                        <label for="alt_${questao.id}_${idx}">
                            ${String.fromCharCode(65 + idx)}) ${alt}
                        </label>
                    </div>
                `).join('')}
            </div>
        `;
        
        return div;
    }
    
    selecionarAlternativa(questaoId, alternativaIndex) {
        console.log('🔘 Alternativa selecionada:', questaoId, alternativaIndex);
        
        this.respostasUsuario[questaoId] = alternativaIndex;
        
        // Atualizar visual
        const alternativas = document.querySelectorAll(`[name="questao_${questaoId}"]`);
        alternativas.forEach((input, idx) => {
            const alternativaDiv = input.closest('.alternativa');
            if (idx === alternativaIndex) {
                alternativaDiv.classList.add('selecionada');
                input.checked = true;
            } else {
                alternativaDiv.classList.remove('selecionada');
            }
        });
        
        this.atualizarProgresso();
    }
    
    atualizarProgresso() {
        const total = this.questoesAtuais.length;
        const respondidas = Object.keys(this.respostasUsuario).length;
        document.getElementById('progresso').textContent = `${respondidas}/${total}`;
    }
    
    iniciarTimer() {
        let tempo = this.tempoRestante;
        const timerElement = document.getElementById('timer');
        
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
        
        this.timerInterval = setInterval(() => {
            const minutos = Math.floor(tempo / 60);
            const segundos = tempo % 60;
            
            timerElement.textContent = `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
            
            if (tempo <= 300) {
                timerElement.parentElement.classList.add('urgente');
            }
            
            if (tempo <= 0) {
                clearInterval(this.timerInterval);
                this.finalizarSimulado();
            }
            
            tempo--;
        }, 1000);
    }
    
    finalizarSimulado() {
        console.log('🏁 Finalizando simulado...');
        
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
        
        // Calcular resultado
        let acertos = 0;
        
        this.questoesAtuais.forEach(questao => {
            const respostaUsuario = this.respostasUsuario[questao.id];
            if (respostaUsuario !== undefined && respostaUsuario === questao.resposta_correta) {
                acertos++;
            }
        });
        
        const total = this.questoesAtuais.length;
        const erros = total - acertos;
        const porcentagem = Math.round((acertos / total) * 100);
        
        // Mostrar resultado
        this.mostrarResultado(acertos, erros, porcentagem);
    }
    
    mostrarResultado(acertos, erros, porcentagem) {
        document.getElementById('acertos').textContent = acertos;
        document.getElementById('erros').textContent = erros;
        document.getElementById('porcentagem').textContent = `${porcentagem}%`;
        
        const feedback = document.getElementById('feedback');
        feedback.className = 'feedback';
        
        if (porcentagem >= 80) {
            feedback.textContent = '🎉 Excelente! Você dominou o conteúdo!';
            feedback.classList.add('excelente');
        } else if (porcentagem >= 60) {
            feedback.textContent = '👍 Bom trabalho! Continue praticando!';
            feedback.classList.add('bom');
        } else {
            feedback.textContent = '💪 Foi um bom começo! Revise o conteúdo e tente novamente!';
            feedback.classList.add('regular');
        }
        
        document.getElementById('areaResultado').style.display = 'block';
        document.getElementById('areaResultado').scrollIntoView({ behavior: 'smooth' });
    }
    
    reiniciarSimulado() {
        document.getElementById('areaQuestoes').style.display = 'none';
        document.getElementById('areaResultado').style.display = 'none';
        this.questoesAtuais = [];
        this.respostasUsuario = {};
        
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
        
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Inicializar sistema
let sistemaQuestoes;
document.addEventListener('DOMContentLoaded', function() {
    sistemaQuestoes = new SistemaQuestoes();
});