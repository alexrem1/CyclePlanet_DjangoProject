# Cycle Planet

This is a Full-Stack ecommerce site designed with ease of use at mind and an intention to give potential users the ability to purchase products and subsequently recieve an email with your order information.
The user doesn't have to be registered or logged in to recieve a confirmation of their order purcharse but if they are logged in then they may view any orders previously placed via their profile which is possible thanks to login required authentication decorators.
Users within the shopping bag have the functionality to update and delete their items from the shopping but they cannot edit or delete products from the database. Full CRUD functionality is only available for admin and management (store owner etc).
Once on the checkout portion of the site, users can enter their shipping details and convieniently save it for faster checkouts next order and/or to populate their 'My Profile' default shipping details.
The purpose of the site is to ultimately to sell Cycle Planet products and make the user experience as easy and pleasant possible.

The link for the app is:

_https://alexrem1-cycle-planet.herokuapp.com/_

## UX

With the user at the forefront of this project, I wanted to create a simple ecommerce bicycle site that has a resonable amount of functions. Starting with

### Viewing and Navigation

> As a shopper I want to be able to view a list of products so that I can select some to purchase.

- my products view allows shopper to do this as it ultimately passes through all products within my database

> As a shopper I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all the products.

- users of the site who land on the products page will have links that allow them to easily filter whichever category they're interested in and quickly identify what product they are interested in

> As a shopper I want to be able to view individual products details so that I can Identify the price, condition, sellers notes, type of product , product name, image, model, colour and size etc.

- users who click on the products image will be taken to a page containing all the useful details of the product so they may make an well informed decision about wether they wil purchase the product.

> As a shopper I want to be able to quickly identify any deals so that I can take advantage of special savings on products I'd like to purchase.

- included in the main navigation bar is a heading labled 'deals' which instantly allows a user to identify exactly which products are on offer. Users may also view this from the products page by clicking on the 'deals' link automatically filtering only products that are on offer

> As a shopper I want to be able to easily view the total of my purchases at any time so that I can spend as much money as I see fit or remind myself to stay below a certain amount.

- contained within the main navigation bar is the shopping bag with an amount displayed that is always updated whenever a product is added to the shopping bag which constantly reminds the user of how much they may be potentially spending.

### Registration and User accounts

> As a site user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile

- thanks to django's builtin allauth package, once all the right settings had been configured within my project, allowing user registration was quick and great for user experience
  > As a site user I want to be able to easily login or logout so that I can access my personal account info
- via the power of django's allauth, if the user is authenticated (registered) then login and logout is available for them, otherwise a login and register is available
  > As a site user I want to be able to easily recover my password in case I forget it so that I can recover access to my account
- When logging in, a forgot password link can be found on the page, following the instructions to check their email and then reset the password is quick and easy enough thanks to allauth
  > As a site user I want to be able to recieve an email confirmation after registration so that I can verify that my account registration was successful
- users who register recieve a confirmation email containing a link that updates the users authentication to log in to the site
  > As a site user I want to be able to have personalized user information so that I can view my personal order history and order confirmations
- now the user is authenticated, they can now see their own profile containing their information, order history and order confirmations

### Sorting and Searching

> As a shopper I want to be able to sort the list of available products so that I can easily identify the best prices and alphabetically sort products

- within the products page, alphabetical and pricing sorting is available to help assist the user finding the right product for them via low to high price sorting for example
  > As a shopper I want to be able to sort a specific category of product so that I can find the best-priced product in a specific category and sort the products in that category by name
- mentioned earlier is the ability to filter a certain category, condition, for example and with that now filtered products page users are able to sort via price or by name
  > As a shopper I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase
- users can type into the search bar in the main nav bar and search results, if they exist, will be displayed
  > As a shopper I want to be able to easily see what I've searched for and the number of results so that I can quickly decide wether the product I want is available
- users can type into the search bar in the main nav bar and it will display what the user has searched as well as search results if they exist

### Purchasing and Checkout

> As a shopper I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I dont accidentally select the wrong product or quantity

- contained in the product details page will be a quantity input box where users will then have the choice to enter what quantity they would like
  > As a shopper I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and at all times I will recieve
- the shopping bag once clicked contains all products that have been added to the bag, the quantity, the subtotal, delivery cost and grand total so users are always informed of what they are buying and for how much
  > As a shopper I want to be able to easily enter my payment information so that I can checkout quickly and with no hassle
- STRIPE credit-card processor allows users to do so
  > As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed info to make a purchase
- STRIPE has been audited by a PCI-certified auditor and is certified to PCI Service Provider Level 1 which is the most stringent level of certification available in the payments industry
  > As a shopper I want to be able to view my order confirmation after checkout so that I can verify that i haven't made any mistakes
- a combination of views and templates set up in the checkout app, after completing their, users will be redirected to a copy of their confirmation order. This can also be seen in their user specific profile under my account
  > As a shopper I want to be able to recieve an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records
- email confirmations have been set up and so users will receive a customised email for this

### Admin and Management

> As a store owner I want to be able to add a product so that I can add new items to my store
> As a store owner I want to be able to edit/update a product so that I can change product prices, descriptions, images and other product criteria
> As a store owner I want to be able to delete a product so that I can remove items that are no longer for sale

- CRUD functionality has been enabled for superusers to create a new product, edit or update an existing product and delete a prodcut

COMPLETE WIREFRAMES HERE

This site is aimed at potential users who are interested in purchasing quality bicycles. I designed my website with the user in mind to enhance their user experience and believe it will increase my chances.

## Features

### Existing Features

- **Nav Bar –** Contains Cycle Planet text that is also a homepage link, a search bar, a few dropdown options and a shopping bag icon. The Navbar is designed to be static because of its white background and it also reverts to a collapsed state with users being able to toggle its view or click on the individial icon links. This collapsed state navbar on screens smaller that medium for enhanced viewing. This is a defensive mobile first design.

- **User Nav Bar –** Following on from above, users that are not aunthenticated have limited access to the products page, the register, login, shopping bag and checkout pages, compared to a user who is authenticated that has the former access and now can view their profile which contains their past order history as well as shipping details.

- **Search Bar –** The Search bar is available on all pages for the user to search for a specific bike by name, description and their SKU number. To filter through the vast amounts of products, a search bar is critical to enhance user experience.

- **Product Card and its Detail–** Each product is rendered in a card format and on this card the name, image, links to categories the product belongs to and its own prices. Users can see what categories the bike belongs without initially sorting the products themselves giving them a snippet of the cards details. With the product card is its own unique details, inwhich the information stored in the database is presented for each unique product (e.g. Name, Seller Notes, Price, Price before, Image, Gender, Color, Number of Speeds, Size, Wheel Size, Bike Type, Brand and Condition). The user can input the quantity they require for each product and press the `Add to Bag` button, to add items to the Cart.

- **To the top button–** Depending on what filter is currently selected, the user may have to scroll quite ways to get back to the top. A button that automatically takes the user back to the top of the page enhances user experience.

- **Display-4 Text–** This specific bootstrap text transformation is defensively designed to be reduced in size on smaller screen sizes all with the intention of enhancing user experiencen by improving site navigation. The larger screen resolutions show its original sizing.

- **Success Message Bar –** When the user performs an action, such as logging in or out, adding a product , removing a product or deleting a product from their shopping bag, confirming their registration email, adding a product, updating a product and removing a product from the database , a green notification banner will appear below the Navbar to tell the user that the operation was a success.

- **Error Message Bar –** When the user performs an action , such as leaving the field empty when searching, all non-superuser actions, checking out with an empty shopping shopping cart and incorrect information in forms, a red notification banner will appear below the Navbar to tell the user that the operation was resulted in an error.

