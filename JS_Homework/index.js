Get references to the tbody element, input field, and button
var tbody = document.querySelector("tbody");
var dateTimeInput = document.querySelector("#datetime");
var searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call
searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredDates to dataSet initially
var filteredDates = dataSet;

// renderTable renders the ufoData to the tbody
function renderTable() {
   tbody.innerHTML = "";
   // While i is less than the length of filteredDates, iterate i by 1
   for (var i = 0; i < filteredDates.length; i++) {
       // Get the date object and its fields
       var date = filteredDates[i];
       // Array of keys (datetime, city, state, country, shape, durationMinutes, comments) stored in fields
       var fields = Object.keys(date);
       // Create a new row in the tbody, set the index to be i + startingIndex
       var row = tbody.insertRow(i);
       // While i is less than the legnth of fields, iterate i by 1
       for (var j = 0; j < fields.length; j++) {
           // For every field in the date object, create a new cell at its inner text to be the current value at the current date's field
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
