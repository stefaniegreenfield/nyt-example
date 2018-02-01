import csv

# reads a CSV from a file, and creates a dictionary of this form:
# grade_dict['homeworks'] = [20, 20, 20, ...]
# grade_dict['lectures'] = [5, 5, 5, ...]
# ...
# params: name of file containing grade estimates
#         columns in file must be as follows:
#           assn_name, assn_category, max_points, expected_points
# returns: a dictionary as specified above
def get_data(fname):
  CATEGORY_INDEX = 1
  EXPECTED_SCORE_INDEX = 3
  global HOMEWORKS_KEY, LECTURES_KEY, DISCUSSIONS_KEY, MIDTERMS_KEY, PROJECTS_KEY
  #try:
  f = open(fname)
  grade_dict = {}
  reader = csv.reader(f)
  for row in reader:
    cat_name = row[CATEGORY_INDEX]
    if cat_name == 'Assignment Group':
      continue
    if cat_name not in grade_dict:
      grade_dict[cat_name] = []
    grade_dict[cat_name].append(int(row[EXPECTED_SCORE_INDEX]))
  return grade_dict
  # except:
  #   print('couldn\'t find a file called', fname)
  #   exit() # no point in going on


# param: list of lecture excercise scores
# return: total scores for lecture exercises, after dropping lowest 4
def calculate_lecture_exercise_score(lecture_scores):
  lecture_scores.sort(reverse=True)
  adjusted_scores = lecture_scores[0:22]
  total = 0
  for score in adjusted_scores:
    total += score
  return total

# param: list of discussion scores
# return: total scores for discussions, dropping lowest 2
def calculate_discussion_score(discussion_scores):
  discussion_scores.sort(reverse=True)
  adjusted_scores = discussion_scores[0:11]
  total = 0
  for score in adjusted_scores:
    total += score
  return total

# param: list of homework scores
# return: total points for homeworks, after dropping lowest 2
def calculate_homework_score(homework_scores):
  homework_scores.sort(reverse=True)
  adjusted_scores = homework_scores[0:12]
  total = 0
  for score in adjusted_scores:
    total += score
  return total

# param: list of midterm scores
# return: total points for midterm category
def calculate_midterm_score(midterm_scores):
  total = 0
  for score in midterm_scores:
    total += score
  return total

# param: list of project scores
# return: total points for project category
def calculate_project_score(project_scores):
  total = 0
  for score in project_scores:
    total += score
  return total

# given the total points earned, converts to the final letter grade
# param: total_score
# return: string representing a letter grade
def convert_to_letter_grade(total_score):
  '''
  INFO FROM SYLLABUS
  Total points available: 1560
  A+  >100 %
  A   94-99.99%
  A-  90-93.99%
  B+  87-89.99%
  B   83-86.99%
  B-  80-82.99%
  C+  77-79.99%
  C   73-76.99%
  C-  70-72.99%
  D+  67-69.99%
  D   63-66.99%
  D-  60-62.99%
  E/F 0-59.99%
'''
  MAX_POINTS = 1560
  percent_grade = total_score / MAX_POINTS

  if percent_grade >= 1.0:
    return 'A+'
  elif percent_grade >= 0.94:
    return 'A'
  elif percent_grade >= 0.90:
    return 'A-'
  elif percent_grade >= 0.87:
    return 'B+'
  elif percent_grade >= 0.83:
    return 'B'
  elif percent_grade >= 0.80:
    return 'B-'
  elif percent_grade >= 0.77:
    return 'C+'
  elif percent_grade >= 0.73:
    return 'C'
  elif percent_grade >= 0.70:
    return 'C-'
  elif percent_grade >= 0.67:
    return 'D+'
  elif percent_grade >= 0.63:
    return 'D'
  elif percent_grade >= 0.60:
    return 'D-'
  else:
    return 'F'

######################
## GLOBAL variables ##
######################
DEFAULT_FILENAME = 'grade_estimates.csv'

