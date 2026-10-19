class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_circular = len(students) - sum(students)
        students_square = sum(students)
        if students_circular == sandwiches.count(0) and students_square == sandwiches.count(1):
            return 0

        stack_sandwiches = [sandwiches[i] for i in range(len(sandwiches) - 1, -1 , -1)]
        current_sandwich_idx = len(stack_sandwiches) - 1
        while students:
            # if (stack_sandwiches[:current_sandwich_idx+1].count(0) and not students.count(0)) or (stack_sandwiches[:current_sandwich_idx+1].count(1) and not students.count(1)):
            is_desired = any([stack_sandwiches[current_sandwich_idx] == student for student in students])
            if not is_desired:
                break
            if students[0] == stack_sandwiches[current_sandwich_idx]:
                students.pop(0)
                current_sandwich_idx -= 1
            else:
                students.append(students.pop(0))
            
        return current_sandwich_idx + 1