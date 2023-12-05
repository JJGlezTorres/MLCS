from flask import Flask, render_template, request, redirect, url_for
import hashlib
import datetime
import db
from models import RegisteredUser, LoggedUser, StaffUser, \
    LoggedStaffUser, RegisteredSupplier, LoggedSupplier, \
    SupplierService, Validation, StaffMovement, StaffStock, \
    ExecutedService, StorehouseMovement, UserMovement, \
    ExecutedSales, PricesSetupLog, InfoClientLog


MyLittleCoboticsShop = Flask(__name__)

'''
##############################################
################ SCRIPT INDEX ################
##############################################

############## ASSIGNMENTS FUNCTIONS ############## 
Go and remake functions -> 49-235

################# ACCOUNT FUNCTIONS #################
Login functions -> 239-434 (order: staff, user, supplier)
Register new account functions -> 437-750 (order: staff, user, supplier)
Account recovery functions -> 752-832
Modify and delete account functions -> 834-1036

################# SHOW FUNCTIONS #################
Staff show functions -> 1042-1337
Supplier show functions -> 1339-1385
User show functions -> 1387-1443

################# TRY FUNCTIONS #################
Staff try functions -> 1449-1724
Supplier try functions -> 1726-1769
User try functions -> None

################# MOVEMENT FUNCTIONS #################
Staff movement functions -> 1774-2173
Supplier movement functions -> None
User movement functions -> 2175-2447


##############################################
##############################################
##############################################
'''

''' ############## Assignments functions ############## '''

@MyLittleCoboticsShop.route("/")
def remake_home_page():
    print("You are being redirected to the home page")
    return render_template("index.html")

@MyLittleCoboticsShop.route("/about-us")
def go_about_us():
    print("You are being redirected to the about us page!")
    return render_template("index.html",
                           show_about_us = True)

@MyLittleCoboticsShop.route("/catalog")
def go_catalog():
    print("You are being redirected to the catalog page!")

    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user="Default",
            date="None",
            Talisman_T_price=1200,
            Overlord_K_price=6000,
            Sentinel_v10_price=8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]
    return render_template("index.html",
                           prices_list=prices_list,
                           show_catalog = True)

@MyLittleCoboticsShop.route("/our-values")
def go_our_values():
    print("You are being redirected to the about us page!")
    return render_template("index.html",
                           show_our_values = True)

@MyLittleCoboticsShop.route("/staff-login-page")
def go_staff_login():
    print("You are being redirected to Login Staff!")
    return render_template("login_staff.html")

@MyLittleCoboticsShop.route("/user-login-page")
def go_user_login():
    print("You are being redirected to Login!")
    return render_template("login_customer.html")

@MyLittleCoboticsShop.route("/supplier-login-page")
def go_supplier_login():
    print("You are being redirected to Login!")
    return render_template("login_supplier.html")

@MyLittleCoboticsShop.route("/staff-space/return")
def remake_staff_space():

    id_supplier_user = request.args.get("id")
    search_for_id = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_supplier_user)).all()

    print("You are being redirected to your private space!")
    return render_template("staff_space.html",
                           department=search_for_id[0].department,
                           access_level=search_for_id[0].access_level,
                           first_name=search_for_id[0].first_name,
                           identification=search_for_id[0].id_user)

@MyLittleCoboticsShop.route("/user-space")
def go_user_space():
    print("You are being redirected to your private space!")
    return render_template("user_space.html")

@MyLittleCoboticsShop.route("/supplier-space/<id>")
def go_supplier_space(id):

    search_for_id = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.id_user.ilike(f"{id}")).all()

    try:
        db.session.close()
    except:
        pass

    print("You are being redirected to your private space!")
    return render_template("supplier_space.html",
                           supplier_name = search_for_id[0].company_name,
                           identification=search_for_id[0].id_user)

@MyLittleCoboticsShop.route("/staff-space/<id>")
def go_staff_space(id):

    search_for_id = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(f"{id}")).all()

    print("You are being redirected to your private space!")
    return render_template("staff_space.html",
                           department=search_for_id[0].department,
                           access_level=search_for_id[0].access_level,
                           first_name=search_for_id[0].first_name,
                           identification=search_for_id[0].id_user)

@MyLittleCoboticsShop.route("/user-space/return")
def remake_user_space():

    id_user = request.args.get("id")
    search_for_id = db.session.query(RegisteredUser).filter(RegisteredUser.id_user.ilike(id_user)).all()


    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user = "Default",
            date = "None",
            Talisman_T_price = 1200,
            Overlord_K_price = 6000,
            Sentinel_v10_price = 8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]

    print("You are being redirected to your private space!")
    return render_template("user_space.html",
                           identification=search_for_id[0].id_user,
                           username=search_for_id[0].username,
                           prices_list=prices_list,
                           show_offer=True)

@MyLittleCoboticsShop.route("/create-new-staff-user")
def go_create_staff_space():
    print("You are being redirected to staff user creation page!")
    return render_template("create_staff_user.html")

@MyLittleCoboticsShop.route("/supplier-space/return")
def remake_supplier_space():

    id_supplier_user = request.args.get("id")
    search_for_id = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.id_user.ilike(id_supplier_user)).all()

    print("You are being redirected to your private space!")
    return render_template("supplier_space.html",
                           supplier_name = search_for_id[0].company_name,
                           identification=search_for_id[0].id_user)

@MyLittleCoboticsShop.route("/create-new-user")
def go_create_user():
    print("You are being redirected to user creation page!")
    return render_template("create_user.html")

@MyLittleCoboticsShop.route("/go-modify-account")
def go_modify_account():
    id_supplier_user = request.args.get("id")
    user_type = request.args.get("user_type")
    identification = request.args.get("user_posing_request")

    if user_type == "user":
        user = db.session.query(RegisteredUser).filter(
        RegisteredUser.id_user.in_([id_supplier_user])).all()

        return render_template("modify_account_info.html",
                               user_type=user_type,
                               user=user[0])

    elif user_type == "supplier":
        user = db.session.query(RegisteredSupplier).filter(
            RegisteredSupplier.id_user.in_([id_supplier_user])).all()

        return render_template("modify_account_info.html",
                               user_type=user_type,
                               user=user[0])

    elif user_type == "staff":
        user = db.session.query(StaffUser).filter(
            StaffUser.id_user.in_([id_supplier_user])).all()

        return render_template("modify_account_info.html",
                               user_type=user_type,
                               user=user[0],
                               identification=identification)


@MyLittleCoboticsShop.route("/forgot-password")
def go_forgot_password():
    print("You are being redirected to forgotten password page!")
    return render_template("forgot_password.html")



'''################# ACCOUNT FUNCTIONS #################'''

@MyLittleCoboticsShop.route("/staff-login-page/staff-try-login", methods=["POST"])
def try_staff_login():

    byted_password = bytes(request.form["tried_password"], 'utf-8')
    login_time = datetime.datetime.now()

    TriedUser = LoggedStaffUser(staff_id=request.form["staff_id"],
                     password=hashlib.sha256(byted_password).hexdigest(),
                     timestamp=login_time
                     )

    print("I have tried to log in your page with the following info:")
    print(f"ID: {TriedUser.staff_id}")
    print(f"Password: {TriedUser.password}")

    # First we verify that the user actually exists in the database

    search_for_id = db.session.query(StaffUser).filter(StaffUser.staff_id.ilike(f"{TriedUser.staff_id}")).all()

    if len(search_for_id) == 1:

        print("That user does exist! Checking for correct password...")

        if search_for_id[0].password == TriedUser.password:

            print("Correct password! Access granted")

            identification = search_for_id[0].id_user

            db.session.add_all([TriedUser])

            db.session.commit()
            db.session.close()

            return redirect(url_for("go_staff_space",
                                    id=identification))

        db.session.close()

        return render_template("login_staff.html", incorrect_password="Incorrect password")

    else:

        print("That user does not exists!")

    db.session.close()

    return render_template("login_staff.html", incorrect_username_or_email="Incorrect username or email")

@MyLittleCoboticsShop.route("/user-login-page/try-user-login", methods=["POST"])
def try_user_login():

    byted_password = bytes(request.form["tried_password"], 'utf-8')
    login_time = datetime.datetime.now()

    TriedUser = LoggedUser(username=request.form["email_address_or_username"],
                     email=request.form["email_address_or_username"],
                     password=hashlib.sha256(byted_password).hexdigest(),
                     timestamp=login_time
                     )

    print("I have tried to log in your page with the following info:")
    print(f"Email or username: {TriedUser.email}")
    print(f"Password: {TriedUser.password}")

    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user="Default",
            date="None",
            Talisman_T_price=1200,
            Overlord_K_price=6000,
            Sentinel_v10_price=8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]

    # First we verify that the user actually exists in the database

    search_for_user = db.session.query(RegisteredUser).filter(RegisteredUser.username.ilike(f"{TriedUser.username}")).all()
    search_for_email = db.session.query(RegisteredUser).filter(RegisteredUser.email.ilike(f"{TriedUser.email}")).all()

    if len(search_for_user) == 1 or len(search_for_email) == 1: # A match in username or email exists

        print("That user does exist! Checking for correct password...")

        # As there are two finding options, the "found" variable assignment is redone, but it's not necessary
        found_user = db.session.query(RegisteredUser).filter(RegisteredUser.username.in_([TriedUser.username])).all()
        found_email = db.session.query(RegisteredUser).filter(RegisteredUser.email.in_([TriedUser.email])).all()

        if len(found_user) != 0:

            if found_user[0].password == TriedUser.password:

                print("Correct password! Access granted")

                identification=found_user[0].id_user
                username=found_user[0].username

                db.session.add_all([TriedUser])
                db.session.commit()
                db.session.close()

                return render_template("user_space.html",
                                       identification=identification,
                                       username=username,
                                       prices_list=prices_list,
                                       show_offer=True)

        elif len(found_email) != 0:

            if found_email[0].password == TriedUser.password:

                print("Correct password! Access granted")

                identification = found_email[0].id_user
                username = found_email[0].username

                db.session.add_all([TriedUser])
                db.session.commit()
                db.session.close()

                return render_template("user_space.html",
                                       identification = identification,
                                       username = username,
                                       prices_list = prices_list,
                                       show_offer=True)

            else:

                print("Incorrect password! Redirecting towards login page...")

                db.session.close()

                return render_template("login_customer.html", incorrect_password="Incorrect password")

        db.session.close()

        return render_template("login_customer.html", incorrect_password="Incorrect password")

    db.session.close()

    return render_template("login_customer.html", incorrect_username_or_email="Incorrect username or email")

