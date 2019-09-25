import pymzn
import remzn

def main():
  age = int(input("Input age: "))
  
  if age < 50 :
    height = int(input("Height in inches: "))
    weight = int(input("Weight in kilograms: "))
    bmi = round(weight / (height * 0.0254)**2,2)
    if bmi < 18.5:
      print('Category: Uderweight')
      defecit = abs(int(22 * (height * 0.0254)**2 ) - weight)
      print('Weight deficit of',defecit,'kg\nAdvice:\nDaily calorie intake should be (to be inserted) and light exercise as given below.')
      partfile = 'part_uw_f.mzn'
      rebuilt_file = 'fitness_uw_f.mzn'
      dummy_dzn_file = 'null.dzn'
      exercises = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'cooldown']
      info = [['A1', 5 , 'light'],['A2', 10, 'light'],['A3', 8, 'light'],['A4', 6, 'light'],['A5', 6, 'light'],['A6', 9, 'light'],['A7', 4,'light'],['A8', 5, 'light'],['A9', 2, 'light'],['A10', 9, 'light'], ['cooldown', 0, 'light']]
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
    elif bmi < 24.5:
      print('Category: Fit')
      print('Advice:\nDaily calorie intake should be (need to insert) and light exercise as given below.')
      partfile = 'part_uw_f.mzn'
      rebuilt_file = 'fitness_uw_f.mzn'
      dummy_dzn_file = 'null.dzn'
      exercises = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'cooldown']
      info = [['A1', 5 , 'light'],['A2', 10, 'light'],['A3', 8, 'light'],['A4', 12, 'light'],['A5', 6, 'light'],['A6', 9, 'light'],['A7', 7,'light'],['A8', 5, 'light'],['A9', 8, 'light'],['A10', 9, 'light'], ['cooldown', 0, 'light']]
      slot = 5
      min_calorie = 150
      print("Daily calorie burn of roughly about",min_calorie,"\n")
      solution = ""
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
    else:
      partfile = 'part_ow.mzn'
      rebuilt_file = 'fitness_ow.mzn'
      dummy_dzn_file = 'null.dzn'
      print('category : Overweight')
      gain = abs(weight - int(22 * (height * 0.0254)**2))
      print('Extra gain of',gain,'kg')
      exercises = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'cooldown']
      info = [['A1', 5 , 'light'],['A2', 10, 'light'],['A3', 8,  'light'],['A4', 15, 'heavy'],['A5', 6, 'light'],['A6', 20, 'heavy'],['A7', 10,'light'],['A8', 5, 'light'],['A9', 21, 'heavy'],['A10', 9, 'light'], ['cooldown', 0, 'light']]
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
              solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':2})
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
              solution = pymzn.minizinc(rebuilt_file, dummy_dzn_file,output_mode='item',data={'min_time':5})
              print(solution[0])
            except(Exception):
              print('Failed to operate MiniZinc Solver')
          else:
            print('Failed to operate, create necessary files')
          return
      else:
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
  else:
    partfile = 'part_uw_f.mzn'
    rebuilt_file = 'fitness_uw_f.mzn'
    dummy_dzn_file = 'null.dzn'
    exercises = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'cooldown']
    info = [['A1', 5 , 'light'],['A2', 10, 'light'],['A3', 8, 'light'],['A4', 6, 'light'],['A5', 6, 'light'],['A6', 9, 'light'],['A7', 4,'light'],['A8', 5, 'light'],['A9', 2, 'light'],['A10', 9, 'light'], ['cooldown', 0, 'light']]
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