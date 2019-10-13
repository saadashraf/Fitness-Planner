import pymzn
import remzn

def main():
  age = abs(int(input("Input age: "))) 
  # this if checks the age and calls the respective partfile 
  if age < 50 :
    height = abs(int(input("Height in inches: ")))
    weight = abs(int(input("Weight in kilograms: ")))
    bmi = round(weight / (height * 0.0254)**2,2)
    #classify the bmi  in three category fit underweight and overweight
    if bmi < 18.5:
      #initialize and execute minizinc file for underweight category
      print('Category: Underweight')
      defecit = abs(int(22 * (height * 0.0254)**2 ) - weight)
      print('Weight deficit of',defecit,'kg\nAdvice:\nDaily calorie intake should be 2400 calories and light exercise as given below.')
      partfile = 'part_uw_f.mzn'
      rebuilt_file = 'fitness_uw_f.mzn'
      dummy_dzn_file = 'null.dzn'
      exercises = ['Walking', 'ClimbingStairs', 'Pushups', 'Plank', 'Twist', 'Squat', 'Situps', 'JumpingJacks', 'cooldown']
      info = [['Walking', 5 , 'light'],['ClimbingStairs', 10, 'light'],['Pushups', 8, 'light'],['Plank', 6, 'light'],['Twist', 6, 'light'],['Squat', 9, 'light'],['Situps', 4,'light'],['JumpingJacks', 5, 'light'], ['cooldown', 0, 'light']]
      slot = 5
      min_calorie = 100
      solution = ""
      print("Daily calorie burn of roughly about",min_calorie,"\n")
      successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
      #checks weather the rebuild was successful 
      if successful:
        try:
          solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item')
          print(solution[0])
        except(Exception):
          print('Failed to operate MiniZinc Solver')
      else:
        print('Failed to operate, create necessary files')
        return
    #condition check for fit
    elif bmi < 24.5:
       #initialize and execute minizinc file for Fit category
      print('Category: Fit')
      print('Advice:\nDaily calorie intake should be 2000 calories and light exercise as given below.')
      partfile = 'part_uw_f.mzn'
      rebuilt_file = 'fitness_uw_f.mzn'
      dummy_dzn_file = 'null.dzn'
      exercises = ['Walking', 'ClimbingStairs', 'Pushups', 'Plank', 'Twist', 'Squat', 'Situps', 'JumpingJacks', 'cooldown']
      info = [['Walking', 5 , 'light'],['ClimbingStairs', 10, 'light'],['Pushups', 8, 'light'],['Plank', 6, 'light'],['Twist', 6, 'light'],['Squat', 9, 'light'],['Situps', 4,'light'],['JumpingJacks', 5, 'light'], ['cooldown', 0, 'light']]
      slot = 5
      min_calorie = 150
      print("Daily calorie burn of roughly about",min_calorie,"\n")
      solution = ""
      successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
      #condition check for successul rebuild
      if successful:
        try:
          solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item')
          print(solution[0])
        except(Exception):
          print('Failed to operate MiniZinc Solver')
      else:
        print('Failed to operate, create necessary files')
        return
        #overweight category
    else:
       #initialize and execute minizinc file for overweight category
      partfile = 'part_ow.mzn'
      rebuilt_file = 'fitness_ow.mzn'
      dummy_dzn_file = 'null.dzn'
      print('category : Overweight')
      gain = abs(weight - int(22 * (height * 0.0254)**2))
      print('Extra gain of',gain,'kg')
      exercises = ['Walking', 'ClimbingStairs', 'Pushups', 'BoxJump', 'Planks', 'Skipping', 'Squats', 'Situps', 'MountainClimber', 'JumpingJacks', 'cooldown']
      info = [['Walking', 5 , 'light'],['ClimbingStairs', 10, 'light'],['Pushups', 8,  'light'],['BoxJump', 15, 'heavy'],['Planks', 6, 'light'],['Skipping', 20, 'heavy'],['Squats', 10,'light'],['Situps', 5, 'light'],['MountainClimber', 21, 'heavy'],['JumpingJacks', 9, 'light'], ['cooldown', 0, 'light']]
      days = int(input('Enter number of days to complete the exercise: '))
      daily = int((gain * 7700) / days)
      if daily <= 100 :
        slot = 5
        min_calorie = 100
        print("Daily calorie burn of roughly about",min_calorie,"\n")
        solution = ""
        successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
        if successful:
          try:
            solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':2})
            print(solution[0])
          except(Exception):
            print('Failed to operate MiniZinc Solver')
        else:
          print('Failed to operate, create necessary files')
        return
        #condition check to enforce a suitable daily calorie burn
      elif daily > 500:
        temp = daily
        while  temp >= 500 :
          print("daily calorie burn exceeds limit max limit is 500 calorie but current value is",temp,"calorie")
          n_input  = int(input("Enter the day again: "))
          temp = int((gain*7700) / n_input)

        if temp <=  100:
          slot = 5
          min_calorie = 100
          solution = ""
          print("Daily calorie burn of roughly about",min_calorie,"\n")
          successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
          if successful:
            try:
              solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':2},solver = pymzn.cbc)
              print(solution[0])
            except(Exception):
              print('Failed to operate MiniZinc Solver')
          else:
            print('Failed to operate, create necessary files')
          return

        else:
          slot = 5
          min_calorie = temp
          print("Daily calorie burn of roughly about",temp,"\n")
          solution = ""
          successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
          if successful:
            try:
              solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':5},solver = pymzn.cbc)
              print(solution[0])
            except(Exception):
              print('Failed to operate MiniZinc Solver')
          else:
            print('Failed to operate, create necessary files')
          return
          #if daily calorie burn is a suitable one
      else:
        # If condition satisfies directly
        slot = 5
        min_calorie = daily
        print("Daily calorie burn of roughly about",daily,"\n")
        solution = ""
        successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
        if successful:
          try:
            solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':2})
            print(solution[0])
          except(Exception):
            print('Failed to operate MiniZinc Solver')
        else:
          print('Failed to operate, create necessary files')
        return
  #for age more than 50
  else:
    partfile = 'part_uw_f.mzn'
    rebuilt_file = 'fitness_uw_f.mzn'
    dummy_dzn_file = 'null.dzn'
    exercises = ['Walking', 'ClimbingStairs', 'Pushups', 'Plank', 'Twist', 'Squat', 'Situps', 'JumpingJacks', 'cooldown']
    info = [['Walking', 5 , 'light'],['ClimbingStairs', 10, 'light'],['Pushups', 8, 'light'],['Plank', 6, 'light'],['Twist', 6, 'light'],['Squat', 9, 'light'],['Situps', 4,'light'],['JumpingJacks', 5, 'light'], ['cooldown', 0, 'light']]
    slot = 5
    min_calorie = 100
    solution = ""
    print("Daily calorie burn of roughly about",min_calorie,"\n")
    successful = remzn.rebuild(exercises, info, slot, min_calorie, partfile, rebuilt_file, dummy_dzn_file)
    if successful:
      try:
        solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item')
        print(solution[0])
      except(Exception):
        print('Failed to operate MiniZinc Solver')
    else:
      print('Failed to operate, create necessary files')
    return

main()
input()