HOMEWORKS_KEY   = 'Homeworks'
LECTURES_KEY    = 'Lecture Exercises'
DISCUSSIONS_KEY = 'Section Attendance'
MIDTERMS_KEY    = 'Midterms'
PROJECTS_KEY    = 'Projects'
FINAL_KEY       = 'Final Project'

##################
## TEST Program ##
##################
def test():
  print('running tests')

  ## TEST 1: Test score calculations
  test_homeworks1 = [20, 20, 20, 20,
                     20, 20, 20, 20,
                     20, 20, 20, 20,
                     20, 20]
  expected_homework_score1 = 20 * 12


  test_homeworks2 = [10, 10, 12, 12,
                     14, 14, 16, 16,
                     18, 18, 20, 20,
                     22, 24]
  expected_homework_score2 = 12 + 12 + 14 + 14 \
                           + 16 + 16 + 18 + 18 \
                           + 20 + 20 + 22 + 24

  if (calculate_homework_score(test_homeworks1) == expected_homework_score1):
    print ('TEST 1.1 passed')
  else:
    print ('TEST 1.1 failed')

  if (calculate_homework_score(test_homeworks2) == expected_homework_score2):
    print ('TEST 1.2 passed')
  else:
    print ('TEST 1.2 failed')

  ## TEST 2: Test final grade calculations
  points1 = 1561
  expected1 = 'A+'
  points2 = 1560 * .99
  expected2 = 'A'
  points3 = 1560 * .73
  expected3 = 'C'
  points4 = 1560 * .20
  expected4 = 'F'

  if convert_to_letter_grade(points1) == expected1:
    print('TEST 2.1 passed')
  else:
    print('TEST 2.1 failed')

  if convert_to_letter_grade(points2) == expected2:
    print('TEST 2.2 passed')
  else:
    print('TEST 2.2 failed')

  if convert_to_letter_grade(points3) == expected3:
    print('TEST 2.3 passed')
  else:
    print('TEST 2.3 failed')

  if convert_to_letter_grade(points4) == expected4:
    print('TEST 2.4 passed')
  else:
    print('TEST 2.4 failed')


  ## TEST 3: Create grade_dict from file
  TEST_FILENAME = DEFAULT_FILENAME
  grade_dict = get_data(TEST_FILENAME)
  if (HOMEWORKS_KEY in grade_dict and
      LECTURES_KEY in grade_dict and
      DISCUSSIONS_KEY in grade_dict and
      MIDTERMS_KEY in grade_dict and
      PROJECTS_KEY in grade_dict and
      FINAL_KEY in grade_dict):
    print ('TEST 3 passed')
  else:
    print ('TEST 3 failed')

  ## TEST 4: Check score lists
  if (len(grade_dict[HOMEWORKS_KEY]) == 14 and
      len(grade_dict[LECTURES_KEY]) == 26):
    print ('TEST 3 passed')
  else:
    print ('TEST 3 failed')


##################
## MAIN Program ##
##################

testing = True

# run this until all tests pass, then set testing=False
if (testing):
  test()
  exit()

grade_dict = get_data(DEFAULT_FILENAME)
total_score = 0
if HOMEWORKS_KEY in grade_dict:
  total_score += calculate_homework_score(grade_dict[HOMEWORKS_KEY])
if LECTURES_KEY in grade_dict:
  total_score += calculate_lecture_exercise_score(grade_dict[LECTURES_KEY])
if DISCUSSIONS_KEY in grade_dict:
  total_score += calculate_discussion_score(grade_dict[DISCUSSIONS_KEY])
if MIDTERMS_KEY in grade_dict:
  total_score += calculate_midterm_score(grade_dict[MIDTERMS_KEY])
if PROJECTS_KEY in grade_dict:
  total_score += calculate_project_score(grade_dict[PROJECTS_KEY])
if FINAL_KEY in grade_dict and len(grade_dict[FINAL_KEY]) > 0:
  total_score += grade_dict[FINAL_KEY][0]

letter_grade = convert_to_letter_grade(total_score)
print('You will get a', letter_grade, 'with', total_score, 'points')
