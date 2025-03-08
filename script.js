async function clicar(pos) {
    let resposta = await fetch('/jogada', {
        method: 'POST',
        body: JSON.stringify({ pos }),
        headers: { 'Content-Type': 'application/json' }
    });

    let dados = await resposta.json();
    atualizarTabuleiro(dados);
}

function atualizarTabuleiro(dados) {
    let quadrados = document.getElementsByClassName("quadrado");
    for (let i = 0; i < 9; i++) {
        quadrados[i].textContent = dados.jogo[i];
    }

    if (dados.vencedor) {
        document.getElementById("status").textContent = 
            dados.vencedor === "Empate" ? "Empate!" : dados.vencedor + " ganhou!";
    } else {
        document.getElementById("status").textContent = "Vez do jogador " + dados.vez;
    }
}

async function reiniciar() {
    let resposta = await fetch('/reiniciar', { method: 'POST' });
    let dados = await resposta.json();
    atualizarTabuleiro(dados);
}
