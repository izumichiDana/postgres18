# # 1 

# class Clock:
#     def current_time(self):
#         import datetime
#         now = datetime.datetime.now()
#         print(now.strftime("%H:%M:%S"))
    
# class Alarm:
#     def on(self):
#         print("Будильник включен")
#     def off(self):
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()


# 2



# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name 
#         self.ball = ball
#     def __lt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'< {res_a < res_b}'
#     def __gt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'> {res_a > res_b}'
#     def __le__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'<= {res_a <= res_b}'
#     def __ge__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'>= {res_a >= res_b}'
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)


# # 3

# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi

#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         return cls(name, language, kpi)
    
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
#     def set_kpi(self, num):
#         self.kpi += num
#         return self.kpi

# student1 = Makers.new_student("John", "Py", 0)
# student2 = Makers.new_student("Ren", "JS", 0)
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)






# class Clock:
#     def current_time(self):
#         import datetime
#         now = datetime.datetime.now()
#         print(now.strftime("%H:%M:%S"))
    
# class Alarm:
#     def on(self):
#         print("Будильник включен")
#     def off(self):
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()



# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name 
#         self.ball = ball
#     def __lt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'< {res_a < res_b}'
#     def __gt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'> {res_a > res_b}'
#     def __le__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'<= {res_a <= res_b}'
#     def __ge__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'>= {res_a >= res_b}'
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)



# class MakersStudents:
#     student_count=0
#     def __init__(self, name,  language, kpi) -> None:
#         self.name = name 
#         self.language = language
#         self.kpi = kpi

#     @classmethod
#     def new_student(cls,name,language,kpi):
#         cls.student_count += 1
#         return (name,language,kpi)

#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
#     def set_kpi(self, num):
#         self.kpi += num
#         return self.kpi

# student = MakersStudents.new_student('Aidana', 'Python' ,0)
# student2 = MakersStudents.new_student("Ren", "JS", 0)
# print(student.set_kpi(89)) 
# print(student.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(MakersStudents.student_count)


# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi

#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         return cls(name, language, kpi)
    
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
#     def set_kpi(self, num):
#         self.kpi += num
#         return self.kpi

# student1 = Makers.new_student("Aidana", "Python", 0)
# student2 = Makers.new_student("Ren", "JS", 0)
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)



def dollarize(float):
    if float >= 0:
        return '${:,.2f}'.format(float)
    else:
        return '-${:,.2f}'.format(-float)

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, value):
        self.amount = value
    
    def __repr__(self):
        return str(self.amount)

    def __str__(self):
        return str(dollarize(self.amount))

cash = MoneyFmt(12345678.021) 
print(cash) 
cash.update(100000.4567) 
print(cash) 
cash.update(-0.3) 
print(cash) 
print(repr(cash))



































