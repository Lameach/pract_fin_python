def fact(x):
  if (x == 0):
    return 1
  else:
    return x*fact(x-1)

# print(fact(10))

def filter_even(li):
  return list(filter(lambda x: x % 2 == 0, li))

# print(filter_even([2,4,5,3,6,7,8,14,53,54,55]))

def square(li):
  return list(map(lambda x: pow(x, 2), li))

# print (square([3,6,9,12]))

def bin_search(li, element):
  return bin_search_rec(li, element, 0, len(li) - 1)

def bin_search_rec(li, element, left, right):
  index = left + (right - left) // 2
  if (left == right and li[index] != element):
    return -1
  elif (li[index] > element):
    return bin_search_rec(li, element, left, index - 1)
  elif (li[index] < element):
    return bin_search_rec(li, element, index + 1, right)
  else:
    return index

# print(bin_search([3,6,7,9,12,14,18], 3))

def is_palindrome(string):
  filtered_string = list(filter(lambda x: x.isalpha(), string.lower()))
  i = 0
  j = 0 if len(filtered_string) == 0 else len(filtered_string) - 1
  while (i != j):
    if (filtered_string[i] != filtered_string[j]):
      return 'NO'
    i += 1
    j -= 1
  return 'YES'

# print(is_palindrome('А роза упала на лапу Азора!'))

def calculate(path2file):
  operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,
    '**': lambda x, y: pow(x, y),
  }
  with open(path2file) as f:
    lines = f.readlines()
    results = []
    for i in range (len(lines)):
      line_content = lines[i].split()
      results.append(operations[line_content[0]](int(line_content[1]), int(line_content[2])))
    return str(results).strip('[]')

# print(calculate('test_input_file_1.txt'))

def substring_slice(path2file_1, path2file_2):
  with open(path2file_1) as f_1, open(path2file_2) as f_2:
    lines = f_1.readlines()
    intervals = f_2.readlines()
    results = []
    for i in range (len(lines)):
      interval = intervals[i].split()
      results.append(lines[i][int(interval[0]):int(interval[1]) + 1])
    return " ".join(results)

# print(substring_slice('test_import_file_2_1.txt', 'test_import_file_2_2.txt'))

