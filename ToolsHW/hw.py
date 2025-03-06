import webbrowser, sys, time, random, os  

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
numbers_list = [i for i in range(100)]  
is_correct_answer = False  
unused_variable = "Unused variable"  
empty_list = [None] * 50  
empty_dict = {}
error_count = 0

def input_math():
    global is_correct_answer, error_count, undefined_variable
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                open_video()
                B1 = True
                UndefinedVar += 1  
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                open_video()
                error_count += 1
    except:
        error_count -= 1
        pass 

def open_video():
    webbrowser.open(video_url)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 1

class UselessClass:
    def __init__(self):
        self.int_value = 1
        self.str_value = "string"
        self.num_list = [1, 2, 3]
        self.key_value_pair = {"key": "value"}
        self.null_value = None
        self.unused = 100

    def useless_method(self):
        try:
            print(self.int_value + self.str_value)
            raise RuntimeError("Fake error")
        except:
            pass 

class AnotherUselessClass(UselessClass, int): 
    def another_method(self):
        for i in range(1000):
            try:
                print(i)
                if i % 100 == 0:
                    raise KeyError("Fake KeyError")
            except:
                pass 

input_math()
