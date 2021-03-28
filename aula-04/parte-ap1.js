/*
    Definição dos grupos de teste
*/

let x11 = 1, x12 = 1, y1 = 1
let x21 = 1, x22 = 0, y2 = 1
let x31 = 0, x32 = 0, y3 = 0
let x41 = 0, x42 = 1, y4 = 0

/*
    Definição dos pesos das entradas (2 entradas)
*/

let w1 = -1
let w2 = -1


/*
    Declarando a função rampa
*/

function funcaoRampa(soma) {
    if (soma < 0) {
        return 0
    } else if (soma > 1) {
        return 1
    } else {
        return soma
    }
}

/*
    Função de ajuste de peso
    saida = saida desejada (y1 ou y2)
    entrada1 = valor de entrada do neoronio (x11, x12, x21, x21)
*/

function ajustePesos(saidaDesejada, saidaObtida,  entrada1, entrada2) {

    if (saidaObtida != saidaDesejada) {
        w1 = w1 + 1 * saidaDesejada - saidaObtida * entrada1
        w2 = w2 + 1 * saidaDesejada - saidaObtida * entrada2
        return 1
    }
    return 0
}

/*
    Função responsavel pela soma ponderada das entradas
*/
function funcaoSoma(entrada1, entrada2) {
    return entrada1 * w1 + entrada2 * w2
}

let ajustes
let y
let res
let ajustesTotais = 0

do {

    ajustes = 0

    res = funcaoSoma(x11, x12)
    y = funcaoRampa(res)
    ajustes += ajustePesos(y1, y, x11, x12)

    res = funcaoSoma(x21, x22)
    y = funcaoRampa(res)
    ajustes += ajustePesos(y2, y, x21, x22)

    res = funcaoSoma(x31, x32)
    y = funcaoRampa(res)
    ajustes += ajustePesos(y3, y, x31, x32)

    res = funcaoSoma(x41, x42)
    y = funcaoRampa(res)
    ajustes += ajustePesos(y4, y, x41, x42)

    ajustesTotais += ajustes

} while (ajustes != 0)

console.log("TERMINOU")
console.log("w1 = ", w1)
console.log("w2 = ", w2)
console.log("Ajustes totais", ajustesTotais)