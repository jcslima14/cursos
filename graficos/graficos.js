function desenharGraficos() {
    var tabela = new google.visualization.arrayToDataTable(
        [
            ['Categoria', 'Valor', { type: 'string', role: 'annotation' }, { type: 'string', role: 'style'}],
            ['Educação', 2000, 'R$2.000', 'blue'],
            ['Transporte', 500, 'R$500', 'grey'],
            ['Lazer', 230, 'R$230', 'grey'],
            ['Saúde', 50, 'R$50', 'grey'],
            ['Cartão de Crédito', 930, 'R$930', '#8904B1'],
            ['Alimentação', 260, 'R$260', 'grey']
        ]
    );

    tabela.sort([ { column: 1, desc: true }]);
    var tabelaJson = tabela.toJSON();
    console.log(tabelaJson);

    var opcoes = {
        title: 'Tipos de Gastos',
        height: 600,
        width: 800,
        pieHole: 0.4,
        is3D: true,
        legend: 'labeled',
        pieSliceText: 'value',
        slices: {
            0: { color: 'pink'},
            1: { color: 'grey'},
            2: { color: 'lightgrey'},
            3: { color: 'grey'},
            4: { offset: 0.2},
            5: { color: 'grey'} 
        }
    }

    var grafico = new google.visualization.PieChart(document.getElementById('graficoPizza'));
    grafico.draw(tabela, opcoes);

    opcoes = {
        title: 'Tipos de Gastos',
        height: 600,
        width: 800,
        hAxis: {
            textPosition: 'none',
            gridlines: {
                count: 0,
                color: 'transparent'
            }
        },
        legend: 'none',
        annotations: {
            alwaysOutside: true
        }
    }

    grafico = new google.visualization.BarChart(document.getElementById('graficoBarra'));
    grafico.draw(tabela, opcoes);

    tabela = new google.visualization.arrayToDataTable(
        [
            ['Mês','Valor'],
            ['jan',800],
            ['fev',400],
            ['mar',1100],
            ['abr',400],
            ['mai',500],
            ['jun',750],
            ['jul',1500],
            ['ago',650],
            ['set',850],
            ['out',400],
            ['nov',1000],
            ['dez',720]
        ]
    );

    opcoes = {
        title: 'Gastos Mensais',
        height: 400,
        width: 800,
        vAxis: {
            format: 'currency',
            gridlines: {
                count: 4,
                color: 'transparent'
            }
        },
        curveType: 'function',
        legend: 'none'
    }

    grafico = new google.visualization.LineChart(document.getElementById('graficoLinha'));
    grafico.draw(tabela, opcoes);

    tabela = google.visualization.arrayToDataTable(
        [
            ['Mês','Entrada','Saída'],
            ['jan',2500,1000],
            ['fev',1000,500],
            ['mar',3000,1300],
            ['abr',1500,1700],
            ['mai',5000,2250],
            ['jun',3567,3000],
            ['jul',3452,1468],
            ['ago',1833,5250],
            ['set',1800,1000],
            ['out',1800,1000],
            ['nov',3569,1500],
            ['dez',3000,1740] 
        ]
    );

    opcoes = {
        title: 'Movimentação Mensal',
        height: 600,
        width: 800,
        vAxis: {
            title: 'Valores',
            format: 'currency',
            gridlines: {
                count: 5,
                color: 'transparent'
            }
        },
        hAxis: {
            title: 'Meses'
        }
    }

    grafico = new google.visualization.ColumnChart(document.getElementById('graficoColuna'));
    grafico.draw(tabela, opcoes);

    // gráfico a partir de JSON
    var dadosJson = $.ajax({
        url: 'https://gist.githubusercontent.com/jcslima14/5f7a9971ba2b735e695fa362eddc24d1/raw/aa5798e2a9c06c59dfe8dd869e3837fc01da65a5/dados.json',
        dataType: 'json',
        async: false
    }).responseText;

    tabela = new google.visualization.DataTable(dadosJson);
    tabela.sort([ { column: 1, desc: true }]);

    opcoes = {
        title: 'Saldo por cliente',
        height: 600,
        width: 800,
        legend: 'none',
        hAxis: {
            textPosition: 'none',
            gridlines: {
                count: 0,
                color: 'transparent'
            },
            }
    }

    grafico = new google.visualization.BarChart(document.getElementById('graficoSaldo'));

    grafico.draw(tabela, opcoes);
}
