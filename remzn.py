def rebuild(exercise, info, slot, min_calorie, mzn_part_path, mzn_output_path, dummy_dzn_path):
    str_exercise = 'enum exercise = ' + str(exercise).replace('[', '{').replace(']', '}').replace('\'', '') + ';\n'
    str_info = 'array[exercise, feature] of int: info = ['
    for item in info:
        str_info += str(item).replace('[', '|').replace(']', '').replace('\'', '')
    str_info += '|];\n'
    str_slot = 'int: slot = ' + str(slot) + ';\n'
    str_min_calorie = 'int: min_calorie = ' + str(min_calorie) + ';\n'
    data = str_exercise + str_info + str_slot + str_min_calorie
    try:
        mzn = open(mzn_part_path, 'r')
        data2 = mzn.readlines()
        mzn.close()
    except(Exception):
        print('Failed to open or find ' + mzn_part_path)
        return False
    for line in data2:
        data += line
    try:
        mzn = open(mzn_output_path, 'w+')
        mzn.write(data)
        mzn.close
    except(Exception):
        print('Failed to create ' + mzn_output_path)
        return False
    try:
        dzn = open(dummy_dzn_path, 'w+')
        dzn.close()
    except(Exception):
        print('Failed to create ' + dummy_dzn_path)
        return False
    return True