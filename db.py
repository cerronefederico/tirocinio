import psycopg

# Dati di connessione al database
DB_HOST = "localhost"
DB_NAME = "miodatabase"
DB_USER = "mio_utente"
DB_PASS = "mia_password"

try:
    # Connessione al database
    with psycopg.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST}") as conn:
        print("Connessione a PostgreSQL avvenuta con successo!")

        # Creazione di un cursore
        with conn.cursor() as cur:
            # Esecuzione di una query
            cur.execute("SELECT * FROM utenti;")

            # Recupero di tutti i risultati
            righe = cur.fetchall()

            # Stampa delle righe
            for riga in righe:
                print(riga)

except psycopg.OperationalError as e:
    print(f"Errore di connessione al database: {e}")

except Exception as e:
    print(f"Si è verificato un errore: {e}")