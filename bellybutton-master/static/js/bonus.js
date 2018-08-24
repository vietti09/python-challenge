/**
 * BONUS Solution
 * */
function buildGauge(wfreq) {
  // Enter the washing frequency between 0 and 180
  var level = parseFloat(wfreq) * 20;
  // Trig to calc meter point
  var degrees = 180 - level;
  var radius = 0.5;
  var radians = (degrees * Math.PI) / 180;
  var x = radius * Math.cos(radians);
  var y = radius * Math.sin(radians);
  // Path: may have to change to create a better triangle
  var mainPath = "M -.0 -0.05 L .0 0.05 L ";
  var pathX = String(x);
  var space = " ";
  var pathY = String(y);
  var pathEnd = " Z";
  var path = mainPath.concat(pathX, space, pathY, pathEnd);
  var gauge_trace = [{
      type: "scatter",
      x: [0],
      y: [0],
      marker: {
          size: 12,
          color: "161925"
      },
      showlegend: false,
      name: "Freq",
      text: level,
      hoverinfo: "text+name"
  }, {
      values: [50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50],
      rotation: 90,
      text: ["8-9", "7-8", "6-7", "5-6", "4-5", "3-4", "2-3", "1-2", "0-1", ""],
      textinfo: "text",
      textposition: "inside",
      marker: {
          colors: ["#ca5230", "#d16a46", "#e7b020", "#efc25e", "#fae67e", "#daff7d", "#b2ef9b", "#8c86aa", "#81559b", "#ffffff"]
      },
      labels: ["8-9", "7-8", "6-7", "5-6", "4-5", "3-4", "2-3", "1-2", "0-1", ""],
      hoverinfo: "label",
      hole: 0.5,
      type: "pie",
      showlegend: false,
  }];
  var gauge_layout = {
      shapes: [{
          type: "path",
          path: path,
          fillcolor: "#000000",
          line: {
              color: "#000000"
          }
      }],
      title: "<b>Belly Button Washing Frequency</b> <br> Scrubs per Week",
      xaxis: {
          zeroline: false,
          showticklabels: false,
          showgrid: false,
          range: [-1, 1]
      },
      yaxis: {
          zeroline: false,
          showticklabels: false,
          showgrid: false,
          range: [-1, 1]
      },
      autosize: false,
      width: 750
  };
  var GAUGE = document.getElementById("gauge");
  Plotly.newPlot(GAUGE, gauge_trace, gauge_layout);
}