// http://www.geeksforgeeks.org/printing-longest-common-subsequence/
  /* Returns length of LCS for X[0..m-1], Y[0..n-1] */
  function shortestSuperSequence (X, Y, elementDiv, elementTable) {

    if ( X == '' || X == undefined ) X = "AGGTAB";
    if ( Y == '' || Y == undefined ) Y = "GXTXAYB";
    
    var m = X.length, n = Y.length, matrix = [];
    for(var i=0; i<m+1; i++)
      matrix[i] = new Array(n+1);
   
    /*Following steps build L[m+1][n+1] in bottom up fashion.
      Note that L[i][j] contains length of LCS of X[0..i-1]
      and Y[0..j-1] */
    for (i=0; i<=m; i++) {
      for (j=0; j<=n; j++) {
        if (i == 0 || j == 0)
          matrix[i][j] = 0;
   
        // If last characters are same, then add 1 to result and
        // recur for X[]
        else if (X[i-1] == Y[j-1])
          matrix[i][j] = matrix[i-1][j-1] + 1;
   
        // Else find shortest of following two
        //  a) Remove last character from X and recur
        //  b) Remove last character from Y and recur
        else 
          matrix[i][j] = Math.max(matrix[i-1][j], matrix[i][j-1]);
      }
    }

    var idx = matrix[m][n],
        lcs = new Array(idx+1),
        i   = m, 
        j   = n;
    while (i>0 && j>0) {
      if (X[i-1] == Y[j-1]){
        lcs[idx-1] = X[idx];
        i--, j--, idx--;
      }
      else if ( matrix[i-1][j] > matrix[i][j-1] )
        i--;
      else
        j--;
    }
    addText('myDIV', "LCS of <b>" 
      + X + "</b> and <b>" 
      + Y + "</b> is <b>" 
      + lcs.join('') + '</b>')

    matrix.unshift(['/'].concat(Y.split("")));
    
    matrix[0].unshift(['/']);
    matrix[1].unshift(['/']);
    for(j = 2, length2 = matrix.length; j < length2; j++){
      matrix[j].unshift(X[j-2]);
    }
    // matrix[m+1].unshift([X.split('')[m-1]]);
    createTable(matrix, elementTable);
  }