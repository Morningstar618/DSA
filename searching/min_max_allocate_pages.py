"""
Find the minimum number of pages to allocate to 
students such that the maximum number of pages 
assigned to a student is minimized.

Approach: Using Binary Search to find the optimal maximum pages
that can be allocated to a student.

NOTE: Good Problem for understanding Binary Search on Answer Space.

Time Complexity: O(N log M) where N is the number of books and M is the sum of pages in all books.
"""

def is_possible(books: list, students: int, max_pages: int) -> bool:
    """Check if it is possible to allocate books such that
    no student gets more than max_pages."""
    required_students = 1
    sum_pages = 0

    for pages in books:
        if sum_pages + pages > max_pages:
            required_students += 1
            sum_pages = pages
        else:
            sum_pages += pages

    return required_students <= students

def min_pages(books: list, students: int) -> int:
    """Find the minimum number of pages to allocate to students."""
    if len(books) < students:
        return -1

    sum_pages = sum(books)
    max_pages = max(books)

    low = max_pages
    high = sum_pages
    result = 0

    while low <= high:
        mid = int((low + high) // 2)

        if is_possible(books, students, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == "__main__":
    books1 = [12, 34, 67, 90]
    print("Minimum number of pages =", min_pages(books1, 2))  # Output: 113

    books2 = [10, 20, 30, 40]
    print("Minimum number of pages =", min_pages(books2, 3))  # Output: 40
