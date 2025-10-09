from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import math
from datetime import datetime

app = Flask(__name__)
CORS(app)

class GeradorQuestoes:
    def __init__(self):
        self.operadores_matematica = ['+', '-', '×', '÷']
        self.temas_portugues = ['gramatica', 'interpretacao', 'ortografia', 'literatura']
        self.conceitos_ciencias = ['biologia', 'fisica', 'quimica', 'ecologia']
        self.periodos_historia = ['antiga', 'medieval', 'moderna', 'contemporanea']
        self.temas_geografia = ['fisica', 'humana', 'economica', 'politica']
    
    def gerar_questao_matematica(self, dificuldade):
        if dificuldade == 'facil':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operador = random.choice(['+', '-', '×'])
            
            if operador == '+':
                resposta = num1 + num2
                enunciado = f"Quanto é {num1} + {num2}?"
            elif operador == '-':
                resposta = max(num1, num2) - min(num1, num2)
                enunciado = f"Quanto é {max(num1, num2)} - {min(num1, num2)}?"
            else:
                resposta = num1 * num2
                enunciado = f"Quanto é {num1} × {num2}?"
                
        elif dificuldade == 'medio':
            num1 = random.randint(10, 50)
            num2 = random.randint(2, 10)
            operador = random.choice(['+', '-', '×', '÷'])
            
            if operador == '÷':
                # Garantir divisão inteira
                num1 = num2 * random.randint(2, 10)
                resposta = num1 // num2
                enunciado = f"Quanto é {num1} ÷ {num2}?"
            elif operador == '×':
                resposta = num1 * num2
                enunciado = f"Quanto é {num1} × {num2}?"
            else:
                if operador == '+':
                    resposta = num1 + num2
                else:
                    resposta = num1 - num2
                enunciado = f"Quanto é {num1} {operador} {num2}?"
                
        else:  # dificil
            # Equações, frações, porcentagem
            tipo = random.choice(['equacao', 'fracao', 'porcentagem', 'geometria'])
            
            if tipo == 'equacao':
                a = random.randint(1, 5)
                b = random.randint(1, 10)
                c = random.randint(1, 20)
                # ax + b = c
                x = (c - b) / a
                enunciado = f"Resolva a equação: {a}x + {b} = {c}"
                resposta = round(x, 2)
                
            elif tipo == 'fracao':
                num1 = random.randint(1, 5)
                den1 = random.randint(2, 6)
                num2 = random.randint(1, 5)
                den2 = random.randint(2, 6)
                operador = random.choice(['+', '×'])
                
                if operador == '+':
                    mmc = den1 * den2
                    resposta_num = (num1 * den2) + (num2 * den1)
                    resposta = f"{resposta_num}/{mmc}"
                    enunciado = f"Some as frações: {num1}/{den1} + {num2}/{den2}"
                else:
                    resposta_num = num1 * num2
                    resposta_den = den1 * den2
                    resposta = f"{resposta_num}/{resposta_den}"
                    enunciado = f"Multiplique as frações: {num1}/{den1} × {num2}/{den2}"
                    
            elif tipo == 'porcentagem':
                numero = random.randint(50, 200)
                porcentagem = random.randint(5, 30)
                resposta = numero * porcentagem / 100
                enunciado = f"Quanto é {porcentagem}% de {numero}?"
                
            else:  # geometria
                raio = random.randint(3, 10)
                resposta = round(math.pi * raio ** 2, 2)
                enunciado = f"Calcule a área de um círculo com raio {raio} (use π=3.14)"
        
        alternativas = self.gerar_alternativas(resposta, dificuldade)
        
        return {
            'enunciado': enunciado,
            'alternativas': alternativas,
            'resposta_correta': resposta,
            'tipo': 'matematica',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_portugues(self, dificuldade):
        temas = {
            'facil': [
                {
                    'enunciado': "Qual alternativa contém palavra escrita corretamente?",
                    'opcoes': ['Casa', 'Kasa', 'Caza', 'Kaza'],
                    'resposta': 'Casa'
                },
                {
                    'enunciado': "Complete: Eu _____ para escola todos os dias.",
                    'opcoes': ['vou', 'vamos', 'vais', 'vão'],
                    'resposta': 'vou'
                }
            ],
            'medio': [
                {
                    'enunciado': "Identifique o sujeito: 'Os alunos estudaram para prova.'",
                    'opcoes': ['estudaram', 'Os alunos', 'para prova', 'prova'],
                    'resposta': 'Os alunos'
                },
                {
                    'enunciado': "Qual é o antônimo de 'alegre'?",
                    'opcoes': ['feliz', 'triste', 'contente', 'jubiloso'],
                    'resposta': 'triste'
                }
            ],
            'dificil': [
                {
                    'enunciado': "Analise a figura de linguagem: 'O tempo é um rio que flui.'",
                    'opcoes': ['Metáfora', 'Comparação', 'Hipérbole', 'Personificação'],
                    'resposta': 'Metáfora'
                },
                {
                    'enunciado': "Qual obra é de Machado de Assis?",
                    'opcoes': ['Dom Casmurro', 'O Cortiço', 'Iracema', 'Vidas Secas'],
                    'resposta': 'Dom Casmurro'
                }
            ]
        }
        
        return random.choice(temas[dificuldade])
    
    def gerar_questao_ciencias(self, dificuldade):
        # Implementar similar às outras matérias
        questoes = {
            'facil': [
                {
                    'enunciado': "Qual planeta é conhecido como 'Planeta Vermelho'?",
                    'opcoes': ['Vênus', 'Marte', 'Júpiter', 'Saturno'],
                    'resposta': 'Marte'
                }
            ],
            'medio': [
                {
                    'enunciado': "Qual processo as plantas usam para produzir alimento?",
                    'opcoes': ['Respiração', 'Fotossíntese', 'Digestão', 'Transpiração'],
                    'resposta': 'Fotossíntese'
                }
            ],
            'dificil': [
                {
                    'enunciado': "Qual a fórmula química da água?",
                    'opcoes': ['CO2', 'H2O', 'O2', 'NaCl'],
                    'resposta': 'H2O'
                }
            ]
        }
        
        return random.choice(questoes[dificuldade])
    
    def gerar_alternativas(self, resposta_correta, dificuldade):
        if isinstance(resposta_correta, (int, float)):
            # Para questões numéricas
            variacao = 5 if dificuldade == 'facil' else 10 if dificuldade == 'medio' else 20
            alternativas = [resposta_correta]
            
            while len(alternativas) < 4:
                variante = resposta_correta + random.randint(-variacao, variacao)
                if variante != resposta_correta and variante not in alternativas:
                    alternativas.append(variante)
            
        else:
            # Para questões de texto
            alternativas = [resposta_correta]
            opcoes_erradas = ['Alternativa A', 'Opção B', 'Resposta C', 'Letra D']
            while len(alternativas) < 4:
                opcao = random.choice(opcoes_erradas)
                if opcao not in alternativas:
                    alternativas.append(opcao)
        
        random.shuffle(alternativas)
        return alternativas
    
    def gerar_lote_questoes(self, materia, dificuldade, quantidade):
        questoes = []
        for _ in range(quantidade):
            if materia == 'matematica':
                questao = self.gerar_questao_matematica(dificuldade)
            elif materia == 'portugues':
                questao = self.gerar_questao_portugues(dificuldade)
            elif materia == 'ciencias':
                questao = self.gerar_questao_ciencias(dificuldade)
            elif materia == 'historia':
                questao = self.gerar_questao_historia(dificuldade)
            elif materia == 'geografia':
                questao = self.gerar_questao_geografia(dificuldade)
            else:  # logica
                questao = self.gerar_questao_logica(dificuldade)
            
            questao['id'] = random.randint(1000, 9999)
            questoes.append(questao)
        
        return questoes

# Instância global do gerador
gerador = GeradorQuestoes()

@app.route('/api/questoes', methods=['GET'])
def obter_questoes():
    materia = request.args.get('materia', 'matematica')
    dificuldade = request.args.get('dificuldade', 'facil')
    quantidade = int(request.args.get('quantidade', 5))
    
    try:
        questoes = gerador.gerar_lote_questoes(materia, dificuldade, quantidade)
        return jsonify({
            'sucesso': True,
            'questoes': questoes,
            'total': len(questoes),
            'materia': materia,
            'dificuldade': dificuldade,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'online', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("🚀 Servidor de Questões iniciando...")
    print("📚 Matérias disponíveis: matematica, portugues, ciencias, historia, geografia, logica")
    print("🎯 Dificuldades: facil, medio, dificil")
    print("🔗 API: http://localhost:5000/api/questoes")
    
    app.run(host='0.0.0.0', port=5000, debug=True)