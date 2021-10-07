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
                print("    LINE #: " + str(i+1))
                print("LINE VALUE: " + line)
            keep_going = False

        #print(question_from_text)
