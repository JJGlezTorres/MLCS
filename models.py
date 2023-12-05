from sqlalchemy import Column, Integer, String, Boolean, REAL
import db

''' REGISTRATION CLASSES '''

class StaffUser(db.Base):
    __tablename__ = "registered_staff"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    internal_phone_number = Column(String(200), nullable=False)
    staff_id = Column(String(200), nullable=False)
    department = Column(String(200), nullable=False)
    access_level = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    def __init__(self, first_name, last_name, internal_phone_number,
                 staff_id, department, access_level, password):
        self.first_name = first_name
        self.last_name = last_name
        self.internal_phone_number = internal_phone_number
        self.staff_id = staff_id
        self.department = department
        self.access_level = access_level
        self.password = password

    def __str__(self):
        return f'''ID: {self.staff_id}
                '''

class LoggedStaffUser(db.Base):
    __tablename__ = "staff_logins"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    staff_id = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    timestamp = Column(String(200), nullable=False)

    def __init__(self, staff_id, password, timestamp):
        self.staff_id = staff_id
        self.password = password
        self.timestamp = timestamp

    def __str__(self):
        return f'''ID user: {self.id_user}
                   Password: {self.password}
                   '''

class RegisteredUser(db.Base):
    __tablename__ ="registered_users"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    date_of_birth = Column(String(20), nullable = False)
    phone_number = Column(String(20), nullable = False)
    country = Column(String(30), nullable = False)
    city = Column(String(30), nullable = False)
    address = Column(String(50), nullable = False)
    zip_code = Column(String(30), nullable = False)
    email = Column(String(50), nullable = False)
    username = Column(String(50), nullable = False)
    password = Column(String(50), nullable = False)
    question = Column(Integer, nullable = False)
    answer = Column(Integer, nullable = False)
    card_number = Column(String(50), nullable = False)
    expiration_date = Column(String(20), nullable = False)
    cvv_code = Column(Integer, nullable = False)
    receives_additional_info = Column(String(20), nullable = True)

    def __init__(self, first_name, last_name, date_of_birth, phone_number, country,
                 city, address, zip_code, email, username, password, question,
                 answer, card_number, expiration_date, cvv_code, receives_additional_info):

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.country = country
        self.city = city
        self.address = address
        self.zip_code = zip_code
        self.username = username
        self.email = email
        self.password = password
        self.question = question
        self.answer = answer
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv_code = cvv_code
        self.receives_additional_info = receives_additional_info

    def __str__(self):
        return f'''{self.first_name} {self.last_name} has created a new user:
                   Email -> {self.email}
                   Username -> {self.username}'''