@MyLittleCoboticsShop.route("/supplier-login-page/try-supplier-login", methods=["POST"])
def try_supplier_login():

    byted_password = bytes(request.form["tried_password"], 'utf-8')
    login_time = datetime.datetime.now()

    TriedSupplier = LoggedSupplier(company_name=request.form["supplier_company_name"],
                                password=hashlib.sha256(byted_password).hexdigest(),
                                timestamp=login_time
                                )

    print("Tried to log in your page with the following info:")
    print(f"ID: {TriedSupplier.company_name}")
    print(f"Password: {TriedSupplier.password}")

    # First we verify that the user actually exists in the database

    search_for_name = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.company_name.ilike(f"{TriedSupplier.company_name}")).all()

    if len(search_for_name) == 1:  # A match in ID exists

        print("That user does exist! Checking for correct password...")

        if search_for_name[0].password == TriedSupplier.password:
            print("Correct password! Access granted")

            db.session.add_all([TriedSupplier])

            identification = search_for_name[0].id_user

            db.session.commit()
            db.session.close()

            return redirect(url_for("go_supplier_space",
                                    id=identification))

        db.session.close()

        return render_template("login_supplier.html", incorrect_password="Incorrect password")

    else:

        print("That user does not exists!")

    db.session.close()

    return render_template("login_supplier.html", incorrect_company_name="Incorrect company name!")


@MyLittleCoboticsShop.route("/create-new-staff-user/try-register", methods=["POST"])
def try_staff_register():

    byted_password = bytes(request.form["password"], 'utf-8')

    StaffNewUser = StaffUser(first_name=request.form["first_name"],
                                       last_name=request.form["last_name"],
                                       internal_phone_number=request.form["internal_phone_number"],
                                       staff_id=request.form["staff_id"],
                                       department=request.form["department"],
                                       access_level=request.form["level"],
                                       password=hashlib.sha256(byted_password).hexdigest(),
                                       )

    ### Checks to decide if it's possible to generate new user:

    found_id = db.session.query(StaffUser).filter(StaffUser.staff_id.in_([StaffNewUser.staff_id])).all()

    no_already_existing_id = True

    # Checks for no repeated email within the db
    if (len(found_id) >= 1):
        print("Found email:", found_id[0].staff_id)
        no_already_existing_id = False

    ### Check to confirm that introduced password do match
    condition_matching_password = request.form["password"] == request.form["repeated_password"]

    if no_already_existing_id and condition_matching_password:

        db.session.add(StaffNewUser)

        db.session.commit()

        new_user_in_db = db.session.query(StaffUser).filter(StaffUser.staff_id.in_([StaffNewUser.staff_id])).all()

        new_user_id_in_db = new_user_in_db[0].id_user

        print("Have created a new user with the following info:")
        print(f"first_name: {StaffNewUser.first_name}")
        print(f"last_name: {StaffNewUser.last_name}")
        print(f"internal_phone_number: {StaffNewUser.internal_phone_number}") # Dates are strings!
        print(f"staff_id: {StaffNewUser.staff_id}")
        print(f"department: {StaffNewUser.department}")
        print(f"access_level: {StaffNewUser.access_level}")
        print(f"password: {StaffNewUser.password}")

        db.session.close()

        return redirect(url_for("go_staff_space", id=new_user_id_in_db))

    # Logic block to pass info to browser according to situation
    if (not no_already_existing_id):

        if (not condition_matching_password):

            db.session.close()

            return render_template("create_staff_user.html", repeated_id_msg="Already registered ID!",
                                    not_maching_passwords="Passwords do not match!"
                                    )

        else:

            db.session.close()

            return render_template("create_staff_user.html", repeated_id_msg="Already registered ID!")

    elif (not condition_matching_password):

        db.session.close()

        return render_template("create_staff_user.html", not_maching_passwords="Passwords do not match!")

    db.session.close()


@MyLittleCoboticsShop.route("/create-new-user/customer_or_supplier", methods=["POST"])
def customer_or_supplier():

    user_type = request.form["customer_or_supplier"]

    return render_template("create_user.html", user_type=user_type)


@MyLittleCoboticsShop.route("/create-new-user/try-customer-register", methods=["POST"])
def try_user_register():

    try:
        receives_additional_info = request.form["receives_additional_info"]
    except:
        receives_additional_info = "off"

    byted_password = bytes(request.form["password"], 'utf-8')

    RegisteredNewUser = RegisteredUser(first_name=request.form["first_name"],
                                       last_name=request.form["last_name"],
                                       date_of_birth=request.form["date_of_birth"],
                                       phone_number=request.form["phone_number"],
                                       country=request.form["country"],
                                       city=request.form["city"],
                                       address=request.form["address"],
                                       zip_code=request.form["zip_code"],
                                       email=request.form["email"],
                                       username=request.form["username"],
                                       password=hashlib.sha256(byted_password).hexdigest(),
                                       question=request.form["question"],
                                       answer=request.form["answer"],
                                       card_number=request.form["card_number"],
                                       expiration_date=request.form["expiration_date"],
                                       cvv_code=request.form["cvv_code"],
                                       receives_additional_info = receives_additional_info
                                       )

    ### Checks to decide if it's possible to generate new user:

    found_username = db.session.query(RegisteredUser).filter(RegisteredUser.username.in_([RegisteredNewUser.username])).all()
    found_email = db.session.query(RegisteredUser).filter(RegisteredUser.email.in_([RegisteredNewUser.email])).all()

    no_already_existing_username = True
    no_already_existing_email = True

    # Checks for no repeated email within the db
    if (len(found_email) >= 1):
        print("Found email:", found_email[0].email)
        no_already_existing_email = False

    # Checks for no repeated username within the db
    if (len(found_username) >= 1):
        print("Found user:", found_username[0].username)
        no_already_existing_username = False

    ### Check to confirm that introduced password do match
    condition_matching_password = request.form["password"] == request.form["repeated_password"]

    if no_already_existing_email and no_already_existing_username and condition_matching_password:

        db.session.add(RegisteredNewUser)

        db.session.commit()

        print("I have created a new user with the following info:")
        print(f"first_name: {RegisteredNewUser.first_name}")
        print(f"last_name: {RegisteredNewUser.last_name}")
        print(f"date_of_birth: {RegisteredNewUser.date_of_birth}") # Dates are strings!
        print(f"phone_number: {RegisteredNewUser.phone_number}")
        print(f"city: {RegisteredNewUser.city}")
        print(f"address: {RegisteredNewUser.address}")
        print(f"zip_code: {RegisteredNewUser.zip_code}")
        print(f"email: {RegisteredNewUser.email}")
        print(f"username: {RegisteredNewUser.username}")
        print(f"password: {RegisteredNewUser.password}")
        print(f"question: {RegisteredNewUser.question}")
        print(f"answer: {RegisteredNewUser.answer}")
        print(f"card_number: {RegisteredNewUser.card_number}")
        print(f"expiration_date: {RegisteredNewUser.expiration_date}")
        print(f"cvv_code: {RegisteredNewUser.cvv_code}")
        print(f"receives_additional_info: {RegisteredNewUser.receives_additional_info}")

        db.session.close()

        return render_template("login_customer.html",
                               user_correctly_created_msg="Your account has been successfully created!")

    # Logic block to pass info to browser according to situation
    if (not no_already_existing_email):

        if (not no_already_existing_username):

            if (not condition_matching_password):

                db.session.close()

                return render_template("create_user.html", repeated_email_msg="Already registered email!",
                                       repeated_username_msg="Already registered username!",
                                       not_maching_passwords="Passwords do not match!",
                                       user_type="customer"
                                       )

            else:

                db.session.close()

                return render_template("create_user.html", repeated_email_msg="Already registered email!",
                                       repeated_username_msg="Already registered username!",
                                       user_type="customer")

        elif (not condition_matching_password):

            db.session.close()

            return render_template("create_user.html", repeated_email_msg="Already registered email!",
                                   not_maching_passwords="Passwords do not match!",
                                   user_type="customer"
                                   )

        else:

            db.session.close()

            return render_template("create_user.html", repeated_email_msg="Already registered email!",
                                   user_type="customer")

    if (not no_already_existing_username):

        if (not condition_matching_password):

            db.session.close()

            return render_template("create_user.html",
                                   repeated_username_msg="Already registered username!",
                                   not_maching_passwords="Passwords do not match!",
                                   user_type="customer"
                                   )

        else:

            db.session.close()

            return render_template("create_user.html",
                                   repeated_username_msg="Already registered username!",
                                   user_type="customer")

    if (not condition_matching_password):

        db.session.close()

        return render_template("create_user.html",
                               not_maching_passwords="Passwords do not match!",
                               user_type="customer"
                               )

    db.session.close()

