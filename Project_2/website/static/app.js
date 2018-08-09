var choice = document.getElementById("choice");



/*var selected = choice.options[choice.selectedIndex].value
console.log(selected);*/

choice.addEventListener("click", function() {
  var selected = choice.options[choice.selectedIndex].value
  console.log(selected)


var arr = ["https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=", selected, "apikey=U0WQNC0GCKN67POF"];

  console.log(arr.join(''));



});
