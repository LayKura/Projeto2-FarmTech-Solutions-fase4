import oracledb, pandas as pd, datetime, os, time

conn = oracledb.connect(user='rm562274', password='090402', dsn='oracle.fiap.com.br:1521/ORCL')
cursor = conn.cursor()

# Inserção de dado
def inserir_dado(umidade, ph, fosforo, potassio, bomba):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO sensores (time, umidade, ph, fosforo, potassio, bomba)
    VALUES (:1, :2, :3, :4, :5, :6)
    ''', (time, umidade, ph, fosforo, potassio, bomba))
    conn.commit()

# Consulta
def listar_dados(min: str | None = ..., max:str | None = ..., date_options: bool = False):
    if date_options == True:
        cursor.execute(f'SELECT * FROM sensores where time between {min} and {max}')
    else:
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

while True:
    os.system('cls')
    menu_option = int(input(f'''{'-'*15}
Seleciona a ação que deseja realizar

[1] Inserir dados
[2] Consultar dados cadastrados
[3] Atualizar dados cadastrados
[4] Excluir dados cadastrados
[5] Sair
{'-'*15}
R: '''))
    try:
        match menu_option:
            case 1:
                os.system('cls')
                while True:
                    try:
                        umidade = int(input('Umidade: '))
                        ph = int(input('PH: '))
                        fosforo = input('Fosforo: ')
                        potassio = int(input('Potassio: '))
                        bomba = input('RELÉ ON ou OFF?: ')
                        bomba = bomba.upper()
                        os.system('cls')

                        if bomba not in ['ON','OFF']:
                            raise ValueError('O Valor da bomba está errado, apenas os valores ON e OFF são compativeis.')
                        
                        inserir_dado(umidade, ph, fosforo, potassio, bomba)
                    except Exception as e:
                        print(f'Erro:{e}')
                        
                    option_1 = int(input('Deseja inserir mais algum dado?:\n1-SIM\n2-NÃO\nR: '))
                    if option_1 == 1:
                        continue
                    elif option_1 == 2:
                        break
                    else:
                        os.system('cls')
                        input('OPÇÃO INVALIDA: Pressione enter para voltar ao MENU')
            
            case 2:
                os.system('cls')
                try:
                    option_2 = int(input('Deseja fazer a consulta com um range de data?\n1-SIM\n2-NÃO\nR: '))
                    if  option_2 == 1:
                        date_min = input('Digite a data minima que deseja pesquisar seguinte o padrão ANO-MES-DIA\nR: ')
                        date_max = input('Digite a data maxima que deseja pesquisar seguinte o padrão ANO-MES-DIA\nR: ')
                        df = listar_dados(date_min, date_max, True)
                    else:
                        df = listar_dados()
                    os.system('cls')
                    print(df)
                    input('Aperte enter para voltar ao MENU')
                ## Armazena os dados de cadastro em formato de dicionário
                except Exception as e:
                    os.system('cls')
                    print(f'ERRO: {e}')
                    time.sleep(2)


            case 5:
                conn.close()
                exit()

    except Exception as error:
        os.system('cls')
        print(f'ERRO: {error}')
            
            