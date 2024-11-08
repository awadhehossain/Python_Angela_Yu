# Find maximum from the list
# use max function
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

# Find minimum from the list
# use min function
print(min(student_scores))

# Manually use loop
Max=student_scores[0] 
Min=student_scores[0]
# Initial value can be any one of the list
for I in student_scores:
    if I>Max:
        Max=I
for k in student_scores:
    if k<Min:
        Min=k
print(Max)
print(Min)





