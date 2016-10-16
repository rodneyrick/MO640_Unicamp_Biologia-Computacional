function createTable(tableData, divId, header) {
  var table = document.createElement('table');
  // var table = $(document.createElement('table'));
  table.id = "table-" + divId;
  table.className = "table table-responsive table-bordered table-hover table-condensed table-striped";

  if (header){
    var tableHeader = document.createElement('thead');
    var row = document.createElement('tr');
    header.forEach(function(cellData) {
      var cell = document.createElement('td');
      cell.appendChild(document.createTextNode(cellData));
      row.appendChild(cell);
    });
    tableHeader.appendChild(row);
    table.appendChild(tableHeader);
  }

  var tableBody = document.createElement('tbody');
  tableData.forEach(function(rowData) {
    var row = document.createElement('tr');

    rowData.forEach(function(cellData) {
      var cell = document.createElement('td');
      cell.appendChild(document.createTextNode(cellData));
      row.appendChild(cell);
    });
    tableBody.appendChild(row);
  });

  table.appendChild(tableBody);
  // document.body.appendChild(table);
  document.getElementById(divId).appendChild(table);
}

function addParagraph(elementDiv, text) {
  var para = document.createElement("P");
  var t = document.createTextNode(text);
  para.appendChild(t);
  document.getElementById(elementDiv).appendChild(para);
}

function addText(elementDiv, text) {
  var div = document.getElementById(elementDiv);
  div.innerHTML = div.innerHTML + text;
}