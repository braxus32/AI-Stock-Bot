"""
 Name: Your Name
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: the current date
 Sources consulted: any books, individuals, etc consulted
 Known Bugs: description of known bugs and other program imperfections
 Creativity: anything extra that you added to the lab
 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math
import random

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    # your code here
    with open(data,"rb") as file:
            data = file.read().split("\n")
        trainData = data[:70]
        testData = data[30:]
        ratio = ((trainData + testData) / 2)


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    # your code here
    with open(data,"rb") as file:
            data = file.read().split("\n")
        random.shuffle(data)
        trainData = data[:70]
        testData = data[30:]

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    if mode == "S":
      data = options.data 
      trainData = options.trainData
      testData = options.testData
      ratio = options.ratio
    if data == '' or trainData == '' or testData == '' or ratio == '' :
      showHelper()
    splitData(data, trainData, testData, ratio) 
    
    if mode == "R":
      data = options.data 
      trainData = options.trainData
      testData = options.testData
      ratio = options.ratio
    if data == '' or trainData == '' or testData == '' or ratio == '' :
      showHelper()
    splitDataRandom(data, trainData, testData, ratio)
    

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("Please provide input augument.\n",
            "'S' for Split Mode.\n",
            "'R' for Random Split Mode.\n",
            "Here are examples:")
    print("python " + sys.argv[0] + " --mode S --data data.txt --trainData trainData.txt --testData testData.txt --ratio 0.5")
    print("python " + sys.argv[0] + " --mode R --data data.txt --trainData trainData.txt --testData testData.txt --ratio 0.5")

    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    # your code here
    if len(sys.argv)<3:
        showHelper()
    main()
