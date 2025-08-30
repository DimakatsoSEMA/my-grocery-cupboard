🛒 My Grocery Cupboard

A pantry management and meal planning application designed to help users keep track of their food inventory, avoid waste, and simplify grocery shopping. The system notifies users about low or out-of-stock items, suggests grocery lists, recommends food swaps, and organizes storage areas like fridge, freezer, and cupboard.

🚀 Features
•	Inventory Management – Track pantry items, quantities, and categories (fridge, freezer, cupboard).
•	Low Stock Alerts – Get notified when items are running low or out of stock.
•	Food Swaps – Get suggestions for ingredient substitutions.

🛠️ Tech Stack
•	Backend: Django & Django REST Framework
•	Database: SQLite (development), PostgreSQL (production ready)
•	Frontend: To be added 
•	Authentication: Django built-in authentication system (with role-based access in future updates)
•	Other Tools: Docker (planned), Git/GitHub for version control

📂 Project Structure
grocery_cupboard/
│
├── inventory/       # App for managing pantry items
├── meals/           # App for managing meals and favorites
├── grocery_cupboard/ # Main Django project settings
└── README.md
________________________________________
⚙️ Installation & Setup
1.	Clone the repository:
2.	git clone https://github.com/yourusername/grocery_cupboard.git
3.	cd grocery_cupboard
4.	Create and activate a virtual environment:
5.	python -m venv venv
6.	source venv/bin/activate   # Mac
7.	Install dependencies:
8.	pip install -r requirements.txt
9.	Apply migrations:
10.	python manage.py migrate
11.	Create a superuser:
12.	python manage.py createsuperuser
13.	Run the development server:
14.	python manage.py runserver
15.	Open your browser and go to:
16.	http://127.0.0.1:8000/
________________________________________
🔮 Future Enhancements
✅ User authentication with profiles
✅ Meal planning calendar
✅ Barcode scanning for faster inventory updates
✅ API endpoints for mobile app integration
✅ Docker & CI/CD setup for deployment
✅ Meal Favorites – Save and organize favorite meals for easy access.
✅ Grocery List Generator – Automatically generate shopping lists based on your inventory.
✅ Organized Storage – Categorize and locate items quickly across different storage areas.
________________________________________
📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
________________________________________
