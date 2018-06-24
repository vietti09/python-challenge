
var tbody = document.querySelector("tbody");
var dateTimeInput = document.querySelector("#datetime");
var searchBtn = document.querySelector("#search");

searchBtn.addEventListener("click", handleSearchButtonClick);

var filteredDates = dataSet;

function renderTable() {
   tbody.innerHTML = "";

   for (var i = 0; i < filteredDates.length; i++) {

       var date = filteredDates[i];
       var fields = Object.keys(date);
       var row = tbody.insertRow(i);

       for (var j = 0; j < fields.length; j++) {

           var field = fields[j];
           var cell = row.insertCell(j);
           cell.innerText = date[field];
       }
   }
}

function handleSearchButtonClick() {
   var filterDate = dateTimeInput.value.trim();

   filteredDates = dataSet.filter(function(date) {
       var ufoDate = date.datetime;
       return ufoDate === filterDate;
    });
    renderTable();
}
renderTable();
