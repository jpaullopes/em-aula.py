import { question } from "readline-sync";

function createArray(lines,colums){
    const array = []

    for(let i = 0;i < lines; i++){
        array.push(criarVetor(colums))
    }

    return array
}

function criarVetor(tamanho, value = 0){
    const vetor = []

    for(let i = 0;i < tamanho;i++){
        vetor.push(value)
    }

    return vetor
}



function main(){
    const lines = parseInt(question('linhas: '))
    const colums = parseInt(question('colunas: '))

    const array = createArray(lines,colums)

    //two dimensions for{}
    for(let i = 0;i < lines; i++){
        for(let j = 0;j < colums;j++){
            array[i][j] = parseInt(question(`Valor[${i}][${j}]: `))
    }

}}


main()
