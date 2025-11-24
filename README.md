# The-Olive-Green
Project-portfolio-4

The Olive Green is a fictional Italian Restaurant located in Nuremberg, Bavaria, Germany. The appp is a restaurant management system designed to allow staff to easily manage the menus and bookings. It also provides customers to make online bookings where they can make their table reservations. The live link can be found here: [Live Site- The Olive Green](https://the-olive-green-c9c6086e4cc3.herokuapp.com/).

![MockUp](docs/readme_images/Mockup.png)

## Table of Contents
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile-Planning](#agile-planning)
      - [Epics](#epics)
      - [User-Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features-Left-To-Be-Implemented](#features-left-to-be-implemented)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
      - [Color Palette](#color-palette)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Technologies](#technologies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Development-Setup](#development-setup)
    - [Version-Control](#version-control)
    - [Heroku-Deployment](#heroku-deployment)
    - [Run-Locally](#run-locally)
  - [Media](#media)
  - [Credits](#credits)


# User Experience Design

## The Strategy Plane

### Site Goals
The site is aimed at helping restaurant staff to easily manage the menus displayed on the website, as welll as keep track of upcoming bookings, editing and deleting as and when necessary. The site also aims to provide customers with a simple, hassle free way to make reservations, without the need to call the restaurant.

### Agile Planning
This project was developed using agile methodologies by delivering small features in incremental steps. The project was assigned to epics, prioritized under the labels, 'Musrt-have', 'Should-have', and 'Could-have'.
Must-have user stories were completed first, then "Should-haves" and finally "Could-haves". It was done this way to ensure that all major requirements were completed first to give the project a complete feel, and then later nice to have features can be added if there is availabilty of time and capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Niraja85/projects/6) and can be viewed to see more information on project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define that functionality that marks that story as complete.

![Kanban image](docs/readme_images/Kanban.png)

#### Epics

The project had 7 main Epics (milestones):

* EPIC 1 - Base Setup:

    * The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

* EPIC 2 - Stand alone pages:

    * The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

* EPIC 3 - Authentication Epic:

    * The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the staff would not be able to manage the bookings securely without regular site visitors also being able to see and perform actions.

* EPIC 4 - Menu:

    * The menu epic is for all stories that relate to the creating, deleting, editing and viewing of menus. This allows for regular users to view menus and for staff to manage them with a simple UI interface.

* EPIC 5 - Booking:

    * The booking epic is for all stories that relate to creating, viewing, updating and deleting bookings. This allows the staff to easily view upcoming bookings, manage the bookings and also for customers to book and manage their own reservations.

* EPIC 6 - Deployment Epic:

    * This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

* EPIC 7 - Documentation:

    * This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

#### User Stories

The following user stories were completed (by epics):

* Epic 1 - Base Setup:

    * As a developer, I need to create the base.html page and structure so that other pages can use that layout.
    * As a developer, I need to create static resources so that images, css and javascript work on the website.
    * As a developer, I need to set up the project so that it is ready for implementing the core features.
    * As a developer, I need to create the footer with social media links and contact information.
    * As a developer, I need to create the navbar so that users can navigate the website from any device.

* Epic 2 - Stand alone pages:

    * As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist.
    * As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.
    * As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views.
    * As a restaurant owner, I would like a home page so that customers can view information on my restaurant.

* Epic 3 - Authentication Epic:

    * As a developer, I need to implement allauth so that users can sign up and have access to the websites features.
    * As a Site Owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.
    * As a site owner, I would like the allauth pages customized to that they fit in with the sites styling.

* Epic 4 - Menu:

    * As a staff user, I want to be able to create a new menu when we have new dishes to offer.
    * As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant.
    * As a staff user, I want to be able to edit a menu when updates are needed.
    * As a staff user, I want to be able to delete a menu when it is no longer used.

* Epic 5 - Booking:

    * As a user, I would like to be able to create a new booking when I want to visit the restaurant.
    * As a user, I would like to view my bookings when I need to check the information.
    * As a user, I would like to be able to edit a booking so that I can make changes when needed.
    * As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully.
    * As a user I would like to delete a booking when I no longer require it.

* Epic 6 - Deployment:

    * As a developer, I need to set up whitenoise so that my static files are served in deployment.
    * As a developer, I need to deploy the project to heroku so that it is live for customers.

* Epic 7 - Documentation:

    * Tasks:
        * Complete readme documentation.
        * Complete testing documentation writeup.

## The Scope Plane

* Responsive Design - Site should be fully functional on all devices from 320px up.
* Hamburger menu for mobile devices.
* Ability to perform CRUD functionality on Menus and Bookings.
* Restricted role based features.
* Home page with restaurant information.

## The Structure Plane

### Features

``USER STORY- As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Menu**

The Navigation contains links for Home, Menu, Bookings and has allauth options.

 The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Bookings (Drop Down):
    * Create Booking -> bookings.html - Visible to logged in users
    * Upcoming BookingS -> manage_bookings.html - Visible to logged in users
  * Menus (Drop Down):
    * View Menus -> menu.html - Visible to all
    * Create Menu -> create_menu.html - Visible to staff
    * Create Menu Item -> create_menu_items.html - Visible to staff
    * Manage Menu -> manage_menu.html - Visible to staff

  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](docs/readme_images/navbar-1.png)
![Navbar2](docs/readme_images/navbar-admin.png)

`` USER STORY- As a restaurant owner I would like to have a restaurant home page, so that customers can view information about my restaurant``

Implementation:

**Home Page**

The home page contains a hero image of the restaurant and information about the restaurant at the top of the page. This will immediately make it evident to the user, what the purpose of the website is.
Under the information section, the opening hours of the restaurant and address with contact details is given, which will allow the user to locate the restaurant and operating times. and there are two buttons, 'View Menu' and 'Reserve a table'. These buttons will allow the user a quick way to navigate to the respective pages if they wish to view menu or make a booking.

![Hero-Image](docs/readme_images/Hero-image.png)

![About-Restaurant](docs/readme_images/about-restaurant%203.png)

``USER STORY- As a developer, I need to create the footer to add the social media links, so that th ecustomer can follow us``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a X, Instagram and Facebook link so that users can follow the restaurant on social media if they want to keep up to date with special offers not advertised on the website. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

![Footer](docs/readme_images/Footer.png)

``USER STORY - As a site Admin I can create or update the menu page content so that it is available on the site.``

Implementation:

**Create Menu/Menu-Items Page**

A Create Menu page was created  to allow staff users to create new menu items via the UI without having to use the backend admin panel.

![Create-Menu-Item](docs/readme_images/Create-menu-item.png)

``USER STORY - As a user, I would like to be able to view the menu, so that I can decide if I want to dine at the restaurant.``

Implementation:

**View Menu Page**

A Menu page has been created to allow users to see the current active menus and decide whether they are interested in the food and drinks that we offer at the restaurant. It is visible to all users regardless of logged in state, as it is not user friendly to restrict core information from users to force them into signing up.

![View-Menu](docs/readme_images/view-menu%202.png)

``USER STORY- As a admin user I can edit the menu/menu items so that updated version will be available``
``USER STORY - As a staff user I can delete the menu/menu items so that Customer can view only what is available up to date``

Implementation:

**Edit Menu Page**

On the manage menus page a button was added to allow staff members to edit a menu when changes need to be made.

![Edit-Menu](docs/readme_images/Edit-menu.png)

``USER STORY- As a user, I would like to be able to create a new booking when I want to visit the restaurant``

Implementation:

**Create Booking Page**

A booking page was created with a form that takes in the customer details and enables the user to easily make a booking through the UI.
If the form is successfully submitted with the validation on the front end, user can view their booking details on the upcoming booking table which gives a visual representation of their reservation.

![Create-Booking](docs/readme_images/Create-booking.png)

``USER-STORY - As a user, I would like to view my bookings when I need to check the information``

``USER-STORY - As a user I would like to delete my booking when no longer require it``

Implementation:

**Upcoming bookings page**

A upcoming bookings page was implemented with validation checks on the user. This shows all of the users bookings. This will allow the user to view their upcoming bookings when needed.

![Empty-Upcoming_booking](docs/readme_images/Empty-upcmng-booking.png)
![Upcoming-Booking](docs/readme_images/Upcoming-booking.png)

``USER-STORY - As a user I would like to be able to edit a booking so that i can make changes when needed``

Implementation:

**Edit Booking Page**

On the manage bookings page an edit button is present that allows the user to direct to a form and update their booking when required. This will allow the user to easily manage their own booking.

![Edited-booking](docs/readme_images/Edited-booking.png)

``USER-STORY - As a user I would like to delete my booking when no longer require it``

Implementation:

**Delete Booking**

![Delete-Booking](docs/readme_images/Confirm-delete-booking.png)

![Deleted-Booking](docs/readme_images/Deleted-booking.png)

**Favicon**
- A site wide favicon was implemented.
- This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon](docs/readme_images/Favicon.png)

### Features left to be implemented
- In future I would like to implement table capacity and table numbers while making a booking reservation, by assigning smaller tables for smaller number of guests.
- A map for the restaurant on the home page.
- I would also like to add multi menu page with images.
- I would also like to add a feedback section, where customers can rate their dining experience.

## The Skeleton Plane

### Wireframes

- Home Page

![Homepage-wireframe](docs/readme_images/Homepage-wf.png)

- Sign Up Page

![Signup-wireframe](docs/readme_images/Signup-wf.png)

- Signin Page

![Signin-wireframe](docs/readme_images/Signin-wf.png)

- Logout Page

![Logout-wireframe](docs/readme_images/Logout-wf.png)

- Manage Menu Page

![Manage-menu](docs/readme_images/Manage-menu-wf.png)

- Create Menu Page

![Create-Menu-wireframe](docs/readme_images/Create-menu-wf.png)

- View Menu Page

![View-menu-wireframe](docs/readme_images/view-menu-wf.png)

- Edit Menu Page

![Edit-menu-wireframe](docs/readme_images/edit-menu-wf.png)

- Delete Menu Page

![Delete-menu-wireframe](docs/readme_images/delete-menu-wireframe.png)

- Create Booking

![Create-Booking-wireframe](docs/readme_images/Create-booking-wf.png)

- Upcoming Bookings

![Upcoming-Booking-wireframe](docs/readme_images/upcoming-booking-wf.png)

- Edit Booking

![Edit-Booking-wireframe](docs/readme_images/Edit-booking-wf.png)

- Delete Booking

![Delete-booking-wireframe](docs/readme_images/delete-booking-wf.png)

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.

One-to-Many: A user can make multiple bookings

Foreign Keys: Used to link bookings to users.

Authentication: Managed via Django’s built-in and Allauth models.

Entity relationship diagram was created using [DBeaver](https://dbeaver.io/download/) and shows the schemas for each of the models and how they are related.

![Entity-Relationship-Diagram](docs/readme_images/TheOliveGreen%20ERD%204.png)

### Security

Views were secured by using the django class based view mixin, UserPassesTextMixin. A test function was created to use the mixin and checks were ran to ensure that the user who is trying to access the page is authorized. Any staff restricted functionality, user edit/delete functionality listed in the features was secured using this method.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.

## The Surface Plane

## Design

### Color Palette

I chose a green color palette with its lighter and darker shades for the headings, buttons and logo and to complement it used white background, black text and dark brown for the forms. These colors complement the name of the restaurant creating an earthy tone which I wanted to incorporate.

![Color-Palette](docs/readme_images/Olive%20Green%20Color%20Palette.png)

### Typography

Google fonts were used for typography.

* <strong>'Noticia Text', serif</strong> was used for Headings, Page titles, Section Headings and Key Emphasis Text.
* <strong>'Roboto', sans-serif</strong> was used for general text, Navigation Links and form labels.


### Imagery

The Website logo was downloaded from google free source and Header/Footer colour was choosen to match website logo.

The hero image was taken from Pexels which is a royalty free image site.

## Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - A touch of JavaScript was used for client-side input control to enhance form usability.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- UXwing.com and FontAwesome
  - These were used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/
- Google
  - This was used to download the logo in header
- TinyPNG
  - This was used to compress the images used in the website for optimal load times.

**Python Modules Used**

* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
* Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions
* messages - Used to pass messages to the toasts to display feedback to the user upon actions
* reverse_lazy - Used to define redirect URLs (like success_url) in class-based views without causing circular import issues.
* date - Date was used in order to search for objects by date.
* method_decorator - Used to wrap them with access restrictions.
* staff_member_required - Used to restrict access to certain views only for staff users(bookings)

**External Python Modules**

* asgiref==3.8.1 - Used internally by Django to support asynchronous features
* bleach==6.2.0 - HTML sanitizing library that cleans user-generated content; useful for rich text editors like Summernote
* certifi==2025.6.15 - Used to secure HTTP requests by providing up-to-date SSL certificates
* cffi==1.17.1 - Used for calling C code from Python - required by cryptography
* charset-normalizer==3.4.2 - Used to detect and normalize text encoding; required by requests
* cloudinary==1.36.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.7 - This was used to allow bootstrap5 use with crispy forms
* cryptography==45.0.4 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.2.23 - Framework used to build the application
* django-allauth==0.57.0 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==2.4 - Used to style the forms on render
* django-summernote==0.8.20.0 - Used for menu page since its a integrated rich text editor for content creation
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.10 - Installed as dependency with another package
* oauthlib==3.3.1 - Installed as dependency with another package
* psycopg2==2.9.10 - Needed for heroku deployment
* pycparser==2.22 - Installed as dependency with another package
* PyJWT==2.10.1 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.32.4 - Installed as dependency with another package
* requests-oauthlib==2.0.0 - Installed as dependency with another package (allauth authentication)
* setuptools==80.9.0 - Used to manage Python packages and dependencies during builds or installations
* six==1.17.0 - Installed as dependency with another package
* sqlparse==0.5.3 - Installed as dependency with another package
* tzdata==2025.2 - Installed as dependency with another package
* urllib3==1.26.20 - Installed as dependency with another package
* webencodings==0.5.1 - Required by bleach to handle web-safe text encoding formats
* whitenoise==5.3.0 - Used to serve static files directly without use of static resource provider like cloundinary

## Testing

Test cases and results can be found in the [TESTING.md](TESTING.md) file. This was moved due to the size of the file.

## Deployment

### Development Setup

This project uses a Python virtual environment located at `.venv`.

#### Using VS Code (Recommended)
- VS Code is configured to automatically use this environment via `.vscode/settings.json`.
- If you open the project folder in VS Code, it will activate the environment automatically.

#### Manual Setup (If Needed)

If the environment doesn’t activate automatically, you can activate it manually by pasting it on terminal:
`.venv\Scripts\Activate.ps1`

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘The Olive Green’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://the-olive-green-c9c6086e4cc3.herokuapp.com/)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Media
* All the free images/hero image used on the site were gotten from https://www.pexels.com/

## Credits

* My mentor [Gareth-McGirr](https://github.com/Gareth-McGirr/) for his insightful suggestions and encouragement throughout the project.

* You Tube channel for Initial set up and way to navigate the apps [https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=2]











