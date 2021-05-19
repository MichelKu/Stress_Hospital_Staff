// Pass canvas id for Chart to work.
let chart = new Chart('chart', {
  type: 'bar',
  data: {
    labels: ["Sometimes", "Very Often", "Never"],
    datasets: [
      {
        order: 0,
        label: 'Stress among hospital staff',
        borderWidth: 3,
        data: [53, 39, 6],
        backgroundColor: ["#FF5768", "#00A5E3", "#FFBF65"]
      },
    ]
  },
  options: {
    onClick(e) {
      // console.log(chart.getElementAtEvent(e)[0])
      let point = chart.getElementAtEvent(e)[0]

      if (point) {
        let label = chart.data.labels[point._index]
        let value = chart.data.datasets[point._datasetIndex].data[point._index]
        console.log(label, value)
      }
    },

    onHover(e) {
      let point = chart.getElementAtEvent(e)[0]
      if (point) {
        e.target.style.cursor = 'pointer'
      } else {
        e.target.style.cursor = 'default'
      }
    }
  }
})
