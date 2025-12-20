# Binary Search on Answer Space

## Overview

Binary Search on Answer Space is a powerful algorithmic technique that applies binary search not to find an element in a sorted array, but to find the optimal answer to an optimization problem. Instead of searching through data, you search through the range of all possible solutions.

## Core Concept

The key insight is that many optimization problems have a monotonic property:
- If answer X satisfies the constraints, then X+1 might also satisfy them (or vice versa)
- This creates a "sorted" answer space where binary search can be applied

By converting an optimization problem into a series of yes/no decision problems ("Can we achieve answer X?"), we can efficiently find the optimal solution.

## When to Use This Technique

Use binary search on answer space when:

1. **You're looking for a minimum or maximum value** (optimization problem)
2. **You can verify if a given answer works** (decision problem is solvable)
3. **The answer space has monotonic properties**:
   - If X works, all values greater than X work (or vice versa)
   - If X fails, all values less than X fail (or vice versa)
4. **The search space is bounded** (you can identify min/max possible answers)

## Algorithm Template

```python
def binary_search_answer(params):
    def is_feasible(answer):
        """
        Check if 'answer' satisfies the problem constraints.
        Returns True if answer works, False otherwise.
        """
        # Implementation depends on the specific problem
        pass
    
    # Define the search space
    left = minimum_possible_answer
    right = maximum_possible_answer
    
    # Binary search for the optimal answer
    while left < right:
        mid = (left + right) // 2
        
        if is_feasible(mid):
            # If looking for minimum: try smaller values
            right = mid
            # If looking for maximum: try larger values
            # left = mid + 1
        else:
            # If looking for minimum: need larger values
            left = mid + 1
            # If looking for maximum: need smaller values
            # right = mid - 1
    
    return left  # or right, they converge to the same value
```

## Classic Examples

### Example 1: Koko Eating Bananas

**Problem**: Koko has piles of bananas and H hours to eat them all. Find the minimum eating speed K (bananas per hour) needed.

**Solution**: Binary search on possible speeds (1 to max pile size).

```python
def minEatingSpeed(piles, h):
    def canFinish(speed):
        """Check if Koko can finish all bananas at this speed"""
        hours_needed = sum((pile + speed - 1) // speed for pile in piles)
        return hours_needed <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try slower speed
        else:
            left = mid + 1  # Need faster speed
    
    return left
```

### Example 2: Capacity To Ship Packages Within D Days

**Problem**: Given an array of package weights and D days, find the minimum ship capacity needed to ship all packages within D days.

**Solution**: Binary search on possible capacities.

```python
def shipWithinDays(weights, days):
    def canShip(capacity):
        """Check if we can ship all packages with this capacity"""
        days_needed = 1
        current_load = 0
        
        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
            else:
                current_load += weight
        
        return days_needed <= days
    
    left = max(weights)  # Must carry heaviest package
    right = sum(weights)  # Carry everything in one day
    
    while left < right:
        mid = (left + right) // 2
        if canShip(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity
    
    return left
```

### Example 3: Split Array Largest Sum

**Problem**: Split an array into m non-empty subarrays. Minimize the largest sum among these subarrays.

**Solution**: Binary search on the possible largest sums.

```python
def splitArray(nums, m):
    def canSplit(max_sum):
        """Check if we can split into m subarrays with max sum <= max_sum"""
        subarrays = 1
        current_sum = 0
        
        for num in nums:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
            else:
                current_sum += num
        
        return subarrays <= m
    
    left = max(nums)  # Minimum possible largest sum
    right = sum(nums)  # Maximum possible largest sum
    
    while left < right:
        mid = (left + right) // 2
        if canSplit(mid):
            right = mid  # Try smaller max sum
        else:
            left = mid + 1  # Need larger max sum
    
    return left
```

## Common Problem Patterns

### 1. Minimize Maximum (Mini-Max Problems)
- Minimize the maximum load/capacity/sum
- Examples: Split array, allocate books, ship packages

### 2. Maximize Minimum
- Maximize the minimum distance/gap
- Examples: Magnetic force between balls, aggressive cows

### 3. Capacity/Rate Problems
- Find minimum capacity or rate to complete a task
- Examples: Koko eating bananas, painter's partition

### 4. Allocation Problems
- Allocate items under constraints
- Examples: Distribute items to workers, cut ribbon

## Time Complexity

- **Search iterations**: O(log(max - min)) where max and min define the answer space
- **Verification function**: O(f(n)) where f depends on the problem
- **Total**: O(f(n) × log(max - min))

Often much better than trying all possible answers: O(f(n) × (max - min))

## Tips and Tricks

1. **Carefully define the search space**: Identify the absolute minimum and maximum possible answers
2. **Design a clear verification function**: Focus on making `is_feasible()` correct first
3. **Watch for edge cases**: Consider empty inputs, single elements, extreme values
4. **Be careful with the loop condition**: Use `left < right` or `left <= right` appropriately
5. **Handle the monotonic property**: Ensure your problem truly has this property
6. **Integer overflow**: When computing `mid`, use `left + (right - left) // 2` if needed

## Practice Problems

### Beginner
- Koko Eating Bananas (LeetCode 875)
- Find Peak Element (LeetCode 162)
- Capacity To Ship Packages (LeetCode 1011)

### Intermediate
- Split Array Largest Sum (LeetCode 410)
- Minimize Max Distance to Gas Station (LeetCode 774)
- Magnetic Force Between Two Balls (LeetCode 1552)

### Advanced
- Median of Two Sorted Arrays (LeetCode 4)
- Find K-th Smallest Pair Distance (LeetCode 719)
- Minimum Number of Days to Make m Bouquets (LeetCode 1482)

## Key Takeaway

Binary search on answer space transforms difficult optimization problems into easier decision problems. When you see "find the minimum/maximum value such that...", consider whether the answer space is monotonic and if you can verify a given answer—if so, binary search might be your solution!