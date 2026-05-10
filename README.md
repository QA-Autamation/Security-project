🛡️ Security System Project
A Python-based security and user management system using SQLite3. This project features a modular architecture, separating user authentication from administrative control.

📂 Project Architecture
The project is organized into a modular structure to ensure clean code and data separation:

Data Base/: Contains the SQLite database files (security.db, registration_base.db).

src/: Contains the core logic scripts.

register_base.py: Database initialization and table creation.

get_reservation.py: The client-side application for Sign-Up and Login.

admin.py: The administrative panel for managing the Blacklist.

🚀 Key Features
1. User Authentication
Sign-Up: Securely registers new users into the database.

Login: Validates credentials against stored data.

Auto-Security Check: Upon login, the system automatically cross-references the username with the Blacklist to deny access to restricted individuals.

2. Admin Dashboard
Blacklist Management: Add offenders with specific reasons and danger levels (1-5).

Live Database View: Fetch and display all current restricted users.

Record Deletion: Remove users from the blacklist once they are cleared.

🛠️ Technical Stack
Language: Python 3.14+

Database: SQLite3

Modules: os, sqlite3

⚙️ Setup & Installation
Initialize the Database:
Run the setup script to create the necessary directories and tables.

Bash
python "register base.py"


2. **Run the Client App**:
   To register or log in as a user:
   ```bash
   python "get_reservation.py"
Access Admin Panel:
To manage security protocols and the blacklist:

Bash
python "admin.py"
👤 Author
Yahyobek
6th-grade student & Self-taught Python Developer
