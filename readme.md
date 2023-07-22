Introduction to Corporate Asset Tracker Application:

This is a simple Corporate Asset Tracker Application that simplifies the asset management process, empowering companies to efficiently monitor and control their assets. Developed by Hijam Ibna Omar using Django Rest Framework.
Key Features:
1. Multi-Company Support: The application is designed to cater to multiple companies, enabling each company to have its own asset management system within the software.
2. Staff Management: Company administrators can easily create and manage staff profiles.
3. Employee Registration: The software allows the registration of employees associated with a company. Each employee's details, such as name, address, email, and phone number, can be conveniently .
4. Asset Creation: Company administrators can add new assets to the system, providing essential details such as asset name and description.
5. Asset Log Tracking: The software facilitates comprehensive asset log tracking, allowing staff to log asset usage, checkout quantity, checkout time, condition, and notes. Additionally, the return date, return quantity, return condition, and return notes can be logged when assets are returned.
6. JWT Authentication: To ensure data security and privacy, the software incorporates Simple JSON Web Token (JWT) authentication, allowing only authorized users to access and manage asset-related information.


API Documentation for Corporate Asset Tracker Software:

1. Register a User and Company as the Owner:
   - URL: `/api/signup-as-company-owner/`
   - Method: POST
   - Parameters:
      - `username` (string): Username of the owner (unique)
      - `password` (string): Password for the owner's account
      - `email` (string): Email address of the owner
      - `first_name` (string): First name of the owner
      - `last_name` (string): Last name of the owner
      - `name` (string): Name of the company 
      - `address` (string): Address of the company
   - Authentication: None (Open to anyone)
   - Response: Company details (ID, user, name, address)

2. Register a User as Staff with a Company:
   - URL: `/api/signup-as-staff/`
   - Method: POST
   - Parameters:
      - `username` (string): Username of the staff (unique)
      - `password` (string): Password for the staff's account
      - `email` (string): Email address of the staff
      - `first_name` (string): First name of the staff
      - `last_name` (string): Last name of the staff
      - `company` (object): Company name of the employee
      - `address` (string): Address of the staff
   - Authentication: None (Open to anyone)
   - Response: Staff details (ID, user, company, address)

3. List All Staffs:
   - URL: `/api/staff/`
   - Method: GET
   - Authentication: JWT Token required
   - Response: List of all staffs with details (ID, user, company, address)

4. Retrieve, Update, or Delete a Staff:
   - URL: `/api/staff/<staff_id>/`
   - Method: GET, PUT, DELETE
   - Authentication: JWT Token required
   - Response: Staff details (ID, user, company, address)

5. Create an Employee for a Company:
   - URL: `/api/employees/create/`
   - Method: POST
   - Parameters:
      - `name` (string): Name of the employee
      - `address` (string): Address of the employee
      - `email` (string): Email address of the employee
      - `phone` (string): Phone number of the employee
   - Authentication: JWT Token required
   - Response: Employee details (ID, company, name, address, email, phone)

6. List All Employees:
   - URL: `/api/employees/`
   - Method: GET
   - Authentication: JWT Token required
   - Response: List of all employees with details (ID, company, name, address, email, phone)

7. Retrieve, Update, or Delete an Employee:
   - URL: `/api/employees/<employee_id>/`
   - Method: GET, PUT, DELETE
   - Authentication: JWT Token required
   - Response: Employee details (ID, company, name, address, email, phone)

8. Create an Asset for a Company:
   - URL: `/api/assets/create/`
   - Method: POST
   - Parameters:
      - `name` (string): Name of the asset (unique within the company)
      - `description` (string): Description of the asset
   - Authentication: JWT Token required
   - Response: Asset details (ID, name, description)

9. List All Assets:
   - URL: `/api/assets/`
   - Method: GET
   - Authentication: JWT Token required
   - Response: List of all assets with details (ID, name, description)

10. Retrieve, Update, or Delete an Asset:
    - URL: `/api/assets/<asset_id>/`
    - Method: GET, PUT, DELETE
    - Authentication: JWT Token required
    - Response: Asset details (ID, name, description)

