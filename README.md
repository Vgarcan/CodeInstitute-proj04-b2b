# Red Bazaar - B2B Marketplace

![Main LOGO](/static/imgs/readme-pics/banner-logo-02.png)

# Victor Garcia Cantalapidera 
- Slack: [@Victor Garcia](https://code-institute-room.slack.com/team/U0695HZA7FZ)
- GitHub: [Vgarcan](https://github.com/Vgarcan)
- LinkedIn: [Victor Garcia](https://www.linkedin.com/in/vgc89/)

## Check us out!

[Red Bazaar - Heroku](https://red-bazaar-1af30a20d60e.herokuapp.com/) 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Development Tools](#development-tools)
- [Technologies Used](#technologies-used)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Project Structure](#project-structure)
  - [Database Schema](#database-schema)
- [Wireframes](#wireframes)
- [Colours](#colours)
  - [Purpose and Implementation](#purpose-and-implementation)
  - [Colour Palette](#colour-palette)
  - [Colour Customization Process](#colour-customization-process)
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
  - [PEP8 Validation](#pep8-validation)
  - [Device Testing](#device-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [JSHint Validation](#jshint-validation)
  - [Project Testing Overview](#project-testing-overview)
    - [Responsiveness Testing](#responsiveness-testing)
    - [C.R.U.D. Testing](#crud-testing)
    - [Features](#features)
  - [User Stories Testing](#user-stories-testing)
- [Current State and Future Plans](#current-state-and-future-plans)
  - [Current State](#current-state)
  - [Future Plans](#future-plans)
  - [Moving Forward](#moving-forward)
- [Deployment](#deployment)
  - [Local Deployment Guide](#local-deployment-guide)
- [License](#license)
- [Bugs and Challenges](#bugs-and-challenges)
  - [Bugs](#bugs)
  - [Challenges](#challenges)
- [Acknowledgement](#acknowledgement)


## Introduction

**RedBazaar** is a B2B platform designed to connect restaurants and suppliers, focusing on fostering trade between small and medium-sized enterprises (SMEs). The platform aims to provide a professional, centralized tool that simplifies the ordering process for restaurants, helping them save time, reduce product waste, and cut costs. For suppliers, especially smaller ones, RedBazaar offers increased visibility, making it easier to reach potential customers in a competitive market.

![AMIRESPONSE photo](static/imgs/readme-pics/amiresp-pic.jpg)

This idea emerged from a personal experience while working in a café, where I observed the inefficiencies of managing orders through multiple platforms. RedBazaar solves this problem by grouping all suppliers under one platform, enabling restaurants to search for products rather than being tied to a specific supplier. For example, if a restaurant needs chicken strips, the platform displays all available options from various suppliers, allowing the business to choose the best deal.

Looking ahead, RedBazaar plans to introduce features that will enhance efficiency and flexibility for both restaurants and suppliers. Future updates will include tools for creating optimised shopping lists, finding the best-priced products, and promoting daily offers from suppliers. By focusing on affordability and accessibility, RedBazaar aims to build a community that empowers SMEs to thrive in the digital marketplace.


## Features

RedBazaar is currently in its initial development phase, providing the core functionality required to facilitate seamless transactions between buyers (restaurants) and suppliers. The platform is focused on delivering a simple and effective e-commerce experience, ensuring it meets the minimum viable product requirements. 

At this stage, RedBazaar includes the following features:
- **Product Search:** Restaurants can browse available products across multiple suppliers.
![SEARCH photo](static/imgs/readme-pics/search.png)
- **Shopping Cart and Transactions:** Buyers can add products to a shopping cart and complete purchases directly through the website.
![CART photo](static/imgs/readme-pics/cart.png)
- **Order Management:** Suppliers receive detailed orders submitted by buyers, including all necessary information to fulfil the requests.
![INVOICE photo](static/imgs/readme-pics/invoice.png)
- **Order Status Updates:** Suppliers can update the status of orders, providing real-time visibility for buyers about their purchases.
![ORDER STATUS photo](static/imgs/readme-pics/order-status.png)
- **Messaging System:**  Buyers and suppliers can communicate directly through a secure and efficient messaging system, allowing for clarification of order details, requests, or any additional information.
![DIRECT MESSAGES photo](static/imgs/readme-pics/direct-sms.png)

While the current state focuses on essential functionality, it sets the foundation for future enhancements that will make the platform more dynamic, efficient, and user-friendly.
## Development Tools

RedBazaar is being developed using a set of tools that streamline the coding, version control, and deployment processes. These tools ensure that development adheres to best practices and allows for efficient collaboration and deployment.

- <img src="static/imgs/readme-pics/ico/vsc-icon.ico" width="18px"> **Visual Studio Code (VSCode):**  
  The primary IDE used for writing and managing the code. VSCode is enhanced with extensions such as:
  - **autoPEP8:** Automatically formats the code to comply with the PEP8 standard, ensuring clean and readable Python code.

- <img src="static/imgs/readme-pics/ico/git-icon.ico" width="18px"> **Git:**  
  Used for version control, enabling the tracking of changes to the codebase and facilitating collaboration among developers.

- <img src="static/imgs/readme-pics/ico/github-icon.ico" width="18px"> **GitHub:**  
  The repository for hosting the project, allowing for remote collaboration, issue tracking, and streamlined version management.

- <img src="static/imgs/readme-pics/ico/pip-icon.ico" width="18px"> **pip and `requirements.txt`:**  
  pip is used for managing project dependencies, with all necessary libraries listed in the `requirements.txt` file for easy installation and environment setup.

- <img src="static/imgs/readme-pics/ico/procfile-filetipe-icon.ico" width="18px"> **Heroku:**  
  The platform used for deploying the project. Heroku allows for quick and scalable deployment, making it easy to share and test the application in a live environment.


## Technologies Used

### Backend

- <img src="static/imgs/readme-pics/ico/dj-icon.ico" width="18px"> **Django:**  
  The primary framework used for building the backend of RedBazaar. Django handles the server-side logic, routing, and database interactions. It also includes a built-in authentication system for managing user registration and login.

- <img src="static/imgs/readme-pics/ico/python-icon.ico" width="18px"> **Python:**  
  The core programming language for RedBazaar, used in conjunction with Django to build robust and scalable server-side functionality.

- <img src="static/imgs/readme-pics/ico/db-icon.ico" width="18px"> **Django ORM and Database:**  
  Django's Object-Relational Mapping (ORM) is used for database operations. The database structure is managed entirely through Django, ensuring consistency and efficiency.

- <img src="static/imgs/readme-pics/ico/mptt-icon.ico" width="18px"> **Django MPTT:**  
  This library is used for managing hierarchical data, particularly in creating parent and child categories for the products. It helps organise the categories into tree structures for better usability and data representation.

- <img src="static/imgs/readme-pics/ico/login-icon.ico" width="18px"> **Django AllAuth:**  
  A library integrated for user authentication, registration, and login. It supports third-party authentication providers like Google and GitHub, allowing users to register with a single click.

### Frontend

- <img src="static/imgs/readme-pics/ico/html_icon.ico" width="18px"> **HTML5:**  
  Used to structure the content of the website, ensuring semantic and accessible markup.

- <img src="static/imgs/readme-pics/ico/css-icon.ico" width="18px"> **CSS3:**  
  Utilised to style the website, providing consistent and responsive designs across different devices.

- <img src="static/imgs/readme-pics/ico/js-icon.ico" width="18px"> **JavaScript:**  
  Enhances interactivity on the site by enabling dynamic content updates and user interactions.

- <img src="static/imgs/readme-pics/ico/bootstrap-icon.ico" width="18px"> **Bootstrap:**  
  A popular front-end framework that helps create responsive and visually appealing designs. Bootstrap is used for layout management, navigation bars, modals, and other UI components.

## Project Structure

- <img src="static/imgs/readme-pics/ico/red-folder-icon.ico" width="18px"> **Root Directory**
    


   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **_core/** (Core functionalities and configurations)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the core module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `settings.py` (Core settings and configurations)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for the core application)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `asgi.py` (ASGI configuration for asynchronous requests)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `wsgi.py` (WSGI configuration for server deployment)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **direct_messages/**
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initialises the direct_messages module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for direct messages)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for direct messages)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models for storing direct messages)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the direct_messages module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for direct messages views)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling direct message interactions)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/** (Handles database schema changes for direct messages)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Main module views and routes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/direct_messages/** (HTML templates for direct_messages-related views)
            - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `chat.html`
      
   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **main/** (Main functionalities of the application)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the main module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to the main module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Main module models and database interactions)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Main module views and routes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/main/** (HTML templates for main-related views)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `index.html`
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `404.html`
         - <p>...</p>

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **media/** (Uploaded media files)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **orders/**
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the orders module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for orders)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for orders)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to orders)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the orders module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for order-related views)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling order-related processes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
            
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/orders/**
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `order-detail.html` (Template for order details)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `supplier-order-detail.html` (Template for supplier order details)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **payment/** (Handles payment-related functionalities)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the payment module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for payments)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for payments)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Payment-related forms for user input)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to payments)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the payment module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for payment-related views)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling payment processes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/payments/**
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `checkout.html` (Template for the checkout page)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `success.html` (Template for the success page after a successful payment)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **products/**
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the products module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for products)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for products)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms for product management)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models related to products)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the products module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for product-related views)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling product-related processes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
            
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/products/**
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `prod-creation.html` (Template for product creation)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `product-detail.html` (Template for product details)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `product-list.html` (Template for listing products)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `shopping-cart.html` (Template for the shopping cart)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **static/** (Static assets for the project)
      - <img src="red-bazaar/static/favicon.ico" width="18px"> `favicon.ico` (Website favicon)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **css/** (Stylesheets for the project)
         - <img src="static/imgs/readme-pics/ico/css-filetype-icon.ico" width="18px"> `checkout-off.css` (Checkout page stylesheet)
         - <img src="static/imgs/readme-pics/ico/css-filetype-icon.ico" width="18px"> `styles.css` (Main project stylesheet)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **imgs/** (Images for the project)
         - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **readme-pics/** (Images for documentation and README)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **js/** (JavaScript files for the project)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `main.js` (Main JavaScript file)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `stripe.js` (Stripe JavaScript logic file)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `dashboard_dash.js` (Stripe JavaScript logic file)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `dashboard.js` (Stripe JavaScript logic file)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `product_details.js` (Stripe JavaScript logic file)
         - <img src="static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `under-dev.js` (Stripe JavaScript logic file)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/** (Main templates directory)
      - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `base.html` (Base template for the project)
      - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `base-tmp.html` (Temporary base template)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **widgets/** (Reusable widget templates)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `alert.html` (Template for alerts and notifications)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `footer.html` (Template for the website footer)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `navbar.html` (Template for the navigation bar)

   - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **users/**
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the users module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `admin.py` (Admin site configuration for user management)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `apps.py` (Application configuration for users)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `decorators.py` (Custom decorators for user-related permissions)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms for user registration, login, and profile management)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Database models for users and profiles)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `signals.py` (Handles signals for user-related events)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `tests.py` (Unit tests for the users module)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `urls.py` (URL routing for user-related views)
      - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Views handling user-related processes)
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **migrations/**
      - <img src="static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/users/**
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `dashboard.html` (User dashboard template)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `edit_profile.html` (Template for editing user profiles)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `home.html` (Home page for logged-in users)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `login.html` (Login page template)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `profile.html` (User profile view template)
         - <img src="static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `signup.html` (User signup page template)

   - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `manage.py` (Entry point script to run the Django application)
   
   - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `utils.py` (Utility functions for common operations across the project)


   - <img src="static/imgs/readme-pics/ico/git-icon.ico" width="18px"> `.gitignore` (Specifies files to be ignored by Git)
   - <img src="static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `requirements.txt` (List of Python dependencies)
   - <img src="static/imgs/readme-pics/ico/ic-info-outline.ico" width="18px"> `README.md` (Project README file)

### Database Schema

The database schema is designed to support the core functionalities of the project, including user management, product listings, order processing, and messaging between users. Below is the relational diagram illustrating the relationships between the key entities:

![Database Schema](static/imgs/readme-pics/DB-schema-BuyNSell.jpg)

#### Key Highlights:
- **Users**: Managed through the `CustomUser` table, which differentiates between Buyers and Suppliers. Each user can have a detailed profile linked via the `Profile` table.
- **Products and Categories**: Products are linked to Suppliers and organised into hierarchical categories using the `Category` table.
- **Orders**: The `Order` table connects Buyers and Suppliers, storing details like order status and shipping information. Each order contains multiple items managed by the `OrderItem` table.
- **Messages**: Private messaging between users is handled through the `Message` table, tracking sender, recipient, and read status.

## Wireframes

The wireframes for this project were carefully designed to ensure a user-centric and professional approach to the platform's development. These visual blueprints provided a solid foundation for the layout and functionality of the website. Among all the pages, the **Landing Page**, **Dashboard**, and **Payment Page** were deemed the most representative of the project’s purpose and user flows. As such, we focused on these key pages to demonstrate the platform's core features, ensuring they reflect trust, modernity, and professionalism.

---

### Landing Page Overview

The **Landing Page** is designed to make a strong first impression, combining modern aesthetics with functional elements to guide users seamlessly into the platform. Each section is purposefully structured to provide clear value and inspire confidence.

#### Key Sections:
1. **Hero with Parallax**:  
   - Features a modern parallax effect to create a visually engaging experience.  
   - Serves as the introduction to the platform, inviting users to explore its features.

2. **Featured Suppliers**:  
   - Highlights top suppliers to establish credibility with new visitors.  
   - Builds trust by showcasing reliable and popular partners.

3. **Categories**:  
   - Displays selected categories to spark user interest and demonstrate the platform's ability to address specific needs.

4. **How It Works**:  
   - Outlines the platform's simplicity in three clear steps, reassuring users of its ease of use.

5. **Call to Action**:  
   - Guides visitors to the registration form after they’ve explored the page’s benefits, ensuring a smooth transition into platform engagement.

#### Wireframes for Landing Page
---
<details>
  <summary>Wireframe for Landing Page Desktop</summary>
  <img src="static/imgs/readme-pics/wf-landing.jpg" style="display: block; margin: auto;" alt="Wireframe for Landing Page - Desktop">
</details>

<details>
  <summary>Wireframe for Landing Page Responsive</summary>
  <img src="static/imgs/readme-pics/wf-landing-resp.jpg" style="display: block; margin: auto;" alt="Wireframe for Landing Page - Mobile">
</details>

---

### Dashboard Page Overview

The **Dashboard** serves as the central hub for users, offering tailored features based on their roles (Buyer or Supplier). Its layout ensures functionality and clarity, making it easy for users to manage their activities.

#### Key Sections:
1. **Order Table**:  
   - Displays a comprehensive list of the user’s orders.  
   - Enables users to manage and track orders efficiently.

2. **Statistics**:  
   - Provides an overview of the user’s activity, such as purchase or sales performance.  
   - Encourages engagement by showcasing progress and trends over time.

3. **Product Management (Suppliers Only)**:  
   - Exclusive to Suppliers, this section features a table displaying all their products.  
   - Allows Suppliers to easily modify or update product details, ensuring smooth management.

4. **Lateral Navbar**:  
   - A sticky navigation bar on the left-hand side for quick access to all dashboard features.  
   - Visible only on desktop devices, it ensures ease of use without overwhelming smaller mobile screens.  
   - Enhances navigation, allowing users to switch between dashboard sections effortlessly.


#### Wireframes for Dashboard
---
<details>
  <summary>Wireframe for Dashboard Desktop</summary>
  <img src="static/imgs/readme-pics/wf-dashboard.jpg" style="display: block; margin: auto;" alt="Wireframe for Dashboard - Desktop">
</details>

<details>
  <summary>Wireframe for Dashboard Responsive</summary>
  <img src="static/imgs/readme-pics/wf-dashboard-resp.jpg" style="display: block; margin: auto;" alt="Wireframe for Dashboard - Mobile">
</details>

---

### Payment Page Overview

The **Payment Page** ensures a seamless and trustworthy checkout experience. Its design focuses on clarity and simplicity, minimising distractions to inspire user confidence.

#### Key Sections:
1. **Form**:  
   - A clean and minimalistic form for entering billing information.  
   - Designed to be distraction-free, ensuring users feel secure during the payment process.

2. **Order Summary**:  
   - Organised by Suppliers, helping users verify that their order details are accurate.  
   - Reinforces trust by presenting information in a clear, structured format.

#### Wireframes for Payment Page
---
<details>
  <summary>Wireframe for Payment Page Desktop</summary>
  <img src="static/imgs/readme-pics/wf-payment.jpg" style="display: block; margin: auto;" alt="Wireframe for Payment Page - Desktop">
</details>

<details>
  <summary>Wireframe for Payment Page Responsive</summary>
  <img src="static/imgs/readme-pics/wf-payment-resp.jpg" style="display: block; margin: auto;" alt="Wireframe for Payment Page - Mobile">
</details>

---

### Why These Wireframes?

These three pages were selected as the most critical to the platform’s overall success. They represent the key user interactions and serve as the backbone of the platform. By focusing on these wireframes, we ensured the design embodies professionalism and user trust. Other pages were developed with flexibility, but these layouts were meticulously crafted to optimise the user experience and reflect the platform’s goals.


## Colours

The colour scheme used in this project is carefully designed to reflect the branding of "Red Bazaar," ensuring a visually engaging yet professional appearance. The primary colours are inspired by shades of red, reinforcing the connection to the project's name and logo. Secondary colours like greys and whites provide balance and readability, creating a polished user experience.

### Purpose and Implementation

- **Bootstrap Overwrite**: The colours are implemented using CSS variables defined under the `:root` selector. This ensures they overwrite Bootstrap's default styles seamlessly, maintaining a consistent design across all components.
- **Centralised Control**: By defining the colours in the root, any future changes can be applied globally, affecting the entire project without needing individual updates to components.
- **Professional Design**: The palette prioritises accessibility and clarity, combining bold reds for identity and soft greys for neutral elements.

### Colour Palette

![Colour Scheme](static/imgs/readme-pics/colour-scheme.png)

1. **`--colour-primary-light`**: `#f8d7da`  
   - A soft, light red used for subtle highlights and less critical notifications. This tone ensures a visual connection to the branding while maintaining readability.

2. **`--colour-primary`**: `#b71c1c`  
   - A bold, rich red that represents the core identity of "Red Bazaar." It is used in headers, buttons, and other key elements to reinforce the branding.

3. **`--colour-primary-dark`**: `#7f0000`  
   - A deeper red providing contrast and depth, used for hover effects or active states to indicate interactivity.

4. **`--colour-secondary-light`**: `#f5f5f5`  
   - A very light grey, ideal for backgrounds and creating a clean, professional look while maintaining a soft contrast with text.

5. **`--colour-secondary`**: `#424242`  
   - A medium grey used for secondary text and neutral elements, ensuring readability without overpowering primary content.

6. **`--colour-secondary-dark`**: `#212121`  
   - A dark grey that provides strong contrast for main text or headers against light backgrounds, enhancing clarity.

7. **`--colour-accent`**: `#d32f2f`  
   - A vivid red accent used for call-to-action buttons, drawing attention to key actions and engaging users.

8. **`--colour-accent-light`**: `#ffcccc`  
   - A lighter red accent applied in hover effects or secondary highlights, adding visual interest without overwhelming.

9. **`--colour-accent-dark`**: `#8c1d1d`  
   - A dark red accent for focused or active states, reinforcing the user’s attention on key elements.

10. **`--colour-background-light`**: `#f7f7f7`  
    - A very light grey background used for sections to create subtle contrasts and maintain a clean design.

11. **`--colour-background`**: `#ffffff`  
    - The standard white background, ensuring a professional and uncluttered appearance.

12. **`--colour-background-dark`**: `#e0e0e0`  
    - A neutral grey background for secondary sections, providing differentiation without drawing too much attention.

13. **`--colour-text-light`**: `#ffffff`  
    - White text, used on dark backgrounds to ensure readability and contrast.

14. **`--colour-text-dark`**: `#2e2e2e`  
    - A dark grey used for primary text, balancing readability and aesthetics.

15. **`--colour-text-muted`**: `#616161`  
    - A muted grey tone for secondary information or less important content, maintaining a clear hierarchy in the design.


### Colour Customization Process

Currently, the colour scheme of the website is fixed and cannot be customised by users. There are no options to switch between different themes or adjust the colour palette according to user preferences. Additionally, the platform does not support a dark mode or light mode toggle; the website operates in a single predefined mode.

#### Future Plans
While there are no immediate plans to allow users to change the colour scheme entirely, we aim to implement a dark mode in the future to accommodate user preferences for a darker interface. However, this will be done in a way that preserves the branding of "Red Bazaar" and aligns with the existing colour scheme and logo.

#### Rationale
The fixed colour scheme ensures consistency with the branding and identity of "Red Bazaar." Allowing users to fully customise the colours could compromise the visual connection to the project's name and logo, which are integral to the platform's identity. As such, any future changes or customisation features will carefully consider this balance.

## How It Works

This section provides an overview of the core functionality and user workflows within the platform. The diagram below illustrates the interaction between Buyers and Suppliers, highlighting the key processes, such as user registration, product management, order placement, and messaging.

### Key Processes:
1. **User Registration and Login**: Users can sign up as Buyers or Suppliers and access role-specific features after logging in.
2. **Product Management**: Suppliers can add, edit, and delete their products, while Buyers can browse and search for products by category or name.
3. **Order Placement and Management**: Buyers can place orders, and Suppliers can view and update order statuses.
4. **Messaging System**: Both Buyers and Suppliers can communicate directly through a secure messaging system.
5. **Payment Processing**: Buyers can securely complete transactions using Stripe integration.

Below is the flowchart representing these processes:

![Platform Workflow](static/imgs/readme-pics/fc-webusage.jpg)


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
![HTML Validation Result](static/imgs/readme-pics/w3c-markup.png)

To validate this HTML code, you can use the [W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fred-bazaar-1af30a20d60e.herokuapp.com%2F).

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
![CSS Validation Result](static/imgs/readme-pics/css-validation-result.png)

To validate this CSS code, you can use the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fred-bazaar-1af30a20d60e.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).

### Accessibility
Accessibility is a core focus for **RedBazaar**, following the Web Content Accessibility Guidelines (WCAG). Key accessibility measures include:

- **Keyboard Navigation:** Ensuring that all navigation and interactive elements are accessible via keyboard inputs.
- **Contrast Ratios:** Maintaining sufficient contrast between text and backgrounds to support readability.
- **Alt Text for Images:** Providing descriptive alt attributes for all images, ensuring compatibility with screen readers.
- **ARIA Roles:** Enhancing interactive elements with appropriate ARIA roles for better accessibility.

A WAVE audit was conducted, confirming compliance with accessibility standards. Minor adjustments, such as improving button contrast, are planned for future updates.

**Wave Validation Screenshot:**

![Wave Validation Result](static/imgs/readme-pics/wave-val-results.png)

#### Contrast Errors

During the validation process, **five contrast errors** were flagged. These errors were identified in the **footer links**, where the background is black, and the text is red. Although Wave reported these as potential contrast issues, we conducted additional testing with users and concluded the following:

1. **Readability**: The links are clearly visible to all users we tested, and no one reported difficulty in reading or interacting with them.
2. **Brand Identity**: The colour scheme aligns with the branding of Red Bazaar and reflects the overall theme and identity of the platform.
3. **Decision**: While we acknowledge the errors flagged by Wave, we have opted to **retain the current colour scheme**. Changing these colours would compromise the brand consistency established for the site.

**Wave Validation Contrast Error:**

![Wave Validation Result](static/imgs/readme-pics/wave-val-contrast.png)

This decision was made after careful consideration and feedback from multiple sources. We will continue to monitor user feedback and revisit this choice if necessary in future updates.

### Lighthouse Validation
**RedBazaar** achieved high Lighthouse scores in performance, accessibility, and SEO. Some notable efforts include:

- Image optimization using WebP format for faster load times without compromising quality.
- Efficient CSS and JavaScript delivery, ensuring quick rendering across devices.
- Meta descriptions and structured data to enhance search engine visibility.

**Lighthouse Validation Screenshot:**

![Lighthouse Validation Result](static/imgs/readme-pics/lighthouse-val.png)

### PEP8 Validation
All Python code in **RedBazaar** adheres to the PEP8 standard, ensuring maintainable and clean code. Validation was conducted using automated tools, with particular attention to:

- Proper indentation and spacing.
- Clear and concise function and class comments.
- Logical organization of imports and modules.

The codebase is fully compliant, with plans to continually monitor and maintain PEP8 standards.

### Device Testing
**RedBazaar** was tested across multiple devices, including:
- Desktops
- Tablets
- Smartphones

Media queries were used to adapt the layout for different screen sizes. Testing confirmed that all features, from navigation to purchasing workflows, function seamlessly across devices.

**Device Testing Example:**
#### Phone Screen

![PHONE RESP HOME](static/imgs/readme-pics/phone-res-home.png)
![PHONE RESP Dashboard](static/imgs/readme-pics/phone-res-dsh.png)
![PHONE RESP HOME](static/imgs/readme-pics/phone-res-list.png)

#### Tablet Screen

![TABLET RESP HOME](static/imgs/readme-pics/tablet-res-home.png)
![TABLET RESP Dashboard](static/imgs/readme-pics/tablet-res-dsh.png)
![TABLET RESP HOME](static/imgs/readme-pics/tablet-res-list.png)

### Browser Compatibility
Comprehensive browser testing was conducted for **RedBazaar**, covering:
- <img src="static/imgs/readme-pics/ico/google-icon.ico" width="18px"> **Google Chrome**
- <img src="static/imgs/readme-pics/ico/edge-icon.ico" width="18px"> **Microsoft Edge**
- <img src="static/imgs/readme-pics/ico/opera-icon.ico" width="18px"> **Opera**
- <img src="static/imgs/readme-pics/ico/firefox-icon.ico" width="18px"> **Mozilla Firefox**
- <img src="static/imgs/readme-pics/ico/safari-icon.ico" width="18px"> **Safari**


The platform performs consistently across all tested browsers, providing a reliable user experience regardless of the user’s preferred browser.

**Browser Testing Example:**

![Browser Compatibility Test](static/imgs/readme-pics/browser-testing-example.webp)

### JSHint Validation
JavaScript used in **RedBazaar** passed validation through JSHint with zero errors. The code is well-documented and follows best practices, ensuring readability and maintainability.

Highlights include:
- Efficient use of JavaScript and jQuery for interactivity.
- Validation and error handling for all user inputs.
- Lightweight and optimized scripts for quick execution.

**JSHint Validation Result:**

![JSHint Validation Result](static/imgs/readme-pics/jshint-validation-result.webp)

### Project Testing Overview

#### Responsiveness Testing

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

#### C.R.U.D. Testing

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

#### Features

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

### User Stories Testing

#### **Restaurants (Buyers)**

| **Feature** | **Action** | **Expected Result** | **Actual Result**|
|-------------|------------|---------------------|------------------|
| **Product Search**        | Use the search bar to find products by name or category.  | Display of relevant products that match the search criteria.         | Works as expected         |
| **Shopping Cart**         | Add products to the shopping cart and view the cart.     | Products appear in the cart with accurate quantities and total cost. | Works as expected         |
| **Secure Payments**       | Complete a transaction using a credit or debit card via Stripe. | Payment is processed securely using Stripe, a confirmation message is displayed, and the order is created successfully. | Works as expected         |
| **Order Tracking**        | Navigate to the orders section to view the order status. | Accurate display of order status, including updates as they occur.   | Works as expected         |

#### **Suppliers**

| **Feature** | **Action** | **Expected Result** | **Actual Result**|
|-------------|------------|---------------------|------------------|
| **Order Management**      | View new orders received on the platform.                | Orders are listed with relevant details (e.g., buyer, products, quantities). | Works as expected         |
| **Update Order Status**   | Change the status of an order to pending, in process, dispatched, completed, or rejected. | Status updates are reflected in the buyer's order tracking.          | Works as expected         |
| **Secure Transactions**   | Process payments through the platform for completed orders. | Payments are securely processed via Stripe, and confirmations are received. | Works as expected         |


## Current State and Future Plans

### Current State

RedBazaar is currently at its **minimum viable product (MVP)** stage, focusing on the essential features required to operate as an e-commerce platform. The project has been developed with a clear goal of delivering a functional foundation that allows seamless interactions between buyers (restaurants) and suppliers. This ensures the platform is ready for further development and expansion.

The current implementation includes the following core features:

1. **Product Search**  
   Restaurants can search and browse products across multiple suppliers, filtering by category or product name to locate items quickly.

2. **Shopping Cart and Transactions**  
   Buyers can add products to their cart, review their selection, and complete purchases securely using Stripe.

3. **Order Management**  
   Suppliers receive detailed orders, including product quantities, shipping addresses, and total costs, enabling them to fulfil buyer requests efficiently.

4. **Order Status Updates**  
   Suppliers can update the status of orders (e.g., Pending, Shipped, Delivered), providing real-time visibility for buyers regarding their purchases.

5. **Messaging System**  
   Buyers and suppliers can communicate directly through a secure messaging system, clarifying order details or addressing post-order inquiries.

6. **Responsive Design**  
   The platform is fully responsive, ensuring a smooth experience across all devices, from desktops to mobile phones.

7. **Role-Specific Navigation**  
   The interface adjusts dynamically based on the user's role. Buyers can browse products, manage orders, and track purchases, while Suppliers can manage product listings and process orders.

This stage provides a solid starting point for the project, demonstrating a functioning e-commerce platform with key features in place. While it represents the minimum necessary to achieve this goal, the project is well-structured for future enhancements.

### Future Plans

Building on the current foundation, RedBazaar aims to implement additional features and improvements to enhance the platform’s functionality, usability, and scalability. These plans include:

1. **Dark Mode Support**  
   Introduce a dark mode option to accommodate user preferences and improve accessibility in low-light environments.

2. **Advanced Search Filters**  
   Allow users to filter products by criteria such as price range, availability, and ratings, improving the browsing experience.

3. **Order Analytics for Suppliers**  
   Provide suppliers with detailed analytics on order trends, product performance, and buyer behaviour, helping them optimise their offerings.

4. **Enhanced Messaging Features**  
   Expand the messaging system to include features like file attachments, read receipts, and group conversations for more robust communication.

5. **Customisable User Profiles**  
   Enable users to personalise their profiles, including adding profile pictures and setting preferences for notifications and communication.

6. **Multi-Currency and Multi-Language Support**  
   Broaden the platform's reach by supporting multiple currencies and languages to cater to a global audience.

7. **Mobile Application**  
   Develop a dedicated mobile app to provide users with an optimised experience on mobile devices.

### Moving Forward

With the foundation established, the focus now shifts to enhancing the platform through the planned features above. Each step will be carefully implemented to ensure consistency with the branding and goals of RedBazaar, while incorporating user feedback to guide development. This forward-thinking approach positions RedBazaar as a scalable and adaptable solution for buyers and suppliers in the e-commerce space.


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


### **Heroku Deployment Guide**

### Prerequisites

1. **Heroku account**: Sign up at [Heroku](https://www.heroku.com).
2. Django project includes:
   - `Procfile`
   - `requirements.txt`
   - `runtime.txt`
   - `.gitignore`
   - Proper settings for `STATICFILES_STORAGE`, `DATABASES`, and `ALLOWED_HOSTS`.

---

### Step-by-Step Deployment

#### 1. Install Required Packages
```bash
pip install gunicorn whitenoise psycopg2-binary
pip freeze > requirements.txt
```

#### 2. Configure `settings.py`
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Other middlewares...
]

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

ALLOWED_HOSTS = ['your-app-name.herokuapp.com']
```

#### 3. Create `Procfile`
```plaintext
web: gunicorn <your_core_directory>.wsgi:application
```

#### 4. Create or Update `runtime.txt`
```plaintext
python-3.12.3
```

#### 5. Run `collectstatic`
```bash
python manage.py collectstatic
```

#### 6. Create Heroku App
1. Go to [Heroku Dashboard](https://dashboard.heroku.com/).
2. Click **New** > **Create New App**.
![Heroku Deployment step 1](static/imgs/readme-pics/heroku-1.png)
3. Choose a unique app name and region.
![Heroku Deployment step 2](static/imgs/readme-pics/heroku-2.png)

#### 7. Connect GitHub Repository
1. Navigate to the **Deploy** tab.
![Heroku Deployment step 3](static/imgs/readme-pics/heroku-3.png)
2. Select **GitHub** as the deployment method.
![Heroku Deployment step 4](static/imgs/readme-pics/heroku-4.png)
3. Connect your repository and enable **Automatic Deploys**.

#### 8. Configure Environment Variables
1. Go to the **Settings** tab > **Reveal Config Vars**.
![Heroku Deployment step 5](static/imgs/readme-pics/heroku-5.png)
2. Add:
![Heroku Deployment step 6](static/imgs/readme-pics/heroku-6.png)
   These variables should match what’s defined in your config.py or .env file locally.

#### 9. Deploy the App
![Heroku Deployment step 7](static/imgs/readme-pics/heroku-7.png)
1. Use the **Manual Deploy** option for the first deployment.
2. Test the app at `https://your-app-name.herokuapp.com`.

#### 10. Monitor and Manage
- View logs for debugging:
  ```bash
  heroku logs --tail
  ```
- Scale dynos via the **Resources** tab.

---

### Example Files

#### Procfile
```plaintext
web: gunicorn _core.wsgi:application
```

#### runtime.txt
```plaintext
python-3.12.3
```

## License

This project is proprietary and is licensed for **educational evaluation purposes only**. The following restrictions apply:

1. **No Redistribution**:  
   This project may not be copied, distributed, or shared in any form, either online or offline.

2. **Limited Usage**:  
   Access to this project is granted solely to:
   - Code Institute instructors, mentors, and supervisors.
   - Members of the academic team responsible for reviewing and grading the project.

3. **No Derivative Works**:  
   The code, design, and any other assets included in this project may not be modified, reused, or incorporated into other projects.

4. **Ownership**:  
   All intellectual property rights of this project remain with the author.

5. **No Commercial Use**:  
   This project may not be used for any commercial purposes under any circumstances.

Any violation of these terms is strictly prohibited. For permissions or inquiries, please contact the author directly.

![No Commercial Use - Lock Pic](static/imgs/readme-pics/lock-license.webp)

## Bugs and Challenges

### Bugs

1. **Product ID Conflict in Shopping Cart** -- (Fixed ✅)
   - **Description**: A recurring issue arises when handling products with an ID of `1`. The problem occurs during actions such as adding the product to the shopping cart or updating its quantity. This is caused by the way JavaScript interacts with the `href` attribute, which was initially used to pass the product ID.
   - **Cause**: Django renders the templates first, generating static IDs for products, but JavaScript modifies these IDs dynamically when the page loads. Since the `href` was directly tied to the product ID, any mismatch during the handoff from Django to JavaScript caused errors, particularly with the product ID `1`.
   - **Temporary Fix**: The `href` attribute was replaced with a `data-*` attribute (e.g., `data-url`) to store the product ID. JavaScript now reads the value from `data-url` instead of relying on the `href`. This approach partially resolved the issue, but intermittent errors persist.

### Challenges

1. **Synchronising Django and JavaScript**
   - **Description**: Integrating Django's server-side rendering with JavaScript's client-side processing proved to be a key challenge. The issue specifically arose because Django's initial rendering generates static product IDs, while JavaScript relies on dynamically updated attributes.
   - **Solution Attempts**: 
     - Replacing `href` with `data-*` attributes to avoid direct conflicts between Django's rendering and JavaScript's expectations.
     - Testing the JavaScript logic to ensure it accurately reads and processes the `data-url` attribute.
   - **Current Status**: While this workaround reduced errors, it did not eliminate them entirely. Further debugging is required to identify and resolve the root cause of the intermittent failures.

2. **Debugging Intermittent Issues**
   - **Description**: Tracking and replicating this bug has been difficult because it does not occur consistently. It mainly manifests during specific interactions with the product ID `1` but not for other IDs.
   - **Lesson Learned**: Intermittent issues like this highlight the importance of robust testing and logging. Implementing additional error tracking within JavaScript and Django could help capture more details about the circumstances under which the bug occurs.

### Next Steps

- Refactor JavaScript to improve how it interacts with the `data-*` attributes, ensuring compatibility with Django's rendering logic.
- Introduce detailed logging to track when and why the error occurs, particularly for the product ID `1`.
- Explore alternative methods to pass product IDs dynamically without relying on static attributes or conflicting values.


## Acknowledgement

This project was made possible thanks to the numerous resources, articles, and videos available online, as well as the structured guidance provided by Code Institute.

Throughout the development process, we frequently referred to tutorials, forums, and documentation to overcome challenges and implement solutions. For instance, the use of the MPTT library for handling hierarchical data was a direct result of research on platforms like Stack Overflow and various documentation sites. As a practice inspired by Django's approach, we have embedded links to some of these references directly within the scripts. These links serve as a point of reference for anyone reviewing or extending the codebase.

While it is difficult to track every single resource used over the course of three months, we want to acknowledge the invaluable support of:

The instructional videos and materials provided by Code Institute.
Open-source libraries like Django, Bootstrap, and Stripe, whose extensive documentation and community contributions were instrumental.
Articles, blogs, and Q&A platforms like Stack Overflow that provided solutions to specific issues encountered during development.
Specific References
Below are some examples of key resources and their use in this project:

MPTT Library Documentation: Utilised for creating and managing hierarchical data structures. A link to the documentation is included in the relevant script.

Stack Overflow Discussions: Helped solve issues related to URL management in Django and JavaScript interactions with template-rendered content.

Bootstrap Documentation: Referenced for styling and responsive layout solutions, ensuring a polished and consistent user interface.

Stripe API Documentation: Used extensively for implementing the payment processing system.
Django Official Documentation: A constant reference for understanding Django ORM, views, and middleware.

YouTube Tutorials: Several video tutorials provided insights into handling edge cases, such as managing cart quantities and avoiding layout shifts.

Our most sincere thanks to [Patrick O'Doherty](https://www.linkedin.com/in/patrickaod/) for his invaluable recommendation to use **WhiteNoise** for managing static files instead of an S3 bucket. His clear and detailed explanation was instrumental in implementing this solution effectively.


Lastly, we extend our gratitude to the Code Institute mentors and reviewers who offered guidance and support throughout this journey.

### Resource Links
- [How To Modify and Override Django Allauth Template Page - by Elesh Channel ](https://www.youtube.com/watch?v=VIoKemDBv8Y&list=LL&index=1)
- [Create A Search Bar - Django Wednesdays #9 - by Codemy.com ](https://www.youtube.com/watch?v=AGtae4L5BbI)
- [ALLAUTH docs](https://docs.allauth.org/en/latest/)
- [MPTT (Modified Preorder Tree Traversal)](https://mptt.readthedocs.io/en/latest/overview.html)
- [Complex lookups with Q objects - Django Docs](https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q-objects)
- [Django 5.1 - STORAGES](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-STORAGES)
- [WHITENOISE docs](https://whitenoise.readthedocs.io/en/latest/)
- [Django Cloudinary Storage](https://pypi.org/project/django-cloudinary-storage/)
- [How to Connect Cloudinary to Your Django Project: Step-by-Step Tutorial - by SnipherDev](https://www.youtube.com/watch?v=gj8bs2lf86A)
- [Chart.js - Manual](https://www.chartjs.org/docs/latest/)

