function local_alignment(str1, str2, gap, match, mismatch, elementDiv, elementTable) {

  var matrix = [
    [str1, str1.length],
    [str2, str2.length],
  ];
  createTable(matrix, elementDiv, ["sequence", "size"]);

  var matrix = [
    [gap, match, mismatch],
  ];
  createTable(matrix, elementDiv, ["GAP", "MATCH", "MISMATCH"]);

  str1 = str1.split("");
  str2 = str2.split("");

  addParagraph(elementDiv, "");

  str1.unshift("\\");
  str1.unshift("\\");
  str2.unshift("\\");

  matrix = [];
  matrix.push(str1)
  for (var i = 0; i < str2.length; i++) {
    c = [];
    c.push(str2[i]);
    c = c.concat(Array.apply(null, Array(str1.length-1)).map(function (_, i) {return 0;}));
    matrix.push(c)
  }

  str1_final = [];
  str2_final = [];

  for (var j = 0; j < matrix[0].length; j++) {
    for (var i = 0; i < matrix.length; i++) {
      
      if ((matrix[1][j] || matrix[i][1]) ){
        matrix[1][j] = 0;
        matrix[i][1] = 0;
      }

      if (i > 1 && j > 1)

        matrix[i][j] = Math.max(
          matrix[i][j-1] + gap,
          matrix[i-1][j-1] + (matrix[0][j] == matrix[i][0] ? match : mismatch),
          matrix[i-1][j] + gap,
          0
        );
    }
  }
  matrix[1][0] = "\\";
  matrix[0][1] = "\\";
  createTable(matrix, "elementTable");
  addParagraph(elementDiv, str1_final);
  addParagraph(elementDiv, str2_final);
}

