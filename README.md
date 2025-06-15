# ShopEzy - E-commerce Web Application

A comprehensive e-commerce platform built with Django 5.0, featuring a robust product management system, user authentication, shopping cart functionality, and order processing.

## Features

- User Authentication (Customer & Vendor)
- Product Management (Electronics, Garments, Groceries)
- Shopping Cart System
- Order Processing
- Customer Profiles
- Vendor Management
- Responsive Design

## Tech Stack

- Backend: Django 5.0
- Database: MySQL 8.0
- Frontend: HTML, CSS, JavaScript
- Additional Libraries: OpenCV, Matplotlib, Pillow

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/HabibUllah61103/ShopEzy-WebApp-SE.git
cd ShopEzy-WebApp-SE
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Database Setup

- Install MySQL Server 8.0
- Copy the `storedb` folder contents to `C:\ProgramData\MySQL\MySQL Server 8.0\Data`
- Create a database named `shopezy`
- Update database settings in `ShopEzy/ShopEzy/settings.py`

5. Run migrations

```bash
python manage.py migrate
```

6. Start development server

```bash
python manage.py runserver
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Habib Ullah - hu3960990@gmail.com
Project Link: https://github.com/HabibUllah61103/ShopEzy-WebApp-SE
