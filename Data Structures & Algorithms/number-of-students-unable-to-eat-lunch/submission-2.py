class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unique_type = set(sandwiches) if len(set(sandwiches)) == 2 else {0, 1}
        counts = dict()
        for sandwich_type in unique_type:
            counts[str(sandwich_type)] = len([student_sandwich for student_sandwich in students if student_sandwich == sandwich_type])

        for sandwich in sandwiches:
            if counts[str(sandwich)] > 0:
                counts[str(sandwich)] -= 1
            else:
                break
        
        return sum([remaining_student for remaining_student in counts.values()])