@MyLittleCoboticsShop.route("/create-new-user/try-supplier-register", methods=["POST"])
def try_supplier_register():

    byted_password = bytes(request.form["password"], 'utf-8')

    RegisteredNewSupplier = RegisteredSupplier(company_name=request.form["company_name"],
                                       number_of_workers=request.form["number_of_workers"],
                                       email=request.form["email"],
                                       phone_number=request.form["phone_number"],
                                       country=request.form["country"],
                                       city=request.form["city"],
                                       address=request.form["address"],
                                       zip_code=request.form["zip_code"],
                                       password=hashlib.sha256(byted_password).hexdigest(),
                                       bank_account=request.form["bank_account"]
                                       )

    ### Checks to decide if it's possible to generate new user:

    found_company = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.company_name.in_([RegisteredNewSupplier.company_name])).all()

    no_already_existing_company_name = True

    # Checks for no repeated email within the db
    if (len(found_company) >= 1):
        print("Found email:", found_company[0].company_name)
        no_already_existing_company_name = False

    ### Check to confirm that introduced password do match
    condition_matching_password = request.form["password"] == request.form["repeated_password"]

    if no_already_existing_company_name and condition_matching_password:
        db.session.add(RegisteredNewSupplier)

        db.session.commit()

        print("I have created a new user with the following info:")
        print(f"company_name: {RegisteredNewSupplier.company_name}")
        print(f"number_of_workers: {RegisteredNewSupplier.number_of_workers}")
        print(f"email: {RegisteredNewSupplier.email}")  # Dates are strings!
        print(f"phone_number: {RegisteredNewSupplier.phone_number}")
        print(f"country: {RegisteredNewSupplier.country}")
        print(f"city: {RegisteredNewSupplier.city}")
        print(f"address: {RegisteredNewSupplier.address}")
        print(f"zip_code: {RegisteredNewSupplier.zip_code}")
        print(f"password: {RegisteredNewSupplier.password}")
        print(f"bank_account: {RegisteredNewSupplier.bank_account}")

        db.session.close()

        return render_template("login_supplier.html",
                               user_correctly_created_msg="Your account has been successfully created!")

    # Logic block to pass info to browser according to situation
    if (not no_already_existing_company_name):

        if (not condition_matching_password):

            db.session.close()

            return render_template("create_user.html", repeated_name_msg="Already registered company name!",
                                   not_maching_passwords="Passwords do not match!",
                                   user_type="supplier"
                                   )

        else:

            db.session.close()

            return render_template("create_user.html", repeated_name_msg="Already registered company name!",
                                   user_type="supplier")

    elif (not condition_matching_password):

        db.session.close()

        return render_template("create_user.html", not_maching_passwords="Passwords do not match!",
                               user_type="supplier")

    db.session.close()

@MyLittleCoboticsShop.route("/login-page/try-locate-user-by-email", methods=["POST"])
def try_locate_user_by_email():

    global questions_dictionary

    questions_dictionary = {
        0: "When you were young, what did you want to be when you grew up?",
        1: "What is the name of your first pet?",
        2: "What was your first car?",
        3: "What elementary school did you attend?",
        4: "Where was your best family vacation as a kid?",
        5: "Who was your childhood hero?"
    }

    global email_to_answer_question

    email_to_answer_question = request.form["email_to_answer_question"]

    matched_users_list = db.session.query(RegisteredUser).filter(RegisteredUser.email.in_([email_to_answer_question])).all()

    matched_email = len(matched_users_list) >= 1

    if matched_email:

        user_trying_to_recover_password = matched_users_list[0]
        username = user_trying_to_recover_password.username
        print("Username:", username)
        question = questions_dictionary[user_trying_to_recover_password.question]
        print("Question:", question)

        return render_template("forgot_password.html",
                               username=username,
                               question=question)

    else:

        print("That email address is not registered in the database!")
        return render_template("forgot_password.html",
                               not_matching_email="Email address not found")

@MyLittleCoboticsShop.route("/login-page/try-answer-question", methods=["POST"])
def try_answer_question():

    answer_to_question = request.form["answer_to_question"]

    user_trying_to_recover = db.session.query(RegisteredUser).filter(RegisteredUser.email.in_([email_to_answer_question])).all()

    if user_trying_to_recover[0].answer == answer_to_question:

        try:
            prices_entrances = db.session.query(PricesSetupLog).all()
            last_prices_entrance = prices_entrances[-1]
        except:
            last_prices_entrance = PricesSetupLog(
                id_staff_user="Default",
                date="None",
                Talisman_T_price=1200,
                Overlord_K_price=6000,
                Sentinel_v10_price=8000
            )
        prices_list = [last_prices_entrance.Talisman_T_price,
                       last_prices_entrance.Overlord_K_price,
                       last_prices_entrance.Sentinel_v10_price]

        print("Your answer is right!")

        return render_template("user_space.html",
                               identification=user_trying_to_recover[0].id_user,
                               username=user_trying_to_recover[0].username,
                               prices_list=prices_list,
                               show_offer=True)

    else:

        print("Your answer is wrong!")

        return render_template("forgot_password.html",
                               username = user_trying_to_recover[0].username,
                               question = questions_dictionary[user_trying_to_recover[0].question],
                               not_matching_answer="Your answer is wrong!"
                               )

@MyLittleCoboticsShop.route("/modify-account-info", methods=["POST"])
def modify_account_info():

    id_account = request.args.get("id")
    user_type = request.args.get("user_type")

    print(f"User of type {user_type} ID {id_account} is trying to modify info account")

    if user_type == "user":
        user_trying_to_recover = db.session.query(RegisteredUser).filter(
        RegisteredUser.id_user.in_([id_account])).all()

        try:
            prices_entrances = db.session.query(PricesSetupLog).all()
            last_prices_entrance = prices_entrances[-1]
        except:
            last_prices_entrance = PricesSetupLog(
                id_staff_user="Default",
                date="None",
                Talisman_T_price=1200,
                Overlord_K_price=6000,
                Sentinel_v10_price=8000
            )
        prices_list = [last_prices_entrance.Talisman_T_price,
                       last_prices_entrance.Overlord_K_price,
                       last_prices_entrance.Sentinel_v10_price]

        try:
            receives_additional_info = request.form["receives_additional_info"]
        except:
            receives_additional_info = "off"

        # Modify its information
        byted_password = bytes(request.form["password"], 'utf-8')
        user_trying_to_recover[0].phone_number = request.form["phone_number"]
        user_trying_to_recover[0].country = request.form["country"]
        user_trying_to_recover[0].city = request.form["city"]
        user_trying_to_recover[0].address = request.form["address"]
        user_trying_to_recover[0].zip_code = request.form["zip_code"]
        user_trying_to_recover[0].password = hashlib.sha256(byted_password).hexdigest()
        user_trying_to_recover[0].question = request.form["question"]
        user_trying_to_recover[0].answer = request.form["answer"]
        user_trying_to_recover[0].card_number = request.form["card_number"]
        user_trying_to_recover[0].expiration_date = request.form["expiration_date"]
        user_trying_to_recover[0].cvv_code = request.form["cvv_code"]
        user_trying_to_recover[0].receives_additional_info = receives_additional_info

        condition_matching_password = request.form["password"] == request.form["repeated_password"]

        if not condition_matching_password:
            return render_template("modify_account_info.html",
                                   user_type="user",
                                   user=user_trying_to_recover[0],
                                   not_matching_passwords_msg="Passwords do not match!")

        identification = user_trying_to_recover[0].id_user
        username = user_trying_to_recover[0].username

        db.session.commit()
        db.session.close()

        return render_template("user_space.html",
                               identification=identification,
                               username=username,
                               prices_list=prices_list,
                               show_offer=True,
                               new_information_correctly_set_msg="Your account information has been correctly updated!")

    elif user_type == "supplier":
        user_trying_to_recover = db.session.query(RegisteredSupplier).filter(
        RegisteredSupplier.id_user.in_([id_account])).all()

        # Modify its information
        byted_password = bytes(request.form["password"], 'utf-8')
        user_trying_to_recover[0].phone_number = request.form["phone_number"]
        user_trying_to_recover[0].country = request.form["country"]
        user_trying_to_recover[0].city = request.form["city"]
        user_trying_to_recover[0].address = request.form["address"]
        user_trying_to_recover[0].zip_code = request.form["zip_code"]
        user_trying_to_recover[0].password = hashlib.sha256(byted_password).hexdigest()
        user_trying_to_recover[0].bank_account = request.form["bank_account"]

        condition_matching_password = request.form["password"] == request.form["repeated_password"]

        if not condition_matching_password:
            return render_template("modify_account_info.html",
                                   user_type="supplier",
                                   user=user_trying_to_recover[0],
                                   not_matching_passwords_msg="Passwords do not match!")

        supplier_name = user_trying_to_recover[0].company_name
        identification = user_trying_to_recover[0].id_user

        db.session.commit()
        db.session.close()

        return render_template("supplier_space.html",
                               supplier_name=supplier_name,
                               identification=identification,
                               new_information_correctly_set_msg="Your account information has been correctly updated!")

    elif user_type == "staff":
        user_trying_to_recover = db.session.query(StaffUser).filter(
        StaffUser.id_user.in_([id_account])).all()

        user_posing_delete_request_id = request.args.get("user_posing_request")
        user_posing_delete_request = db.session.query(StaffUser).filter(
            StaffUser.id_user.in_([user_posing_delete_request_id])).all()

        print("user_posing_delete_request_id:", user_posing_delete_request_id)

        # Modify its information
        byted_password = bytes(request.form["password"], 'utf-8')
        user_trying_to_recover[0].internal_phone_number = request.form["internal_phone_number"]
        user_trying_to_recover[0].department = request.form["department"]
        user_trying_to_recover[0].access_level = request.form["level"]
        user_trying_to_recover[0].password = hashlib.sha256(byted_password).hexdigest()

        condition_matching_password = request.form["password"] == request.form["repeated_password"]

        if not condition_matching_password:
            return render_template("modify_account_info.html",
                                   user_type="staff",
                                   user=user_trying_to_recover[0],
                                   not_matching_passwords_msg="Passwords do not match!")

        department = user_posing_delete_request[0].department
        access_level = user_posing_delete_request[0].access_level
        first_name = user_posing_delete_request[0].first_name
        identification = user_posing_delete_request[0].id_user

        db.session.commit()
        db.session.close()

        return render_template("staff_space.html",
                               department=department,
                               access_level=access_level,
                               first_name=first_name,
                               identification=identification,
                               new_information_correctly_set_msg=f"The {identification} user information has been correctly updated!")


