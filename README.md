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
  - [Database Schema](#database-schema)
- [Wireframes](#wireframes)
- [Colors](#colors)
  - [Color Customization Process](#color-customization-process)
- [How It Works](#how-it-works)
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

### Database Schema

The database schema is designed to support the core functionalities of the project, including user management, product listings, order processing, and messaging between users. Below is the relational diagram illustrating the relationships between the key entities:

![Database Schema](red-bazaar/static/imgs/readme-pics/DB-schema-BuyNSell.jpg)

#### Key Highlights:
- **Users**: Managed through the `CustomUser` table, which differentiates between Buyers and Suppliers. Each user can have a detailed profile linked via the `Profile` table.
- **Products and Categories**: Products are linked to Suppliers and organised into hierarchical categories using the `Category` table.
- **Orders**: The `Order` table connects Buyers and Suppliers, storing details like order status and shipping information. Each order contains multiple items managed by the `OrderItem` table.
- **Messages**: Private messaging between users is handled through the `Message` table, tracking sender, recipient, and read status.

## Wireframes

[Not Ready Yet]

## Colors

[Not Ready Yet]

### Color Customization Process

[Not Ready Yet]

## How It Works

This section provides an overview of the core functionality and user workflows within the platform. The diagram below illustrates the interaction between Buyers and Suppliers, highlighting the key processes, such as user registration, product management, order placement, and messaging.

### Key Processes:
1. **User Registration and Login**: Users can sign up as Buyers or Suppliers and access role-specific features after logging in.
2. **Product Management**: Suppliers can add, edit, and delete their products, while Buyers can browse and search for products by category or name.
3. **Order Placement and Management**: Buyers can place orders, and Suppliers can view and update order statuses.
4. **Messaging System**: Both Buyers and Suppliers can communicate directly through a secure messaging system.
5. **Payment Processing**: Buyers can securely complete transactions using Stripe integration.

Below is the flowchart representing these processes:

![Platform Workflow](red-bazaar/static/imgs/readme-pics/fc-webusage.jpg)


## User Experience

### Key Principles

1. **User-Centric Design**  
   The platform is designed to cater to two main user groups: Suppliers managing their products and Buyers exploring and purchasing them. The experience is streamlined for both roles, ensuring efficiency and ease of use.

2. **Role-Specific Navigation**  
   The interface dynamically adapts based on the user’s role, providing Buyers with features such as product browsing and cart management, while offering Suppliers tools to manage products and track orders.

3. **Clear and Intuitive Interaction**  
   Every action, from creating a product to completing a purchase, provides immediate feedback to the user, ensuring clarity and confidence in their interactions.

4. **Responsive and Accessible**  
   The platform is fully responsive, ensuring a seamless experience across all devices and screen sizes. Accessibility has been considered to accommodate diverse user needs.

5. **Effective Communication**  
   A built-in messaging system enables seamless communication between Buyers and Suppliers, with clear indicators for unread messages to ensure important communications are not missed.

6. **Organised and Searchable Content**  
   Products are categorised and searchable by name or category, making it easy for Buyers to find what they need. The shopping cart and product listings are organised by Supplier for clarity.

7. **Secure and Reliable Transactions**  
   Payments are processed securely using Stripe in test mode. The platform validates all payment and billing details to prevent errors and ensure a smooth checkout process.

8. **Transparency and Feedback**  
   The system provides clear and transparent feedback for all user actions, whether it’s a success message for an order or detailed error information for debugging.


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
The HTML structure of **RedBazaar** adheres to web standards and was validated using the W3C Validator. The validation process confirmed that all pages are error-free and meet modern HTML5 standards.

Validation efforts ensured that:
- The structure is semantically correct.
- There are no broken tags or misplaced elements.
- Accessibility features, such as alt attributes and ARIA roles, are properly integrated.

**HTML Validation Result:**
![HTML Validation Result](red-bazaar/static/imgs/readme-pics/html-validation-result.jpg)

### CSS Validation

<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

The CSS of **RedBazaar** has been validated with the W3C CSS Validator. The stylesheets passed the validation process with zero errors, ensuring compliance with modern CSS standards.

Highlights include:
- Fully responsive design, ensuring optimal layout across all devices.
- Consistent use of modern CSS3 features, including flexbox and grid layouts.
- Readable and maintainable code structure.

**CSS Validation Result:**
![CSS Validation Result](red-bazaar/static/imgs/readme-pics/css-validation-result.webp)

### Accessibility
Accessibility is a core focus for **RedBazaar**, following the Web Content Accessibility Guidelines (WCAG). Key accessibility measures include:

- **Keyboard Navigation:** Ensuring that all navigation and interactive elements are accessible via keyboard inputs.
- **Contrast Ratios:** Maintaining sufficient contrast between text and backgrounds to support readability.
- **Alt Text for Images:** Providing descriptive alt attributes for all images, ensuring compatibility with screen readers.
- **ARIA Roles:** Enhancing interactive elements with appropriate ARIA roles for better accessibility.

A WAVE audit was conducted, confirming compliance with accessibility standards. Minor adjustments, such as improving button contrast, are planned for future updates.

**Wave Validation Screenshot:**
![Wave Validation Result](red-bazaar/static/imgs/readme-pics/wave-validation.jpg)

### Lighthouse Validation
**RedBazaar** achieved high Lighthouse scores in performance, accessibility, and SEO. Some notable efforts include:

- Image optimization using WebP format for faster load times without compromising quality.
- Efficient CSS and JavaScript delivery, ensuring quick rendering across devices.
- Meta descriptions and structured data to enhance search engine visibility.

**Lighthouse Validation Screenshot:**
![Lighthouse Validation Result](red-bazaar/static/imgs/readme-pics/lighthouse-validation.jpg)

### PEP8 Validation
All Python code in **RedBazaar** adheres to the PEP8 standard, ensuring maintainable and clean code. Validation was conducted using automated tools, with particular attention to:

- Proper indentation and spacing.
- Clear and concise function and class comments.
- Logical organization of imports and modules.

The codebase is fully compliant, with plans to continually monitor and maintain PEP8 standards.

**PEP8 Validation Result:**
![PEP8 Validation Result](red-bazaar/static/imgs/readme-pics/pep8-validation-result.jpg)

### Device Testing
**RedBazaar** was tested across multiple devices, including:
- Desktops
- Tablets
- Smartphones

Media queries were used to adapt the layout for different screen sizes. Testing confirmed that all features, from navigation to purchasing workflows, function seamlessly across devices.

**Device Testing Example:**
![Responsive Device Testing](red-bazaar/static/imgs/readme-pics/device-testing-example.jpg)

### Browser Compatibility
Comprehensive browser testing was conducted for **RedBazaar**, covering:
- <img src="red-bazaar/static/imgs/readme-pics/ico/google-icon.ico" width="18px"> **Google Chrome**
- <img src="red-bazaar/static/imgs/readme-pics/ico/edge-icon.ico" width="18px"> **Microsoft Edge**
- <img src="red-bazaar/static/imgs/readme-pics/ico/opera-icon.ico" width="18px"> **Opera**
- <img src="red-bazaar/static/imgs/readme-pics/ico/firefox-icon.ico" width="18px"> **Mozilla Firefox**
- <img src="red-bazaar/static/imgs/readme-pics/ico/safari-icon.ico" width="18px"> **Safari**


The platform performs consistently across all tested browsers, providing a reliable user experience regardless of the user’s preferred browser.

**Browser Testing Example:**
![Browser Compatibility Test](red-bazaar/static/imgs/readme-pics/browser-testing-example.webp)

### JSHint Validation
JavaScript used in **RedBazaar** passed validation through JSHint with zero errors. The code is well-documented and follows best practices, ensuring readability and maintainability.

Highlights include:
- Efficient use of JavaScript and jQuery for interactivity.
- Validation and error handling for all user inputs.
- Lightweight and optimized scripts for quick execution.

**JSHint Validation Result:**
![JSHint Validation Result](red-bazaar/static/imgs/readme-pics/jshint-validation-result.webp)

### Responsiveness Testing

| **TEST**  | **ACTION**    | **EXPECTATION**   | **RESULT** |
| --------- | ------------- | ----------------- | ---------- |
| Landing page - responsiveness | Resize site to 320px      | All elements remain visible and functional   | ✅         |
| Landing page - responsiveness | Resize site to 1920px     | All elements remain visible and functional   | ✅         |
| Login page - responsiveness    | Resize site to 320px      | All elements remain visible and functional   | ✅         |
| Login page - responsiveness    | Resize site to 1920px     | All elements remain visible and functional   | ✅         |
| Sign-in page - responsiveness  | Resize site to 320px      | All elements remain visible and functional   | ✅         |
| Sign-in page - responsiveness  | Resize site to 1920px     | All elements remain visible and functional   | ✅         |
| Dashboard - responsiveness     | Resize site to 320px      | All elements remain visible and functional; sidebar is hidden in tablet/mobile view | ✅         |
| Dashboard - responsiveness     | Resize site to 1920px     | All elements remain visible and functional; sidebar is visible | ✅         |
| Profile page - responsiveness  | Resize site to 320px      | All elements remain visible and functional   | ✅         |
| Profile page - responsiveness  | Resize site to 1920px     | All elements remain visible and functional   | ✅         |
| Edit profile page - responsiveness | Resize site to 320px  | All elements remain visible and functional   | ✅         |
| Edit profile page - responsiveness | Resize site to 1920px | All elements remain visible and functional   | ✅         |
| Create product page - responsiveness | Resize site to 320px | All elements remain visible and functional   | ✅         |
| Create product page - responsiveness | Resize site to 1920px | All elements remain visible and functional   | ✅         |
| Edit product page - responsiveness | Resize site to 320px  | All elements remain visible and functional   | ✅         |
| Edit product page - responsiveness | Resize site to 1920px | All elements remain visible and functional   | ✅         |
| Chat page - responsiveness     | Resize site to 320px      | All elements remain visible and functional   | ✅         |
| Chat page - responsiveness     | Resize site to 1920px     | All elements remain visible and functional   | ✅         |

### C.R.U.D. Testing

| **TEST**  | **ACTION**    | **EXPECTATION**   | **RESULT** |
| --------- | ------------- | ----------------- | ---------- |
| Create User                  | Register a new user              | User account is created successfully               | ✅         |
| Edit User                    | Modify user details              | Changes are saved and reflected in the profile     | ✅         |
| Login User                   | Log in with valid credentials    | User is authenticated and redirected to dashboard  | ✅         |
| Logout User                  | Log out from the account         | User is logged out, and the session is cleared     | ✅         |
| Create Profile               | Set up a profile for the user    | Profile is created successfully                    | ✅         |
| Edit Profile                 | Modify profile information       | Changes are saved and reflected in the profile     | ✅         |
| Create Order (Buyers only)   | Place an order                   | Order is created and stored in the system          | ✅         |
| View Orders                  | Access order/invoice details     | Orders are visible to Buyers and Suppliers, including shipment address, product list, and quantities | ✅         |
| Edit Order (Suppliers only)  | Update the status of an order    | Order status is updated correctly                 | ✅         |
| View Products                | Browse available products        | Products are visible to both Buyers and Suppliers  | ✅         |
| Create Product (Suppliers only) | Add a new product              | Product is created and visible in the shop         | ✅         |
| Edit Product (Suppliers only) | Modify a product they own        | Changes are saved and reflected in the system      | ✅         |
| Delete Product (Suppliers only) | Remove a product they own       | Product is deleted and no longer visible           | ✅         |
| Search Products              | Search for products by name or category | Search results are displayed correctly for all users | ✅         |
| Send Message                 | Send a message to a user         | Message is delivered to the recipient              | ✅         |
| Receive Message              | Receive a message from a user    | Message is visible in the recipient's inbox        | ✅         |

### Features

| **TEST**  | **ACTION**    | **EXPECTATION**   | **RESULT** |
| --------- | ------------- | ----------------- | ---------- |
| User Registration            | Users can register by creating a new account. Input data is validated for integrity using AllAuth. | Account is created successfully                                  | ✅          |
| User Login                   | Users can log in with valid credentials and receive a success message. Input data is validated for integrity using AllAuth. | User is authenticated and redirected to the dashboard            | ✅          |
| User Logout                  | Users can log out from their account.                                                      | User is logged out, and the session is cleared                   | ✅          |
| Profile Creation             | Users can create a personal profile after registration.                                    | Profile is created successfully                                  | ✅          |
| Profile Editing              | Users can update their personal information and receive feedback for success or errors.    | Changes are saved and reflected in the profile                   | ✅          |
| Create Product               | Suppliers can create new products and add them to the store.                               | Product is created and visible in the shop                       | ✅          |
| Edit Product                 | Suppliers can edit their own products (name, price, description, etc.) with feedback provided for success or errors. | Changes are saved and reflected                                  | ✅          |
| Delete Product               | Suppliers can delete their own products.                                                   | Product is deleted and no longer visible in the shop             | ✅          |
| View Products                | Users can browse and view all available products in the store.                             | Products are visible to all users                                | ✅          |
| Search Products              | Users can search for products by name or category.                                         | Search results are displayed correctly                           | ✅          |
| Create Order (Buyers only)   | Buyers can place orders for products and receive confirmation messages.                    | Order is created successfully                                    | ✅          |
| View Orders                  | Buyers and Suppliers can view order details, including shipment address and product info.   | Orders and details are displayed accurately                      | ✅          |
| Edit Order Status            | Suppliers can update the status of their orders (e.g., Pending, Shipped, Delivered, etc.). | Order status is updated successfully                             | ✅          |
| Process Payments             | Payments are processed using Stripe in test mode, validating billing information, and preventing invalid transactions. Checkout forms validate input fields, including phone number, country, and data correctness. | Payment is processed, or specific error messages are displayed   | ✅          |
| Send Message                 | Users can send messages to other users (Suppliers or Buyers).                              | Message is delivered to the recipient                            | ✅          |
| Receive Message              | Users can receive messages from other users.                                               | Message is visible in the recipient's inbox                      | ✅          |
| Feedback Messages            | Users receive contextual feedback based on actions, including success or error messages for debugging. | Feedback is displayed based on the user’s actions                | ✅          |
| Sidebar Navigation           | Sidebar adapts to screen size, hiding on smaller devices and showing on larger screens.     | Sidebar is hidden or displayed as expected                       | ✅          |
| Role-Based Navigation        | Navigation menu adjusts based on the user type (Buyer or Supplier).                        | Navigation menu displays correct options based on the user role   | ✅          |
| Shopping Cart                | Shopping cart stores items in cookies, organizes them by Supplier, and displays the cart in the sidebar on the product listing page. | Cart is displayed with items organized by Supplier               | ✅          |
| Cart Item Counter            | Navigation bar button displays the number of items in the shopping cart.                   | Item count is updated and displayed accurately                   | ✅          |
| Unread Messages Counter      | Navigation bar button displays the number of unread messages.                              | Message count is updated and displayed accurately                | ✅          |


## Current State and Future Plans

### Current State

[Not Ready Yet]

### Future Plans

[Not Ready Yet]

## Deployment

### **Local Deployment Guide**

#### **1. Clone the Repository**
Open your terminal and run the following command to clone the repository to your local machine:
```bash
git clone https://github.com/Vgarcan/CodeInstitute-proj04-b2b.git
```

#### **2. Navigate to the Project Directory**
Move into the project directory:
```bash
cd CodeInstitute-proj04-b2b
```

---

#### **3. Set Up a Virtual Environment**
It’s recommended to use a virtual environment to manage project dependencies.

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

**Tip:** If you encounter issues activating the virtual environment, ensure Python is installed and accessible via your system's PATH.

---

#### **4. Install Dependencies**
With the virtual environment activated, install the required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

**Tip:** If you see errors during installation, ensure you have the latest version of `pip`:
```bash
pip install --upgrade pip
```

---

#### **5. Set Up Environment Variables**
Create a `.env` file in the project’s root directory and configure the necessary environment variables. An example configuration might look like this:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
EMAIL_HOST_USER=your_email_address
EMAIL_HOST_PASSWORD=your_email_password
```

**Tips for Environment Variables:**
- Make sure your `SECRET_KEY` is a secure, random string.
- Use the appropriate `DATABASE_URL` for your local database setup (e.g., SQLite, PostgreSQL).
- If using Stripe in test mode, ensure you use test keys, which are prefixed with `sk_test_` (secret key) and `pk_test_` (public key).

---

#### **6. Apply Database Migrations**
Run the following commands to apply database migrations and prepare the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

**Tip:** If migrations fail, check your `DATABASE_URL` and ensure your database server is running locally.

---

#### **7. Create a Superuser (Optional)**
To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

---

#### **8. Load Initial Data (Optional)**
If the project includes fixtures or pre-defined data, load them into the database:
```bash
python manage.py loaddata fixtures.json
```

**Tip:** Ensure the `fixtures.json` file exists in the project and is correctly formatted.

---

#### **9. Run the Development Server**
Start the development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser to view the application.

---

#### **Troubleshooting Tips**

- **Dependencies Fail to Install**:
  - Ensure your Python version matches the project's requirements (e.g., Python 3.8+).
  - Check for compatibility issues with installed system libraries (e.g., `psycopg2` for PostgreSQL).

- **Environment Variable Issues**:
  - Double-check the `.env` file formatting; it should not contain extra spaces or special characters.
  - Ensure the `.env` file is in the root project directory.

- **Database Errors**:
  - Ensure the database server (e.g., PostgreSQL) is running if using an external database.
  - Verify the `DATABASE_URL` format:
    ```plaintext
    postgres://USER:PASSWORD@HOST:PORT/DBNAME
    ```

- **Server Fails to Start**:
  - Check for syntax errors or missing modules.
  - Ensure all migrations have been applied:
    ```bash
    python manage.py showmigrations
    python manage.py migrate
    ```

- **Static Files Not Loading**:
  - Run the following command to collect static files locally:
    ```bash
    python manage.py collectstatic
    ```


## License

[Not Ready Yet]

## Bugs and Challenges

### Bugs

[Not Ready Yet]

### Challenges

[Not Ready Yet]

## Acknowledgement

[Not Ready Yet]
