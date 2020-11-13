# Megapixel Groups Creative Hub

Data Centric Development Milestone Project @ Code Institute

This project is a creative hub where creatives and employers meet.
The web application is built using flask and pymongo.
It allows you to perform CRUD operations for users, creatives, briefs and skills.
It has a form for logging in user and a form for contacting the creative/employer.
The application provides contact information and a link to Megapixels marketing services.
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

[Back to Top](#megapixel-groups-creative-hub)
***

## UX

The application is designed using the [materialize](https://materializecss.com/) framework.
It is designed to be user friendly, simple and clean with the purpose to present all information in a visually appealing manner on all devices.
It is made for creatives/employers who wants to connect with one another.
They want to be able to create a user, creative ads and briefs.
They want to edit user, creative ad and brief details.
They want to be able to find creative ads and briefs.
They want to be able to delete creative ads and briefs.
To provide that information this application is a simple and straightforward web application.
It contains an index page, user interface, sections for creative ads/briefs as well as for performing CRUD operations, contact etc.
The footer provides contact information and a link to Megapixels marketing services.

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

The user stories are showing pictures from an earlier stage of the project and not the deployed version.
You can access the deployed project [here](https://creative-hub.herokuapp.com/) to try the user stories yourself.

#### Story 1

As a user, I want to click on a navigation link -
![alt text](static/images/click-create-account.jpg "Click Create Account")

So that I can get navigated towards the desired link location.
![alt text](static/images/location-create-account.jpg "Location Create Account")

#### Story 2

As a user, I want to create a user account -
![alt text](static/images/create-user-account.jpg "Create User Account")

So that I can log in to my user interface
![alt text](static/images/user-interface.jpg "User Interface")

#### Story 3

As a user, I want to be able to log out -
![alt text](static/images/log-out.jpg "Log out")

And I want to be able to log in.
![alt text](static/images/log-in.jpg "Log in")

#### Story 4

As a user, I want to be able to create a brief -
![alt text](static/images/create-brief.jpg "Create Brief")

And a creative ad.
![alt text](static/images/create-creative-ad.jpg "Create Creative Ad")

#### Story 5

As a user, I want to be able to delete a brief/creative ad -
![alt text](static/images/delete-creative-ad.jpg "Delete Creative Ad")

And edit/update a brief/creative ad.
![alt text](static/images/update-brief.jpg "Update Brief")

#### Story 6

As a user, I want to be able to find briefs/creative ads -
![alt text](static/images/find-creatives.jpg "Find Creatives")

And contact the creative/employer.
![alt text](static/images/contact-employer.jpg "Contact Employer")

#### Story 7

As a user, I want to get information (social links, contact info etc.) about the owner of the site, so that I can contact the owner if I want to.
![alt text](static/images/contact-information.jpg "Contact Information")

---

### Strategy

I want to create an e-commerce to sell ugly mugs for people who loves ugly mugs
The shopper gets the benefit of buying that ugly mug that they love. 
The shopper gets the benefit of a seamless and secure shopping experience with control of their shopping with e-mail confirmations etc. 
The site user can easily register an account and view all purchase history and information about the user. 
The store owner can add, edit and delete products. 

---

### Scope

A shopper can view the website on any device including mobile, tablet, desktop.
A shopper can view products and product details before adding it to the cart.
A shopper can add, edit and delete products to and from the cart.
A shopper can find purchase history and orders.
A shopper can register and edit an account including shipping and billing details.
A shopper can filter mugs on years / months.
A shopper can log in and out of the account.
A shopper can navigate easily and make safe purchases.
A shopper can't make purchases that are empty and submit forms that doesn't meet all the requirements.
A store owner can manage products in the backend via staff login.

Future releases may introduce:
More interaction with the shoppers and how they can utilize the website (e.g search function when required).
Use data in fun and valueable ways for the shoppers and the store owners. Ex. show how many mugs each edition sold for.
Introduce more products and methods to purchase the products e.g introduce subscriptions.

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

[Back to Top](#megapixel-groups-creative-hub)
***

## Features

The application contains several features with a few left to be implemented.

---

### Existing Features

#### Navbar

A materialize [component](https://materializecss.com/navbar.html "Materialize Navbar") with a hamburger menu for mobile.

#### Footer

A materialize [component](https://materializecss.com/footer.html "Materialize Footer").

#### Icons

A materialize [component](https://materializecss.com/icons.html "Materialize Icons").

#### Forms

##### Text Inputs

Materialize [form input](https://materializecss.com/text-inputs.html "Materialize Text Inputs").

##### Select

Materialize [form select](https://materializecss.com/select.html "Materialize Select").

##### Date picker

Materialize [form date picker](https://materializecss.com/pickers.html "Materialize Pickers").

#### User login

The application allows the user to log in and out of a session.

#### CRUD Operations

The application operates to a MongoDB with 4 collections - users, briefs, creatives and skills.

##### Create document

The application allows the user to create a document in the MongoDB.

##### Read document

The application allows the user to read a document in the MongoDB.

##### Update document

The application allows the user to update a document in the MongoDB.

##### Delete document

The application allows the user to delete a document in the MongoDB.

#### Send email

I use [emailjs](https://www.emailjs.com/ "EmailJS") to let the user send emails to the site owner.
The user gets notified wether it is a success or of it fails.

---

### Features Left to Implement

#### Smarter interactivity for users

Make functions, collections and the exchange of information between users better.
E.g. pagination, search functions for retrieving data from the backend, categorized in a more user friendly way as the application grows larger.

#### Recourses, functions and content

Provide more information, resources and possibilities to create better ads to improve success rate for user interaction.

#### Add images, links etc.

Give users the ability to add images, documents, links etc.

#### Defensive design

Make the application more compatible with browsers other than Chrome. Customize the 404 error webpage.
More secure way to log in.

#### Livechat and chat function

I might add a livechat for contacting the site owner and a chat function for communication between users.

#### Your thoughts

Are there any features that you would like me to implement to improve the application? Please get in touch and share your thoughts.

[Back to Top](#megapixel-groups-creative-hub)
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

---

### Databases
- [PostgreSQL](https://www.postgresql.org/ "PostgreSQL") database service provided directly by Heroku
- [SQlite3](https://www.sqlite.org/index.html "SQlite3") provided by django

[Back to Top](#megapixel-groups-creative-hub) 
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

[Back to Top](#megapixel-groups-creative-hub)
***

## Deployment

This project is stored in a GitHub repository and hosted on Heroku.

---

### How to deploy to Github

1. Click [here](https://github.com/robinwesterback/creative-hub/ "Creative Hub Repository") to get to the projects repository.

2. Click on 'Settings' to the far right in navigation menu below your repository name.

3. Scroll down to 'GitHub Pages' and select 'master branch' as the source.

4. Click save.

5. The link to the site hosted on GitHub Pages should appear at the top of the section.

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

---

### How to clone this repository in order to run the code locally on your machine

1. Created a new application using the Heroku dashboard.

2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).

3. Install Heroku via the console using 'npm install -g Heroku'.

4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.

5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.

6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.

7. Connect GitHub to Heroku via the console using 'heroku git:remote a creative-hub'

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

[Back to Top](#megapixel-groups-creative-hub)
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

Big thanks to my mentor who provided me with tips, support and some helpful resources.

[Back to Top](#megapixel-groups-creative-hub)
***

## Resources

Below is a list of the resources used to create this project:

- [Log in system](https://www.youtube.com/watch?v=vVx1737auSE&ab_channel=PrettyPrinted "Log in system")
- [Materialize](https://materializecss.com/ "Materialize")
- [EmailJS](https://emailjs.com/ "EmailJS")
- [Flask Cheatcheet](https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf "Flask Cheatcheet")
