class Solution:

  def lexPalindromicPermutation(self, s: str, target: str) -> str:
    n = len(s)
    half_len = n // 2

    # Step 1: Count frequency of each character in s
    freq = [0] * 26
    for ch in s:
      freq[ord(ch) - ord('a')] += 1

    
    odd_count = 0
    mid_char = ''
    for i in range(26):
      if freq[i] % 2 != 0:
        odd_count += 1
        mid_char = chr(ord('a') + i)

    if odd_count > 1:
      return ''

    
    for i in range(26):
      freq[i] //= 2

    
    def make_palindrome(first_half: list[str]) -> str:
      first_str = ''.join(first_half)
      if n % 2 == 1:
        return first_str + mid_char + first_str[::-1]
      else:
        return first_str + first_str[::-1]

    # Step 2: Try matching target prefix of length i from m down to 0
    for i in range(half_len, -1, -1):
      
      cur_freq = freq.copy()
      prefix = []
      possible = True

      
      for j in range(i):
        idx = ord(target[j]) - ord('a')
        if cur_freq[idx] > 0:
          cur_freq[idx] -= 1
          prefix.append(target[j])
        else:
          possible = False
          break

      if not possible:
        continue

      # Case 1: Exact prefix match of length half_len
      if i == half_len:
        cand = make_palindrome(prefix)
        if cand > target:
          return cand
        continue

      # Case 2: Pick character at position i strictly greater than target[i]
      target_char_idx = ord(target[i]) - ord('a')
      for c_idx in range(target_char_idx + 1, 26):
        if cur_freq[c_idx] > 0:

          cand_freq = cur_freq.copy()
          cand_freq[c_idx] -= 1

          cand_half = prefix + [chr(ord('a') + c_idx)]

        
          for k in range(26):
            if cand_freq[k] > 0:
              cand_half.extend([chr(ord('a') + k)] * cand_freq[k])

          cand = make_palindrome(cand_half)
          if cand > target:
            return cand

    return ''