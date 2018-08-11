/ set html elements to variables
var $tbody = document.querySelector("tbody");

var $dateInput = document.querySelector("#date");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");

var $searchBtn = document.querySelector("#search");
var $resetBtn = document.querySelector("#reset");

// create EventListeners for buttons
$searchBtn.addEventListener("click", handleSearchButtonClick);
$resetBtn.addEventListener("click", handleResetButtonClick);

// set the dataSet to a variable to be filtered
var filteredData = dataSet;

// creates the table according to the filtered data
function renderTable() {

    // clear the table body in preparation for rendering
    $tbody.innerHTML = "";

    // create a new row for each object in filteredData
    for (var i = 0; i < filteredData.length; i++) {
      var datum = filteredData[i];
      var fields = Object.keys(datum);
      var $row = $tbody.insertRow(i);

      // create a new cell for each field in the data object
      for (var j = 0; j < fields.length; j++) {
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = datum[field];
      }
    }
}

// filters dataSet according to input from search fields
function handleSearchButtonClick() {

    // set input fields to variables
    var filterDate = $dateInput.value.trim();
    var filterCity = $cityInput.value.trim().toLowerCase();
    var filterState = $stateInput.value.trim().toLowerCase();
    var filterCountry = $countryInput.value.trim().toLowerCase();
    var filterShape = $shapeInput.value.trim().toLowerCase();

    // check for values and filter dataSet if found
    if (filterDate != "") {
        filteredData = filteredData.filter(function(datum) {
            return datum.datetime == filterDate;
    })};
    if (filterCity != "") {
        filteredData = filteredData.filter(function(datum) {
            return datum.city == filterCity;
    })};
    if (filterState != "") {
        filteredData = filteredData.filter(function(datum) {
            return datum.state == filterState;
    })};
    if (filterCountry != "") {
        filteredData = filteredData.filter(function(datum) {
            return datum.country == filterCountry;
    })};
    if (filterShape != "") {
        filteredData = filteredData.filter(function(datum) {
            return datum.shape_ == filterShape;
    })};

    renderTable();
}

// reset the table for a new search
function handleResetButtonClick() {

    // clear the input fields
    $dateInput.value = "";
    $cityInput.value = "";
    $stateInput.value = "";
    $countryInput.value = "";
    $shapeInput.value = "";

    // reset filteredData to the full dataSet
    filteredData = dataSet;

    renderTable();
}

// render the full table on page load
renderTable();
