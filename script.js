let jogo = ["", "", "", "", "", "", "", "", ""];
let vez = "X";
let acabou = false;

function clicar(i) {
    if (jogo[i] === "" && !acabou) {
        jogo[i] = vez;
        document.getElementsByClassName("quadrado")[i].textContent = vez;
        vez = vez === "X" ? "O" : "X";
        document.getElementById("status").textContent = "Vez do jogador " + vez;
        verificar();
    }
}

function verificar() {
    let v = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    for (let i of v) {
        if (jogo[i[0]] && jogo[i[0]] === jogo[i[1]] && jogo[i[0]] === jogo[i[2]]) {
            acabou = true;
            document.getElementById("status").textContent = jogo[i[0]] + " ganhou!";
        }
    }
    if (!jogo.includes("") && !acabou) {
        document.getElementById("status").textContent = "Empate!";
    }
}

function reset() {
    jogo = ["", "", "", "", "", "", "", "", ""];
    vez = "X";
    acabou = false;
    document.getElementById("status").textContent = "Vez do jogador X";
    let quadrados = document.getElementsByClassName("quadrado");
    for (let q of quadrados) {
        q.textContent = "";
    }
}
