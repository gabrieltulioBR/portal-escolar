from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import math
from datetime import datetime

app = Flask(__name__)
CORS(app)

class GeradorQuestoes:
    def __init__(self):
        self.questoes_geradas = set()
    
    def gerar_questao_matematica(self, dificuldade):
        # Gera ID único baseado no timestamp e random
        questao_id = f"mat_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        if dificuldade == 'facil':
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            operador = random.choice(['+', '-', '×'])
            
            if operador == '+':
                resposta = num1 + num2
                enunciado = f"Quanto é {num1} + {num2}?"
                resposta_idx = 0
            elif operador == '-':
                num1, num2 = max(num1, num2), min(num1, num2)
                resposta = num1 - num2
                enunciado = f"Quanto é {num1} - {num2}?"
                resposta_idx = 0
            else:
                # Multiplicação com números menores para facilitar
                num1 = random.randint(2, 10)
                num2 = random.randint(2, 10)
                resposta = num1 * num2
                enunciado = f"Quanto é {num1} × {num2}?"
                resposta_idx = 0
                
        elif dificuldade == 'medio':
            num1 = random.randint(10, 100)
            num2 = random.randint(2, 20)
            operador = random.choice(['+', '-', '×', '÷'])
            
            if operador == '÷':
                # Garantir divisão inteira
                num2 = random.randint(2, 10)
                num1 = num2 * random.randint(5, 20)
                resposta = num1 // num2
                enunciado = f"Quanto é {num1} ÷ {num2}?"
                resposta_idx = 0
            elif operador == '×':
                resposta = num1 * num2
                enunciado = f"Quanto é {num1} × {num2}?"
                resposta_idx = 0
            else:
                if operador == '+':
                    resposta = num1 + num2
                else:
                    resposta = num1 - num2
                enunciado = f"Quanto é {num1} {operador} {num2}?"
                resposta_idx = 0
                
        else:  # dificil
            tipo = random.choice(['equacao', 'fracao', 'porcentagem', 'geometria'])
            
            if tipo == 'equacao':
                a = random.randint(1, 5)
                b = random.randint(1, 15)
                c = random.randint(10, 30)
                # ax + b = c
                x = (c - b) / a
                enunciado = f"Resolva a equação: {a}x + {b} = {c}"
                resposta = round(x, 2)
                resposta_idx = 0
                
            elif tipo == 'fracao':
                num1 = random.randint(1, 5)
                den1 = random.randint(2, 8)
                num2 = random.randint(1, 5)
                den2 = random.randint(2, 8)
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
                resposta_idx = 0
                    
            elif tipo == 'porcentagem':
                numero = random.randint(50, 500)
                porcentagem = random.randint(5, 50)
                resposta = round(numero * porcentagem / 100, 2)
                enunciado = f"Quanto é {porcentagem}% de {numero}?"
                resposta_idx = 0
                
            else:  # geometria
                tipo_geo = random.choice(['area_circulo', 'perimetro_quadrado', 'volume_cubo'])
                if tipo_geo == 'area_circulo':
                    raio = random.randint(3, 15)
                    resposta = round(math.pi * raio ** 2, 2)
                    enunciado = f"Calcule a área de um círculo com raio {raio} (use π=3.14)"
                elif tipo_geo == 'perimetro_quadrado':
                    lado = random.randint(5, 20)
                    resposta = 4 * lado
                    enunciado = f"Calcule o perímetro de um quadrado com lado {lado}"
                else:
                    lado = random.randint(3, 10)
                    resposta = lado ** 3
                    enunciado = f"Calcule o volume de um cubo com aresta {lado}"
                resposta_idx = 0
        
        # Gerar alternativas únicas
        alternativas = self.gerar_alternativas(resposta, dificuldade)
        
        # Encontrar índice da resposta correta
        for idx, alt in enumerate(alternativas):
            if str(alt) == str(resposta):
                resposta_idx = idx
                break
        
        return {
            'id': questao_id,
            'enunciado': enunciado,
            'alternativas': alternativas,
            'resposta_correta': resposta_idx,
            'tipo': 'matematica',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_portugues(self, dificuldade):
        questao_id = f"port_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        todas_questoes = [
            # FÁCIL
            {
                'enunciado': "Qual alternativa contém palavra escrita corretamente?",
                'alternativas': ['Casa', 'Kasa', 'Caza', 'Kaza'],
                'resposta_correta': 0,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Complete: Eu _____ para escola todos os dias.",
                'alternativas': ['vou', 'vamos', 'vais', 'vão'],
                'resposta_correta': 0,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Qual palavra é um substantivo?",
                'alternativas': ['correr', 'bonito', 'casa', 'rapidamente'],
                'resposta_correta': 2,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Qual é o plural de 'casa'?",
                'alternativas': ['casas', 'case', 'casos', 'casais'],
                'resposta_correta': 0,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Complete: Ela _____ muito bem.",
                'alternativas': ['canta', 'cantamos', 'cantam', 'canto'],
                'resposta_correta': 0,
                'dificuldade': 'facil'
            },
            # MÉDIO
            {
                'enunciado': "Identifique o sujeito: 'Os alunos estudaram para prova.'",
                'alternativas': ['estudaram', 'Os alunos', 'para prova', 'prova'],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual é o antônimo de 'alegre'?",
                'alternativas': ['feliz', 'triste', 'contente', 'jubiloso'],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual frase está na voz ativa?",
                'alternativas': [
                    'O bolo foi comido pela criança.',
                    'A criança comeu o bolo.',
                    'O bolo é comido.',
                    'Está sendo comido o bolo.'
                ],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            # DIFÍCIL
            {
                'enunciado': "Analise a figura de linguagem: 'O tempo é um rio que flui.'",
                'alternativas': ['Metáfora', 'Comparação', 'Hipérbole', 'Personificação'],
                'resposta_correta': 0,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual obra é de Machado de Assis?",
                'alternativas': ['Dom Casmurro', 'O Cortiço', 'Iracema', 'Vidas Secas'],
                'resposta_correta': 0,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual período literário pertence 'Os Lusíadas'?",
                'alternativas': ['Romantismo', 'Classicismo', 'Modernismo', 'Realismo'],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            }
        ]
        
        # Filtrar por dificuldade e escolher aleatoriamente
        questoes_filtradas = [q for q in todas_questoes if q['dificuldade'] == dificuldade]
        questao = random.choice(questoes_filtradas) if questoes_filtradas else todas_questoes[0]
        
        return {
            'id': questao_id,
            'enunciado': questao['enunciado'],
            'alternativas': questao['alternativas'],
            'resposta_correta': questao['resposta_correta'],
            'tipo': 'portugues',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_ciencias(self, dificuldade):
        questao_id = f"cien_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        todas_questoes = [
            # FÁCIL
            {
                'enunciado': "Qual planeta é conhecido como 'Planeta Vermelho'?",
                'alternativas': ['Vênus', 'Marte', 'Júpiter', 'Saturno'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Quantos ossos tem o corpo humano adulto?",
                'alternativas': ['106', '156', '206', '256'],
                'resposta_correta': 2,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Qual animal é um mamífero?",
                'alternativas': ['Tubarão', 'Golfinho', 'Crocodilo', 'Pinguim'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            # MÉDIO
            {
                'enunciado': "Qual processo as plantas usam para produzir alimento?",
                'alternativas': ['Respiração', 'Fotossíntese', 'Digestão', 'Transpiração'],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual é o maior órgão do corpo humano?",
                'alternativas': ['Fígado', 'Coração', 'Pele', 'Intestino'],
                'resposta_correta': 2,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual gás as plantas absorvem durante a fotossíntese?",
                'alternativas': ['Oxigênio', 'Nitrogênio', 'Dióxido de Carbono', 'Hidrogênio'],
                'resposta_correta': 2,
                'dificuldade': 'medio'
            },
            # DIFÍCIL
            {
                'enunciado': "Qual a fórmula química da água?",
                'alternativas': ['CO2', 'H2O', 'O2', 'NaCl'],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual lei da física define que 'ação e reação têm mesma intensidade'?",
                'alternativas': [
                    'Lei da Gravidade',
                    'Lei de Ohm', 
                    '3ª Lei de Newton',
                    'Lei da Conservação'
                ],
                'resposta_correta': 2,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual célula é responsável pela defesa do organismo?",
                'alternativas': ['Hemácia', 'Neurônio', 'Leucócito', 'Osteócito'],
                'resposta_correta': 2,
                'dificuldade': 'dificil'
            }
        ]
        
        questoes_filtradas = [q for q in todas_questoes if q['dificuldade'] == dificuldade]
        questao = random.choice(questoes_filtradas) if questoes_filtradas else todas_questoes[0]
        
        return {
            'id': questao_id,
            'enunciado': questao['enunciado'],
            'alternativas': questao['alternativas'],
            'resposta_correta': questao['resposta_correta'],
            'tipo': 'ciencias',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_historia(self, dificuldade):
        questao_id = f"hist_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        todas_questoes = [
            # FÁCIL
            {
                'enunciado': "Quem descobriu o Brasil?",
                'alternativas': [
                    'Cristóvão Colombo',
                    'Pedro Álvares Cabral',
                    'Vasco da Gama',
                    'Fernão de Magalhães'
                ],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Em que ano o Brasil foi descoberto?",
                'alternativas': ['1492', '1500', '1520', '1450'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            # MÉDIO
            {
                'enunciado': "Qual foi o principal produto econômico do Brasil Colonial?",
                'alternativas': ['Ouro', 'Café', 'Açúcar', 'Algodão'],
                'resposta_correta': 2,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Quem proclamou a Independência do Brasil?",
                'alternativas': [
                    'Dom Pedro I',
                    'Dom João VI',
                    'Tiradentes',
                    'José Bonifácio'
                ],
                'resposta_correta': 0,
                'dificuldade': 'medio'
            },
            # DIFÍCIL
            {
                'enunciado': "Qual tratado dividiu as terras entre Portugal e Espanha em 1494?",
                'alternativas': [
                    'Tratado de Paris',
                    'Tratado de Tordesilhas',
                    'Tratado de Versalhes',
                    'Tratado de Madrid'
                ],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual foi o último imperador do Brasil?",
                'alternativas': [
                    'Dom Pedro I',
                    'Dom Pedro II',
                    'Dom João VI',
                    'Dom Miguel'
                ],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            }
        ]
        
        questoes_filtradas = [q for q in todas_questoes if q['dificuldade'] == dificuldade]
        questao = random.choice(questoes_filtradas) if questoes_filtradas else todas_questoes[0]
        
        return {
            'id': questao_id,
            'enunciado': questao['enunciado'],
            'alternativas': questao['alternativas'],
            'resposta_correta': questao['resposta_correta'],
            'tipo': 'historia',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_geografia(self, dificuldade):
        questao_id = f"geo_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        todas_questoes = [
            # FÁCIL
            {
                'enunciado': "Qual é a capital do Brasil?",
                'alternativas': ['Rio de Janeiro', 'São Paulo', 'Brasília', 'Salvador'],
                'resposta_correta': 2,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Quantos estados tem o Brasil?",
                'alternativas': ['25', '26', '27', '28'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            # MÉDIO
            {
                'enunciado': "Qual o maior estado brasileiro em área?",
                'alternativas': ['Pará', 'Mato Grosso', 'Amazonas', 'Minas Gerais'],
                'resposta_correta': 2,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual desses países não faz fronteira com o Brasil?",
                'alternativas': ['Argentina', 'Chile', 'Colômbia', 'Peru'],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            # DIFÍCIL
            {
                'enunciado': "Qual o bioma predominante no Nordeste brasileiro?",
                'alternativas': ['Cerrado', 'Caatinga', 'Mata Atlântica', 'Pantanal'],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual a maior bacia hidrográfica do mundo?",
                'alternativas': [
                    'Bacia do Congo',
                    'Bacia do Mississippi',
                    'Bacia Amazônica', 
                    'Bacia do Nilo'
                ],
                'resposta_correta': 2,
                'dificuldade': 'dificil'
            }
        ]
        
        questoes_filtradas = [q for q in todas_questoes if q['dificuldade'] == dificuldade]
        questao = random.choice(questoes_filtradas) if questoes_filtradas else todas_questoes[0]
        
        return {
            'id': questao_id,
            'enunciado': questao['enunciado'],
            'alternativas': questao['alternativas'],
            'resposta_correta': questao['resposta_correta'],
            'tipo': 'geografia',
            'dificuldade': dificuldade
        }
    
    def gerar_questao_logica(self, dificuldade):
        questao_id = f"log_{dificuldade}_{datetime.now().timestamp()}_{random.randint(1000,9999)}"
        
        todas_questoes = [
            # FÁCIL
            {
                'enunciado': "Complete a sequência: 2, 4, 6, 8, ?",
                'alternativas': ['9', '10', '11', '12'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Se A = 1, B = 2, C = 3, quanto é A + B + C?",
                'alternativas': ['5', '6', '7', '8'],
                'resposta_correta': 1,
                'dificuldade': 'facil'
            },
            {
                'enunciado': "Qual o próximo número: 5, 10, 15, 20, ?",
                'alternativas': ['25', '30', '35', '40'],
                'resposta_correta': 0,
                'dificuldade': 'facil'
            },
            # MÉDIO
            {
                'enunciado': "Se todos os homens são mortais e Sócrates é homem, então:",
                'alternativas': [
                    'Sócrates é mortal',
                    'Sócrates não é mortal', 
                    'Alguns homens não são mortais',
                    'Nenhuma das alternativas'
                ],
                'resposta_correta': 0,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Complete: Se hoje é sexta-feira, depois de amanhã será:",
                'alternativas': ['sábado', 'domingo', 'segunda', 'terça'],
                'resposta_correta': 1,
                'dificuldade': 'medio'
            },
            {
                'enunciado': "Qual número completa: 1, 1, 2, 3, 5, 8, ?",
                'alternativas': ['11', '12', '13', '14'],
                'resposta_correta': 2,
                'dificuldade': 'medio'
            },
            # DIFÍCIL
            {
                'enunciado': "Em programação, o que é um 'loop infinito'?",
                'alternativas': [
                    'Um loop que nunca termina',
                    'Um loop muito rápido',
                    'Um loop com muitas variáveis',
                    'Um loop que executa uma vez'
                ],
                'resposta_correta': 0,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "Qual a saída do código: for i in range(3): print(i)",
                'alternativas': ['0 1 2', '1 2 3', '0 1 2 3', '1 2'],
                'resposta_correta': 0,
                'dificuldade': 'dificil'
            },
            {
                'enunciado': "O que é um algoritmo?",
                'alternativas': [
                    'Uma linguagem de programação',
                    'Uma sequência de passos para resolver um problema',
                    'Um tipo de hardware',
                    'Um banco de dados'
                ],
                'resposta_correta': 1,
                'dificuldade': 'dificil'
            }
        ]
        
        questoes_filtradas = [q for q in todas_questoes if q['dificuldade'] == dificuldade]
        questao = random.choice(questoes_filtradas) if questoes_filtradas else todas_questoes[0]
        
        return {
            'id': questao_id,
            'enunciado': questao['enunciado'],
            'alternativas': questao['alternativas'],
            'resposta_correta': questao['resposta_correta'],
            'tipo': 'logica',
            'dificuldade': dificuldade
        }
    
    def gerar_alternativas(self, resposta_correta, dificuldade):
        if isinstance(resposta_correta, (int, float)):
            variacao = 5 if dificuldade == 'facil' else 10 if dificuldade == 'medio' else 20
            alternativas = [resposta_correta]
            
            while len(alternativas) < 4:
                variante = resposta_correta + random.randint(-variacao, variacao)
                # Evitar números negativos e repetidos
                if variante >= 0 and variante != resposta_correta and variante not in alternativas:
                    alternativas.append(variante)
                elif len(alternativas) < 4:
                    # Se não conseguiu gerar alternativas únicas, adiciona valores fixos
                    alternativas.append(resposta_correta + random.choice([1, 2, 3, 5, 10]))
            
        else:
            # Para questões de texto, usar alternativas fixas
            alternativas = [resposta_correta, "Alternativa Incorreta A", "Alternativa Incorreta B", "Alternativa Incorreta C"]
        
        random.shuffle(alternativas)
        return alternativas
    
    def gerar_lote_questoes(self, materia, dificuldade, quantidade):
        questoes = []
        tentativas = 0
        max_tentativas = quantidade * 3  # Evitar loop infinito
        
        while len(questoes) < quantidade and tentativas < max_tentativas:
            tentativas += 1
            
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
            
            # Verificar se a questão já foi gerada (evitar repetição)
            questao_hash = f"{questao['enunciado']}_{'-'.join(map(str, questao['alternativas']))}"
            
            if questao_hash not in self.questoes_geradas:
                self.questoes_geradas.add(questao_hash)
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
        # Limpar questões geradas anteriormente para evitar repetição entre requests
        gerador.questoes_geradas.clear()
        
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
    print("💡 Dica: Use ?materia=matematica&dificuldade=medio&quantidade=5")
    
    app.run(host='0.0.0.0', port=5000, debug=True)