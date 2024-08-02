# Moon Mocha - Coffee Shop Website

Welcome to **Moon Mocha**, the ultimate online destination for coffee lovers! This repository contains the codebase for a Django-powered coffee shop website. Here, customers can browse our delicious menu, add items to their cart, and place orders for both hot and cold coffees.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Menu Display**: View the full range of hot and cold coffees with detailed descriptions and pricing.
- **Add to Cart**: Users can easily add items to their cart with customizable quantities.
- **User Authentication**: Secure login and registration system.
- **Order Management**: Users can view and manage their orders.
- **Responsive Design**: The site is fully responsive and works across all devices.

## Technologies Used

- **Django 4.2.x**: The web framework used to build the website.
- **SQLite**: Default database for development.
- **Bootstrap**: For responsive design and UI components.
- **HTML5/CSS3**: Core front-end technologies.
- **JavaScript**: For interactive elements on the site.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Git
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/moon-mocha.git
   cd moon-mocha
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional but recommended for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

### Running the Project

To run the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the site.

## Usage

- **Home Page**: Browse through the different sections of the website.
- **Menu**: View the coffee menu with prices and descriptions.
- **Add to Cart**: Add your favorite coffee to the cart and specify the quantity.
- **Login/Signup**: Create an account or log in to manage your orders.
- **Order**: Review your cart and place an order.


## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## Contact

For any questions or suggestions, feel free to open an issue or contact the project maintainer:

- **Email**: moonmocha@example.com
- **GitHub**: [yourusername](https://github.com/Sanjoli2002)

---

Enjoy your coffee with **Moon Mocha**! ☕
```
