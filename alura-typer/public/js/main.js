var tempoInicial = $('#tempo-restante').text();

function atualizaInformacoesFrase() {
    var frase = $('.frase').text();
    var numPalavras = frase.split(' ').length;
    var tamanhoFrase = $('#tamanho-frase');    
    tamanhoFrase.text(numPalavras);
}

function atualizaTempo(tempo) {
    tempoInicial = tempo;
    $('#tempo-restante').text(tempo);
}

var campoDigitacao = $('.campo-digitacao');
var cronId = null;

function inicializaContadores() {
    campoDigitacao.on('input', function() {
        $('#contador-palavras').text(campoDigitacao.val().split(/\S+/).length - 1);
        $('#contador-caracteres').text(campoDigitacao.val().trim().length);
    });
}

function inicializaCronometro() {
    campoDigitacao.one('focus', function() {
        var tempoRestante = tempoInicial;
        cronId = setInterval(function() {
            tempoRestante--;
            $('#tempo-restante').text(tempoRestante);

            if (tempoRestante == 0) {
                finalizaJogo();
            }
        }, 1000);
    });
}

function finalizaJogo() {
    clearInterval(cronId);
    campoDigitacao.attr('disabled', true);
    campoDigitacao.addClass('campo-desativado');

    inserePlacar($('#usuarios').val(), $('#contador-palavras').text());
}

function comparaFrase() {
    var parteComparavel = $('.frase').text().substr(0, campoDigitacao.val().length);
    if (parteComparavel == campoDigitacao.val()) {
        campoDigitacao.addClass('texto-correto');
        campoDigitacao.removeClass('texto-errado');
    } else {
        campoDigitacao.addClass('texto-errado');
        campoDigitacao.removeClass('texto-correto');
    }
}

function reiniciaJogo() {
    $('#contador-palavras').text(0);
    $('#contador-caracteres').text(0);
    $('#tempo-restante').text(tempoInicial);
    campoDigitacao.val(''),
    campoDigitacao.attr('disabled', false);
    campoDigitacao.off('focus');
    campoDigitacao.removeClass('campo-desativado');
    campoDigitacao.removeClass('texto-correto');
    campoDigitacao.removeClass('texto-errado');
    clearInterval(cronId);
    inicializaCronometro();
}

// $(document).ready() é o mesmo que $()
$(function() {
    inicializaContadores();
    inicializaCronometro();
    atualizaInformacoesFrase();
    buscaPlacar();
    $('#reiniciar-jogo').click(reiniciaJogo);
    campoDigitacao.on('input', comparaFrase);
    $('#usuarios').selectize({
        create: true,
        sortField: 'text'
    });
    $('.tooltip').tooltipster({
        trigger: 'custom'
    });
});
