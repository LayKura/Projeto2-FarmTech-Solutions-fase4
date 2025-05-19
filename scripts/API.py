import random
import oracledb
from datetime import datetime
import time

# Conecta/cria banco
# conn = oracledb.connect(user='rm562274', password='090402', dsn='oracle.fiap.com.br:1521/ORCL')
# cursor = conn.cursor()

# def leitura_simulada():
#     sensor_p = random.randint(0, 1)
#     sensor_k = random.randint(0, 1)
#     ph = round(random.uniform(4.5, 8.0), 2)
#     umidade = round(random.uniform(10.0, 80.0), 1)
#     rele_status = 'ON' if umidade < 40.0 else 'OFF'
#     data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    
#     cursor.execute('''
#     INSERT INTO sensores (time, umidade, ph, fosforo, potassio, bomba)
#     VALUES (:1, :2, :3, :4, :5, :6)
#     ''', (data_hora, umidade, ph, sensor_k, sensor_p, rele_status))
#     conn.commit()

#     print(f"[{data_hora}] Inserido: P={sensor_p}, K={sensor_k}, pH={ph}, Umidade={umidade}, Relé={rele_status}")

# # Loop de leitura
# for _ in range(100):
#     leitura_simulada()
#     time.sleep(1)

# conn.close()
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))