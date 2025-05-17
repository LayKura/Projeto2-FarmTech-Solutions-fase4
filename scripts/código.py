import oracledb, pandas as pd, datetime, time, random

conn = oracledb.connect(user='rm562274', password='090402', dsn='oracle.fiap.com.br:1521/ORCL')
cursor = conn.cursor()

# Inserção de dado
def inserir_dado(umidade, ph, fosforo, potassio, bomba):
    timestamp = datetime.now().isoformat()
    cursor.execute('''
    INSERT INTO sensores (timestamp, umidade, ph, fosforo, potassio, bomba)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, umidade, ph, fosforo, potassio, bomba))
    conn.commit()

# Consulta
def listar_dados():
    cursor.execute('SELECT * FROM sensores')
    return cursor.fetchall()

# Atualizar dado
def atualizar_dado(id, campo, valor):
    cursor.execute(f'''
    UPDATE sensores SET {campo} = ? WHERE id = ?
    ''', (valor, id))
    conn.commit()

# Remover dado
def deletar_dado(id):
    cursor.execute('DELETE FROM sensores WHERE id = ?', (id,))
    conn.commit()

# Função para inserir dados simulados
def leitura_simulada(loop):
    df = pd.DataFrame({'data':'', 'umidade':'', 'ph':'', 'fosforo':'', 'potassio':'', 'bomba':''})
    for _ in range(loop):
        sensor_p = random.randint(0, 1)
        sensor_k = random.randint(0, 1)
        ph = round(random.uniform(4.5, 8.0), 2)
        umidade = round(random.uniform(10.0, 80.0), 1)
        rele_status = 'ON' if umidade < 40.0 else 'OFF'
        data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"[{data_hora}] Inserido: P={sensor_p}, K={sensor_k}, pH={ph}, Umidade={umidade}, Relé={rele_status}")
        
        # df = pd.DataFrame({'data':'', 'umidade':'', 'ph':'', 'fosforo':'', 'potassio':'', 'bomba':''})
        
        df['data'].add(data_hora)


leitura_simulada(100)
time.sleep(1)

conn.close()