# Without Type Safety
# def insert_patient_data(name, age):
#     print(name)
#     print(age)
#     print("inserted into database")

# insert_patient_data('shubham', 'twenty')

# With Type Safety
# Inserting Data
def insert_patient_data(name: str, age: int):
    # type error
    if type(name) == str and type(age) == int:
        # value error (data validation)
        if age < 0:
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError('Incorrect data type')

insert_patient_data('shubham', 20)

# Updating Data
def update_patient_data(name: str, age: int):
    # type error
    if type(name) == str and type(age) == int:
        # value error (data validation)
        if age < 0:
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print("updated into database")
    else:
        raise TypeError('Incorrect data type')

update_patient_data('shubham', 20)