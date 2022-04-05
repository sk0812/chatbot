import os.path
import shutil

answer = input("Are you sure you want to remove all the trained data and python cache files?: ")
if answer == "yes":
    if os.path.exists("tflearn_logs"):
        shutil.rmtree("tflearn_logs")
        print("Successfully deleted tflearn_logs")
    else:
        print("tflearn_logs does not exist")
    if os.path.exists("checkpoint"):
        os.remove("checkpoint")
        print("Successfully deleted checkpoint")
    else:
        print("checkpoint does not exist")
    if os.path.exists("model.tflearn.data-00000-of-00001"):
        os.remove("model.tflearn.data-00000-of-00001")
        print("Successfully deleted model.tflearn.data-00001-of-00001")
    else:
        print("model.tflearn.data-00001-of-00001 does not exist")
    if os.path.exists("model.tflearn.meta"):
        os.remove("model.tflearn.meta")
        print("Successfully deleted model.tflearn.meta")
    else:
        print("model.tflearn.meta does not exist")
    if os.path.exists("model.tflearn.index"):
        os.remove("model.tflearn.index")
        print("Successfully deleted model.tflearn.index")
    else:
        print("model.tflearn.index does not exist")
    if os.path.exists("training_data"):
        os.remove("training_data")
        print("Successfully deleted training_data")
    else:
        print("training_data does not exist")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
        print("Successfully deleted __pycache__")
    else:
        print("__pycache__ does not exist")
    if os.path.exists("skills/weather/__pycache__"):
        shutil.rmtree("skills/weather/__pycache__")
        print("Successfully deleted __pycache__ from skills/weather")
    else:
        print("unable to delete __pycache__ form skills/weather")
    if os.path.exists("skills/websites/__pycache__"):
        shutil.rmtree("skills/websites/__pycache__")
        print("Successfully deleted __pycache__ from websites")
    else:
        print("__pycache__ does not exist in websites")
    if os.path.exists("skills/weather/__pycache__"):
        shutil.rmtree("skills/weather/__pycache__")
        print("successfully deleted __pycache__ from weather")
    else:
        print("__pycache__ does not exist in weather")
    if os.path.exists("skills/misc/__pycache__"):
        shutil.rmtree("skills/misc/__pycache__")
        print("successfully deleted __pycache__ from misc")
    else:
        print("__pycache__ does not exist in misc")
    if os.path.exists("skills/search/__pycache__"):
        shutil.rmtree("skills/search/__pycache__")
        print("successfully deleted __pycache__ from search")
    else:
        print("__pycache__ does not exist in search")
    if os.path.exists("skills/terminal/__pycache__"):
        shutil.rmtree("skills/terminal/__pycache__")
        print("Successfully deleted __pycache__ from terminal")
    else:
        print("__pycache__ does not exist in terminal")
    if os.path.exists("skills/todo_list/__pycache__"):
        shutil.rmtree("skills/todo_list/__pycache__")
        print("Successfully deleted __pycache__ from todo list")
    else:
        print("__pycache__ does not exist in todo list")