@MyLittleCoboticsShop.route("/delete-account", methods=["POST"])
def delete_account():
    id_account = request.args.get("id")
    user_type = request.args.get("user_type")

    print(f"User of type {user_type} ID {id_account} is trying escape")

    if user_type == "user":
        user_to_delete = db.session.query(RegisteredUser).filter_by(id_user=id_account).delete()
        db.session.commit()
        db.session.close()
        return render_template("index.html")

    if user_type == "supplier":
        user_trying_to_delete = db.session.query(RegisteredSupplier).filter(
            RegisteredSupplier.id_user.in_([id_account])).all()
        user_to_delete = db.session.query(RegisteredSupplier).filter_by(id_user=id_account).delete()

        # In the case of suppliers we must also delete its active services
        services_to_delete = db.session.query(SupplierService).filter_by(
            company_name=user_trying_to_delete[0].company_name).delete()

        db.session.commit()
        db.session.close()
        return render_template("index.html")

@MyLittleCoboticsShop.route("/staff-space/delete-staff-users")
def delete_staff_users():
    id_staff_member = request.args.get("id")
    id_user_to_delete = request.args.get("user_to_delete_id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    print(f"User {id_staff_member} is trying to delete another user")

    user_to_delete = db.session.query(StaffUser).filter_by(id_user=id_user_to_delete).delete()

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user

    db.session.commit()
    db.session.close()

    # We have to show again the new users list
    list_of_staff_users = db.session.query(StaffUser).all()

    for user in list_of_staff_users:
        if int(user.id_user) == int(id_staff_member):
            list_of_staff_users.remove(user)

    return render_template("staff_space.html",
                           department=department,
                           access_level=access_level,
                           first_name=first_name,
                           identification=identification,
                           list_of_staff_users=list_of_staff_users,
                           display_staff_users=True
                           )



''' ############## SHOW FUNCTIONS ############## '''

### Staff show functions

@MyLittleCoboticsShop.route("/staff-space/show_stocks")
def show_current_stock():
    id_staff_member = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    print(f"The staff user {staff_member[0].first_name} is trying to see the current stocks")

    try:

        stock_entries = db.session.query(StaffStock).all()
        last_stock_entry = stock_entries[-1]

        stock_dictionary = {
            "distance_sensor_RJ10": last_stock_entry.distance_sensor_RJ10,
            "lidar_sensor_OSx": last_stock_entry.lidar_sensor_OSx,
            "camera_C_vision33": last_stock_entry.camera_C_vision33,
            "servoX10Standard": last_stock_entry.servoX10Standard,
            "servoX10Ultra": last_stock_entry.servoX10Ultra,
            "servoX20Ultra": last_stock_entry.servoX20Ultra,
            "pcb_3x": last_stock_entry.pcb_3x,
            "pcb_6x": last_stock_entry.pcb_6x,
            "engine_Max12V": last_stock_entry.engine_Max12V,
            "bodywork_type1": last_stock_entry.bodywork_type1,
            "bodywork_type2": last_stock_entry.bodywork_type2,
            "bodywork_type3": last_stock_entry.bodywork_type3,
            "wire_5V": last_stock_entry.wire_5V,
            "wire_12V": last_stock_entry.wire_12V,
            "led_3_3V": last_stock_entry.led_3_3V
        }

    except:

        stock_dictionary = {
            "distance_sensor_RJ10": 0,
            "lidar_sensor_OSx": 0,
            "camera_C_vision33": 0,
            "servoX10Standard": 0,
            "servoX10Ultra": 0,
            "servoX20Ultra": 0,
            "pcb_3x": 0,
            "pcb_6x": 0,
            "engine_Max12V": 0,
            "bodywork_type1": 0,
            "bodywork_type2": 0,
            "bodywork_type3": 0,
            "wire_5V": 0,
            "wire_12V": 0,
            "led_3_3V": 0
        }

    keys_list = list(stock_dictionary.keys())
    key_list_by_row = [keys_list[:5], keys_list[5:10], keys_list[10:]]

    max_distance_sensor_RJ10_capacity = 1800
    max_lidar_sensor_OSx_capacity = 200
    max_camera_C_vision33_capacity = 500
    max_servoX10Standard_capacity = 3500
    max_servoX10Ultra_capacity = 1400
    max_servoX20Ultra_capacity = 200
    max_pcb_3x_capacity = 3100
    max_pcb_6x_capacity = 1000
    max_engine_Max12V_capacity = 1000
    max_bodywork_type1_capacity = 400
    max_bodywork_type2_capacity = 100
    max_bodywork_type3_capacity = 200
    max_wire_5V_capacity = 1400
    max_wire_12V_capacity = 500
    max_led_3_3V_capacity = 4000

    capacity_dictionary = {
        "distance_sensor_RJ10": round(stock_dictionary["distance_sensor_RJ10"]/max_distance_sensor_RJ10_capacity*100,1),
        "lidar_sensor_OSx": round(stock_dictionary["lidar_sensor_OSx"]/max_lidar_sensor_OSx_capacity*100,1),
        "camera_C_vision33": round(stock_dictionary["camera_C_vision33"]/max_camera_C_vision33_capacity*100,1),
        "servoX10Standard": round(stock_dictionary["servoX10Standard"]/max_servoX10Standard_capacity*100,1),
        "servoX10Ultra": round(stock_dictionary["servoX10Ultra"]/max_servoX10Ultra_capacity*100,1),
        "servoX20Ultra": round(stock_dictionary["servoX20Ultra"]/max_servoX20Ultra_capacity*100,1),
        "pcb_3x": round(stock_dictionary["pcb_3x"]/max_pcb_3x_capacity*100,1),
        "pcb_6x": round(stock_dictionary["pcb_6x"]/max_pcb_6x_capacity*100,1),
        "engine_Max12V": round(stock_dictionary["engine_Max12V"]/max_engine_Max12V_capacity*100,1),
        "bodywork_type1": round(stock_dictionary["bodywork_type1"]/max_bodywork_type1_capacity*100,1),
        "bodywork_type2": round(stock_dictionary["bodywork_type2"]/max_bodywork_type2_capacity*100,1),
        "bodywork_type3": round(stock_dictionary["bodywork_type3"]/max_bodywork_type3_capacity*100,1),
        "wire_5V": round(stock_dictionary["wire_5V"]/max_wire_5V_capacity*100,1),
        "wire_12V": round(stock_dictionary["wire_12V"]/max_wire_12V_capacity*100,1),
        "led_3_3V": round(stock_dictionary["led_3_3V"]/max_led_3_3V_capacity*100,1)
    }

    # Iterate again on the dictionary keys to detect if any of them is lower than 90%
    keys_list = list(stock_dictionary.keys())
    missing_materials = []

    for key in keys_list:
        if capacity_dictionary[key] < 90:
            missing_materials.append(key)

    if len(missing_materials) != 0:
        low_stock_msg = "Low stock in the following materials:"
    else:
        low_stock_msg = ""

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           stock_dictionary=stock_dictionary,
                           capacity_dictionary=capacity_dictionary,
                           key_list_by_row=key_list_by_row,
                           missing_materials=missing_materials,
                           low_stock_msg=low_stock_msg,
                           display_stock=True)

@MyLittleCoboticsShop.route("/staff-space/show-storehouse")
def show_current_storehouse():
    id_staff_member = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    print(f"The staff user {staff_member[0].first_name} is trying to see the current storehouse")

    storehouse_entries = db.session.query(StorehouseMovement).all()

    if len(storehouse_entries)==0:
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               empty_storehouse_msg="There is no product in storehouse!")
    else:
        storehouse_last_entry = storehouse_entries[-1]
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               storehouse_last_entry=storehouse_last_entry,
                               display_storehouse=True
                               )


@MyLittleCoboticsShop.route("/staff-space/show_movements")
def show_last_movements():

    id_staff_member = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    all_movements = db.session.query(StaffMovement).all()
    try:
        last_10_movements = all_movements[-100:]
    except:
        last_10_movements = all_movements[-len(all_movements):]

    last_10_movements.reverse()

    print(f"The staff user {staff_member[0].first_name} is trying to see the last movements")

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           movements_list = last_10_movements,
                           display_movements=True)

@MyLittleCoboticsShop.route("/staff-space/get-sales-info")
def get_sales_info():

    id_staff_user = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_user)).all()
    all_sales = db.session.query(ExecutedSales).all()

    if len(all_sales)==0:
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               no_sales_to_show_msg="No sale has been made yet!")

    all_sales.reverse()

    try:
        last_100_sales = all_sales[-100:]
    except:
        last_100_sales = all_sales[-len(all_sales):]

    print(f"The staff user {staff_member[0].first_name} is trying to get the sales")

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           sales_list=last_100_sales,
                           display_sales=True)

@MyLittleCoboticsShop.route("/staff-space/get-clients-info")
def get_clients_info():

    id_staff_user = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_user)).all()
    clients_info = db.session.query(InfoClientLog).all()

    if len(clients_info)==0:
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               no_clients_to_show_msg="No sale has been made yet!")

    clients_info.reverse()

    try:
        last_100_clients = clients_info[-100:]
    except:
        last_100_clients = clients_info[-len(clients_info):]

    print(f"The staff user {staff_member[0].first_name} is trying to get the clients information")

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           clients_info_list=last_100_clients,
                           display_clients=True)



