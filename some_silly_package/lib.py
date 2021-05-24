import time

def try_me():
    for i in range (0, 5):
        print(5 - i, "."*(5 - i))
        time.sleep(1)
    print("########################")
    print("#      ||||||||        #")
    print("#      |      |        #")
    print("#     @| 0  0 |@       #")
    print("#      |  * *  |       #")
    print("#      |. ___. |       #")
    print("#      |_______|       #")
    print("#         | |          #")
    print("########################")

if __name__ == "__main__":
    try_me()