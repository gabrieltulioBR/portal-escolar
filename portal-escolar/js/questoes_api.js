// js/questoes_api.js - Cliente para API Python
class QuestoesAPI {
    constructor() {
        this.apiUrl = 'http://localhost:5000/api';
    }

    async gerarQuestoes(materia, dificuldade, quantidade) {
        try {
            console.log(`📡 Buscando questões da API: ${materia}, ${dificuldade}, ${quantidade}`);
            
            const response = await fetch(
                `${this.apiUrl}/questoes?materia=${materia}&dificuldade=${dificuldade}&quantidade=${quantidade}`
            );
            
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (!data.sucesso) {
                throw new Error(data.erro || 'Erro desconhecido na API');
            }
            
            console.log('✅ Questões recebidas da API Python:', data.questoes);
            
            // Adaptar o formato da API Python para o formato do seu sistema
            const questõesAdaptadas = data.questoes.map((questao, index) => ({
                id: questao.id || Date.now() + index,
                enunciado: questao.enunciado,
                alternativas: questao.alternativas || questao.opcoes,
                resposta_correta: 0, // A API Python retorna a resposta correta, vamos encontrar o índice
                tipo: questao.tipo || materia,
                dificuldade: questao.dificuldade || dificuldade
            }));
            
            return questõesAdaptadas;
            
        } catch (error) {
            console.error('❌ Erro ao buscar da API Python:', error);
            console.log('🔄 Usando questões locais (fallback)');
            return this.gerarQuestoesLocais(materia, dificuldade, quantidade);
        }
    }

    gerarQuestoesLocais(materia, dificuldade, quantidade) {
        const questões = [];
        
        for (let i = 0; i < quantidade; i++) {
            const questao = {
                id: Date.now() + i,
                enunciado: `${this.formatarMateria(materia)} - Questão ${i+1} (${this.formatarDificuldade(dificuldade)})`,
                alternativas: [
                    `Alternativa Correta ${i+1}`,
                    `Alternativa Incorreta A ${i+1}`,
                    `Alternativa Incorreta B ${i+1}`,
                    `Alternativa Incorreta C ${i+1}`
                ],
                resposta_correta: 0,
                tipo: materia,
                dificuldade: dificuldade
            };
            questões.push(questao);
        }
        
        return questões;
    }

    formatarMateria(materia) {
        const materias = {
            'matematica': 'Matemática',
            'portugues': 'Português',
            'ciencias': 'Ciências',
            'historia': 'História', 
            'geografia': 'Geografia',
            'logica': 'Lógica'
        };
        return materias[materia] || materia;
    }

    formatarDificuldade(dificuldade) {
        const dificuldades = {
            'facil': 'Fácil',
            'medio': 'Médio',
            'dificil': 'Difícil'
        };
        return dificuldades[dificuldade] || dificuldade;
    }

    // Verificar se a API está online
    async verificarConexao() {
        try {
            const response = await fetch(`${this.apiUrl}/health`);
            const data = await response.json();
            return data.status === 'online';
        } catch (error) {
            return false;
        }
    }
}