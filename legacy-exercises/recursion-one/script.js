function sum(arr, n) {
    // Base Case
    if (n <= 0){
      return 0;
    // Recursive call to itself 
    } else {
      return sum(arr, n - 1) + arr[n - 1];
    }
  }