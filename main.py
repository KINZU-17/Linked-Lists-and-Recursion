from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    roster = LinkedList()
    
    # 2) Insert some sample data using insert_at_front or insert_at_end
    roster.insert_at_front(30)
    roster.insert_at_front(20)
    roster.insert_at_front(10)
    roster.insert_at_end(40)
    
    # 3) Display the list to verify insertion
    print("Initial Linked List:")
    roster.display()  # Expected: 10 -> 20 -> 30 -> 40 -> None
    
    # 4) Call recursive_sum and print the result
    total_sum = roster.recursive_sum()
    print(f"\nRecursive Sum of Nodes: {total_sum}")  # Expected: 100
    
    # 5) Call recursive_search with a target and print result
    target_found = roster.recursive_search(30)
    target_missing = roster.recursive_search(99)
    print(f"Searching for 30 (Present): {target_found}")   # Expected: True
    print(f"Searching for 99 (Missing): {target_missing}") # Expected: False
    
    # 6) Call recursive_reverse, then display the reversed list
    print("\nReversing the list in-place recursively...")
    roster.recursive_reverse()
    roster.display()  # Expected: 40 -> 30 -> 20 -> 10 -> None