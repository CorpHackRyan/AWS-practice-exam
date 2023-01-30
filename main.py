import random
import time

def rand_num_gen():
    question_num = random.randint(1, 891)
    return question_num

if __name__ == '__main__':
    total_questions = 0
    correct_answers = 0
    start_time = time.time()

    keep_going = True
    while keep_going:
        question_from_text = "QUESTION " + str(rand_num_gen())
        with open("aws_test.txt", "r") as aws_test_file:
            searchlines = aws_test_file.readlines()
        for i, line in enumerate(searchlines):
            if str(question_from_text) in line:
                question_index = i
                print("\n" + line)
                for j in range(question_index+1, len(searchlines)):
                    if "Correct Answer" in searchlines[j]:
                        correct_answer = searchlines[j].split(":")[1].strip()
                        break
                    print(searchlines[j].strip())
                total_questions += 1
                question_start_time = time.time()
                user_answer = input("Enter your answer: ")
                question_elapsed_time = time.time() - question_start_time

                if user_answer.strip() == correct_answer:
                    correct_answers += 1
                    print("Correct!")
                else:
                    print(f"Incorrect! The correct answer is {correct_answer}")
                break
        score = correct_answers/total_questions * 100
        elapsed_time = time.time() - start_time
        print(f"Score: {correct_answers}/{total_questions} ({score:.2f}%)")
        print(f"Time taken for this question: {question_elapsed_time // 60:.0f} minutes and {question_elapsed_time % 60:.0f} seconds")
        print(f"Total time taken: {elapsed_time//3600:.0f} hours and {(elapsed_time%3600)//60:.0f} minutes")
        keep_going = input("\n" + "Do you want to continue? (y/n) ") == 'y'
