import random


def rand_num_gen():
    question_num = random.randint(1, 891)
    return question_num


if __name__ == '__main__':
    aws_test_file = "aws_test.txt"

    while True:
        question_from_text = rand_num_gen()
        print(question_from_text)



