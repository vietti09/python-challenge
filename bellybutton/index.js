// Function to add the dropdown for samples
function addDropdown() {
  console.log("inside addDropdown()");

  // put list of sample names into an array
  sampleNames = [];
  // queryURL = 'https://herokuapp.com/names';
  queryURL = 'http://127.0.0.1:5000';
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



// Create pie chart
function init() {
  console.log("inside init()");

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

  //Create Bubble Chart
  var bubbleLayout = {
      margin: { t: 0 },
      hovermode: 'closest',
      xaxis: { title: 'OTU ID' }
  };
  var bubbleData = [{
      x: sampleNames[0]['otu_ids'],
      y: sampleNames[0]['sample_values'],
      text: labels,
      mode: 'markers',
      marker: {
          size: sampleNames[0]['sample_values'],
          color: sampleNames[0]['otu_ids'],
      }
  }];
  var BUBBLE = document.getElementById('bubble');
  Plotly.plot(BUBBLE, bubbleData, bubbleLayout);
