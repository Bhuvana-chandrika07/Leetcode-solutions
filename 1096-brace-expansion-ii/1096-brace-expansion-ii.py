class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        group = []
        curr =[""]

        for char in expression:
            if char == '{':
                #saving outer context
                stack.append((group,curr))
                group = []
                curr = [""]

            elif char == '}':
                #set of words inside a specific brace
                brace_res = group + curr
                #restore the outer context
                prev_group, prev_curr = stack.pop()

                # Cartesian product: append the new brace results to the outer current string
                curr = [p + s for p in prev_curr for s in brace_res]
                group = prev_group

            elif char == ',':
                # Union operator: lock in the current concatenated strings
                group.extend(curr)
                curr = [""]

            else:
                # Concatenation operator: append the character to all current strings
                curr = [p + char for p in curr]
                
        # Combine remaining elements, deduplicate using a set, and sort
        return sorted(list(set(group + curr)))




        