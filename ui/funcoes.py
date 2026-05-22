import psycopg2

def conexao():
    try:
        conexao = psycopg2.connect(database = "defaultdb", host = "pg-20fe24c4-ilaninhaaa22-0019.i.aivencloud.com", user = "avnadmin", password = "AVNS_dUBTFOg8pU7MRHo_ied", port= "21277", sslmode="require")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar {e}")
        return None
    
