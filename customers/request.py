CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hannah@hall.com"
    },
    {
        "id": 2,
        "name": "Phillip Jacobs",
        "address": "7004 Chestnut Ct",
        "email": "phillip@jacobs.com"
    },
    {
        "id": 3,
        "name": "John Michael",
        "address": "7006 Chestnut Ct",
        "email": "john@michael.com"
    },
    {
        "id": 4,
        "name": "Janice Karen",
        "address": "7008 Chestnut Ct",
        "email": "janice@karen.com"
    },
    {
        "id": 5,
        "name": "Jarett Williamson",
        "address": "7010 Chestnut Ct",
        "email": "jarett@williamson.com"
    },
    {
        "email": "super@b.com",
        "name": "super b",
        "id": 6
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):

    requested_customer = None

    for customer in CUSTOMERS:

        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer
