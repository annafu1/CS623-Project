import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

#For isolation: SERIALIZABLE
conn.set_isolation_level(3)

#For atomicity
conn.autocommit = False

try:
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Delete p1 from the product id in the Stock table
    cur.execute("""
        DELETE FROM stock
        WHERE stock.prod_id = 'p1'
    """)

    # Delete p1 from the product id in the Product table
    cur.execute("""
        DELETE FROM product
        WHERE product.prod_id = 'p1'
    """)

    # Insert the new pp1 to Product table
    cur.execute("""
        INSERT INTO product (prod_id, pname, price)
        VALUES ('pp1', 'tape', 2.5)
    """)

    # Update the prod_id in the product table
    cur.execute("""
        UPDATE product
        SET prod_id = 'pp1'
        WHERE prod_id = 'p1'
    """)

    # Insert the new pp1 to Stock table
    cur.execute("""
        INSERT INTO stock (prod_id, dep_id, quantity)
        VALUES ('pp1', 'd1', 100000),
               ('pp1', 'd2', -100),
               ('pp1', 'd4', 12000)
    """)

    # Commit the transaction if everything is successful
    conn.commit()

except (Exception, psycopg2.DatabaseError) as e:
    # Rollback the transaction if an error occurs
    conn.rollback()
    print(f"Error: {e}")

finally:
    if conn:
        # Commit the transaction if everything is successful
        conn.commit()
        cur.close()
        conn.close()
        print("PostgreSQL connection is now closed")

print("End")