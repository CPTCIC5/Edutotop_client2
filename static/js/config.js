const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',

  ];
const data = {
    labels: labels,
    datasets: [{
      label: 'Likes',
      backgroundColor: 'blue',
      borderColor: 'blue',
      data: [0, 10, 5, 2, 20, 30, 45,45,45,45,45,70],
    },
    {
        label: 'Views',
        backgroundColor: 'green',
        borderColor: 'green',
        data: [03, 14, 8, 5, 23, 33, 47,43,47,47,47,39],
      }
]
  };

const config = {
  type: 'line',
  data: data,
};

var myChart = new Chart(
    document.getElementById('myChart'),
    config
);