@MyLittleCoboticsShop.route("/staff-space/show-staff-users")
def show_staff_users():
    id_staff_member = int(request.args.get("id"))

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    print(f"User {id_staff_member} is trying to see the list of staff users")

    list_of_staff_users = db.session.query(StaffUser).all()

    for user in list_of_staff_users:
        if int(user.id_user) == id_staff_member:
            list_of_staff_users.remove(user)

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           list_of_staff_users=list_of_staff_users,
                           display_staff_users=True)


@MyLittleCoboticsShop.route("/staff-space/show-suppliers-to-validate")
def show_suppliers_to_validate():

    id_staff_member = request.args.get("id")

    # Search in database to identify the staff user making the request
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    # Search in database to show suppliers with less than 3 validations

    #services_to_validate = db.session.query(SupplierService).filter(SupplierService.validations < 3).all()
    services_to_validate = db.session.query(SupplierService).all()

    list_of_suppliers = []
    # We need to transform all the "validations" attributes into integer values:
    # Also we make a list with the different company names and then we nake a set of it
    for service in services_to_validate:
        service.validations = int(service.validations)
        list_of_suppliers.append(service.company_name)

    set_of_suppliers = set(list_of_suppliers)

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           list_of_services_to_validate=services_to_validate,
                           set_of_suppliers = set_of_suppliers,
                           display_services = True)

### Supplier show functions

@MyLittleCoboticsShop.route("/supplier-space/see-my-services")
def see_supplier_posted_services():

    # Firstly we need to identify who is the supplier making the requets
    id_supplier_user = request.args.get("id")
    supplier_user = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.id_user.ilike(id_supplier_user)).all()

    print(f"The supplier user {supplier_user[0].company_name} is making a request to see its posted services")

    suppliers_services = db.session.query(SupplierService).filter(SupplierService.company_name.ilike(supplier_user[0].company_name)).all()

    if len(suppliers_services)==0:
        return render_template("supplier_space.html",
                               supplier_name=supplier_user[0].company_name,
                               identification=supplier_user[0].id_user,
                               no_services_offered_msg="You are not currently offering any service!")

    return render_template("supplier_space.html",
                           supplier_name=supplier_user[0].company_name,
                           identification=supplier_user[0].id_user,
                           list_of_suppliers_services = suppliers_services,
                           display_services=True)

@MyLittleCoboticsShop.route("/supplier-space/see-requested-services")
def see_supplier_requested_services():

    # Firstly we need to identify who is the supplier making the requets
    id_supplier_user = request.args.get("id")
    supplier_user = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.id_user.ilike(id_supplier_user)).all()

    print(f"The supplier user {supplier_user[0].company_name} is trying to see which of its services have been requested")

    suppliers_services = db.session.query(ExecutedService).filter(ExecutedService.company_name.ilike(supplier_user[0].company_name)).all()

    if len(suppliers_services)==0:
        return render_template("supplier_space.html",
                               supplier_name=supplier_user[0].company_name,
                               identification=supplier_user[0].id_user,
                               no_services_executed_msg="None of your services has been accepted yet!")

    return render_template("supplier_space.html",
                           supplier_name=supplier_user[0].company_name,
                           identification=supplier_user[0].id_user,
                           list_of_executed_services = suppliers_services,
                           display_executed_services = True)

### User show functions

@MyLittleCoboticsShop.route("/user-space/my-wallet")
def show_user_wallet():

    id_user = request.args.get("id")

    # Search in database to identify the staff user making the request
    user = db.session.query(RegisteredUser).filter(RegisteredUser.id_user.ilike(id_user)).all()

    identification = user[0].id_user
    username = user[0].username

    all_movements = db.session.query(UserMovement).filter(UserMovement.origin_user.ilike(id_user)).all()

    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user="Default",
            date="None",
            Talisman_T_price=1200,
            Overlord_K_price=6000,
            Sentinel_v10_price=8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]

    if len(all_movements)==0:
        return render_template("user_space.html",
                               identification=identification,
                               username=username,
                               prices_list=prices_list,
                               show_offer=True,
                               no_movements_to_show_msg="You have made no movements!")

    try:
        last_100_movements = all_movements[-100:]
    except:
        last_100_movements = all_movements[:]

    last_100_movements.reverse()

    for entry in last_100_movements:
        entry.total = round(entry.total, 2)

    print(f"The staff user {user[0].first_name} is trying to see the last movements")

    return render_template("user_space.html",
                           identification=identification,
                           username=username,
                           movements_list = last_100_movements,
                           show_offer = False,
                           prices_list = prices_list,
                           display_movements=True)



''' ############## TRY FUNCTIONS ############## '''

### Staff try functions

@MyLittleCoboticsShop.route("/staff-space/show-suppliers-to-validate/applied-filters", methods=["POST"])
def apply_filters_to_shown_suppliers():

    # get URL parameters
    id_staff_member = request.args.get("id_user")

    # get user asking for the filtering
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    # get POST method parameters
    service_id_filter = request.form["service_id"]
    supplier_name_filter = request.form["supplier_name"]
    category_filter = request.form["category"]
    min_price_filter = request.form["min_price"]
    max_price_filter = request.form["max_price"]
    validation_state = request.form["state"]

    print("service_id_filter",service_id_filter)
    print("supplier_name_filter", supplier_name_filter)
    print("category_filter", category_filter)
    print("min_price_filter", min_price_filter)
    print("max_price_filter", max_price_filter)

    ### Service filtering ###

    # Firstly we get all services
    services_to_validate = db.session.query(SupplierService).all()
    range_to_iterate = range(len(services_to_validate))

    # get the set of current suppliers
    list_of_suppliers = []
    for service in services_to_validate:
        service.validations = int(service.validations)
        list_of_suppliers.append(service.company_name)

    set_of_suppliers = set(list_of_suppliers)

    aux_counter = 0

    # Then we filter them
    for service in range_to_iterate:

        # For each search argument, verify firstly if it's been given
        # Then eliminate the service if it does not comply with the condition
        if service_id_filter == "":
            condition_service_id = True
        else:
            condition_service_id = services_to_validate[service - aux_counter].id_service == int(service_id_filter)

        if condition_service_id:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

        if supplier_name_filter == "":
            condition_supplier_name = True
        else:
            condition_supplier_name = services_to_validate[service - aux_counter].company_name == supplier_name_filter

        if condition_supplier_name:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

        if category_filter == "":
            condition_category = True
        else:
            condition_category = services_to_validate[service - aux_counter].category == category_filter

        if condition_category:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

        if min_price_filter == "":
            condition_min_price = True
        else:
            condition_min_price = float(services_to_validate[service - aux_counter].price) > float(min_price_filter)

        if condition_min_price:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

        if max_price_filter == "":
            condition_max_price = True
        else:
            condition_max_price = float(services_to_validate[service - aux_counter].price) < float(max_price_filter)

        if condition_max_price:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

        if validation_state == "":
            condition_validation_state = True
        elif validation_state == "validated":
            condition_validation_state = services_to_validate[service - aux_counter].validations == 3
        elif validation_state == "not_validated":
            condition_validation_state = services_to_validate[service - aux_counter].validations < 3

        if condition_validation_state:
            pass
        else:
            services_to_validate.pop(service - aux_counter)
            aux_counter += 1
            continue

    # In the end we get a list of services complying with all the given search conditions

    if len(services_to_validate)==0:

        no_match_found_msg = "No result found!"

    else:

        no_match_found_msg = False

    return render_template("staff_space.html",
                           department=staff_member[0].department,
                           access_level=staff_member[0].access_level,
                           first_name=staff_member[0].first_name,
                           identification=staff_member[0].id_user,
                           list_of_services_to_validate=services_to_validate,
                           set_of_suppliers=set_of_suppliers,
                           display_services=True,
                           no_match_found_msg=no_match_found_msg)


@MyLittleCoboticsShop.route("/staff-space/show-suppliers-to-validate/validate-service")
def validate_service():

    # Recovering the parameters from url
    id_staff_member = request.args.get("id_user")
    id_service = request.args.get("id_service")

    # Services available to validate
    #services_to_validate = db.session.query(SupplierService).filter(SupplierService.validations < 3).all()
    services_to_validate = db.session.query(SupplierService).all()

    # The first thing to do is verify that the user has not already validated that service
    # A list of all validations that this user has performed
    check_staff_member_validations = db.session.query(Validation).filter(Validation.id_staff_user.ilike(id_staff_member)).all()

    # The user making the validation and the service being validated
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()
    the_service_to_validate = db.session.query(SupplierService).filter(
        SupplierService.id_service.ilike(id_service)).all()

    print("The user", staff_member[0].first_name, "is trying to validate the service",
          the_service_to_validate[0].id_service)

    # If one of those validations correspond to the current service, do not allow validation
    for check_staff_member in check_staff_member_validations:

        if check_staff_member.id_service == id_service:

            list_of_suppliers = []

            # We need to transform all the "validations" attributes into integer values:
            for service in services_to_validate:
                service.validations = int(service.validations)
                list_of_suppliers.append(service.company_name)

            set_of_suppliers = set(list_of_suppliers)

            print("This user has already validated this product. Aborting validation.")

            return render_template("staff_space.html",
                                   department=staff_member[0].department,
                                   access_level=staff_member[0].access_level,
                                   first_name=staff_member[0].first_name,
                                   identification=staff_member[0].id_user,
                                   list_of_services_to_validate=services_to_validate,
                                   set_of_suppliers = set_of_suppliers,
                                   display_services=True,
                                   failed_to_validate_msg = "That service has already been validated by you!")

        else:
            pass

    # Increment the number of validations
    the_service_to_validate[0].validations = int(the_service_to_validate[0].validations) + 1

    GivenValidation = Validation(
        id_staff_user=id_staff_member,
        id_service=id_service
    )

    db.session.add(GivenValidation)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user

    list_of_suppliers = []

    # We need to transform all the "validations" attributes into integer values:
    # Also we make a list with the different company names and then we nake a set of it
    for service in services_to_validate:
        service.validations = int(service.validations)
        list_of_suppliers.append(service.company_name)

    set_of_suppliers = set(list_of_suppliers)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user
    validations = the_service_to_validate[0].validations

    db.session.commit()
    db.session.close()

    print("Service SUCCESSFULLY validated!")

    return render_template("staff_space.html",
                            department=department,
                            access_level=access_level,
                            first_name=first_name,
                            identification=identification,
                            validations=int(validations),
                            service_validated_msg=f"Service id {id_service} has been correctly validated (already {validations} in total)")

