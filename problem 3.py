#Divide students equally in each group and show leftovers
class1 = 32
class2 = 45
class3 = 51

#grouped students
class1_grouped = class1 // 5
class2_grouped = class2 // 7
class3_grouped = class3 // 6

#leftover students
class1_leftover = class1 % 5
class2_leftover = class2 % 7
class3_leftover = class3 % 6

print('Number of students in each group:')
print('Class 1:', class1_grouped)
print('Class 2:', class2_grouped)
print('Class 3:', class3_grouped)

print('Number of students leftover:')
print('Class 1:', class1_leftover)
print('Class 2:', class2_leftover)
print('Class 3:', class3_leftover)