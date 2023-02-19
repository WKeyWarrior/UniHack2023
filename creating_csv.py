import csv
import random

with open('work_out.csv', "w") as work_out:
  wo_writer = csv.writer(work_out, delimiter = ',', quotechar = '"',
                         quoting = csv.QUOTE_MINIMAL)
  wo_writer.writerow(['height', 'sex', 'weight', 'age', 'experience',
                      'exercise frequency per week', 'reps', 'bench',
                     'curl', 'squat', 'pulldown', 'row', 'pushdown', 'toe',
                     'shoulder', 'rdl'])
  for i in range(1, 10000):
    height = random.randint(48,85)
    sex = random.random() > 0.5 #sex = false is female, sex = true is male
    weight = (26/703)*height*height * random.randint(80, 120)/100
    age = random.randint(16, 81)
    experience_n = random.randint(0, 3)
    if(experience_n == 0):
      experience = 0.5
    elif(experience_n == 1):
      experience = 1
    else:
      experience = 1.5
    exercise_frequency = random.randint(1, 8)
    reps_n = random.random()
    if(reps_n < 1/3):#reps < 0 is gain muscle, weight used 0.33-0.67 is no response, 0.67-1 is leaner
      reps = 5
    elif(reps_n < 2/3):
      reps = 10
    else:
      reps = 15
    weight_used = (int)(((((weight/height)*experience*703 - reps)/200)*5)/10)#weight used will be the dependent variable (based on body weight) This determines a number that will be used for each exercise to determine the weight of the exercise
    bench = weight_used*15 + random.randrange(-1, 2)*5
    curl = weight_used*5
    squat = weight_used*20 + random.randrange(-1, 2)*5
    pulldown = weight_used*10 + random.randrange(-1, 2)*5
    row = weight_used*15 + random.randrange(-1, 2)*5
    pushdown = weight_used*5
    toe = weight_used*20 + random.randrange(-1, 2)*5
    shoulder = weight_used*5
    rdl = weight_used*10 + random.randrange(-1, 2)*5
    #dictionary for minimum avg: bench 15, curl 10, squat 40, pull-down 30, row 30, push-downs 10, toe press 60, shoulder press 10, roman dead lift 30
    wo_writer.writerow([height, sex, weight, age, experience,
                        exercise_frequency, reps, bench,
                     curl, squat, pulldown, row, pushdown, toe,
                     shoulder, rdl])
