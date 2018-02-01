
# reads a CSV from a file, and creates a dictionary of this form:
# grade_dict['homeworks'] = [20, 20, 20, ...]
# grade_dict['lectures'] = [5, 5, 5, ...]
# ...
# params: none
# returns: a dictionary as specified above
def get_data():
  return {}

# param: list of lecture excercise scores
# return: total scores for lecture exercises, after dropping lowest 4
def calculate_lecture_exercise_score(lecture_scores):
    return 0

# param: list of discussion scores
# return: total scores for discussions, dropping lowest 2
def calculate_discussion_score(discussion_scores):
  return 0

# param: list of homework scores
# return: total points for homeworks, after dropping lowest 2
def calculate_homework_score(homework_scores):
  return 0

# param: list of midterm scores
# return: total points for midterm category
def calculate_midterm_score(midterm_scores):
  return 0

# param: list of project scores
# return: total points for project category
def calculate_project_score(project_scores):
  return 0

# given the total points earned, converts to the final letter grade
# param: total_score
# return: string representing a letter grade
def convert_to_letter_grade(total_score):
  return 'X'

def test():
    #test for calculate_homework_score
    homeworks=[20,20,20,20,20,20,20,20,20,20,20,20,20,20]
    expected_output= 20 * 12
    homeworks2= [10,10,12,12,14,14,16,16,18,18,20,20,22,22]
    expected_output2= 12+12+14+14+16+16+18+18+20+20+22+22
    if calculate_homework_score(homeworks)== expected_output:
        print('pass 1')
    else:
        print('fail 1')
    if calculate_homework_score(homeworks2)== expected_output2:
        print('pass 2')
    else:
        print('fail 2')


grade_dict = get_data()
total_score = 0
if 'homeworks' in grade_dict:
    total_score += calculate_homework_score(grade_dict['homeworks'])

# same for the other categories

letter_grade = convert_to_letter_grade(total_score)
print('You will get a', letter_grade, 'with', total_score, 'points')

# write some tests here
