# UglyMugs.com

Full Stack Frameworks With Django Milestone Project @ Code Institute



This project is an e-commerce that sells limited edition ugly mugs to people who loves ugly mugs. 
The shop offers ugly mugs that are only created in a limited number, with new designs releasing continuously.
It allows the shopper to perform a number of actions including:

- Navigate the site for info
- View mugs
- View the "mug of the month"
- Add mugs to the cart
- Adjust, update and remove items in the cart
- Check out quickly with no hassles
- Receive and view order confirmations
- Store my shipping details and my order confirmation in a user profile

It allows the store admin to add, edit/update and delete a mug from the backend.

The web application is built using [Django](https://www.djangoproject.com/ "Django") as a [Python](https://www.python.org/ "Python") Web framework.
You can find the application [here](https://creative-hub.herokuapp.com/).

***

## Table of Contents
- [UX](#ux)
    - [Database structure](#database-structure)
    - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to Implement](#features-to-implement)
- [Technologies Used](#technologies-used)
    - [HTML](#html)
    - [CSS](#css)
    - [JS](#js)
    - [Python](#python)
    - [Flask](#flask)
    - [MongoDB](#mongodb)
- [Testing](#testing)
    - [Functionality](#functionality)
    - [User Stories](#user-stories)
    - [Different Browsers and devices](#different-browsers-and-devices)
    - [Responsiveness](#responsiveness)
    - [Code validation](#code-validation)
    - [Defensive design](#defensive-design)
    - [Bugs discovered](#bugs-discovered)
    - [Conclusion](#conclusion)
- [Deployment](#deployment)
    - [How to deploy to Github](how-to-deploy-to-github)
    - [How to clone this repository in order to run the code locally on your machine](#how-to-clone-this-repository-in-order-to-run-the-code-locally-on-your-machine)
    - [How to deploy to Heroku](#how-to-deploy-to-heroku)
    - [Running the application locally using Gitpod](#running-the-application-locally-using-gitpod)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
- [Resources](#resources)

[Back to Top](#uglymugs.com)
***

## UX

The application is designed using the [materialize](https://materializecss.com/ "Materialize") framework.
It is designed to be user friendly, simple and clean with the purpose to present all information in a visually appealing manner on all devices.
It is made for shoppers who wants to view and buy ugly mugs.
They want to easily use and navigate the site.
They easily want to browse and purchase mugs.
For convenience they want a login that stores shipping details and order history.
To provide that information this application is a simple and straightforward web application.
It contains index, about, contact, register/login/logout, profile, mugs, mug details, cart, checkout and checkout success pages.
The footer provides further navigation links for a better user experience.

---

### User Stories

You can access the deployed project [here](https://ugly-mugs.herokuapp.com/ "Ugly Mugs") to try the user stories yourself.

- As a shopper I want to be able to view a list of mugs so that I can select some to purchase
- As a shopper I want to be able to view individual mug details so that I can get the details I wan
- As a shopper I want to be able to easily navigate on the site  so that I can find what I need
- As a shopper I want to be able to easily select the quantity of a mug when purchasing it so that I can ensure I don't accidentaly select the wrong mug or quantity
- As a shopper I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
- As a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a shopper I want to be able to easily enter my payment information so that I can check out quickly and with no hassles
- As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
- As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes

- As a user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile
- As a user I want to be able to easily login and logout so that I can access my personal account information
- As a user I want to be able to easily recover my password in case I forget it so that I can recover access to my account
- As a user I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful
- As a user I want to be able to have a personalized user profile so that I can view my personal order history and save my payment information

- As a store owner I want to be able to add a mug so that I can add new items to my store
- As a store owner I want to be able to edit/update a mug so that I can change mug prices, descriptions and other mug criteria
- As a store owner I want to be able to delete a mug so that I can remove items that are no longer for sale

---

### Strategy

I want to create an e-commerce to sell ugly mugs for people who loves ugly mugs
The shopper gets the benefit of buying that ugly mug that they love. 
The shopper gets the benefit of a seamless and secure shopping experience with control of their shopping with e-mail confirmations etc. 
The site user can easily register an account and view all purchase history and information about the user. 
The store owner can add, edit and delete mugs. 

---

### Scope

The first release of the website will be simple as much functionality is not needed yet as there only will be 1 mug available on the site.
For the projects sake I added a mugs view with pagination which I can build upon later on when filtering and search functions are needed.

A shopper can view the website on any device including mobile, tablet, desktop.
A shopper can view mugs and mug details before adding it to the cart.
A shopper can add, edit and delete mugs to and from the cart.
A shopper can find purchase history and orders.
A shopper can register and edit an account including shipping and billing details.
A shopper can filter mugs on years / months.
A shopper can log in and out of the account.
A shopper can navigate easily and make safe purchases.
A shopper can't make purchases that are empty and submit forms that doesn't meet all the requirements.
A store owner can manage mugs in the backend via staff login.

Future releases may introduce:
More interaction with the shoppers and how they can utilize the website (e.g search function when required).
Use data in fun and valueable ways for the shoppers and the store owners. Ex. show how many mugs each edition sold for.
Introduce more mugs and methods to purchase the mugs e.g introduce subscriptions.
Add functionality for register with social media account.
Overall improvements to each part of the website.

---

### Structure

Communication and interactions with the user is central for a site like this. 
It uses minimal but powerful design to interact with the user in a consistent, predictable, learnable and visible way providing clear and intuitive feedback.

---

### Skeleton

In this [link](https://github.com/robinwesterback/ugly-mugs-e-commerce/tree/master/wireframes "Wireframes") you can find the wireframes for each section that serves as the skeleton for the project.

---

### Surface

In this [link]() you can find the mockups for the website created with [figma](https://github.com/robinwesterback/ugly-mugs-e-commerce/tree/master/mockups).

#### Fonts
I used Poppins from [Google Fonts](https://fonts.google.com/ "Google Fonts").

#### Colors
- Black
- White
- #EF2A82 - Pink
- #40BFFF - blue

[Back to Top](#uglymugs.com)
***

## Features

The application contains several features with a few left to be implemented.

---

### Existing Features

#### Navbar

A materialize [component](https://materializecss.com/navbar.html "Materialize Navbar") with a hamburger menu for mobile.

#### Footer

A materialize [component](https://materializecss.com/footer.html "Materialize Footer") for improving user experience.

#### Icons

A materialize [component](https://materializecss.com/icons.html "Materialize Icons") for improving user experience.

#### Forms

Forms to allow users to pass information to the store.

#### User login

Registration, login and logout that stores shipping details and order history.

#### Showcase mugs

The application allows the shopper to view mugs in the store.

#### View cart

The application allows the shopper to view items in the cart.

#### Add to cart

The application allows the shopper to add items to the cart.

#### Edit/update cart

The application allows the shopper to edit/update items in the cart.

#### Remove from cart

The application allows the shopper to remove items from the cart.

#### Checkout solution

The application provides a checkout solution using [Stripe](https://stripe.com/en-se "Stripe").

#### Alerts / notifications

The application communicates with the user notifying what's going on using [toasts](https://materializecss.com/toasts.html "Toasts") and [messages](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/#using-messages-in-views-and-templates "Django messages").

#### Add mugs

The application allows the store owner to add mugs to the db.

#### Edit/update mugs

The application allows the store owner to edit/update mugs in the db.

#### Remove mugs

The application allows the store owner to remove mugs from the db.

---

### Features Left to Implement

#### More and better use of mugs

As more mugs and additional products/services will be released I want to improve functionality for searching and browsing mugs.

#### Social media accounts

Allow users to register and login with social media accounts.

#### Overview / data / statistics

Use data gathered to provide value for shoppers and store owners.

#### Defensive design

Continue to improve the defensive design to keep the website safe for shoppers and the store owner.

#### Livechat and chat function

I might add a livechat for contacting the store.

#### Finish up styling and Functions

As you might have noticed I didn't manage to finish everything in time for submission, the site is going to get polished and look good on all devices.

#### Your thoughts

Are there any features that you would like me to implement to improve the application? Please get in touch and share your thoughts.

[Back to Top](#uglymugs.com)
***

## Technologies Used

### Languages
- [HTML5](https://html.com/ "HTML")
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html "CSS")
- [JavaScript](https://www.javascript.com/ "JavaScript")
- [Python](https://www.python.org/ "Python")

---

### Libraries, frameworks, tools used
- [Django](https://docs.djangoproject.com/en/3.1/ "Django") as python web framework used for rapid development, maintainable, clean design
- [Psycopg2](https://pypi.org/project/psycopg2/ "Psycopg2") as database adapter for the Python
- [dj-database-url](https://pypi.org/project/dj-database-url/ "dj-database-url")
- [Gunicorn](https://gunicorn.org/ "Gunicorn") or Green Unicorn, a WSGI server implementation used to run Python web application
- [miniwebtool](https://miniwebtool.com/django-secret-key-generator/ "miniwebtool") for generating new SECRET_KEY
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html "django-allauth") for handling users, registrations and login / logout functionality
- [materialize](https://materializecss.com "materalize") for access to some core css and js for a responsive and user friendly app
- [jQuery](https://code.jquery.com/ "jQuery") for implementing functions provided by materialize
- [Pillow](https://pillow.readthedocs.io/en/stable/ "Pillow") for saving image file formats
- [JSON formatter](https://jsonformatter.org/ "JSON formatter") for formatting JSON
- [Django Countries](https://pypi.org/project/django-countries/#installation "Django Countries") for CountryField
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/ "django-crispy-forms") for forms
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "Boto3") for AWS SDK
- [django-storages](https://django-storages.readthedocs.io/en/latest/ "django-storages") is a collection of custom storage backends for Django
- [temp-mail.org](https://temp-mail.org/ "temp-mail.org") for testing the site
- [Stripe](https://stripe.com/ "Stripe") for receiving payments for the mugs
- [Gitpod](https://www.gitpod.io/ "Gitpod") was used as a code editor
- [Git](https://git-scm.com/ "Git") version control
- [GitHub](https://github.com/ "GitHub") used as a Git repository hosting service
- [Heroku](https://www.heroku.com/ "Heroku") is a container-based cloud platform, I used Heroku to deploy this app.
- [W3C Validator](https://validator.w3.org/ "W3C Validator") used to check the validity of my HTML and CSS
- [PEP 8 Online Validator](http://pep8online.com/ "PEP 8 Online Validator") used to check my Python code
- [Balsamiq](https://balsamiq.com/ "Balsamiq") for creating wireframes
- [Figma](https://www.figma.com/ "Figma") for creating mockups
- [AWS S3 Bucket](https://aws.amazon.com/s3/ "AWS S3 Bucket") as a cloud storage
- [Ajax Gif Loader](http://www.ajaxload.info/ "Ajax Gif Loader") for creating a loading indicator

---

### Databases
- [PostgreSQL](https://www.postgresql.org/ "PostgreSQL") database service provided directly by Heroku
- [SQlite3](https://www.sqlite.org/index.html "SQlite3") provided by django

[Back to Top](#uglymugs.com) 
***

## Testing

I have tested the application and looked for flaws in the design and errors in the functionality on several browsers on desktop, laptop and iPhone 7.
I have also tested the user stories to see if the application fills its purpose towards the user.
The expected outcome is that the application is responsive and functional on all browsers/devices.
Functions like links, CRUD operations and contact forms should work properly e.g "target=”\_blank"" where appropriate. Below are my findings and comments.

---

- As a shopper I want to be able to view a list of mugs so that I can select some to purchase
- As a shopper I want to be able to view individual mug details so that I can get the details I wan
- As a shopper I want to be able to easily navigate on the site so that I can find what I need
- As a shopper I want to be able to easily select the quantity of a mug when purchasing it so that I can ensure I don't accidentaly select the wrong mug or quantity
- As a shopper I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
- As a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a shopper I want to be able to easily enter my payment information so that I can check out quickly and with no hassles
- As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
- As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes

- As a user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile
- As a user I want to be able to easily login and logout so that I can access my personal account information
- As a user I want to be able to easily recover my password in case I forget it so that I can recover access to my account
- As a user I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful
- As a user I want to be able to have a personalized user profile so that I can view my personal order history and save my payment information

- As a store owner I want to be able to add a mug so that I can add new items to my store
- As a store owner I want to be able to edit/update a mug so that I can change mug prices, descriptions and other mug criteria
- As a store owner I want to be able to delete a mug so that I can remove items that are no longer for sale

### User Stories

| Description                                    |                Expected outcome                 | Pass | Comments |
| ---------------------------------------------- | :---------------------------------------------: | ---: | -------: |
| View a list of mugs | The collection template renders |  Yes |        - |
| View individual mug details | The mug details template renders |  Yes |        - |
| Easily navigate on the site | Navigation links are visible and clickable |  Yes |        - |
| Easily select the quantity of a mug | Quantity adjusts |  Yes |        - |
| View items in my bag  | See items in bag |  Yes |        - |
| Adjust the quantity of individual items in my bag | Quantity adjusted |  Yes |        - |
| Check out quickly and with no hassles | The checkout succeeds |  Yes |        - |
| View an order confirmation after checkout | See order confirmation |  Yes |        - |
| Register for an account | Account registered |  Yes |        - |
| Login and logout | Login and logout works |  Yes |        - |
| Recover my password | Password recovered |  Yes |        - |
| A personalized user profile | The profile template renders |  Yes |        - |
| As a store owner I want to be able to add/edit/update/delete a mug | Staff status and links to backend renders for users with staff status |  Yes |        - |

---

### Different Browsers and devices

#### Desktop

| Description     |          Expected outcome           | Pass | Comments |
| --------------- | :---------------------------------: | ---: | -------: |
| Microsoft Edge  | The application works appropriately |  Yes |        - |
| Google Chrome   | The application works appropriately |  Yes |        - |
| Mozilla Firefox | The application works appropriately |  Yes |        - |
| Safari          | The application works appropriately |  Yes |        - |

#### Mobile

| Description   |          Expected outcome           | Pass | Comments |
| ------------- | :---------------------------------: | ---: | -------: |
| Google Chrome | The application works appropriately |  Yes |        - |
| Safari        | The application works appropriately |  Yes |        - |

---

### Responsiveness

The site is not fully responsible yet, almost though. Need to finish up the CSS.

---

### Code validation

#### CSS

I validated my CSS with the [Jigsaw W3C Validation Service](https://jigsaw.w3.org/css-validator/ "CSS Validation").
1 error was located related to materialize or django. As the application works as intended it's nothing to be concerned about.
Therefore I choose to leave it for now even though jigsaw regards the CSS as an error.

#### HTML

I validated my HTML with the [W3C Markup Validation Service](https://validator.w3.org/ "HTML Validator") with no errors to show.

---

### Defensive design

I've implemented defensive designs throughout the application. Fields are required before submitting.
`maxLength` is applied to `input` fields. Error messages pops up where appropriate.
Email confirmation message pops up after successfully sent email.
There are more defensive design you can add to improve the user experience,
such as confirmation before deleting a creative ad/brief or adding interactive questionmarks that provide relevant information.

---

### Conclusion

After testing the deployed application my overall conclusion is that the application is working as intended apart from the CSS.
It has a lot of potential to provide even more value for the user with future installations of the application.
The javascript and python works as intended.

[Back to Top](#uglymugs.com)
***

## Deployment

This project is stored in a GitHub repository and hosted on Heroku.

---

### How to clone this repository in order to run the code locally on your machine

1. Click [here](https://github.com/robinwesterback/creative-hub/ "Creative Hub Repository") to get to the projects repository.

2. Click "Clone or Download".

3. Click the "copy" icon.

4. Open Git Bash in your local IDE.

5. Change your current working directory to where you want the cloned directory to be made.

6. Type `$ git clone` and then paste the URL you copied earlier.

   `git clone https://github.com/USERNAME/REPOSITORY`

7. When you press enter your local clone will be ready.

8. Install the requirements from requirements.txt

---

### How I deployed the project on Heroku/AWS S3

Here is a summary of deployment. Deploying Django Projects to Heroku/AWS S3

ugly-mugs-app
1. requirements.txt
2. Procfile
3. DB Connection
4. S3 Connection
5. Environment Variables
6. Github

Heroku
1. Database
2. Config Vars (Environment Variables)
3. Deploy (Github)

AWS
1. S3 Buckets
2. IAM (Security)

We can use either MySQL or Postgres DB on Heroku.
I used Postgres for this project.
1. Create a Heroku Personal Project
    1. Optionally enter a project name. Must be unique accross heroku. Perhaps prefix with name or website e.g. niels-ecommerce
    2. Choose 'Europe' as Runtime Selection
    3. Select 'Resources' and under 'Add-ons' enter postgres, and select Heroku Postgres. Provision a hobby (free) database.
    4. Click on Settings, Reveal Config Vars and note that there is now a DATABASE_URL setting.
2. Modify App to Connect to Heroku DB instead of local
    1. sudo pip3 install dj-database-url
    2. sudo pip3 install psycopg2
    3. sudo pip3 freeze --local > requirements.txt
    4. In settings.py import dj_database_url
    5. Change the existing DB connection in settings.py to use a URL. Comment out the following:
    `
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    `
    Replace with this.
    `
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
    `
    6. Create a file called env.py in the project folder (Same folder as settings.py). Add the DATABASE_URL and SECRET_KEY variables as follows.
    `
    import os
    os.environ.setdefault("SECRET_KEY", "<KEY HERE>")
    os.environ.setdefault("DATABASE_URL", "<DB URL HERE>")
    `
    7. python3 manage.py makemigrations 
       python3 manage.py migrate
    8. python3 manage.py createsuperuser
3. Get Project Ready to run on Heroku
    1. Create Procfile(s). One file called Procfile (Upper case P, no file extension) 
    `
    web: gunicorn projectfolder.wsgi:application
    `
    projectfolder above is the name of the project file that we want to run.
    2. sudo pip3 install gunicorn`
    3. pip3 freeze --local > requirements.txt

---

### Running the application locally using Gitpod

1. Clone the repository as outlined above and upload it to GitPod.

2. Install the necessary libraries specified in the requirements.txt.

3. Set your environment variables by creating and adding them into a env.py file.

4. Create a .gitignore file in the root directory and add the env.py file to avoid it being pushed to GitHub.

5. Import the env.py file into the app.py file.

6. Run the application.

[Back to Top](#uglymugs.com)
***

## Credits

---

### Content

All content on the application was written by me.

---

### Media

The Icons used for this project was from [Materialize](https://materializecss.com/ "Materialize").
The images used were found on [Unsplash](https://unsplash.com/ "Unsplash")

---

### Acknowledgements

Big thanks to my mentor who provided me with tips, support and helpful resources.

[Back to Top](#uglymugs.com)
***