import pymysql
import openpyxl

# Configurar as informações de conexão
host = '192.168.1.14'  # Endereço do servidor MySQL
user = 'root'  # Seu nome de usuário
password = 'root_password'  # Sua senha
db = 'dados'  # Nome do banco de dados

# Conectar ao banco de dados
conn = pymysql.connect(host=host, user=user, password=password, db=db)

try:
    # Criar um cursor para executar consultas SQL
    cursor = conn.cursor()

    # Definir a consulta SQL que deseja executar
    query = "SELECT * FROM plantao"

    # Executar a consulta
    cursor.execute(query)

    # Recuperar os resultados
    results = cursor.fetchall()

    # Criar uma nova planilha XLSX
    wb = openpyxl.Workbook()
    ws = wb.active

    # Adicionar cabeçalhos às colunas
    column_names = [i[0] for i in cursor.description]
    ws.append(column_names)

    # Adicionar os resultados à planilha
    for row in results:
        ws.append(row)

    # Salvar a planilha em um arquivo
    wb.save('resultado.xlsx')

finally:
    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()
