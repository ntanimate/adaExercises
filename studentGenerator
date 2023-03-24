import random

student_ids = []
student_emails = []
student_records = []
names = []

for i in range (5):
  name = input("Student name:")
  names.append(name)


for i in range(len(names)):
  student_ids.append(random.randint(11111, 99999))

for i in range(len(names)):
  for i in range(5):
    [first, last] = names[i].split(" ")
    student_emails.append(first[0] + last + str(student_ids[i])[-3:] + "@example.org")

for i in range(len(names)):
  student_records.append(
      {
          "name": names[i],
          "id"  : student_ids[i],
          "email": student_emails[i]
      }
  )


for record in student_records:
  print(f"Name: {names[i].capitalize()}\nId: {student_ids[i]}\nEmail: {student_emails[i]}\n")
