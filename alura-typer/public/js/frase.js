$('#botao-nova-frase').click(fraseAleatoria);
$('#botao-busca-frase').click(buscaFrase);

function buscaFrase() {
    mostraProgresso();

    var fraseId = $('#id-frase').val();
    
    $.get('http://localhost:3000/frases/', { id: fraseId }, trocaFrase)
        .fail(mostraErro)
        .always(escondeProgresso);
}

function fraseAleatoria() {
    mostraProgresso();

    $.get('http://localhost:3000/frases', trocaFraseAleatoria)
        .fail(mostraErro)
        .always(escondeProgresso);
}

function mostraErro() {
    $('#erro').fadeIn(500, function() {
        setTimeout(function() {
            $('#erro').fadeOut(500);
        }, 5000);
    })
}

function mostraProgresso() {
    $('#spinner').show();
}

function escondeProgresso() {
    $('#spinner').hide();
}

function trocaFraseAleatoria(data) {
    var pos = Math.floor(Math.random() * data.length);
    trocaFrase(data[pos]);
}

function trocaFrase(frase) {
    $('.frase').text(frase.texto);
    atualizaInformacoesFrase();
    atualizaTempo(frase.tempo);
}