def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    if is_palindrome(s):
        return -1
    
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if is_palindrome(s[i:n - 1 - i]):
                return n - 1 - i
            else:
                return i
    
    return -1

if __name__ == '__main__':
    q = int(input("Enter the number of test cases: ").strip())

    for q_itr in range(q):
        s = input("Enter the string: ")

        result = palindromeIndex(s)

        if result == -1:
            print("The string is already a palindrome.")
        else:
            print(f"Remove character at index {result} to make the string a palindrome.")
