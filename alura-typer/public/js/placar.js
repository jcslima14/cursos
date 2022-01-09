$('#botao-placar').click(function() {
    $('.placar').stop().slideToggle(600);
});

$('#sincroniza-placar').click(sincronizaPlacar);

function sincronizaPlacar() {
    var placar = [];
    var linhas = $('tbody>tr');

    linhas.each(function () {
        var usuario = $(this).find('td:nth-child(1)').text();
        var palavras = $(this).find('td:nth-child(2)').text();

        var score = {
            usuario: usuario,
            pontos: palavras
        }

        placar.push(score);
    });

    $.post('http://localhost:3000/placar', { placar: placar }, function() {
        $('.tooltip').tooltipster('open');
    })
    .fail(function() {
        $('.tooltip').tooltipster('open').tooltipster('content', 'Ocorreu um erro ao sincronizar o placar');
    })
    .always(function() {
        setTimeout(function() {
            $('.tooltip').tooltipster('close');
        }, 3000);
    });
}

function inserePlacar(jogador, numPalavras) {
    var corpoTabela = $('.placar').find('table').find('tbody');
    var linha = novaLinha(jogador, numPalavras);

    corpoTabela.append(linha);

    $('.placar').stop().slideDown(600);
    setTimeout(function() {
        scrollPlacar();
    }, 600);
}

function scrollPlacar() {
    var topoPlacar = $('.placar').offset().top;

    $('body,html').animate({
        scrollTop: `${topoPlacar}px`
    }, 1000);
}

function novaLinha(usuario, placar) {
    var linha = $('<tr>');
    var colunaUsuario = $('<td>').text(usuario);
    var colunaPlacar = $('<td>').text(placar);
    var colunaRemover = $('<td>');
    var linkRemover = $('<a>').addClass('botao-remover').attr('href', '#').click(function(event) {
        event.preventDefault();
        var linha = $(this).parent().parent();
        linha.fadeOut(600, function() {
            linha.remove();
        });
    });
    var iconeRemover = $('<i>').text('delete').addClass('small material-icons');
    linkRemover.append(iconeRemover);
    colunaRemover.append(linkRemover);
    linha.append(colunaUsuario);
    linha.append(colunaPlacar);
    linha.append(colunaRemover);

    return linha;
}

function buscaPlacar() {
    $.get('http://localhost:3000/placar', montaPlacar);
}

function montaPlacar(dados) {
    $(dados).each(function() {
        inserePlacar(this.usuario, this.pontos);
    })
}