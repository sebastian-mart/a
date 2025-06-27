import threading
from threading import Lock, RLock, Semaphore

def write(i,file,l):
    l.acquire()
    f=open(file,'a')
    f.write(f"{i} ")
    if i<=0:
        f.write("\n")
    else:
        write(i-1,file,l)
    l.release()


def main():
    lock = Lock()
    rlock = RLock()
    semaphore = Semaphore(2)
    t1=threading.Thread(target=write,args=[2,"lock.txt",lock])
    t2 = threading.Thread(target=write, args=[0, "lock.txt", lock])
    t3 = threading.Thread(target=write, args=[2, "rlock.txt", rlock])
    t4 = threading.Thread(target=write, args=[2, "sem.txt", semaphore])

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()

