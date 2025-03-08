from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Estado do jogo
jogo = [""] * 9
vez = "X"

# Combinações para ganhar
vitoria = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]  
]

def verificar_vencedor():
    for comb in vitoria:
        a, b, c = comb
        if jogo[a] and jogo[a] == jogo[b] == jogo[c]:
            return jogo[a]
    if "" not in jogo:
        return "Empate"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogada', methods=['POST'])
def jogada():
    global vez
    dados = request.json
    pos = dados['pos']

    if jogo[pos] == "":
        jogo[pos] = vez
        vencedor = verificar_vencedor()
        vez = "O" if vez == "X" else "X"
        return jsonify({"jogo": jogo, "vencedor": vencedor, "vez": vez})

    return jsonify({"erro": "Posição já ocupada"})

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global jogo, vez
    jogo = [""] 
