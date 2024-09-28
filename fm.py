from pyamf.remoting.client import RemotingService
from pyamf.remoting import RemotingError
import json
import time
from concurrent.futures import ThreadPoolExecutor

def amf_service_call(service_name, params):
    remoting_gateway = "https://amf.playshinobirevenge.com/"
    try:
        client = RemotingService(remoting_gateway)
        service = client.getService(service_name)
        response = service(params)
        response_new = str(response)
        response_new = response_new.replace("'", '"')
        response_new = response_new.replace("False", 'false')
        response_new = response_new.replace("True", 'true')
        response_new = response_new.replace('None', 'null')
        return response_new
    except RemotingError:
        return {'respuesta': 'er1'}
    except Exception:
        return {'respuesta': 'er2'}
    except:
        return {'respuesta': 'er3'}

def login(user, contra):
    return amf_service_call("SystemLogin.loginUser", [user, contra])

def getchars(accountid, userkey):
    return amf_service_call("SystemLogin.getAllCharacters", [accountid, userkey])

def claimDaily(userID, userKey):
    params = [userID, userKey, "normal", 3]
    return amf_service_call("DailyService.executeService", ["claimReward", params])

# Proceso individual para cada cuenta
def process_account(account):
    try:
        user, contra = account.split()
        print(f"Iniciando sesión para: {user}")
        
        resp = login(user, contra)
        data = json.loads(resp)

        # Obtener personajes
        resp = getchars(data["uid"], data["sessionkey"])
        data2 = json.loads(resp)
        charID = data2["account_data"][0]["char_id"]

        # Realizar el proceso de reclamación diaria cada 2 segundos
        contador = 0
        while contador < 10000:
            contador += 1
            resp = claimDaily(charID, data["sessionkey"])
            print(f"{user} - Reclamación {contador}: {resp}")
            time.sleep(2)  # Pausa de 2 segundos entre cada solicitud
    
    except Exception as e:
        print(f"Error al procesar la cuenta {account}: {e}")

# Lista de cuentas
accounts = [
    'shadowp z'
]

# Ejecutar todos los procesos simultáneamente usando ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=len(accounts)) as executor:
    executor.map(process_account, accounts)

# from pyamf.remoting.client import RemotingService
# from pyamf.remoting import RemotingError
# import json
# import time
# from concurrent.futures import ThreadPoolExecutor

# def amf_service_call(service_name, params):
#     remoting_gateway = "https://amf.playshinobirevenge.com/"
#     try:
#         client = RemotingService(remoting_gateway)
#         service = client.getService(service_name)
#         response = service(params)
#         response_new = str(response)
#         response_new = response_new.replace("'", '"')
#         response_new = response_new.replace("False", 'false')
#         response_new = response_new.replace("True", 'true')
#         response_new = response_new.replace('None', 'null')
#         return response_new
#     except RemotingError:
#         return {'respuesta': 'er1'}
#     except Exception:
#         return {'respuesta': 'er2'}
#     except:
#         return {'respuesta': 'er3'}

# def login(user, contra):
#     return amf_service_call("SystemLogin.loginUser", [user, contra])

# def getchars(accountid, userkey):
#     return amf_service_call("SystemLogin.getAllCharacters", [accountid, userkey])

# def claimDaily(userID, userKey):
#     params = [userID, userKey, "normal", 3]
#     return amf_service_call("DailyService.executeService", ["claimReward", params])

# # Proceso individual para cada cuenta
# def process_account(account):
#     try:
#         user, contra = account.split()
#         print(f"Iniciando sesión para: {user}")
        
#         resp = login(user, contra)
#         data = json.loads(resp)

#         # Obtener personajes
#         resp = getchars(data["uid"], data["sessionkey"])
#         data2 = json.loads(resp)
#         charID = data2["account_data"][0]["char_id"]

#         # Realizar el proceso de reclamación diaria cada 2 segundos
#         contador = 0
#         while contador < 10000:
#             contador += 1
#             resp = claimDaily(charID, data["sessionkey"])
#             print(f"{user} - Reclamación {contador}: {resp}")
#             time.sleep(2)  # Pausa de 2 segundos entre cada solicitud
    
#     except Exception as e:
#         print(f"Error al procesar la cuenta {account}: {e}")

# # Lista de cuentas
# accounts = [
#     'spirit 2393', 'Hash 2393', 'Dan 2393', 'darkness 2393', 'kill 2393', 'latin 2393', 
#     'js 2393', 'blackx 2393', 'orion 2393', 'ryden 2393', 'saruma 2393', 'Mizukage 2393', 
#     'darknes 2393', 'aeon 2393', 'firecracker 2393', 'saphire 2393', 'donovan 2393', 
#     'queen 2393', 'blackcode 2393', '123456789 2393', 'abcxyz 2393', 'gayelquelolea 2393', 'kazes 2393'
# ]

# # Ejecutar todos los procesos simultáneamente usando ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=len(accounts)) as executor:
#     executor.map(process_account, accounts)



