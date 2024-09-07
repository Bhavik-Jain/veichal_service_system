# Vehicle Service System

## Overview

The Vehicle Service System is a full-stack web application for managing vehicle services. It allows operations users to register components, manage vehicles and issues, and calculate transactions. The system also provides revenue analytics through responsive graphs.

## Tech Stack

- **Backend:** Django
- **Database:** SQLite
- **API:** Django REST Framework

## Features

1. **Component Management:** Register components with pricing and manage them.
2. **Vehicle Management:** Add and manage vehicles.
3. **Issue Tracking:** Add issues for vehicles, choose between new components or repairs.
4. **Transaction Management:** Calculate and manage transactions.

## Installation

### Backend Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Bhavik-Jain/veichal_service_system.git
    cd vehicle_s_system
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Server:**

    ```bash
    python manage.py runserver

7. **Admin Pannel:**

    accessing the admin panel using 'admin' as pass and user:

8. **Navigate to the Admin Panel:**

    Once the server is running, open your web browser and go to:

    ```
    http://127.0.0.1:8000/admin/
    ```

    Log in using the superuser credentials you created in the previous step.

9. **Add Data to Models:**

    - **Components:** Go to the "Components" section in the admin panel to add components. Enter the required details, including the name, price, and description.
  
    - **Vehicles:** In the "Vehicles" section, you can add vehicles by providing the relevant information such as vehicle name, type, and other related data.

    - **Issues:** Navigate to the "Issues" section to add and manage issues related to vehicles. You can select between adding new components or repairs for each issue.

    - **Transactions:** Manage financial transactions related to services in the "Transactions" section. Add transaction details to keep track of payments and revenue.

10. **Start Using the Application:**

    With data added, you can now use the Vehicle Service System for managing vehicle services, tracking issues, and calculating transactions.
