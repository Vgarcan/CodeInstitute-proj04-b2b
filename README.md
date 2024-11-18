# Red Bazaar - B2B Marketplace

![Main LOGO](/red-bazaar/static/imgs/banner1.webp)

# Victor Garcia Cantalapidera 
- Slack: [@Victor Garcia](https://code-institute-room.slack.com/team/U0695HZA7FZ)
- GitHub: [Vgarcan](https://github.com/Vgarcan)
- LinkedIn: [Victor Garcia](https://www.linkedin.com/in/vgc89/)

## Check us out!

[Red Bazaar - Heroku](https://redbazaar.herokuapp.com/) 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Development Tools](#development-tools)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Wireframes](#wireframes)
- [Colors](#colors)
  - [Color Customization Process](#color-customization-process)
- [User Experience](#user-experience)
  - [Key Principles](#key-principles)
  - [User Stories](#user-stories)
  - [Future Enhancements](#future-enhancements)
- [Testing](#testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Accessibility](#accessibility)
  - [Wave Validation](#wave-validation)
  - [Lighthouse Validation](#lighthouse-validation)
  - [JSHint Validation](#jshint-validation)
  - [PEP8 Validation](#pep8-validation)
  - [Device Testing](#device-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [User Stories Testing](#user-stories-testing)
- [Collaborative Efforts](#collaborative-efforts)
- [Current State and Future Plans](#current-state-and-future-plans)
  - [Current State](#current-state)
  - [Future Plans](#future-plans)
- [Deployment](#deployment)
- [License](#license)
- [Bugs and Challenges](#bugs-and-challenges)
- [Acknowledgement](#acknowledgement)

## Introduction

**RedBazaar** is a B2B platform designed to connect restaurants and suppliers, focusing on fostering trade between small and medium-sized enterprises (SMEs). The platform aims to provide a professional, centralized tool that simplifies the ordering process for restaurants, helping them save time, reduce product waste, and cut costs. For suppliers, especially smaller ones, RedBazaar offers increased visibility, making it easier to reach potential customers in a competitive market.

This idea emerged from a personal experience while working in a café, where I observed the inefficiencies of managing orders through multiple platforms. RedBazaar solves this problem by grouping all suppliers under one platform, enabling restaurants to search for products rather than being tied to a specific supplier. For example, if a restaurant needs chicken strips, the platform displays all available options from various suppliers, allowing the business to choose the best deal.

Looking ahead, RedBazaar plans to introduce features that will enhance efficiency and flexibility for both restaurants and suppliers. Future updates will include tools for creating optimised shopping lists, finding the best-priced products, and promoting daily offers from suppliers. By focusing on affordability and accessibility, RedBazaar aims to build a community that empowers SMEs to thrive in the digital marketplace.


## Features

RedBazaar is currently in its initial development phase, providing the core functionality required to facilitate seamless transactions between buyers (restaurants) and suppliers. The platform is focused on delivering a simple and effective e-commerce experience, ensuring it meets the minimum viable product requirements. 

At this stage, RedBazaar includes the following features:
- **Product Search:** Restaurants can browse available products across multiple suppliers.
- **Shopping Cart and Transactions:** Buyers can add products to a shopping cart and complete purchases directly through the website.
- **Order Management:** Suppliers receive detailed orders submitted by buyers, including all necessary information to fulfil the requests.
- **Order Status Updates:** Suppliers can update the status of orders, providing real-time visibility for buyers about their purchases.

While the current state focuses on essential functionality, it sets the foundation for future enhancements that will make the platform more dynamic, efficient, and user-friendly.
## Development Tools

RedBazaar is being developed using a set of tools that streamline the coding, version control, and deployment processes. These tools ensure that development adheres to best practices and allows for efficient collaboration and deployment.

- **Visual Studio Code (VSCode):**  
  The primary IDE used for writing and managing the code. VSCode is enhanced with extensions such as:
  - **autoPEP8:** Automatically formats the code to comply with the PEP8 standard, ensuring clean and readable Python code.

- **Git:**  
  Used for version control, enabling the tracking of changes to the codebase and facilitating collaboration among developers.

- **GitHub:**  
  The repository for hosting the project, allowing for remote collaboration, issue tracking, and streamlined version management.

- **pip and `requirements.txt`:**  
  pip is used for managing project dependencies, with all necessary libraries listed in the `requirements.txt` file for easy installation and environment setup.

- **Heroku:**  
  The platform used for deploying the project. Heroku allows for quick and scalable deployment, making it easy to share and test the application in a live environment.


## Technologies Used

### Backend

- **Django:**  
  The primary framework used for building the backend of RedBazaar. Django handles the server-side logic, routing, and database interactions. It also includes a built-in authentication system for managing user registration and login.

- **Python:**  
  The core programming language for RedBazaar, used in conjunction with Django to build robust and scalable server-side functionality.

- **Django ORM and Database:**  
  Django's Object-Relational Mapping (ORM) is used for database operations. The database structure is managed entirely through Django, ensuring consistency and efficiency.

- **Django MPTT:**  
  This library is used for managing hierarchical data, particularly in creating parent and child categories for the products. It helps organise the categories into tree structures for better usability and data representation.

- **Django AllAuth:**  
  A library integrated for user authentication, registration, and login. It supports third-party authentication providers like Google and GitHub, allowing users to register with a single click.

### Frontend

- **HTML5:**  
  Used to structure the content of the website, ensuring semantic and accessible markup.

- **CSS3:**  
  Utilised to style the website, providing consistent and responsive designs across different devices.

- **JavaScript:**  
  Enhances interactivity on the site by enabling dynamic content updates and user interactions.

- **Bootstrap:**  
  A popular front-end framework that helps create responsive and visually appealing designs. Bootstrap is used for layout management, navigation bars, modals, and other UI components.

## Project Structure

- <img src="red-bazaar/static/imgs/readme-pics/ico/red-folder-icon.ico" width="18px"> **Root Directory**
    
    - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **red-bazaar/** (Main application folder)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **_core/** (Core functionalities and configurations)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the core module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `settings.py` (Core settings and configurations)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for the core application)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `asgi.py` (ASGI configuration for asynchronous requests)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `wsgi.py` (WSGI configuration for server deployment)
            
        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **main/** (Main functionalities of the application)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the main module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to the main module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Main module models and database interactions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Main module views and routes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/main/** (HTML templates for main-related views)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `index.html`
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `404.html`
                - <p>...</p>

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **media/** (Uploaded media files)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **orders/**
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the orders module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for orders)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for orders)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to orders)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the orders module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for order-related views)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling order-related processes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
                
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/orders/**
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `order-detail.html` (Template for order details)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `supplier-order-detail.html` (Template for supplier order details)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **payment/** (Handles payment-related functionalities)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the payment module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for payments)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for payments)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Payment-related forms for user input)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to payments)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the payment module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for payment-related views)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling payment processes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/payments/**
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `checkout.html` (Template for the checkout page)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `success.html` (Template for the success page after a successful payment)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **products/**
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the products module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for products)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for products)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms for product management)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to products)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the products module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for product-related views)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling product-related processes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
                
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/products/**
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `prod-creation.html` (Template for product creation)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `product-detail.html` (Template for product details)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `product-list.html` (Template for listing products)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `shopping-cart.html` (Template for the shopping cart)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **static/** (Static assets for the project)
            - <img src="red-bazaar/static/favicon.ico" width="18px"> `favicon.ico` (Website favicon)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **css/** (Stylesheets for the project)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/css-filetype-icon.ico" width="18px"> `checkout-off.css` (Checkout page stylesheet)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/css-filetype-icon.ico" width="18px"> `styles.css` (Main project stylesheet)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **imgs/** (Images for the project)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **readme-pics/** (Images for documentation and README)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **js/** (JavaScript files for the project)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `main.js` (Main JavaScript file)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/** (Main templates directory)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `base.html` (Base template for the project)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `base-tmp.html` (Temporary base template)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **widgets/** (Reusable widget templates)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `alert.html` (Template for alerts and notifications)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `footer.html` (Template for the website footer)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `navbar.html` (Template for the navigation bar)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **users/**
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the users module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for user management)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for users)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `decorators.py` (Custom decorators for user-related permissions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms for user registration, login, and profile management)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models for users and profiles)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `signals.py` (Handles signals for user-related events)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the users module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for user-related views)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling user-related processes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/users/**
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `dashboard.html` (User dashboard template)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `edit_profile.html` (Template for editing user profiles)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `home.html` (Home page for logged-in users)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `login.html` (Login page template)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `profile.html` (User profile view template)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `signup.html` (User signup page template)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `manage.py` (Entry point script to run the Django application)
        - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `utils.py` (Utility functions for common operations across the project)


    - <img src="red-bazaar/static/imgs/readme-pics/ico/git-icon.ico" width="18px"> `.gitignore` (Specifies files to be ignored by Git)
    - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `requirements.txt` (List of Python dependencies)
    - <img src="red-bazaar/static/imgs/readme-pics/ico/ic-info-outline.ico" width="18px"> `README.md` (Project README file)

## Wireframes

[Not Ready Yet]

## Colors

[Not Ready Yet]

### Color Customization Process

[Not Ready Yet]

## User Experience

### Key Principles

[Not Ready Yet]

### User Stories

#### **Restaurants (Buyers)**
1. **As a buyer**, I want to search for products easily on the platform so I can quickly find what I need.
2. **As a buyer**, I want to add products to a shopping cart to organise my orders before confirming the transaction.
3. **As a buyer**, I want to make secure and reliable payments using my credit or debit card to ensure my transactions are safe and effective.
4. **As a buyer**, I want to track the status of my orders (e.g., pending, in process, dispatched, completed, rejected) to stay informed about their progress.

#### **Suppliers**
1. **As a supplier**, I want to receive orders from buyers through the platform to manage my sales efficiently.
2. **As a supplier**, I want to update the status of orders (e.g., pending, in process, dispatched, completed, rejected) to keep buyers informed about their progress.
3. **As a supplier**, I want all transactions to be handled securely and effectively, giving me confidence in the platform's reliability.

#### **System Administrators**
1. **As an administrator**, I want a straightforward panel where I can monitor the platform's performance and operations.
2. **As an administrator**, I want exclusive control over creating and managing product categories to maintain order and consistency within the system.


### Future Enhancements

As RedBazaar evolves, several advanced features are planned to enhance the platform and expand its functionality for both buyers and suppliers. The vision for RedBazaar includes:

- **QR Code Integration:** Buyers will be able to add products to their shopping lists by scanning QR codes. This will speed up the process and allow predefined quantities to be adjusted before completing purchases.
- **Smart Price Comparison Wizard:** A tool designed to help buyers optimise their shopping lists by identifying the best deals based on price, supplier ratings, or other preferences.
- **Calendar-Based Insights:** Both buyers and suppliers will have access to a calendar feature that leverages historical data:
  - Buyers will receive reminders about past purchases, such as increased orders for specific products during seasonal events, helping them plan more effectively.
  - Suppliers will be notified of past periods of high demand, allowing them to adjust their inventory, prepare special offers, or target specific customers more strategically.
- **Enhanced Supplier Visibility:** Suppliers will have the ability to promote their products and daily deals, ensuring maximum exposure on the platform.
- **API for Market Insights:** A free API will provide valuable analytics and trends for both buyers and suppliers, helping them make informed business decisions.
- **Dynamic Supplier Selection:** Buyers will have more flexibility in choosing suppliers, with tools that allow them to compare products and switch suppliers easily.

These future plans aim to make RedBazaar a comprehensive solution for connecting restaurants and suppliers, fostering growth and collaboration within the small and medium-sized business community.

## Testing

### HTML Validation

[Not Ready Yet]

### CSS Validation

[Not Ready Yet]

### Accessibility

[Not Ready Yet]

### Wave Validation

[Not Ready Yet]

### Lighthouse Validation

[Not Ready Yet]

### JSHint Validation

[Not Ready Yet]

### PEP8 Validation

[Not Ready Yet]

### Device Testing

[Not Ready Yet]

### Browser Compatibility

[Not Ready Yet]

### User Stories Testing

#### **Restaurants (Buyers)**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-----------|----------|---------|--------------------|
| **Product Search**          | Use the search bar to find specific products             | Display of relevant product listings matching the search criteria        | Works as expected       |
| **Shopping Cart Management**| Add products to the shopping cart                       | Products are added to the cart and displayed in the summary              | Works as expected       |
| **Order Status Tracking**   | Navigate to the order history page to view order statuses| Order status (e.g., pending, in process, dispatched, completed) is shown | Works as expected       |
| **Secure Payment**          | Use a credit/debit card to make a purchase               | Payment is processed securely and the order is confirmed                 | Works as expected       |

#### **Suppliers**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-----------|----------|---------|--------------------|
| **Order Reception**         | Check received orders in the supplier dashboard          | All new orders are displayed, including relevant details                 | Works as expected       |
| **Order Status Updates**    | Update the status of an order (e.g., pending, completed) | Buyers see the updated order status in their dashboard                   | Works as expected       |
| **Secure Payment Confirmation** | View payment confirmation for processed orders        | Payment confirmation details are visible and accurate                    | Works as expected       |

#### **System Administrators**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-----------|----------|---------|--------------------|
| **Category Management**       | Use the admin panel to create or modify categories   | New categories are added or existing ones are updated successfully       | Works as expected       |
| **Order Monitoring**          | View orders and transactions in the admin dashboard | Full details of orders and transactions are available for review         | Works as expected       |



## Current State and Future Plans

### Current State

[Not Ready Yet]

### Future Plans

[Not Ready Yet]

## Deployment

[Not Ready Yet]

## License

[Not Ready Yet]

## Bugs and Challenges

### Bugs

[Not Ready Yet]

### Challenges

[Not Ready Yet]

## Acknowledgement

[Not Ready Yet]