class LoggedUser(db.Base):
    __tablename__ = "users_logins"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    username = Column(String(200), nullable = False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    timestamp = Column(String(200), nullable=False)

    def __init__(self, username, email, password, timestamp):
        self.username = username
        self.email = email
        self.password = password
        self.timestamp = timestamp

    def __str__(self):
        return f'''User: {self.username}
                   Email: {self.email}
                   Password: {self.password}
                   '''

class RegisteredSupplier(db.Base):
    __tablename__ ="registered_suppliers"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    company_name = Column(String(50), nullable = False)
    number_of_workers = Column(String(50), nullable = False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(20), nullable = False)
    country = Column(String(30), nullable = False)
    city = Column(String(30), nullable = False)
    address = Column(String(50), nullable = False)
    zip_code = Column(String(30), nullable = False)
    password = Column(String(50), nullable = False)
    bank_account = Column(String(50), nullable = False)


    def __init__(self, company_name, number_of_workers, email, phone_number,
                 country, city, address, zip_code, password, bank_account):

        self.company_name = company_name
        self.number_of_workers = number_of_workers
        self.email = email
        self.phone_number = phone_number
        self.country = country
        self.city = city
        self.address = address
        self.zip_code = zip_code
        self.password = password
        self.bank_account = bank_account

    def add_validation(self):

        self.validations += 1;

    def __str__(self):
        return f'''{self.company_name} has created a new user:
                   Email -> {self.email}
                   Number of workers -> {self.number_of_workers}'''

class LoggedSupplier(db.Base):
    __tablename__ = "suppliers_logins"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    company_name = Column(String(200), nullable = False)
    password = Column(String(200), nullable=False)
    timestamp = Column(String(200), nullable=False)

    def __init__(self, company_name, password, timestamp):
        self.company_name = company_name
        self.password = password
        self.timestamp = timestamp

    def __str__(self):
        return f'''User: {self.username}
                   Number of workers: {self.password}
                   '''



''' SERVICES CLASSES '''

class SupplierService(db.Base):
    __tablename__ = "supplier_services"
    __table_args__ = {'sqlite_autoincrement': True}
    id_service = Column(Integer, primary_key=True)
    company_name = Column(String(200), nullable=False)
    category = Column(String(200), nullable=False)
    model = Column(String(200), nullable=False)
    price = Column(String(200), nullable=False)
    quantity = Column(String(200), nullable=False)
    delivery_time = Column(String(200), nullable=False)
    validations = Column(Integer, nullable=False)

    def __init__(self, company_name, category, model,
                 price, quantity, delivery_time):
        self.company_name = company_name
        self.category = category
        self.model = model
        self.price = price
        self.quantity = quantity
        self.delivery_time = delivery_time

        self.validations = 0

    def __str__(self):
        return f'''Company: {self.company_name},
                   Category: {self.category},
                   Model: {self.model}
                '''

class Validation(db.Base):
    __tablename__ = "validations"
    __table_args__ = {'sqlite_autoincrement': True}
    id_validation = Column(Integer, primary_key=True)
    id_staff_user = Column(String(200), nullable=False)
    id_service = Column(String(200), nullable=False)

    def __init__(self, id_staff_user, id_service):
        self.id_staff_user = id_staff_user
        self.id_service = id_service

    def __str__(self):
        return f'''ID staff user: {self.id_staff_user},
                   ID service: {self.id_service}
                '''

class ExecutedService(db.Base):
    __tablename__ = "executed_services"
    __table_args__ = {'sqlite_autoincrement': True}
    executed_service_id = Column(Integer, primary_key=True)
    id_service = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    company_name = Column(String(200), nullable=False)
    model = Column(String(200), nullable=False)
    price = Column(String(200), nullable=False)
    quantity = Column(String(200), nullable=False)

    def __init__(self, id_service, date, company_name, model, price, quantity):
        self.id_service = id_service
        self.date = date
        self.company_name = company_name
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'''Date: {self.date},
                   Price: {self.price},
                   Model: {self.model}
                '''

class ExecutedSales(db.Base):
    __tablename__ = "executed_sales"
    __table_args__ = {'sqlite_autoincrement': True}
    executed_sale_id = Column(Integer, primary_key=True)
    id_product = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    buyer_user = Column(String(200), nullable=False)
    product = Column(String(200), nullable=False)
    price = Column(String(200), nullable=False)

    def __init__(self, id_product, date, buyer_user, product, price):
        self.id_product = id_product
        self.date = date
        self.buyer_user = buyer_user
        self.product = product
        self.price = price

    def __str__(self):
        return f'''Date: {self.date},
                   Price: {self.price},
                   Model: {self.model}
                '''


''' MOVEMENTS CLASSES '''

class StaffMovement(db.Base):
    __tablename__ = "staff_movements"
    __table_args__ = {'sqlite_autoincrement': True}
    id_validation = Column(Integer, primary_key=True)
    origin_staff_member = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    amount = Column(REAL, nullable=False)
    type = Column(String(200), nullable=False) 
    object = Column(String(200), nullable=False)
    total = Column(REAL, nullable=False)

    def __init__(self, origin_staff_member, destination, date,
                 amount, type, object, total):
        self.origin_staff_member = origin_staff_member
        self.destination = destination
        self.date = date
        self.amount = amount
        self.type = type
        self.object = object
        self.total = total

    def __str__(self):
        return f'''Origin: {self.origin_staff_user},
                   Destination: {self.destination}, 
                   Amount: {self.amount}
                '''

class UserMovement(db.Base):
    __tablename__ = "user_movements"
    __table_args__ = {'sqlite_autoincrement': True}
    id_movement = Column(Integer, primary_key=True)
    origin_user = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    amount = Column(REAL, nullable=False)
    type = Column(String(200), nullable=False)
    object = Column(String(200), nullable=False)
    total = Column(REAL, nullable=False)

    def __init__(self, origin_user, destination, date,
                 amount, type, object, total):
        self.origin_user = origin_user
        self.destination = destination
        self.date = date
        self.amount = amount
        self.type = type
        self.object = object
        self.total = total

    def __str__(self):
        return f'''Origin: {self.origin_user},
                   Destination: {self.destination}, 
                   Amount: {self.amount}
                '''

class StaffStock(db.Base):
    __tablename__ = "staff_stock"
    __table_args__ = {'sqlite_autoincrement': True}
    id_stock = Column(Integer, primary_key=True)
    date = Column(String(200), nullable=False)
    movement_type = Column(String(200), nullable=False)
    distance_sensor_RJ10 = Column(Integer, nullable=False)
    lidar_sensor_OSx = Column(Integer, nullable=False)
    camera_C_vision33 = Column(Integer, nullable=False)
    servoX10Standard = Column(Integer, nullable=False)
    servoX10Ultra = Column(Integer, nullable=False)
    servoX20Ultra = Column(Integer, nullable=False)
    pcb_3x = Column(Integer, nullable=False)
    pcb_6x = Column(Integer, nullable=False)
    engine_Max12V = Column(Integer, nullable=False)
    bodywork_type1 = Column(Integer, nullable=False)
    bodywork_type2 = Column(Integer, nullable=False)
    bodywork_type3 = Column(Integer, nullable=False)
    wire_5V = Column(Integer, nullable=False)
    wire_12V = Column(Integer, nullable=False)
    led_3_3V = Column(Integer, nullable=False)

    def __init__(self, date, movement_type,
                 distance_sensor_RJ10, lidar_sensor_OSx, camera_C_vision33,
                 servoX10Standard, servoX10Ultra, servoX20Ultra,
                 pcb_3x, pcb_6x, engine_Max12V,
                 bodywork_type1, bodywork_type2, bodywork_type3,
                 wire_5V, wire_12V, led_3_3V):
        self.date = date
        self.movement_type = movement_type
        self.distance_sensor_RJ10 = distance_sensor_RJ10
        self.lidar_sensor_OSx = lidar_sensor_OSx
        self.camera_C_vision33 = camera_C_vision33
        self.servoX10Standard = servoX10Standard
        self.servoX10Ultra = servoX10Ultra
        self.servoX20Ultra = servoX20Ultra
        self.pcb_3x = pcb_3x
        self.pcb_6x = pcb_6x
        self.engine_Max12V = engine_Max12V
        self.bodywork_type1 = bodywork_type1
        self.bodywork_type2 = bodywork_type2
        self.bodywork_type3 = bodywork_type3
        self.wire_5V = wire_5V
        self.wire_12V = wire_12V
        self.led_3_3V = led_3_3V

    def __str__(self):
        return f'''distance_sensor_RJ10: {self.distance_sensor_RJ10},
                   servoX10Standard: {self.servoX10Standard}, 
                   pcb_3x: {self.pcb_3x}
                '''

class StorehouseMovement(db.Base):
    __tablename__ = "storehouse_movements"
    __table_args__ = {'sqlite_autoincrement': True}
    id_movement = Column(Integer, primary_key=True)
    origin_staff_member = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    product = Column(String(200), nullable=False)
    production_cost = Column(REAL, nullable=False)
    talisman_t_total = Column(Integer, nullable=False)
    overlord_k_total = Column(Integer, nullable=False)
    sentinel_v10_total = Column(Integer, nullable=False)

    def __init__(self, origin_staff_member, date, product, production_cost,
                 talisman_t_total, overlord_k_total, sentinel_v10_total):
        self.origin_staff_member = origin_staff_member
        self.date = date
        self.product = product
        self.production_cost = production_cost
        self.talisman_t_total = talisman_t_total
        self.overlord_k_total = overlord_k_total
        self.sentinel_v10_total = sentinel_v10_total

    def __str__(self):
        return f'''Origin: {self.origin_staff_user},
                   Product: {self.product}, 
                   Production Cost: {self.production_cost}
                '''

class PricesSetupLog(db.Base):
    __tablename__ = "prices_setup_log"
    __table_args__ = {'sqlite_autoincrement': True}
    id_setup = Column(Integer, primary_key=True)
    id_staff_user = Column(String(200), nullable=False)
    date = Column(String(200), nullable=False)
    Talisman_T_price = Column(Integer, nullable=False)
    Overlord_K_price = Column(Integer, nullable=False)
    Sentinel_v10_price = Column(Integer, nullable=False)

    def __init__(self, id_staff_user, date,
                 Talisman_T_price, Overlord_K_price, Sentinel_v10_price):
        self.id_staff_user = id_staff_user
        self.date = date
        self.Talisman_T_price = Talisman_T_price
        self.Overlord_K_price = Overlord_K_price
        self.Sentinel_v10_price = Sentinel_v10_price

    def __str__(self):
        return f'''User: {self.id_staff_user},
                   Date: {self.date}, 
                '''

class InfoClientLog(db.Base):
    __tablename__ ="info_client_log"
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    sale_date = Column(String(50), nullable = False)
    product_bought = Column(String(50), nullable = False)
    price = Column(String(50), nullable = False)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    date_of_birth = Column(String(20), nullable = False)
    phone_number = Column(String(20), nullable = False)
    country = Column(String(30), nullable = False)
    city = Column(String(30), nullable = False)
    address = Column(String(50), nullable = False)
    zip_code = Column(String(30), nullable = False)
    email = Column(String(50), nullable = False)
    username = Column(String(50), nullable = False)
    card_number = Column(String(50), nullable = False)

    def __init__(self, sale_date, product_bought, price,
                 first_name, last_name, date_of_birth, phone_number, country,
                 city, address, zip_code, email, username, card_number):

        self.sale_date = sale_date
        self.product_bought = product_bought
        self.price = price
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.country = country
        self.city = city
        self.address = address
        self.zip_code = zip_code
        self.username = username
        self.email = email
        self.card_number = card_number

    def __str__(self):
        return f'''Date: {self.sale_date},
                   Product: {self.product_bought}, 
                   Price: {self.price},
                   Username: {self.username},
                   Date of birth: {self.date_of_birth}
                '''