11. Log Asset Usage:
    - URL: `/api/asset-logs/create/`
    - Method: POST
    - Parameters:
       - `asset` (object): Asset details (name)
       - `employee` (object): Employee details (name)
       - `checkout_quantity` (integer): Quantity of assets being checked out
       - `checkout_time` (datetime): Timestamp of checkout
       - `checkout_condition` (string): Condition of the asset during checkout (good, fair, poor)
       - `checkout_note` (string): Notes for checkout
       - `duration` (date): Return date for the asset
       - `is_returned` (boolean): True if the asset is returned, False otherwise
       - `return_time` (datetime): Timestamp of asset return (optional)
       - `return_quantity` (integer): Quantity of assets returned (optional)
       - `return_condition` (string): Condition of the asset during return (good, damaged, lost) (optional)
       - `returned_note` (string): Notes for asset return (optional)
    - Authentication: JWT Token required
    - Response: Log details (ID, asset, employee, checkout_quantity, checkout_time, checkout_condition, checkout_note, duration, is_returned, return_time, return_quantity, return_condition, returned_note)



12. List All Asset Logs:
    - URL: `/api/asset-logs/`
    - Method: GET
    - Authentication: JWT Token required
    - Response: List of all asset logs with details (ID, asset, employee, checkout_quantity, checkout_time, checkout_condition, checkout_note, duration, is_returned, return_time, return_quantity, return_condition, returned_note)

13. Retrieve, Update, or Delete an Asset Log:
    - URL: `/api/asset-logs/<asset_log_id>/`
    - Method: GET, PUT, DELETE
    - Authentication: JWT Token required
    - Response: Asset Log details (ID, asset, employee, checkout_quantity, checkout_time, checkout_condition, checkout_note, duration, is_returned, return_time, return_quantity, return_condition, returned_note)


Some JSON Object Examples for Request/Response:

1. Register a User and Company as the Owner (POST):
```
{
    "user": {
        "username": "owner123",
        "password": "pass123",
        "email": "owner@example.com",
        "first_name": "Razib",
        "last_name": "Hossain"
    },
    "name": "REPLIQ",
    "address": "Main Street Mohammadpur"
}

Response:
{
    "id": 12,
    "user": {
        "username": "owner1234",
        "email": "owner@example.com",
        "first_name": "Razib",
        "last_name": "Hossain"
    },
    "name": "REPLIQ",
    "address": "Main Street Mohammadpur"
}
```

2. Register a User as Staff with a Company (POST):
```
{
    "user": {
        "username": "staff123",
        "password": "staff123",
        "email": "staff123@gmail.com",
        "first_name": "staff",
        "last_name": "123"
    },
    "company": {
        "name": "REPLIQ"
    },
    "address": "Dhaka"
}

Response:

{
    "id": 13,
    "user": {
        "id": 33,
        "username": "staff123",
        "email": "staff123@gmail.com",
        "first_name": "staff",
        "last_name": "123"
    },
    "company": {
        "name": "REPLIQ"
    },
    "address": "Dhaka"
}
```
3. Create an Employee for a Company (POST):
```
{
   "name": "Employee Name",
   "address": "789 Street",
   "email": "employee@example.com",
   "phone": "123-456-7890"
}
```

4. Create an Asset for a Company (POST):
```
{
   "name": "Laptop",
   "description": "Dell Inspiron 15"
}
```

5. Log Asset Usage (POST):
```
{
    "asset": "Laptop",
    "employee": "Employee Name",
    "checkout_quantity": 1,
    "checkout_time": "2023-07-20T12:00:00",
    "checkout_condition": "good",
    "chekout_note": "Asset checked out for a project",
    "duration": "2023-08-20",
    "is_returned": false

}

Response:
{
"id":8,
"asset":"Laptop",
"employee":"Employee Name",
"checkout_quantity":1,
"checkout_time":"2023-07-20T12:00:00Z",
"checkout_condition":"good",
"chekout_note":"Asset checked out for a project",
"duration":"2023-08-20",
"is_returned":false,
"return_time":null,
"return_quantity":0,
"return_condition":null,
"returned_note":null
}
```