@MyLittleCoboticsShop.route("/staff-space/setup-new_prices", methods=["POST"])
def set_up_new_prices():

    id_user = request.args.get("id")
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_user)).all()
    new_talisman_price = request.form["talisman_t_price"]
    new_overlord_price = request.form["overlord_k_price"]
    new_sentinel_price = request.form["sentinel_v10_price"]

    print(f'''User {staff_member[0].id_user} has set Talisman, Overlord and 
            Sentienl to {new_talisman_price}, {new_overlord_price} and 
            {new_sentinel_price}, respectively''')

    date = datetime.datetime.now()

    new_prices_set = PricesSetupLog(
        id_staff_user = staff_member[0].staff_id,
        date = date,
        Talisman_T_price = new_talisman_price,
        Overlord_K_price = new_overlord_price,
        Sentinel_v10_price = new_sentinel_price
    )

    db.session.add(new_prices_set)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user

    db.session.commit()
    db.session.close()

    return render_template("staff_space.html",
                           department=department,
                           access_level=access_level,
                           first_name=first_name,
                           identification=identification,
                           correctly_set_prices_msg="New prices correctly assigned!")

### Supplier try functions

@MyLittleCoboticsShop.route("/supplier-space/try-service-register", methods=["POST"])
def try_service_register():

    id_supplier_user = request.args.get("id")

    # Search in database to identify the supplier user making the request
    supplier_creating_service = db.session.query(RegisteredSupplier).filter(RegisteredSupplier.id_user.ilike(id_supplier_user)).all()

    # Determine to which category each service belongs
    if request.form["model"] in ["Distance Sensor RJ10", "LiDAR Sensor OSx", "Camera CVision33"]:
        service_category = "Sensor"
    elif request.form["model"] in ["Servo XH10Standard", "Servo XH10Ultra", "Servo XH20Ultra"]:
        service_category = "Servomechanism"
    elif request.form["model"] in ["PCB-3x", "PCB-6x", "Engine Max12V"]:
        service_category = "Electronics"
    elif request.form["model"] in ["Bodywork Type1", "Bodywork Type2", "Bodywork Type3"]:
        service_category = "3D printing"
    elif request.form["model"] in ["Wire 5V", "Wire 12V", "LED 3.3V"]:
        service_category = "Miscellaneous"


    NewService = SupplierService(
        company_name=supplier_creating_service[0].company_name,
        category=service_category,
        model=request.form["model"],
        price=request.form["price"],
        quantity=request.form["quantity"],
        delivery_time=request.form["delivery_time"],
    )

    db.session.add(NewService)

    supplier_name = supplier_creating_service[0].company_name
    identification = supplier_creating_service[0].id_user

    db.session.commit()
    db.session.close()

    return render_template("supplier_space.html",
                           supplier_name=supplier_name,
                           identification=identification,
                           successfully_created_service_msg="The service has been created successfully!")


''' ############## MOVEMENTS FUNCTIONS ############## '''

### Staff movement functions

@MyLittleCoboticsShop.route("/staff-space/make-deposit", methods=["POST"])
def staff_make_deposit():

    # Get the id of the user making the deposit
    id_staff_member = request.args.get("id")
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    # Get the quantity of the deposit passed through POST method
    deposit_quantity = float(request.form["deposit_quantity"])

    # Get the last deposit executed to calculate the current total
    try:
        last_movement_executed = db.session.query(StaffMovement).all()
        previous_total = float(last_movement_executed[-1].total)
    except:
        previous_total = 0


    NewMovement = StaffMovement(
        origin_staff_member=id_staff_member,
        destination="Cobotics",
        date=str(datetime.datetime.now()),
        amount=deposit_quantity,
        type="deposit",
        object="deposit",
        total = previous_total + deposit_quantity
    )

    db.session.add(NewMovement)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user

    new_total = NewMovement.total

    db.session.commit()
    db.session.close()

    return render_template("staff_space.html",
                           department=department,
                           access_level=access_level,
                           first_name=first_name,
                           identification=identification,
                           correct_movement_msg=f"Deposit performed correctly! The current total is {new_total}$")


@MyLittleCoboticsShop.route("/staff-space/purchase-service")
def purchase_service():

    # Get the information arriving as URL parameter
    id_staff_member = request.args.get("id_user")
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()
    id_service = request.args.get("id_service")
    service_to_purchase = db.session.query(SupplierService).filter(SupplierService.id_service.ilike(id_service)).all()
    purchase_time = str(datetime.datetime.now())

    print(f"The user {staff_member[0].first_name} is trying to buy product {service_to_purchase[0].model}")

    '''The first thing to do is the movement in the Cobotics account
    Therefore, we create a StaffMovement object'''

    # To give the new total is necessary to retrieve all the movements from db
    try:
        all_movement_executed = db.session.query(StaffMovement).all()
        previous_total = float(all_movement_executed[-1].total)
    except:
        previous_total = 0

    # verify is the total available is enough to buy the service
    if previous_total < float(service_to_purchase[0].price):
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               not_enough_total_msg=f"There is not enough money to buy this service!")

    # Create the movement, which is equivalent to pay
    PurchaseMovement = StaffMovement(
        origin_staff_member=id_staff_member,
        destination=service_to_purchase[0].company_name,
        date=purchase_time,
        amount=float(service_to_purchase[0].price),
        type="purchase",    # The other possible type will be sale (for clients)
        object=service_to_purchase[0].model,
        total = previous_total - float(service_to_purchase[0].price)
    )

    print("I have arrive till the end of the Movement operation!")

    '''The second step is to add the service to the Cobotics' stock'''

    # To see the previous stock is necessary to retrieve all the entrances from db
    try:
        all_stock_entrances = db.session.query(StaffStock).all()
        previous_stock_entrance = all_stock_entrances[-1]
    except:
        # If there is no stock, create a new one with every value equal to zero
        previous_stock_entrance = StaffStock(date=purchase_time,
            movement_type="purchase", distance_sensor_RJ10=0,
            lidar_sensor_OSx=0, camera_C_vision33=0, servoX10Standard=0,
            servoX10Ultra=0, servoX20Ultra=0, pcb_3x=0, pcb_6x=0,
            engine_Max12V=0, bodywork_type1=0, bodywork_type2=0,
            bodywork_type3=0, wire_5V=0, wire_12V=0, led_3_3V=0)

    # It's necessary to create a new object from zero to get a new correct primary key
    AdditionToStock = StaffStock(
        date=purchase_time,
        movement_type="purchase",
        distance_sensor_RJ10=previous_stock_entrance.distance_sensor_RJ10,
        lidar_sensor_OSx=previous_stock_entrance.lidar_sensor_OSx,
        camera_C_vision33=previous_stock_entrance.camera_C_vision33,
        servoX10Standard=previous_stock_entrance.servoX10Standard,
        servoX10Ultra=previous_stock_entrance.servoX10Ultra,
        servoX20Ultra=previous_stock_entrance.servoX20Ultra,
        pcb_3x=previous_stock_entrance.pcb_3x,
        pcb_6x=previous_stock_entrance.pcb_6x,
        engine_Max12V=previous_stock_entrance.engine_Max12V,
        bodywork_type1=previous_stock_entrance.bodywork_type1,
        bodywork_type2=previous_stock_entrance.bodywork_type2,
        bodywork_type3=previous_stock_entrance.bodywork_type3,
        wire_5V=previous_stock_entrance.wire_5V,
        wire_12V=previous_stock_entrance.wire_12V,
        led_3_3V=previous_stock_entrance.led_3_3V
    )

    # Update the value of the attribute corresponding to the bought model
    model_to_acquire = service_to_purchase[0].model

    # If structure to add the model acquired to the corresponding column
    if model_to_acquire == "Distance Sensor RJ10":
        AdditionToStock.distance_sensor_RJ10 += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "LiDAR Sensor OSx":
        AdditionToStock.lidar_sensor_OSx += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Camera CVision33":
        AdditionToStock.camera_C_vision33 += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Servo XH10Standard":
        AdditionToStock.servoX10Standard += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Servo XH10Ultra":
        AdditionToStock.servoX10Ultra += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Servo XH20Ultra":
        AdditionToStock.servoX20Ultra += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "PCB-3x":
        AdditionToStock.pcb_3x += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "PCB-6x":
        AdditionToStock.pcb_6x += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Engine Max12V":
        AdditionToStock.engine_Max12V += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Bodywork Type1":
        AdditionToStock.bodywork_type1 += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Bodywork Type2":
        AdditionToStock.bodywork_type2 += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Bodywork Type3":
        AdditionToStock.bodywork_type3 += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Wire 5V":
        AdditionToStock.wire_5V += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "Wire 12V":
        AdditionToStock.wire_12V += int(service_to_purchase[0].quantity)
    elif model_to_acquire == "LED 3.3V":
        AdditionToStock.led_3_3V += int(service_to_purchase[0].quantity)

    '''The third step is to create an object ExecutedService to registered bought services'''

    ServicePurchased = ExecutedService(
        id_service=service_to_purchase[0].id_service,
        date=purchase_time,
        company_name=service_to_purchase[0].company_name,
        model=service_to_purchase[0].model,
        price=service_to_purchase[0].price,
        quantity=service_to_purchase[0].quantity
    )

    '''The last step is to delete the service from the registered service list'''
    service_to_delete = db.session.query(SupplierService).filter_by(id_service=service_to_purchase[0].id_service).delete()

    # Auxiliar operations to show again all services
    services_to_validate = db.session.query(SupplierService).all()
    list_of_suppliers = []

    for service in services_to_validate:
        service.validations = int(service.validations)
        list_of_suppliers.append(service.company_name)

    set_of_suppliers = set(list_of_suppliers)

    # Add both objects to the db
    db.session.add(PurchaseMovement)
    db.session.add(AdditionToStock)
    db.session.add(ServicePurchased)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user
    id_service = service_to_purchase[0].id_service

    db.session.commit()

    db.session.close()

    return render_template("staff_space.html",
                           department=department,
                           access_level=access_level,
                           first_name=first_name,
                           identification=identification,
                           bought_service_msg=f"Service ID {id_service} has been bought successfully!",
                           )

