var choice = document.getElementById("choice");

console.log(choice);

function buildPlot() {
    /* data route */
  var url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IXIC&apikey=U0WQNC0GCKN67POF";

  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IXIC&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=INX&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=A&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AMD&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=ARQL&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AU&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BHP&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BLIN&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BOSC&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BP&apikey=U0WQNC0GCKN67POF
  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BTI&apikey=U0WQNC0GCKN67POF




  Plotly.d3.json(url, function(error, response) {

    console.log(response["Weekly Time Series"][i]["4. close"]);

    var data = [response];

    var layout = {
      title: "Pet Pals",
      xaxis: {
        title: "Pet Type"
      },
      yaxis: {
        title: "Number of Pals"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();