- **Register Page –** The registration page form allows the user to register with the site by providing a email address, email address confirmation, username, password and password confirmation. When clicking the `Sign up` button, if the email or username used is already in the database the user will be notified via an error but if not, users will be redirected to information relating to how they can activate their account and be able to log in.

- **Login Page –** The Login page form allows user to login using their username or email and password. If users forget their password, there is a reset password link that sends an email (email in the database, the user must already have registered) to the user directing them on how to reset their password. To do they will have to enter a password and then confirm it again. To finish it off, there is a `sign up` link that takes the user to the registration page.

- **Logout Navbar Button –** If pressed qnd subsequently confirming the sign out, the user will be logged out from the site and the user is taken back to the unathorised user homepage. The user is notified by a green notification success message banner that they have successfully logged out.

- **Shopping Bag Page –** If there are no items in the Cart and the user somehow accesses the checkout view, the user will be redirected back to whichever page they were on with a message of 'here's nothing in your bag at the moment'. If the user has items in their bag they will be displayed in the Shopping Bag page along with the options to `Update` the quantity, `Remove` the product from the bag, `Secure Checkout`, or `Keep Shopping` button with the former redirecting them to a confirmation order and the latter redirects back to the products page. The page also consists of an image of the product, name, quantity, SKU, subtotal, shipping costs and finally a grand total. Users are aware of all main aspects before they finally decide on a purchasing a product. I have incorporated a defensive mobile design that enhances the user experience by changing the layout to be more accomadating for mobile users.

