import random

def rand_num_gen():
    question_num = random.randint(1, 891)
    return question_num

if __name__ == '__main__':

    keep_going = True

    while keep_going:
        question_from_text = "QUESTION " + str(rand_num_gen())
        with open("aws_test.txt", "r") as aws_test_file:
            searchlines = aws_test_file.readlines()
        for i, line in enumerate(searchlines):
            if str(question_from_text) == line.rstrip():
                question_index = i
                question_num = line.split(' ')[1]
                print("LINE NUMBER: " + str(question_index + 1))
                print("QUESTION NUMBER: " + question_num)
                print("QUESTION: " + searchlines[question_index + 1].rstrip())
                print("OPTIONS:")
                option_index = question_index + 2
                while "Correct Answer" not in searchlines[option_index]:
                    print(searchlines[option_index].rstrip())
                    option_index += 1
                correct_answer = searchlines[option_index].split(': ')[1].rstrip()
                print("\nCorrect Answer: " + correct_answer)
                keep_going = False