@MyLittleCoboticsShop.route("/staff-space/manufacture-product", methods=["POST"])
def manufacture_product():

    # Get the id of the user ordering the manufacturing process
    id_staff_member = request.args.get("id")
    staff_member = db.session.query(StaffUser).filter(StaffUser.id_user.ilike(id_staff_member)).all()

    # Get the product name and the quantity requested
    product_name = request.form["product_name"]
    product_quantity = int(request.form["product_quantity"])

    manufacturing_time = datetime.datetime.now()

    print(f"User {staff_member[0].first_name} is trying to manufacture \ "
          f"{product_quantity} units of product {product_name}")

    ### Firstly we need to deduct the materials needed to manufacture the product

    # Recover the last movement in the stock table
    try:
        all_stock_entrances = db.session.query(StaffStock).all()
        previous_stock_entrance = all_stock_entrances[-1]
    except:
        # If there is no stock, create a new one with every value equal to zero
        previous_stock_entrance = StaffStock(date=manufacturing_time,
                                             movement_type="manufacture", distance_sensor_RJ10=0,
                                             lidar_sensor_OSx=0, camera_C_vision33=0, servoX10Standard=0,
                                             servoX10Ultra=0, servoX20Ultra=0, pcb_3x=0, pcb_6x=0,
                                             engine_Max12V=0, bodywork_type1=0, bodywork_type2=0,
                                             bodywork_type3=0, wire_5V=0, wire_12V=0, led_3_3V=0)

    current_materials = [previous_stock_entrance.distance_sensor_RJ10, previous_stock_entrance.lidar_sensor_OSx,
                         previous_stock_entrance.camera_C_vision33, previous_stock_entrance.servoX10Standard,
                         previous_stock_entrance.servoX10Ultra, previous_stock_entrance.servoX20Ultra,
                         previous_stock_entrance.pcb_3x, previous_stock_entrance.pcb_6x,
                         previous_stock_entrance.engine_Max12V,
                         previous_stock_entrance.bodywork_type1, previous_stock_entrance.bodywork_type2,
                         previous_stock_entrance.bodywork_type3, previous_stock_entrance.wire_5V,
                         previous_stock_entrance.wire_12V, previous_stock_entrance.led_3_3V]

    needed_materials = {
        "Distance Sensor RJ10": 0, "LiDAR Sensor OSx": 0, "Camera CVision33": 0,
        "Servo XH10Standard": 0, "Servo XH10Ultra": 0, "Servo XH20Ultra": 0,
        "PCB-3x": 0, "PCB-6x": 0, "Engine Max12V": 0, "Bodywork Type1": 0,
        "Bodywork Type2": 0, "Bodywork Type3": 0, "Wire 5V": 0, "Wire 12V": 0, "LED 3.3V": 0,
    }

    if product_name == "Talisman T":
        production_cost = 150*product_quantity
        added_products = [product_quantity, 0, 0]
        bill_of_materials = [4, 0, 1, 5, 2, 0, 8, 0, 0, 1, 0, 0, 2, 0, 5]
        for ind,key in enumerate(needed_materials.keys()):
            needed_materials[key] = bill_of_materials[ind]*product_quantity

    elif product_name == "Overlord K":
        production_cost = 900*product_quantity
        added_products = [0, product_quantity, 0]
        bill_of_materials = [4, 1, 1, 20, 5, 0, 10, 5, 4, 0, 1, 1, 5, 3, 10]
        for ind,key in enumerate(needed_materials.keys()):
            needed_materials[key] = bill_of_materials[ind]*product_quantity

    elif product_name == "Sentinel v10":
        production_cost = 1000*product_quantity
        added_products = [0, 0, product_quantity]
        bill_of_materials = [6, 1, 2, 5, 5, 2, 5, 5, 6, 2, 0, 1, 5, 2, 20]
        for ind,key in enumerate(needed_materials.keys()):
            needed_materials[key] = bill_of_materials[ind]*product_quantity

    list_of_insufficient_materials = []

    for ind, val in enumerate(needed_materials.values()):
        if val > current_materials[ind]:
            lacking_item = list(needed_materials.keys())[ind]
            list_of_insufficient_materials.append(f"{lacking_item} ({val-current_materials[ind]} needed)")

    # If there are not enough materials, abort the manufacturing process
    if len(list_of_insufficient_materials) > 0:
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               insufficient_materials_msg="There are not enough materials in stock to manufacture this product",
                               list_of_insufficient_materials=list_of_insufficient_materials)

    new_stock_entrance = StaffStock(date=manufacturing_time,
            movement_type="manufacture",
            distance_sensor_RJ10=current_materials[0] - bill_of_materials[0]*product_quantity,
            lidar_sensor_OSx=current_materials[1] - bill_of_materials[1]*product_quantity,
            camera_C_vision33=current_materials[2] - bill_of_materials[2]*product_quantity,
            servoX10Standard=current_materials[3] - bill_of_materials[3]*product_quantity,
            servoX10Ultra=current_materials[4] - bill_of_materials[4]*product_quantity,
            servoX20Ultra=current_materials[5] - bill_of_materials[5]*product_quantity,
            pcb_3x=current_materials[6] - bill_of_materials[6]*product_quantity,
            pcb_6x=current_materials[7] - bill_of_materials[7]*product_quantity,
            engine_Max12V=current_materials[8] - bill_of_materials[8]*product_quantity,
            bodywork_type1=current_materials[9] - bill_of_materials[9]*product_quantity,
            bodywork_type2=current_materials[10] - bill_of_materials[10]*product_quantity,
            bodywork_type3=current_materials[11] - bill_of_materials[11]*product_quantity,
            wire_5V=current_materials[12] - bill_of_materials[12]*product_quantity,
            wire_12V=current_materials[13] - bill_of_materials[13]*product_quantity,
            led_3_3V=current_materials[14] - bill_of_materials[14]*product_quantity)

    print("Have created the object new_stock_entrance")

    ### The next step is to create the movement to deduct the cost of the manufacturing process (~20% of the materials cost)
    # It is necessary to recover the last movement
    try:
        last_movement_executed = db.session.query(StaffMovement).all()
        previous_total = float(last_movement_executed[-1].total)
    except:
        previous_total = 0

    # Check if there is enough money to afford production costs
    if production_cost > previous_total:
        return render_template("staff_space.html",
                               department=staff_member[0].department,
                               access_level=staff_member[0].access_level,
                               first_name=staff_member[0].first_name,
                               identification=staff_member[0].id_user,
                               insufficient_money_msg=f"There is no money enough to afford the production costs ({production_cost-previous_total}$ needed)")

    manufacturing_cost = StaffMovement(
        origin_staff_member=staff_member[0].staff_id,
        destination="manufacturing process",
        date=manufacturing_time,
        amount=production_cost,
        type="internal cost",
        object=f"{product_quantity} {product_name}",
        total=previous_total - production_cost
    )

    print(f"The product has been manufactured and the current total is {manufacturing_cost.total}")

    ### The final step is to add the quantity of manufactured products to the db
    # For that again, we need to recover the previous entrance on this table
    try:
        storehouse_movements = db.session.query(StorehouseMovement).all()
        previous_storehouse_state = storehouse_movements[-1]
    except:
        previous_storehouse_state = StorehouseMovement(
        origin_staff_member=staff_member[0].staff_id,
        date=manufacturing_time,
        product=product_name,
        production_cost=production_cost,
        talisman_t_total=0,
        overlord_k_total=0,
        sentinel_v10_total=0
        )

    new_storehouse_movement = StorehouseMovement(
        origin_staff_member=staff_member[0].staff_id,
        date=manufacturing_time,
        product=product_name,
        production_cost=production_cost,
        talisman_t_total=previous_storehouse_state.talisman_t_total + added_products[0],
        overlord_k_total=previous_storehouse_state.overlord_k_total + added_products[1],
        sentinel_v10_total=previous_storehouse_state.sentinel_v10_total + added_products[2]
        )

    print(f'''The new quantities of the different products are: 
            talisman_t_total: {new_storehouse_movement.talisman_t_total}
            overlord_k_total: {new_storehouse_movement.overlord_k_total}
            sentinel_v10_total: {new_storehouse_movement.sentinel_v10_total}
            ''')

    # To finish the function, we add the three objects to the db:
    # The reduction in the stock
    db.session.add(new_stock_entrance)
    # The expenses of the manufacturing costs
    db.session.add(manufacturing_cost)
    # The manufactured products to the storehouse
    db.session.add(new_storehouse_movement)

    department = staff_member[0].department
    access_level = staff_member[0].access_level
    first_name = staff_member[0].first_name
    identification = staff_member[0].id_user

    db.session.commit()
    db.session.close()

    return render_template("staff_space.html",
                           department=department,
                           access_level=access_level,
                           first_name=first_name,
                           identification=identification,
                           correctly_manufactured_process = "The product was correctly manufactured!")

