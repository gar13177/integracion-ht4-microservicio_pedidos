import threading, time, json

from testing.integration.login_test import LoginRpcClient

NUMBER_OF_THREADS = 10
WORK_FOR_THREAD = 20

stats = {
    "login":{
        "times":[],
        "duration":0.0
    },
    "order":{
        "times":[],
        "duration":0.0
    }
}

def multiple_login(stats):
    times = []
    inicio_de_sesion = {
        "user":"prueba@prueba",
        "password": "prueba"
    }
    login_rpc = LoginRpcClient()
    for i in range(WORK_FOR_THREAD):
        init_time = time.time()
        response = login_rpc.call(json.dumps(inicio_de_sesion))
        times.append(time.time()-init_time) # se agrega solamente la diferencia de tiempo
    stats['login']['times'].append(times)

def stress_test_login():
    threads = []
    init_time = time.time()
    for i in range(NUMBER_OF_THREADS):
        thread = threading.Thread(name='Thread'+str(i), target=multiple_login, args=(stats,))
        threads.append(thread)
        try:
            print ("Iniciando thread "+str(i))
            thread.start()
        except Exception as e:
            print ("error en thread: "+str(e.message))
    
    print ("threads iniciados")
    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            print("error en join al thread "+str(e.message))
    stats['login']['duration']=time.time()-init_time
    print ("threads finalizados")

def stress_test():
    stress_test_login()
    print("login threads: "+str(len(stats['login'])))
    print("login number: "+str(NUMBER_OF_THREADS*WORK_FOR_THREAD))
    print("login avg time: "+str(sum([sum(row) for row in stats['login']['times']])/(NUMBER_OF_THREADS*WORK_FOR_THREAD)))
    print("login test duration: "+str(stats['login']['duration']))