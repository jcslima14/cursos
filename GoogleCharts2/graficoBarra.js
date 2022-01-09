function desenharGraficoPizza(){

	var tabela = new google.visualization.DataTable();

	// tabela.addColumn('string','categorias');
	// tabela.addColumn('number', 'valores');
	// tabela.addColumn({ type: 'string', role: 'style' });
	// tabela.addColumn({ type: 'string', role: 'annotation' });

	// 	tabela.addRows([
	// 		['Tecnologia', 47814, "color: #a6a6a6", 'R$ 47.814,00'],
	// 		['Marketing', 22552, "color: #a6a6a6", 'R$ 22.552,00'],
	// 		['Administrativo', 65243, "color: #a6a6a6", 'R$ 65.243,00'],
	// 		['Linhas de crédito', 55504, "color: #a6a6a6", 'R$ 55.504,00'],
	// 		['Segurança', 86085, "color: #1b9af5", 'R$ 86.085,00'], 
	// 		['Atendimento ao cliente', 12605, "color: #f5921b", 'R$ 12.605,00']
	// 	]);	

	tabela.addColumn('string', 'Categorias');

	tabela.addColumn('number', 'Tecnologia');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });
	tabela.addColumn('number', 'Marketing');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });
	tabela.addColumn('number', 'Administrativo');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });
	tabela.addColumn('number', 'Linhas de Crédito');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });
	tabela.addColumn('number', 'Segurança');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });
	tabela.addColumn('number', 'Adtendimento ao Cliente');
	tabela.addColumn({ type: 'number', role: 'annotation' });
	tabela.addColumn({ type: 'string', role: 'style' });

	tabela.addRows([['Categorias', 
						47814, 47814, 'color: #a6a6a6',
						22552, 22552, 'color: #1b9af5',
						65243, 65243, 'color: #a6a6a6',
						55504, 55504, 'color: #a6a6a6',
						86085, 86085, 'color: #f5921b',
						12605, 12605, 'color: #a6a6a6']]);

		tabela.sort({column: 1, asc: true});

		var opcoes = {
			title:'Gastos por unidade de negócio',
			height: 400,
			width: 900,
			legend: 'none',
			hAxis: {
				textPosition: 'none',
				gridlines: {
					count: 0
				},
				ticks: []
			},
			isStacked: 'percent',
			// pieSliceText: 'value',
			// slices: 
			// 	{
			// 		0:{color:'#a6a6a6'},
			// 		1:{color:'#a6a6a6'},
			// 		2:{color:'#a6a6a6'},
			// 		3:{color:'#a6a6a6'},
			// 		4:{color:'#1b9af5', offset: 0.15},
			// 		5:{color:'#f5921b', offset: 0.2}	
			// 	},
			// pieStartAngle: 4,
			titleTextStyle: 
				{ 
					color: '#5e5851',
					fontName: 'Arial',
					fontSize: 20,
					bold: true,
					italic: false 
				},
			chartArea:
				{
					left: 160,
					top: 100,
					width:'70%',
					height:'70%'
				}
			};
	
	var grafico = new google.visualization.BarChart(document.getElementById('graficoPizza'));
            grafico.draw(tabela, opcoes);
    
}