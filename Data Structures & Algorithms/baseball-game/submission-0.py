class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def _is_string(val):
            try:
                int(val)
                return True
            except ValueError:
                return False
        if len(operations) == 0: return 0
        n = len(operations)
        records = [0] * n
        index = 0
        for i in range(n):
            if _is_string(operations[i]) and isinstance(int(operations[i]), int):
                records[index] = operations[i]
                index += 1
                continue
            if operations[i] == '+':
                if len(records) < 2:
                    continue
                records[index] = str(int(records[index-2]) + int(records[index-1]))
                index += 1
            if operations[i] in ('D', 'C'):
                if len(records) < 1:
                    continue
                if operations[i] == 'D':
                    records[index] = str(2 * int(records[index-1]))
                    index += 1
                    continue
                if operations[i] == 'C':
                    records[index-1] = str(0)
                    index -= 1
                    continue
        new_records = records[:index+1]
        result = 0
        for e in new_records:
            result += int(e)
        return result
        # NOTE: VERIFY whether to use records[i] or records[index] is correct ?
        # Convert string to integer since the output is an integer