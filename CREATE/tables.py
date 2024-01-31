from base import Database

def create_payment_type():
       query = f"""
       CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT NOW ())"""
       data = Database.connect("localhost","universitet","postgres","azizbek",query)
       print(data)

def create_address():
       query = f"""
       CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            city_id INT REFERENCES city(city_id),
            last_update TIMESTAMP DEFAULT NOW ())"""
       status = Database.connect("localhost","apteka","postgres","azizbek",query)
       print(status)

def create_apteka():
       query = f"""
       CREATE TABLE apteka(
            apteka_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            address_id INT REFERENCES address(address_id),
            work_start_time TIME,
             work_end_time TIME,
            last_update TIMESTAMP DEFAULT NOW ())"""
       status = Database.connect("localhost","apteka","postgres","azizbek",query)
       print(status)

def create_ferma():
       query = f"""
       CREATE TABLE ferma(
            apteka_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            address_id INT REFERENCES address(address_id),
            phone_number VARCHAR(10),
            last_update TIMESTAMP DEFAULT NOW ())"""
       status = Database.connect("localhost","apteka","postgres","azizbek", query)
       print(status)


def create_staff():
    query = f"""
       CREATE TABLE staff(
            staff_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            address_id INT REFERENCES address(address_id),
            birth_day DATE,
            phone_number VARCHAR(10),
            apteka_id INT REFERENCES  apteka(apteka_id),
            last_update TIMESTAMP DEFAULT NOW ())"""
    status = Database.connect("localhost", "apteka", "postgres", "azizbek",query)
    print(status)

def create_product():
    query = f"""
       CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            serial_id INT,
            count INT,
            price NUMERIC(10 ,2),
            start_te TIME,
            end_te TIME,
            last_update TIMESTAMP DEFAULT NOW ())"""
    status = Database.connect("localhost", "apteka", "postgres", "azizbek",query)
    print(status)


def create_apteka_product():
    query = f"""
       CREATE TABLE apteka_product(
            apteka_id INT REFERENCES apteka(apteka_id), 
            product_id INT REFERENCES product( product_id),
            last_update TIMESTAMP DEFAULT NOW ())"""
    status = Database.connect("localhost", "apteka", "postgres", "azizbek", query)
    print(status)

def create_payment_type():
    query = f"""
       CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL ,
            last_update TIMESTAMP DEFAULT NOW ())"""
    status = Database.connect("localhost", "apteka", "postgres", "azizbek", query)
    print(status)

def create_payment():
    query = f"""
       CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product( product_id),
            apteka_id INT REFERENCES apteka(apteka_id),
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            last_update TIMESTAMP DEFAULT NOW ())"""
    status = Database.connect("localhost", "apteka", "postgres", "azizbek", query)
    print(status)

if __name__ == "__main__":
    create_payment_type()




