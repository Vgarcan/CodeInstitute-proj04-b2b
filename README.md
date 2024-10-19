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

Red Bazaar is a B2B marketplace designed to connect suppliers and companies efficiently. This project was born from the idea of simplifying the procurement process for businesses, allowing suppliers to showcase their products while enabling companies to find the best deals.

## Features

- **User Registration and Authentication:** Secure registration and login for suppliers and companies.
- **Product Listings Management:** Suppliers can create, update, and delete product listings.
- **Dynamic Dashboard:** A user-friendly dashboard for suppliers and companies to manage their interactions.
- **Advanced Search and Filters:** Companies can search for products based on various criteria.

## Development Tools

- **Django:** The web framework used for building the application.
- **Bootstrap:** Utilized for responsive design and UI components.

## Technologies Used

### Backend
- **Django:** Core framework for handling server-side logic and database interactions.

### Frontend
- **HTML, CSS, JavaScript:** Used for structuring, styling, and adding interactivity to the website.

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

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **orders/** (Handles order-related functionalities)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/orders/** (HTML templates for order-related views)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `order-summary.html`
                - <p>...</p>

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **products/** (Handles product-related functionalities)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the products module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to product management)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (Product models and database interactions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (Product views and routes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/products/** (HTML templates for product-related views)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `product-list.html`
                - <p>...</p>

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **static/** (Static assets like images, CSS, and JS files)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **css/** (Contains CSS stylesheets)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/css-filetype-icon.ico" width="18px"> `main.css` (Main stylesheet)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **js/** (Contains JavaScript files)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/js-filetype-icon.ico" width="18px"> `main.js` (Main JavaScript file)
            - <img src="red-bazaar/static/favicon.ico" width="18px"> `favicon.ico` (Favicon for the website)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/** (Main templates directory)

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **users/** (Handles user-related functionalities)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the user module)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to user interactions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `models.py` (User models and database interactions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `views.py` (User views and routes)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `signals.py` (Handles signals for user-related events)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/py-filetype-icon.ico" width="18px"> `decorators.py` (Custom decorators for user interactions)
            - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **templates/users/** (HTML templates for user-related views)
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `dashboard.html`
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `profile.html`
                - <img src="red-bazaar/static/imgs/readme-pics/ico/html-filetype-icon.ico" width="18px"> `login.html`
                - <p>...</p>

        - <img src="red-bazaar/static/imgs/readme-pics/ico/folder-icon.ico" width="18px"> **manage.py** (Script to run the Django application)

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

[Not Ready Yet]

### Future Enhancements

[Not Ready Yet]

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

[Not Ready Yet]

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