- **Add product to bag toast –** If there is a `grand total` and the user is not 'on profile page' adding a product to the shopping bag will display a success toast message of what was added to the bag and also a preview of the what is in the bag eg how many products are in the bag, the image, price, quantity, price, total (incase there's a quantity of more than 1 of the same product).

- **Add a review –** If the user `is.authenticated` they will have the ability to leave a review which will print their username, date and time of post and their review comment compared to non-registered users who will have to sign up before they can leave a review.

- **Profile Page –** The My Profile page under the dropdown My account allows the registered and thus authenticated users to insert their default delivery information such as name, address, postcode, phone number etc. These details are prepopulated within the users checkout form for quick and easy payments.

- **Order History –** Located within the My Profile section page is the users order history where they can find their order number, shipping details, order date and time and order summary of product name, sellers notes, price, quantity, subtotal and grand total including the delivery cost. This is helpful for users if they don't have access to their emails at the time and in general good ecommerce practice.

- **Product Management –** Located under the dropdown My Account, site owners, admin or managent who are superusers will have access to all CRUD functionality. They will be able to create a new product, read and locate that new product or existing products, update these products and/or delete a product from the database. This is crucial for site maintanence and users will greatly appreciate this.

### Features left to implement

- Write more tests in tests.py files for each individual app.

- Pagination

- Create an update quantity view to increase/decrease amount of product whilst in the shopping bag.

- Footer

- Due to time constraint it was not possible to implement the functionality and page of a Contact Us page

## Technologies Used

- **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the web-app. https://www.gitpod.io/

- **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently during the development of the web-app. https://github.com/

- **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database.
  https://heroku.com/

- **SQlite3 -** SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. https://www.sqlite.org/index.html

- **PostgreSQL -** PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/

- **Django 1.11.29 -** Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. https://www.djangoproject.com/

- **AWS S3 -** Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. https://aws.amazon.com/s3/

### Front-End Technologies

- **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a better understanding.

- **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the _style.css_ file.

- **Bootstrap 3.3.7 -** The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised
  to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/

- **Django-crispy-forms 1.9.2 -** A simple bootstrap filter for Django forms. Extracted from the bootstrap theme.
  https://django-bootstrap3.readthedocs.io/en/latest/

- **Django Allauth 0.42.0 -** Supports multiple authentication schemes (e.g. login by user name, or by e-mail), as well as multiple strategies for account verification (ranging from none to e-mail verification. Allowing greater control over security and to scale out your build infrastructure as needed.

- **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.
  https://www.javascript.com/

- **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation.
  https://www.jquery.com/jquery-3.4.1

- **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

- **Python 3.8.6 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small,
  and it is easy to learn for brginners. https://www.python.org/

- **Gunicorn 20.0.4 -** Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with
  various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

- **Pillow 7.2.0 -** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides
  extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
  https://pillow.readthedocs.io/en/stable/handbook/overview.html

- **Psycopg2-binary 2.8.6 -** Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are
  the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/

- **Django Storages 1.10.1 -** Django Storages is a collection of custom storage backends for Django.

- **boto3 1.16.6 -** Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS
  services, such as EC2 and S3. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- **Stripe 2.55.0 -** Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices
  and is designed to increase conversion. Checkout makes it easy to build a first-class payments experience.
  https://stripe.com/docs/payments/checkout

## Testing

The main basic functions of the site that required rigorous testing in different scenarios are listed below.

- **Navbar**
  - All Navbar links are coded within the base.html and includes (main-nav.html and mobile-top-header) that extends to each html page. The logo is a home link that has been tested form each page and each link
    (e.g. `Products`; `Register`; `Login`; `Bag`; `Product Management`; `Profile`; `Logout`) works correctly accross all devices and screen resolutions. Each link directs the
    user to the relevant page and the `Logout` button logs the user out of the site, not before the user being prompted to cancel or log out.

- **Search Bar**

  - The Search bar is used to search all available products across the site and can be found contained in the nav bar inbetween the logo and the dropdown links. The search bar returns items that are related to the `name`, `SKU` and `seller notes` of the product. Users who don't enter before they search will be met with an error message letting them know they didn't search for anthing. This function works correctly.

  - **To the top button**

  - This works as intended, on all screen sizes and resolutions.

- **Product Card**

  - Each product card shows various types of information, coming directly from the database, related to the individual product such as the product name, an image, 4 category sorting parameter links and the price of the product. All tests ran smoothly as all links on that page work as intended.

- **Product Details Link**

  - Every product in the database is unique and to be able to view the full details of that product, users must click on the image rendered where they'll be redirected to that products unique details. This view works as intended.

- **Add a Review**

  - Each product review generated by an authenticated user redirects them back to the products detail page returning the username, comment and the date and time. I created a model with the fields mentioned above, linking to the individual product with the Foreign Key as well as giving the user a Foreign Key to the django allauth users to be able to populate the correct user. If the user is not registered, a redirect to the login page will occur followed by an error message letting them know they must sign up to leave product reviews. The functionality for this feature works as expected.

- **Add To Bag**

  - This button inserts a selected number of each individual product into the shopping bag. Validation of this can be seen when the user presses the `Add to bag` button and the number
    quantity of items can be seen in the shopping bag preview located in the right corner of the Navbar. Once the user views the contents of the shopping bag, all of the selected items will be shown eg the products price, quantity and its subtotal.

- **Shopping Bag Preview**

  - Testing occured via numerous additions of products to the bag. It works as intended and displays all the right informtion.

- **Sorting and Filtering**

  - Users are able to sort products alphabetically and by its price by clicking on the `sort by` select box. This would redirect back to the same page with one of 4 options (price - low to high / high to low or alphabetically - A-Z / Z-A) selected and thus the sorted method initialised. Right across from the 'sort by' feature is the sorting method. Users click on either condition, brand, deals or bikes where in each instance users are offered multiple sorting parameters. For example a user may want to filter a mountain bike and sort with a method of low to high price. This has been tested extensively from the first implementation and it has worked as intended.


- **Registration Form**

  - In the Registration Page the user can set up an account by inserting a Username, Email Address, Email Address Confirmation, Password and Password Confirmation. The form automatically cross
    checks the the validity of the Email Address and Password Confirmation. There is an optional link for the user to Sign In if they already have an account.

- **Login Page**

  - A user who has already registered can log in to the site via the `Login` Navbar menu item. This page authenticates the user against those stored in the database.
    A verified user will be logged in and if they're not verified but have already signed up a new confirmation email will be sent to the registered address. There is a Forgotten password link and a link for a user who is not registered.

- **Password Reset Page**

  - if a user has prevbiously registered to the site they can insert their email address into the field and reset their password. An email is sent via smtp.gmail.com to the
    users email address. This functionality has been tested utilising multiple email addresses. The link in the email allows the user to create a new password, new password confirmation and then confirm.
    Once completed the user is directed back to the Login Page where they recieve a message success letting them know they've verified their email address and are able to login with thier email address or user name and password.This function has been
    rigorously tested.

- **Shopping Bag Page**

  - The shopping bag page displays products that the user has selected to purchase, its quantity, its subtotal, the delivery cost and the grand total. The user can amend the remove the product(s) to be purchased using the `remove` link. If the user clicks that button the product will be deleted from their shopping bad. This function has been extensively tested. The 'Grand Total' figure has been calculated by the product ID's and quantities of each product first within /bag/contexts.py/ and finally in /bag/views.py/. This has been tested repeatidly. The `Secure Checkout` button directs the user to the Checkout page and the `Continue Shopping` button takes the user back to the products page with their prior products still in the Bag.

- **Profile Page - Form**

  - This form allows the user to update their 'Default Delivery Information' (e.g. Street Address 1, Street Address 2, Town or City, County, Post Code, Country and Phone Number). This information will be stored under the 'User Profile' information in the Django database and can be utilised to pre-populate fields in the Checkout page.

- **Checkout Page**

  - The Checkout page displays the products that the user has selected to purchase along with its image, their related quantities and prices, subtotal, delivery cost and the grand total shopping bag figure. These elements have been tested and return the correct figures.

- **Checkout - Payment Details Form**

  - The Checkout Payment Details form is directly linked to the Stripe payment API and allows the user to input their Full Name, Email Address, Phone Number and their shipping details (if the user has already registered their Profile details and opted to save their details to the database, these fields will be prepopulated).

- **Checkout - Payment Card Info Form**

  - The user is able to input their Credit card information to purchase the shopping bag contents. This function has only been tested using Stripes dummy card information that consists of `Credit card number` 4242424242424242; `Month` A month in advance of current month; `Year` a year in advance of the current year and `Security Code` 424;. This functionality has been tested and can be checked in the /admin/home/checkout/orders/ section of the Admin panel. These payments are also visible on the https://dashboard.stripe.com/payments page. This confirms all the payments that have been passed through the system. The payment will not submit through the `Complete Order` button if the card information is incorrect and if the cart is empty and the user attempts to checkout, they'll be redirected back to the home page with an error message saying there's nothing in your bag.

- **Checkout - Submit Payment Button**

  - Submits the Payment and returns the user to the Homepage with the Django success banner 'You have successfully paid'. If payment is not successful, the user will be not
    leave the Checkout page.

- **Profile Page - Order History**

  - The order history has been tested via multiple checkout successes which prints out a order number that attaches to the users order history in their profile each time containing their order number, your shipping details, order date and everything relating to costs. Also a automated email is sent out containing the exact same information. Everything works as intended

* **AWS S3**

  - The AWS S3 allows access to stored files within the site owners AWS bucket that are shared through the users AWS account. The accompanying AWS info is linked through the relavant AWS info in the
    `settings.py` file. The testing of this functionality is shown in the availability of the stored data in the post prodution database andsite.

* **Responsive / Mobile First design**

  - In some instances I've tried to think about a mobile first approach by implementing a collapsable navbar on smaller screens, smaller buttons, smaller text-display and refactoring the shopping bag
  - Continuous testing throughout the development has been implemented to check the quality of the code. The aim is to check the functionality of the code on different devices (mobile, tablet, desktop) with an overall perspective of responsive pkand mobile first design. The site has been viewed and tested in **Firefox**, **Safari**, **Chrome**
    **Microsoft Edge** and **Explorer**. The devices used to test the site are **iPhone 5/SE**, **Samsung Galaxy**, **iPad**, **iPad Pro**
    **iPhone X**, **iPhone 6/7/8**, **Pixel 2**, **Pixel 2 XL** , **Hudle2** and **Samsung / Lenovo / HP laptop**.

* **W3 Nu Html Checker**

  - All .html files require validation through the online checker. This ensures that the code is more legible and does
    not contain formatting errors. https://validator.w3.org/

* **W3C CSS Validator**

  - The style.css file requires validation through the online checker. This ensures that the code is more legible and does
    not contain formatting errors. https://jigsaw.w3.org/css-validator/validator

* **PEP8 Online**
  - The Python (.py) pages require validation through the online checker. This ensures that the code is more legible and does not contain formatting
    errors. http://pep8online.com/


## Deployment

The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding.
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it
functioned correctly or easily find lost pieces of code.

### To deploy the project to Github the following steps were taken:

1. created a `master` branch in Github repository
2. Used Gitpod environment used to build the site
3. Committed files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m"add message"`
4. Pushed files to the working environment using `git push`, which then updates the repository.
5. Published site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`
6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository
7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
8. Open Git Bash Terminal
9. Type `git clone`, and then paste the URL
10. Press `Enter`. A local clone will be created.

### To set gitignore environment variables the following steps were taken:

1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
2. If you don't have one already, create a file named .gitignore in the root directory of your project.
3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore file add the following text: env.py
4. At the top of your env.py file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os”
   underneath you can assign your environment variables using the following syntax:  
   `os.environ["Variable Name Here"] = "Value of Variable Goes Here"`
5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project. Add this under your
   other imports at the top of the file  
   `from os import path`
   `if path.exists("env.py"):`
   `import env`
6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed, for example using the following syntax:  
   `DATABASES = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}`

### To deploy the project to Heroku the following steps were taken:

1. created a Heroku account @ https://signup.heroku.com/
2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type
   `pip3 freeze --local > requirements.txt`.
3. To install the Heroku command line on Gitpod, use the following command `npm install -g heroku`
4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us
   to push our changes using Git to update the application at any given time.
5. To login to Heroku from the CLI, use the command `heroku login -i`
6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this:
   `echo web: python app.py`
7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
   `git add .`
   `git commit -m "fist Heroku commit"`
   `git push`
8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a [followed by name of Heroku app]`
10. To push to Heroku Master Branch, then simply use `git push heroku master`
11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
12. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku. To do this go to `Settings`
    tab > `Config Variables` and input: `AWS_ACCESS_KEY_ID`; `AWS_SECRET_ACCESS_KEY`; `DATABASE_URL`; `DISABLE_COLLECTSTATIC`; `EMAIL_ADDRESS`; `EMAIL_PASSWORD`
    `EMAIL_PASSWORD`; `SECRET_KEY`; `STRIPE_PUBLISHABLE`; `STRIPE_SECRET`.
13. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
14. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands `mmakemigrations` and `migrate` from the command line.
15. Once the build in Heroku is complete, click the `Open app` button.
16. Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials.

## Credits

### Content

This README.md file is based on the Code Institute template.

Data_Bike.json - came from this free dataset at Kaggle: https://www.kaggle.com/tysonpo/bike-ads-images-prices-specifications?select=data_ebay.json which I had to massively update due to low res images and incomplete dataset

### Media

All landing page images and favicon - used have been displayed with the permisson of Blindside-Brewing.

Favicon – created using https://www.freelogodesign.org/

### Acknowledgments

I would like to thank everyone involved in, especially my mentor Sandeep Aggarwal and the Code Insitute Tutors for both their invaluable feedback.
