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

### Database structure

There are 4 collection in the database:

- users:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "email":                 <string>,
  "phone":                 <string>,
  "city":                  <string>,
  "country":               <string>,
  "password":              <Binary>
}
```

- Briefs:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "city":                  <string>,
  "country":               <string>,
  "company_name":          <string>,
  "title":                 <string>,
  "hours":                 <string>,
  "duration":              <string>,
  "required_skills":       <string>,
  "budget":                <string>,
  "project_start":         <string>,
  "description":           <string>,
  "action":                <string>,
  "email":                 <string>
}
```

- Creatives:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "city":                  <string>,
  "country":               <string>,
  "skills":                <string>,
  "hourly_rate":           <string>,
  "description":           <string>,
  "action":                <string>,
  "email":                 <string>
}
```

- Skills:

```
{
  "_id":                   <ObjectId>,
  "skill_name":            <string>
}
```

---

### User Stories

You can access the deployed project [here](https://creative-hub.herokuapp.com/) to try the user stories yourself.

- As a shopper I want to be able to view a list of mugs si that I can select some to purchase
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

In this [link](https://github.com/robinwesterback/creative-hub/tree/master/wireframes) you can find the wireframes for each section that serves as the skeleton for the project.

---

### Surface

In this [link]() you can find the mockups for the website created with [figma]().

#### Fonts
I used from SF Pro Text and SF Pro Display [Google Fonts]():

#### Colors
- #111111 - font Colors
- #222222 - background Colors

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

#### Pagination

The application provides [pagination](https://materializecss.com/pagination.html "Pagination") to the website clean.

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

### Functionality

| Description                                    |                   Expected outcome                   | Pass | Comments |
| ---------------------------------------------- | :--------------------------------------------------: | ---: | -------: |
| Input 50 letters in campaign_name              |               Max input of 30 letters                |  Yes |        - |
| Post a form without filling in required fields | Shouldn't work, both backend and frontend validation |  Yes |        - |
| Log in with an e-mail that is not registered   |      Shouldn't work, error message should show       |  Yes |        - |
| Send an empty contact form                     |         Shouldn't work, fields are required          |  Yes |        - |

---

### User Stories

| Description                                    |                Expected outcome                 | Pass | Comments |
| ---------------------------------------------- | :---------------------------------------------: | ---: | -------: |
| Click on a navigation link                     | Get navigated towards the desired link location |  Yes |        - |
| Create user account                            |              User account created               |  Yes |        - |
| Create a user account with a registered e-mail |  It doesn't work and an error-message pops up   |  Yes |        - |
| Delete a creative ad                           |               Creative ad deleted               |  Yes |        - |
| Edit and update brief                          |            Brief edited and updated             |  Yes |        - |
| Send a message from the contact form           |                Message gets sent                |  Yes |        - |

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

I have tested the responsiveness of the application [here](http://ami.responsivedesign.is/# "Am I Responsive?") and it is responsive.

![alt text](src/assets/images/responsive-app.jpg "I am responsive!")

---

### Code validation

#### CSS

I validated my CSS with the [Jigsaw W3C Validation Service](https://jigsaw.w3.org/css-validator/ "CSS Validation").
1 error was located related to materialize. As the application works as intended it's nothing to be concerned about.
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

### Bugs discovered

#### Solved bugs

1. Bug#1
    - Description of bug
    - Solution for bug

---

### Conclusion

After testing the deployed application my overall conclusion is that the application is working as intended.
It has a lot of potential to provide even more value for the user with future installations of the application.
The javascript and python works as intended.
The minor flaws that exist don’t ruin the user experience but should be corrected in the future.

[Back to Top](#megapixel-groups-ugly-mugs)
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

### How I deployed the project on Heroku

1. Create a new application using the Heroku dashboard.

2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).
Add settings accordingly to settings.py.

3. Postgres on Heroku and install [gunicorn]( ""), [dj-database-url]( ""), and [psycopg2-binary]( "") 

4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.

5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.

6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.

7. Connect GitHub to Heroku via the console using 'heroku git:remote a ugly-mugs'

8. Commit all files in your project via the console using 'git add .' and 'git commit -m "Message"'.

9. Deploy your project to Heroku via the consol using 'git push heroku master'.

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
The design was inspired by [Materialize](https://materializecss.com/ "Materialize").

---

### Media

The favicon used for this project was delivered by [Megapixel Group](https://www.megapixel.group/ "Megapixel Group").
The Icons used for this project was from [Materialize](https://materializecss.com/ "Materialize").

---

### Code

- Code borrowed
- Code borrowed
- Code borrowed

---


### Acknowledgements

Big thanks to my mentor who provided me with tips, support and helpful resources.

[Back to Top](#uglymugs.com)
***

## Resources

Below is a list of the resources used to create this project:

- [Materialize](https://materializecss.com/ "Materialize")