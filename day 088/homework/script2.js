function calculateFactorial(N) {
    let factorial = 1;
  
    for (let i = 1; i <= N; i++) {
      factorial *= i;
    }
  
    return factorial;
  }
  
  const N = 5;
  console.log(`რიცხვი ${N}-ის ფაქტორიალი არის ${calculateFactorial(N)}`);
  