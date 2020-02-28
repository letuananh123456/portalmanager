var config = {
			type: 'line',
			data: {
				labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
				datasets: [{
					label: 'dataset - big points',
					data: [
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()
					],
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					fill: false,
					borderDash: [5, 5],
					pointRadius: 15,
					pointHoverRadius: 10,
				}, {
					label: 'dataset - individual point sizes',
					data: [
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()
					],
					backgroundColor: window.chartColors.blue,
					borderColor: window.chartColors.blue,
					fill: false,
					borderDash: [5, 5],
					pointRadius: [2, 4, 6, 18, 0, 12, 20],
				}, {
					label: 'dataset - large pointHoverRadius',
					data: [
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()
					],
					backgroundColor: window.chartColors.green,
					borderColor: window.chartColors.green,
					fill: false,
					pointHoverRadius: 30,
				}, {
					label: 'dataset - large pointHitRadius',
					data: [
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()
					],
					backgroundColor: window.chartColors.yellow,
					borderColor: window.chartColors.yellow,
					fill: false,
					pointHitRadius: 20,
				}]
			},
			options: {
				responsive: true,
				legend: {
					position: 'bottom',
				},
				hover: {
					mode: 'index'
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Month'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Value'
						}
					}]
				},
				title: {
					display: true,
					text: 'Chart.js Line Chart - Different point sizes'
				}
			}
		};

		window.onload = function() {
			var ctx = document.getElementById('canvas').getContext('2d');
			window.myLine = new Chart(ctx, config);
		};