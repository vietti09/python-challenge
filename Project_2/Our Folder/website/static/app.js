var choice = document.getElementById("choice");
var selected = "A"

var url_ndq = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IXIC&apikey=U0WQNC0GCKN67POF";
var url_sp = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=INX&apikey=U0WQNC0GCKN67POF";
var url_select = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=A&apikey=U0WQNC0GCKN67POF";
/*var selected = choice.options[choice.selectedIndex].value
console.log(selected);*/

choice.addEventListener("click", function() {
  selected = choice.options[choice.selectedIndex].value
  var arr = ["https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=", selected, "&apikey=U0WQNC0GCKN67POF"];
  url_select = console.log(arr.join(''));
});
