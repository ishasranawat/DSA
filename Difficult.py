# Book allocation Array
def isPossible(arr, n, m, max_pages):
    student_count = 1  # Start with the first student
    current_pages = 0  # Pages allocated to the current student

    for pages in arr:
        if current_pages + pages > max_pages:
            # If adding this book exceeds max_pages, allocate a new student
            student_count += 1
            current_pages = pages  # Start a new student's allocation
            if student_count > m:
                return False
        else:
            current_pages += pages
    
    return True

def allocateBooks(arr, n, m):
    if m > n:
        return -1  # Not enough books for the students

    # Binary search between the maximum book pages and total sum of book pages
    low = max(arr)
    high = sum(arr)
    
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(arr, n, m, mid):
            result = mid  # This value is feasible, try for a smaller maximum
            high = mid - 1
        else:
            low = mid + 1  # This value is not feasible, try a larger maximum
    
    return result

# Example input/output handling
n, m = map(int, input().split())  # Read number of books (n) and number of students (m)
arr = list(map(int, input().split()))  # Read the array of pages
print(allocateBooks(arr, n, m))
