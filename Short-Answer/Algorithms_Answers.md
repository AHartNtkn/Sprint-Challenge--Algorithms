#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The algorithm runs in O(n) time, with respect to n. The while loop is adding n × ns together until it gets an n × n × n. By the definition of times, this is just n, n × ns added together.

b)
I would guess O(n log(n)). The program mostly increases linearly with the size of n, but, periodically, whenever n crosses a threshold where it's a square number, the evaluation time will jump by a factor of `j`'s highest value, which should be about the size of n.

More formally, the run time will be exactly `sum`, since `sum` increases by `1` each step. Every for loop, it increases by `⌊log₂ (n-1)⌋ + 1`. Since sum is just summing these values for each loop of the for loop, the function can be redefined as

```
 n
 Σ  ⌊log₂ (n-1)⌋ + 1
i=1
```

which simplifies to 

```
n ⌊log₂ (n-1)⌋ + n
```

which, by syntactic observation, is in O(n log(n)). Though, this refactoring runs in constant time; I'd probably use it instead.

c)
It appears to be O(n) in the size of bunnies. It recurses once for every bunny, and it doesn't do anything outside of that which is not a constant operation.

## Exercise II
The "number of eggs dropped" corresponds to the number of eggs which are dropped (duh); but this is not the same thing as the number of drops. According to the problem, we can do as many drops as we want; it's the number of eggs used we want to minimize. So, the simple thing to do is start at the bottom floor, and drop the same egg over and over, going up one floor each time, until it breaks. At the end, there will be 1 egg dropped, and 1 egg broken; both being the same egg. This procedure will be linear in the number of floors.

For fun, if we wanted to minimize the number of drops, we can start in the middle floor; if the egg breaks, go down to the halfway point where you are and the ground floor, otherwise go to the halfway point between where you are and the top floor. Repeat this until you're 1 floor below a floor you know the egg will break at. This should have O(log n) run time in the number of floors; the standard run time for a binary search.
