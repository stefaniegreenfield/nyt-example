#13 discussions drop 2
#14 homeworks drop 2
#26 leture exercises drop 4
#2 midterms
#3 projects
#1 final project

#what our program needs to do:
#add points- third step
#drop scores-sort- second step
#get data- first step
#convert to letter grade- fifth step
#convert to percentage- fourth step

def get_data():
    pass

#return a sorted list of scores for a particular type of assignment
#param: list of scores
#return: sorted list of scores
def sorted_scores(scores):
    pass

#params: list of scores
#return: total score after dropping lowest 4
def calculate_lecture_exercise_score(lecture_scores):
    pass

#params: list of scores
#return: total score after dropping lowest 2
def calculate_discussion_exercise_score(discussion_scores):
    pass

#params: list of scores
#return: total score after dropping lowest 2
def calculate_homework_score(homework_scores):
    pass

#params: list of scores
#return: total score
def calculate_midterm_score(midterm_scores):
    pass

#params: list of scores
#return: total score
def calculate_project_score(project_scores):
    pass

#param: total score after dropping and applying policies
#return: float representing a percentage between 0,1
def convert_to_percent(total_score):
    pass

#param: percentage score
#return: string representing a letter grade
def convert_to_letter_grade(percentage_score):
    pass
