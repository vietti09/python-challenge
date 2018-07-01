// Function to add the dropdown for samples
function addDropdown() {
  console.log("inside addDropdown()");
  
  // put list of sample names into an array
  sampleNames = [];
  // queryURL = 'https://herokuapp.com/names';
  queryURL = 'http://localhost:5000';
  // Take response and assign to sampleNames array
  d3.json(queryURL, function (error, response) {
    if (error) {
      console.log(error);
    }
    else {
      sampleNames = response;

      // Add each item as option to dropdown  
      for (var i = 0; i < sampleNames.length; i++) {
        d3.select("#samplesDropdown").append("option")
          .attr("value", sampleNames[i]["name"])
          .text(sampleNames[i]);
      }

      optionChanged(sampleNames[0]);

    }
  });

}



// Function to create a default pie chart and scatter plot
function init() {
  console.log("inside init()");
  
  // default pie chart 
  var data = [{
    values: [22, 44, 77, 99],
    labels: ["label 1", "label 2", "label 3", "label 4"],
    text: ["label_text_1", "label_text_2", "label_text_3", "label_text_4"],
    type: "pie"
  }];

  var layout = {
    margin: {
      b: 0,
      t: 10,
      pad: 0
    },
    title: false,
    height: 350,
    width: 475
  };

  Plotly.plot("pie", data, layout);

// Create default scatter plot 
var trace1 = {
    x: [1, 2, 3, 4],
    y: [10, 11, 12, 13],
    text: ['A size: 40', 'B size: 60', 'C size: 80', 'D size: 100'],
    mode: 'markers',
    hoverinfo: 'text',
    marker: {
      color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
      size: [10, 60, 30, 90]
    }
  };

  var data = [trace1];

  var layout = {
    margin: {
      l: 25,
      r: 200,
      b: 35,
      t: 10,
      pad: 0
    },
    xaxis: {title: "OTU ID's"},

    showlegend: false,
    height: 400,
    width: 1200
  };

  Plotly.newPlot('scatterPlot', data, layout);

}