### User movements functions

@MyLittleCoboticsShop.route("/user-space/make-deposit", methods=["POST"])
def user_make_deposit():

    # Get the id of the user making the deposit
    id_user = request.args.get("id")
    print("id_user:", id_user)
    user = db.session.query(RegisteredUser).filter(RegisteredUser.id_user.ilike(id_user)).all()

    # Get the quantity of the deposit passed through POST method
    deposit_quantity = float(request.form["deposit_quantity"])

    print(f"The user {id_user} is trying to make a deposit of {deposit_quantity}")

    # Get the last deposit executed to calculate the current total
    try:
        last_movement_executed = db.session.query(UserMovement).filter(UserMovement.origin_user.ilike(id_user)).all()
        previous_total = float(last_movement_executed[-1].total)
    except:
        previous_total = 0

    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user="Default",
            date="None",
            Talisman_T_price=1200,
            Overlord_K_price=6000,
            Sentinel_v10_price=8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]

    if abs(deposit_quantity) > previous_total and deposit_quantity < 0:
        return render_template("user_space.html",
                               username=user[0].username,
                               identification=user[0].id_user,
                               prices_list=prices_list,
                               show_offer=True,
                               incorrect_movement_msg=f"Not enough money to extract from account!")


    NewMovement = UserMovement(
        origin_user=id_user,
        destination="User account",
        date=str(datetime.datetime.now()),
        amount=deposit_quantity,
        type="Deposit",
        object="Deposit",
        total = previous_total + deposit_quantity
    )

    db.session.add(NewMovement)

    username = user[0].username
    identification = user[0].id_user
    new_total = round(NewMovement.total,2)

    db.session.commit()
    db.session.close()

    return render_template("user_space.html",
                           username=username,
                           identification=identification,
                           prices_list=prices_list,
                           show_offer=True,
                           correct_movement_msg=f"Deposit performed correctly! The current total is {new_total}$")

@MyLittleCoboticsShop.route("/user-space/purchase-product", methods=["POST"])
def purchase_product():

    # Get the information arriving as URL parameter
    id_user = request.args.get("id")
    user = db.session.query(RegisteredUser).filter(RegisteredUser.id_user.ilike(id_user)).all()
    product_name = request.args.get("product") # talisman, overlord or sentinel
    purchase_time = str(datetime.datetime.now())

    print(f"The user {user[0].first_name} is trying to buy product {product_name}")


    try:
        prices_entrances = db.session.query(PricesSetupLog).all()
        last_prices_entrance = prices_entrances[-1]
    except:
        last_prices_entrance = PricesSetupLog(
            id_staff_user="Default",
            date="None",
            Talisman_T_price=1200,
            Overlord_K_price=6000,
            Sentinel_v10_price=8000
        )
    prices_list = [last_prices_entrance.Talisman_T_price,
                   last_prices_entrance.Overlord_K_price,
                   last_prices_entrance.Sentinel_v10_price]

    if product_name=="Talisman":
        product_price = prices_list[0]
    elif product_name=="Overlord":
        product_price = prices_list[1]
    elif product_name=="Sentinel":
        product_price = prices_list[2]

    '''The first thing to do deduct the price to the user, so it's
    necessary to create a user movement'''

    # To give the new total is necessary to retrieve all the movements from db
    try:
        # Select only movements from this user
        all_movement_executed = db.session.query(UserMovement).filter(UserMovement.origin_user.ilike(id_user)).all()
        previous_total = float(all_movement_executed[-1].total)
    except:
        previous_total = 0

    # verify is the total available is enough to buy the service
    if previous_total < product_price:
        return render_template("user_space.html",
                               identification=user[0].id_user,
                               username=user[0].username,
                               prices_list=prices_list,
                               show_offer=True,
                               not_enough_money_message="There isn't enough money in your account to do that. Please, make a deposit!")

    # Create the movement, which is equivalent to pay
    user_buying_movement = UserMovement(
        origin_user=id_user,
        destination="Cobotics",
        date=purchase_time,
        amount=product_price,
        type="Purchase",    # The other possible type will be sale (for clients)
        object=product_name,
        total = previous_total - product_price
    )

    print("I have arrive till the end of the Movement operation!")

    ''' The second step is to add the money to the cobotcs account'''

    try:
        # Here it's not necessary to filter because there is only one "bank account" for the company Cobotics
        all_movement_executed = db.session.query(StaffMovement).all()
        previous_total = float(all_movement_executed[-1].total)
    except:
        previous_total = 0

    # Create the movement, which is equivalent to pay
    sale_movement = StaffMovement(
        origin_staff_member="Client",
        destination="Cobotics",
        date=purchase_time,
        amount=product_price,
        type="Sale",  # The other possible type will be sale (for clients)
        object=product_name,
        total=previous_total + product_price
    )

    '''The third step is to deduct the product from the Cobotics products storehouse'''

    # To see the previous stock is necessary to retrieve all the entrances from db
    try:
        all_storehouse_entrances = db.session.query(StorehouseMovement).all()
        previous_stock_entrance = all_storehouse_entrances[-1]
    except:
        # If there is no stock, create a new one with every value equal to zero
        previous_stock_entrance = StorehouseMovement(origin_staff_member=None,
            date=purchase_time, product=None, production_cost=0,
            talisman_t_total=0, overlord_k_total=0, sentinel_v10_total=0)

    if product_name == "Talisman":
        if previous_stock_entrance.talisman_t_total > 0:
            product_key = "TAL"
            new_talisman_quantity = previous_stock_entrance.talisman_t_total - 1
            new_overlord_quantity = previous_stock_entrance.overlord_k_total
            new_sentinel_quantity = previous_stock_entrance.sentinel_v10_total
        else:
            return render_template("user_space.html",
                                   identification=user[0].id_user,
                                   username=user[0].username,
                                   prices_list=prices_list,
                                   show_offer=True,
                                   product_not_available_message="We are out of stock of Talisman T, sorry!")
    elif product_name == "Overlord":
        if previous_stock_entrance.overlord_k_total > 0:
            product_key = "OVE"
            new_overlord_quantity = previous_stock_entrance.overlord_k_total - 1
            new_talisman_quantity = previous_stock_entrance.talisman_t_total
            new_sentinel_quantity = previous_stock_entrance.sentinel_v10_total
        else:
            return render_template("user_space.html",
                                   identification=user[0].id_user,
                                   username=user[0].username,
                                   prices_list=prices_list,
                                   show_offer=True,
                                   product_not_available_message="We are out of stock of Overlord K, sorry!")
    elif product_name == "Sentinel":
        if previous_stock_entrance.sentinel_v10_total > 0:
            product_key = "SEN"
            new_sentinel_quantity = previous_stock_entrance.sentinel_v10_total - 1
            new_talisman_quantity = previous_stock_entrance.talisman_t_total
            new_overlord_quantity = previous_stock_entrance.overlord_k_total
        else:
            return render_template("user_space.html",
                                   identification=user[0].id_user,
                                   username=user[0].username,
                                   prices_list=prices_list,
                                   show_offer=True,
                                   product_not_available_message="We are out of stock of Sentinel v10, sorry!")

    # Then we create a new StorehouseMovement object to register the movement

    storehouse_movement = StorehouseMovement(
        origin_staff_member="Client",
        date=purchase_time,
        product=product_name,
        production_cost=0,
        talisman_t_total=new_talisman_quantity,
        overlord_k_total=new_overlord_quantity,
        sentinel_v10_total=new_sentinel_quantity
    )

    ''' To have a clear vision of made sales, we create an object executed sales'''

    finished_sale = ExecutedSales(
        id_product = product_key,
        date = purchase_time,
        buyer_user = user[0].username,
        product = product_name,
        price = product_price
    )

    ''' To supply high level access staff users with extended information, we create the following product'''

    client_extended_information = InfoClientLog(
        sale_date = purchase_time,
        product_bought = product_name,
        price = product_price,
        first_name = user[0].first_name,
        last_name = user[0].last_name,
        date_of_birth = user[0].date_of_birth,
        phone_number = user[0].phone_number,
        country = user[0].country,
        city = user[0].city,
        address = user[0].address,
        zip_code = user[0].zip_code,
        username = user[0].username,
        email = user[0].email,
        card_number = user[0].card_number
    )

    '''Finally, store the new entrances in db and return users to their spaces'''

    db.session.add(user_buying_movement)
    db.session.add(sale_movement)
    db.session.add(finished_sale)
    db.session.add(storehouse_movement)
    db.session.add(client_extended_information)

    db.session.commit()

    username = user[0].username
    identification = user[0].id_user

    db.session.close()

    return render_template("user_space.html",
                           identification=identification,
                           username=username,
                           prices_list=prices_list,
                           show_offer=True,
                           product_correctly_bought_msg=f"That {product_name} is yours! Enjoy!")

''' ############## Welcoming page assigment ############## '''

@MyLittleCoboticsShop.route("/")
def home():
    print("Welcome to MyLittleCoboticsShop!")
    return render_template("index.html")

if __name__ == "__main__":

    db.Base.metadata.create_all(db.engine)

    MyLittleCoboticsShop.run(debug=True)
