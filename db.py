import psycopg

# Dati di connessione al database
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "user_admin"
DB_PASS = "admin"

try:
    # Connessione al database
    with psycopg.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST}") as conn:
        print("Connessione a PostgreSQL avvenuta con successo!")

        # Creazione di un cursore
        with conn.cursor() as cur:
            # Esecuzione di una query
            cur.execute("CREATE TABLE schema.a(num INTEGER PRIMARY KEY)")


except psycopg.OperationalError as e:
    print(f"Errore di connessione al database: {e}")

except Exception as e:
    print(f"Si è verificato un errore: {e}")