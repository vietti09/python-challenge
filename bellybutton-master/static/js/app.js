//----------------------------------------buildMetadata Function -------------------------------------//
function buildMetadata(sample) {
    // Use `d3.json` to fetch the metadata for a sample
    var url = `/metadata/${sample}`;
    d3.json(url).then(function (response) {
        console.log(response);
        // var data = response;
        var meta_data = d3.select("#sample-metadata");
        meta_data.html("");
        console.log(response);
        Object.entries(response).forEach(([key, value]) => {
            var cell = meta_data.append("li");
            cell.text(`${key}: ${value}`);
        });
    });
}
// BONUS: Build the Gauge Chart
// buildGauge(data.WFREQ);
function buildCharts(sample) {
    var url = `/samples/${sample}`;
    console.log("---- buildCharts initiated ----");
    // Build a Bubble Chart using the sample data
    d3.json(url).then(function (response) {
        var s_x = response.otu_ids;
        var s_y = response.sample_values;
        var s_text = response.otu_labels;
        var trace = {
            x: s_x,
            y: s_y,
            mode: "markers",
            marker: {
                size: s_y,
                color:  ["e76b74","e0385a","de636f","ef3868","fd93a9","c60031","ff6600","ff1424","d30000","ff4800", "f6a335","f69132","f47d37","f66430","f65632","ffd400","ffc300","ffa500","f48300","df6210","fbfc1b","9ef42e","2cc16a","005c49","405932","3f9e00","42bc00","66bf00","88d622","a6e02a","03256c","2541b2","1768ac","06bee1","028090","001226","001833","162a40","114073","005bbf", "7456a5","3a1772","c39eff","a976fc","814bd8","e069c2","d15cbb","bf3796","912d6c","8e0179","e76b74","e0385a","de636f","ef3868","fd93a9","c60031","ff6600","ff1424","d30000","ff4800", "f6a335","f69132","f47d37","f66430","f65632","ffd400","ffc300","ffa500","f48300","df6210","fbfc1b","9ef42e","2cc16a","005c49","405932","3f9e00","42bc00","66bf00","88d622","a6e02a","03256c","2541b2","1768ac","06bee1","028090","001226","001833","162a40","114073","005bbf", "7456a5","3a1772","c39eff","a976fc","814bd8","e069c2","d15cbb","bf3796","912d6c","8e0179","e76b74","e0385a","de636f","ef3868","fd93a9","c60031","ff6600","ff1424","d30000","ff4800", "f6a335","f69132","f47d37","f66430","f65632","ffd400","ffc300","ffa500","f48300","df6210","fbfc1b","9ef42e","2cc16a","005c49","405932","3f9e00","42bc00","66bf00","88d622","a6e02a","03256c","2541b2","1768ac","06bee1","028090","001226","001833","162a40","114073","005bbf", "7456a5","3a1772","c39eff","a976fc","814bd8","e069c2","d15cbb","bf3796","912d6c","8e0179","e76b74","e0385a","de636f","ef3868","fd93a9","c60031","ff6600","ff1424","d30000","ff4800", "f6a335","f69132","f47d37","f66430","f65632","ffd400","ffc300","ffa500","f48300","df6210","fbfc1b","9ef42e","2cc16a","005c49","405932","3f9e00","42bc00","66bf00","88d622","a6e02a","03256c","2541b2","1768ac","06bee1","028090","001226","001833","162a40","114073","005bbf", "7456a5","3a1772","c39eff","a976fc","814bd8","e069c2","d15cbb","bf3796","912d6c","8e0179"]
            },
            text: s_text,
        };
        var data = [trace];
        var layout = {
            title: "<b>Sample Sizes</b>",
            showlegend: false,
            autosize: true
        };
        Plotly.newPlot("bubble", data, layout, {
            scrollZoom: true
        });
    });
    //----------------------------------------Pie Chart -------------------------------------//
    // Build a Pie Chart for the top 10 sample types
    d3.json(url).then(function (response) {
        var s_labels = response.otu_ids.slice(0, 10);
        var s_values = response.sample_values.slice(0, 10);
        var s_hover = response.otu_labels.slice(0, 10);
        var trace1 = {
            labels: s_labels,
            values: s_values,
            hovertext: s_hover,
            hoverinfo: "hovertext",
            textposition: "outside",
            marker: {
                colors: ["#ca5230", "#d16a46", "#e7b020", "#efc25e", "#fae67e", "#daff7d", "#b2ef9b", "#8c86aa", "#81559b", "#7e3f8f"]
            },
            type: "pie"
        };
        var data1 = [trace1];
        var layout1 = {
            title: "<b>Top 10 Samples</b>",
            autosize: true
        };
        Plotly.newPlot("pie", data1, layout1);
    });
}

function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    // Use the list of sample names to populate the select options
    d3.json("/names").then((sampleNames) => {
        sampleNames.forEach((sample) => {
            selector.append("option").text(sample).property("value", sample);
        });
        // Use the first sample from the list to build the initial plots
        const firstSample = sampleNames[0];
        buildCharts(firstSample);
        buildGauge(firstSample);
        buildMetadata(firstSample);
    });
}

function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts(newSample);
    buildGauge(newSample);
    buildMetadata(newSample);
}
// Initialize the dashboard
init();