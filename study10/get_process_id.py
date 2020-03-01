# Author:Fuhong Gao
import multiprocessing,os
def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process id:',os.getppid()) #打印父进程的id
    print('process id:',os.getpid()) #打印当前进程的id
    print('\n')
def f(name):
    info('\033[31;1mcalled child process from function f\033[0m')#每一个进程都是由其父进程启动的
    print('Hello,',name)
if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = multiprocessing.Process(target=f,args=('Fuhong Gao',))
    p.start()