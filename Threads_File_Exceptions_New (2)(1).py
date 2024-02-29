#https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
# Python program showing
# how to kill two threads
# using exception handling (Keyboard Interrupt)
# flag
 
import keyboard
import threading, time, random, datetime, csv

filename = ""

stop_thread_2 = False
stop_thread_1 = False
key_one = "1"
key_two = "2"
lock = threading.Lock()

def run1():
    while True:
        time.sleep(random.randint(1,5)) #sleep random second
        #print('thread 1 running\n')
        global stop_thread_1
        with lock:
            if stop_thread_1:
                print("T1 Stopped")
                break
            print("T1 has the lock\n")
            value = random.randrange(1,100)
            with open(filename,"a+") as out:
                cw=csv.writer(out, delimiter = "\t", lineterminator = "\n", quotechar = '"')
                ranString=str(value)
                ranDate=("T1: "+str(datetime.datetime.now()))
                cw.writerow([ranDate, ranString])

def run2():
    while True:
        time.sleep(random.randint(1,5)) #sleep random second
        #print('thread 2 running\n')
        global stop_thread_2
        with lock:
            if stop_thread_2:
                print("T2 Stopped")
                break
            print("T2 has the lock:\n")
            value = random.randrange(100,10000)
            with open(filename,"a+") as out:
                cw=csv.writer(out, delimiter = "\t", lineterminator = "\n", quotechar = '"')
                ranString=str(value)
                ranDate=("T2: "+str(datetime.datetime.now()))
                cw.writerow([ranDate, ranString])


def handleKeypress(key):
    global stop_thread_1
    global stop_thread_2
    if keyboard.is_pressed(key_one):
        stop_thread_1 = True
    if keyboard.is_pressed(key_two):
        stop_thread_2 = True

def main():
    global stop_threads, filename
    
    actualTime=datetime.datetime.now()
    BaseName=actualTime.strftime("%Y%m%d_%H:%M:%S")
    ProbandName = input("Insert proband's name: ")
    filename = "./Data/"+ BaseName + "_" + ProbandName + ".csv"
    print("filename: "+ filename)
    t1 = threading.Thread(target = run1)
    t1.start()

    t2 = threading.Thread(target = run2)
    t2.start()
    keyboard.on_press(handleKeypress)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_threads = True
        pass
    finally:
        t1.join()
        t2.join()
        print('Keyboard Interrupt detected! -> threads killed')
        print('End main')

if __name__ == '__main__':
    main()
