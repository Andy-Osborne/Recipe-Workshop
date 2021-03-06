
<div align="center">
    <a href="https://recipeworkshop.herokuapp.com/" target="_blank" rel="noopener noreferrer">
        <img src="https://res.cloudinary.com/andy-osborne/image/upload/v1596140513/Recipe_Workshop/logo_jhedw0.png" alt="Recipe Workshop Logo">
    </a>
</div>

# Recipe-Workshop

[Recipe Workshop](https://recipeworkshop.herokuapp.com/) is an interactive and responsive website that allows users to create an account, browse recipes, upload and share their own cooking recipe creations.

The website has been built with CRUD functionality in mind and allows users access to Create recipes and accounts, Read recipes that have been uploaded, Update recipes and their account details, and Delete their recipes from the website.

I have created this website to cater to all users with an emphasis on those who are looking to either find a recipe to try out and bake or looking to share their latest creation with the world.

I have used HTML, CSS, [Bootstrap Framework](https://getbootstrap.com/), [jQuery](https://jquery.com/), Python, [Flask](https://palletsprojects.com/p/flask/), and [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to build this project. This forms part of my ongoing portfolio of work.

![Preview of Recipe Workshop](https://res.cloudinary.com/andy-osborne/image/upload/v1596095299/Recipe_Workshop/new-repsonsive_u0rb39.png)

## Demo

A live demo of the website is hosted through Heroku and can be found [here](https://recipeworkshop.herokuapp.com/).

## Table of Contents

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)
        - [Variation Between Wireframes and Final Product](#variation-between-wireframes-and-final-product)

2. [**Technologies Used**](#technologies-used)

3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features To Be Implemented**](#features-to-be-implemented)

4. [**Structure of Code**](#structure-of-code)

5. [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
    - [**Manual Testing**](#manual-testing)

6. [**Deployment**](#deployment)
    - [**Step 1 - Run Locally**](#step-1---run-locally)
    - [**Step 2 - Deploying to Heroku**](#step-2---deploying-to-heroku)

7. [**Credits**](#credits)
    - [**Recipes & Recipe Images**](#recipes-and-recipe-images)
    - [**Privacy Policy Generator**](#privacy-policy-generator)
    - [**Site Images**](#site-images)
    - [**Code Credits**](#code-credits)
    - [**Learning Resources**](#learning-resources)
    - [**Acknowledgements**](#acknowledgements)

8. [**Disclaimer**](#disclaimer)

## __UX__

### User stories

As a user:

- I want the landing page of the website to be visually appealing to me as this sets my expectation for the rest of the website.

- I want to be able to see the most liked recipe on the landing page of the website so I am able to try this recipe out for myself.

- I want to be able to see recently added recipes on the landing page as these can give me inspiration of what I can search for, or even try them out myself.

- I want to be able to navigate myself around the site with ease and with as little guidance as necessary.

- I want the website to be responsive and adjust accordingly to the screen I am viewing it on.

- I want to be able to view and search for recipes that have been uploaded to the website.

- I want to be able to search for different recipes whether it is by name, ingredient or dish type.

- I want to be able to rate the recipes that I have tried so others know that the recipe is good and to share my appreciation with the author.

- I want to be able to create an account on the website which will allow me to edit recipes that I have created.

- I want to ensure that when I create an account, my password is only known to me and cannot be seen by the website admin.

- I want to be able to update my password or email address.

- I want to be able to upload my own recipes for other users to try.

- I want to be able to upload a picture for my recipe.

- I want to be able to manage my recipe, or even delete it from the website.

- I want to be able to create a profile page and upload an image of myself and an introduction for other users to see when they view my recipes.

## Design Choices

### Colours

- **Navbar** - I decided to use ``#91CCD4``(Morning Glory) for the navbar as the colour stood out on the site, and especially complimented the whitespace on the site. The psychology from blue can imprint on visitors that of quality, wisdom, productivity and calmness. Whilst there are negative sides to blue depending on the shade used with food-related websites, I feel the shade used avoids these associated negative aspects.

- **Navbar and Primary User Interaction Buttons** - I decided to use ``#EA9C76``(Dark Salmon) as this not only stood out well with the sites colour scheme and complimented those colours as well as standing out to the user.

- **Recipe Front Card** - I decided to use ``#92C5CC`` which is a lighter shade of Morning Glory. I decided upon this as I wanted to use lighter tones of the same colour scheme as used in the website rather a completely different colour. This colour as mentioned, is used to show the recipe name & description (where applicable) on the Feature Recipe, Recent Recipes, Search Result Recipes and for the Recipe Page high level details when viewed on small devices.

- **Font Colour** - I decided to use the default colour for the fonts as this suited the simple approach of a recipe website and I felt it didn't need to change.

- **Link Colours**

  - For the links, I used the following:

    - Normal Link - ``#275F9A``(Endeavour) as this colour stood out well on a white background, fitted in with the sites colour scheme and was easy on the users eyes with a contrast ratio, as given by Chrome Dev Tools, of 6.58.

    - On Hover - ``#A54A1E``(Rich Gold) as this colour stood out well on a white background, fitted in with the sites colour scheme and was easy on the users eyes with a contrast ratio, as given by Chrome Dev Tools, of 5.84.

    For the profile link from a recipe page, I used ``#947232``(Buttered Rum) for the standard colour as I felt that it complimented the sites overall colour scheme and it didn't contrast too heavily compared to the black text to instantly make the user lose focus on what they were reading. The contrast ration as given by Chrome Dev Tools is 4.46.

### Fonts

- [**Averia Serif Libre**](https://fonts.google.com/specimen/Averia+Serif+Libre) - I used this font for the site headers as it reminded me of the typography you would see in recipe books which aids in helping the user feel at "home" on this recipe website.

- [**PT Sans**](https://fonts.google.com/specimen/PT+Sans) - I used this font for the text within modals as it had a great quirky feel to it that complimented Spicy Rice.

### Wireframes

- The wireframes for the initial layout of the website were created using [whimsical](https://whimsical.com/) and you can view the wireframes for Recipe Workshop [here](https://github.com/Andy-Osborne/Recipe-Workshop/tree/master/wireframes) alternatively, you can access them individually here:

  - [Desktop Wireframes](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/wireframes/Desktop%20Wireframes.pdf)

  - [Tablet Portrait Wireframes](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/wireframes/Tablet%20-%20Landscape%20Wireframes.pdf)

  - [Tablet Landscape Wireframes](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/wireframes/Tablet%20-%20Landscape%20Wireframes.pdf)

  - [Tablet Portrait Wireframes](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/wireframes/Mobile%20-%20Portrait%20Wireframes.pdf)

  - [Mobile Landscape Wireframes](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/wireframes/Mobile%20-%20Landscape%20Wireframes.pdf)

#### Variation Between Wireframes and Final Product

During the initial design and creation of the website, I followed the wireframes as designed however there were a few changes as follows:

##### Navbar

- I removed the search bar from the navbar when the user is on the landing page as the user could interact with the search bar on the top of that page and it did not make sense to have the search bar duplicated.

- I added an additional button - "Home" so that the user can click on this and return to the landing page rather than relying on the user to click on the logo to take them back to the home page.

##### Recipe Page

- I did not include the icons to include with the Preparation/Cooking time, Skill Required and servings as I was unable to find a suitable free-to-use favicon as provided in the wireframe design.

- I did not include the option to "Add ingredients to list" due to time constraints.

## Technologies Used

1. [HTML](https://en.wikipedia.org/wiki/HTML) - This was used for the overall structure of the website.

2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This was used for the overall and bespoke styling of elements on the website.

3. [jQuery](https://jquery.com/)- This was used to create overall logic and interactivity of the website, including the use of Ajax for the account management options.

4. [Python](https://www.python.org/) - This was used for all the backend coding of the website.

5. [Flask](https://palletsprojects.com/p/flask/) - The flask micro-framework was used to aid in the construction of the website and its built-in tools like Jinja templating.

6. [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - This was used to connect to the NoSQL database, MongoDB.

7. [Flask-Paginate](https://flask-paginate.readthedocs.io/en/master/) - This was used to paginate the search results.

8. [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - This was used in conjunction with WTForms to create the login and registration page forms, including the validation.

9. [WTForms](https://wtforms.readthedocs.io/en/2.2.1/) - Please see above.

10. [passlib.hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) - This was used for salting and hashing user passwords.

11. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - This was used as the NoSQL database that stores all user recipes, profiles, etc.

12. [Bootstrap Framework](https://getbootstrap.com/) - This was used to create the overall responsiveness of the website through the use of their flexible grid layout.

13. [Cloudinary](https://cloudinary.com/) - This was used to not only host the images used on the website but also allowed users to upload/delete their images through the use of their API.

14. [Google Fonts](https://fonts.google.com/) - I used Google Fonts to obtain the fonts used on the website which are "Averia Serif Libre" and "PT Sans".

15. [GitHub](https://github.com/) - I used to store my repository for the project and record all my commits.

16. [Git](https://git-scm.com/) - This was used for version control.

17. [Heroku](https://www.heroku.com/) - I used Heroku to deploy the live version of my site.

18. [Autoprefixer](https://autoprefixer.github.io/) - I used this project to make sure all CSS prefixes were used where required to ensure cross-browser compatibility.

19. [Visual Studio Code](https://code.visualstudio.com/) - I used this to write the code for my site.

20. [Font Awesome](https://fontawesome.com/) - Used for the Like, Add, and Minus icons used in the site.

## Features

### Existing Features

#### User Authentication Features

The site features user authentication which allows users to:

- **Registration Page**

  - A user is able to register for an account on the website.

  - When the user registers their username there is a minimum length for the user of 3 characters and a regex which means the user can only user alphanumeric characters to create their username. If the user enters in a username that does not meet this requirement then a message appears and tells them that they can only use lowercase, uppercase or numbers.

    ![registration page preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596123808/Recipe_Workshop/registration_h9w59q.png)

  - The password requires a minimum length of 8 characters. If the user enters in a password that is too short then a message will inform them of the required password length.

  - When the user submits their registration form, the username and email address is checked against already registered users. If the username has been taken then it informs the user that they need to pick a unique username. If the email address has already been registered, then it asks the user to login instead.

  - Once the registration is complete, it redirects the user to their profile.

  - Their password is hashed and salted using the ``passlib`` library before being added to the database.

  - If a logged in user tried to access the registration page via the URL (as the navbar button for the registration page is not displayed), they are redirected to their profile page.

- **Registration Page**

  - A user is able to login to their account on the website.

  - Login to their account. When a user tries to sign into their account, their password is verified against the password held in the database using the ``passlib`` library for verifying the passwords. If either the password or email address is wrong then a message is flashed to the user which says that "Incorrect e-mail/password combination.". This has been done to add an extra layer of protection to a users account and not provide a potential hacker clues as to what could be wrong.

  - If a user who is logged in tries to access the login, it will automatically redirect them to their profile page.

  - Once signed in, the user gains access to more of the sites functionality such as adding & managing recipes and creating their own profile.

    ![Login Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596124983/Recipe_Workshop/login_mbxrrd.png)

- **Logout Feature**

  - A user is able to logout of their account by clicking the logout button in the navbar which will log them out by clearing the session cookie.

#### Landing Page

The landing page page consists of of multiple features that have been implemented:

- **Search Bar** - When a user views the landing page they are greeted by a hero image with a search bar on it that allows them to search for recipes by key word, ingredients, names, or course.

  ![landing page](https://res.cloudinary.com/andy-osborne/image/upload/v1596122829/Recipe_Workshop/landing%20page%20scroll.gif)

- **Top Rated Recipe** - The top rated recipe is below the search bar and is the second item the user sees on the page. This recipe changes based on the recipe with the most likes so it will constantly change according to user interaction on recipes. When the mouse hovers over the recipes picture it adds a zoom effect which slowly zooms into the image.

    ![featured recipe zoom](https://res.cloudinary.com/andy-osborne/image/upload/v1596121857/Recipe_Workshop/top-rated-recipe.gif)

- **Recent Recipes** - This area shows the 8 most recently added recipes that users have uploaded to the database with their image and their recipe name. On desktop, when the mouse hovers over the recipes picture it adds a zoom effect which slowly zooms into the image. The order that the recent recipes are displayed are based on the date and time they have been submitted.

    ![recently added section](https://res.cloudinary.com/andy-osborne/image/upload/v1596122022/Recipe_Workshop/recently-added.gif)

- **Newsletter Sign Up Banner** - At the bottom of the page there is a newsletter sign up form where the user can enter their email in to sign up for the mailing list.

  - If the user is logged in, their session username is included with their email so the banner will no longer show for them going forward.
  
  - If there is no user logged in, then it will show for repeat visits.
  
  - If the user then signs up to the site and re-enters their email it will add their username against the email in the database and no longer show for them.
  
  - After hitting submit, the form area disappears and is replaced by a confirmation text. When the mouse hovers over the "Join Now" button it changes colour to green which stands out against the banner.

    ![newsletter banner](https://res.cloudinary.com/andy-osborne/image/upload/v1596122499/Recipe_Workshop/newsletter.gif)

#### Navigation Bar

- The navigation bar sticks to the top of the page and scrolls down with the user as the explore the page.

- Conditional Statements have been used from Jinja templating to achieve the following:

  - If the user is on the landing page, the search bar does not show however this will show to the user if they are on any other page as the landing page contains a search bar for the user to use.

  - An active class is applied to the navigation links to highlight to the user what page they are on as that link will be shown in a different colour.

  - If there is no user logged in, the navigation bar will show the "Home", "Sign Up", and "Login" as well as the search bar when not on landing page.

  - If there is a user logged into session then the navigation bar will show "Home", "Add Recipe", "Profile" and "Logout" in addition to the search bar. Additionally, a check is done to see if the user is visiting their own profile or someone elses. If it is not their own profile then the active class is not applied to the profile link.

  - When a user hovers over the navigational links, they marginally increase in size to add an extra level of interactivity to help stimulate the users senses.

    ![Navbar Menu Options - Mobile Version](https://res.cloudinary.com/andy-osborne/image/upload/v1596123355/Recipe_Workshop/Navbar%20menu%20options%20-%20mobile.gif)

#### Profile

- When a user registers for an account on the site they get assigned a profile which is linked to their username.

- The account owner is able to add a blurb about themselves on their profile page and upload a profile picture which is sent through the Cloudinary API. This information is viewable to other users who look at that persons profile. If the user does not upload a profile picture or add a blurb about themselves then a default picture and blurb is used.

  - The profile image they upload gets validated to ensure it is an image and that the file size is below 2mb.

  ![update profile](https://res.cloudinary.com/andy-osborne/image/upload/v1596126291/Recipe_Workshop/update%20profile.gif)

- The account owner is able to change their account password and email from the account management modal. This is only viewable by the account owner and is only generated in the HTML code should the session user and user profile be the same. The default function of the form has been disabled in jQuery and sent through as an AJAX request to server which allows a flash message to confirm to the user on what has been done and the modal to stay open rather than the page refreshing and closing the modal.

- The profile page shows the recipes that have been created by the user and are interactive links so users can click on them to view those recipes.

- The use of conditional statements available from Jinja have been used as the "Welcome .." text at the top of the page changes to greet the user themselves if it's their profile or states "Welcome to the Profile of .." where .. is the profile owner.  

- In addition, the text used to show the recipes uses two conditional statements:
  
  - The first statement changes based on whether it is the owner or a visiter viewing the page. This will either show "My recipes" or "Their recipe creations". The decision to use "My" recipes is to make the user feel at home.

  - The second statement is when the user has not yet created any recipes and changes based on whether it is the owner or a visitor viewing the page. If it's the owner, the text asks them to submit a recipe and provides the link, otherwise placeholder text is shown to the visitor saying to check back soon.

- If someone tries to visit the profile of a user who does not exist then the page displays the following message:

  ![No Profile Exists](https://res.cloudinary.com/andy-osborne/image/upload/v1596127643/Recipe_Workshop/No_Profile_wxmf29.png)

#### Add Recipe

When a user is logged in they are able to access the "Add Recipe" page.

- Users are able to upload an image with their recipe which is uploaded to Cloudinary through their API in a similar fashion to the profile image. When a user uploads their image this is then verified by the jQuery functionality I built that checks:

  - If the file extension is an acceptable file - JPG, JPEG or PNG. If it is then it checks to see if the file size is below 2MB. Assuming all conditions are passed, then a message appears saying that a "Valid Image Uploaded".

  - If an invalid file type or too large of an image has been uploaded, then a message appears to the user and the submit button of the form is disabled until the image has been changed.

      ![Image Validator](https://res.cloudinary.com/andy-osborne/image/upload/v1596127057/Recipe_Workshop/Image%20validation.gif)

- As the amount of ingredients and steps required to make a recipe vary from recipe to recipe, I have included custom jQuery code that are linked to + or - buttons within the form and a message that informs them that they can press either to add or remove a row. This allows for a dynamic form that a user can interact with.

    ![Add or Remove Recipe/Step Input](https://res.cloudinary.com/andy-osborne/image/upload/v1596127278/Recipe_Workshop/dynamic%20fields.gif)

- There is a minimum and maximum character length in place for the recipe name and description. In addition to this, there is text below each field to let the user know when they are approaching the character limit which updates as the user inputs text. When the user reaches the maximum character limit, the text changes to red.

    ![Recipe Character Limit](https://res.cloudinary.com/andy-osborne/image/upload/v1595805606/Recipe_Workshop/Recipe%20character%20limit.gif)

- A pattern has been applied to both the Recipe Name, Steps and Ingredient field inputs.

  - For the Recipe Name, this has limited the text that user can enter to only uppercase and lowercase characters as well as only 1 space between words.

  - For the Steps and Ingredient field inputs a similar rule has been applied however a user can also brackets, commas, and hyphens.

  - To aid in accessibility, titles have been included on these fields to prompt the user what to look for should they break the pattern.

- If a user who is not logged in tries to access the add recipe page then it will redirect them to the login page.

#### Manage Recipe

If the user viewing a recipe is the recipe owner, the will see a button to manage the recipe which will allow them to update the recipe or delete it.

The information in the recipe is populated using the information from the database. The user is able to click on a button in the form to upload a new image.

- This will then unhide the image upload inputs for the form and add the required ``enctype`` to the form and ``required`` attribute to the input.
  
- When a new image has been chosen, it will be validated as per the initial image upload.

- The same patterns have been applied to the Recipe Name, Steps and Ingredient fields.

- If the user decides to cancel the image change then they can press the cancel button which will hide the input and remove the added attributes.

If the user decides they want to delete the recipe, they can press on the "Delete Recipe" button.

- This will launch a modal asking them if they are sure they want to delete the recipe.

- If the user presses "Confirm" then the recipe will be deleted, otherwise they can press cancel and the modal will close.

  ![Delete recipe Modal](https://res.cloudinary.com/andy-osborne/image/upload/v1596128661/Recipe_Workshop/delete%20recipe.gif)

The user is able to add and remove rows for the ingredients and recipe steps.

Once a user is happy with their changes, they can press the submit button to send their updates for the recipe.

If a user who is not the recipe owner tries to access this section to edit a recipe that is no theirs then they are redirected to the landing page.

#### View Recipe

Users are able to view the uploaded recipes by either searching for them or by clicking on a link for that recipe.

- The layout of the recipe page adapts based on the media device it is being viewed on.

  - On small screen to medium screen devices - Due to the small size of the screen I opted to use buttons to show/hide the recipe ingredients and steps. Each of these have their own button that the user can click on and adds an additional interactivity for the user.

    ![mobile recipe view](https://res.cloudinary.com/andy-osborne/image/upload/v1596128868/Recipe_Workshop/mobile%20recipe%20view.gif)  

  - On large screen and above devices - the steps and ingredients are shown at all times.

- At the bottom of the recipe page there is a button that a user can click to "like" the recipe. Only a user who is logged in can interact with the button otherwise if there is no user in session then the button is disabled and has a message asking that user to log in so they can like the recipe.

  - When a logged in user interacts with the button, an AJAX request is made which sends information to the server that includes the session username and increments the like on the recipe by 1. This is updated asynchronously within the page so it does not refresh as this could irritate a user. If the user has previously liked the recipe and presses the button again, then this is a treated as the user unliking the recipe and it removes their username from the liked_by field in the database and decreases the recipe likes by 1.

    ![like feature](https://res.cloudinary.com/andy-osborne/image/upload/v1595759426/Recipe_Workshop/like%20feature.gif)

  - When a user likes a recipe the icon changes to a filled in red heart and when a user unlikes the recipe, it returns to its default red outlined heart with no fill.

#### Search Functionality

The search functionality allows a user to search for various key terms based on the index created within the server. The index allows a full text search functionality and searches in the following fields:

- Recipe Name
- Ingredients
- Recipe Course (i.e. breakfast, brunch, lunch etc)
- Recipe Description
- Recipe Author

The results are then displayed according to its meta score, which is how closely the result matches the search term.

When the search results page has been generated for the user, the results are limited to 4 per page and uses ``pagination`` to allow the user to click through to view the results. In addition to this, in the top left corner of the search results page it shows the user how many results were found for their search term.

![Search page with pagination preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596129688/Recipe_Workshop/pagination.gif)

If no results are found, text is shown to the user saying no results were found - an example is given below:

![no results search query](https://res.cloudinary.com/andy-osborne/image/upload/v1595537460/Recipe_Workshop/noresults_rngdbl.png)

#### Privacy Policy

The site includes a privacy policy that was generated through a privacy policy generator however; as the site is for educational purposes only, the contact email address is a placeholder.

![404 Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596130378/Recipe_Workshop/Privacy_w2sw5w.png)

#### Advertise With Us

This site has an advertise with us page however it is a placeholder page for the moment.

![Advertise With Us Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596130246/Recipe_Workshop/Advertise_h4fnxz.png)

#### 404 Page

The site includes a custom 404 page that shows a message to the user when they try to go to a link/page that does not exist.

![404 Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596130121/Recipe_Workshop/404_e74agq.png)

#### 410 Page

The site includes a custom 410 page that shows a message to the user when they try to go to a link/page that does not exist.

![410 Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596138514/Recipe_Workshop/410_ir5giq.png)

#### 500 Page

The site includes a custom 500 page that shows a message to the user when there is an internal server error.

![500 Page Preview](https://res.cloudinary.com/andy-osborne/image/upload/v1596138515/Recipe_Workshop/500_fatljf.png)

### Features To Be Implemented

#### Admin Page

- I want to introduce an Admin section to the site that would allow the administrator to manage/delete recipes and users.

#### Additional User Login Functionality

- I want to include the functionality for a user to be able to reset their password if they forget it.

#### Profile Page Updates

- I want to include the functionality of allowing a user to update their profile description and image.

- I want to change the way the recipes are displayed on the user profile and instead of just having a link, I would like to show a thumbnail image and name of the recipe as this will be more visually appealing to the user.

- I want to show the recipes that a user has liked on their profile page.

#### Additional Search Functionality

- I want to have an option to allow a user to view all recipes in the database.

#### Recipe Page Additions

- I want to include the option for a user to be able to share recipes on their desired social media.

- I want to include the option for a user to print or email the recipe.

- I want to allow users to be able to click on a button and add all the recipe ingredients to a document so they can review them later on.

## Structure of Code

To assist in making the code modular and aiding in readability, I have broken the code used into separate folders and files as follows:

```markdown
.
┣ app
┃ ┣ static
┃ ┃ ┣ css
┃ ┃ ┃ ┗ style.css
┃ ┃ ┣ images
┃ ┃ ┃ ┣ favicons
┃ ┃ ┃ ┃ ┣ android-icon-36x36.png
┃ ┃ ┃ ┃ ┣ apple-icon-180x180.png
┃ ┃ ┃ ┃ ┣ apple-icon-60x60.png
┃ ┃ ┃ ┃ ┣ favicon-16x16.png
┃ ┃ ┃ ┃ ┗ favicon-32x32.png
┃ ┃ ┃ ┗ logo.png
┃ ┃ ┗ js
┃ ┃ ┃ ┣ file-validation.js
┃ ┃ ┃ ┣ form-validation.js
┃ ┃ ┃ ┣ main.js
┃ ┃ ┃ ┗ recipe-form.js
┃ ┣ templates
┃ ┃ ┣ 404.html
┃ ┃ ┣ 410.html
┃ ┃ ┣ 500.html
┃ ┃ ┣ advertise.html
┃ ┃ ┣ create_recipe.html
┃ ┃ ┣ index.html
┃ ┃ ┣ login.html
┃ ┃ ┣ manage_recipe.html
┃ ┃ ┣ privacy.html
┃ ┃ ┣ profile.html
┃ ┃ ┣ public_base.html
┃ ┃ ┣ recipe.html
┃ ┃ ┣ register.html
┃ ┃ ┗ search.html
┃ ┣ config.py
┃ ┣ errors.py
┃ ┣ footerviews.py
┃ ┣ helpers.py
┃ ┣ landing.py
┃ ┣ recipe.py
┃ ┣ search.py
┃ ┣ user.py
┃ ┗ ___init___.py
┣ env.py
┗ run.py
```

## Testing

### Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made.

- CSS - All styling was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure it was valid and no errors were made.

- jQuery - All my script was run through the [JSHint](https://jshint.com/) validator and no errors were found.

- Python - All code was run through [PEP8](http://pep8online.com/) and the [SolarLint](https://www.sonarlint.org/) plugin for VSCode was used. All code is PEP8 compliant.

### Manual Testing

You can view the testing done in the [test.md](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/testing.md) where I have written in-depth on the various tests I have performed.

## Deployment

I developed this project using [Visual Studio Code](https://code.visualstudio.com/). Version control was done using git and hosting the repository was done through GitHub.

The live version of this site is hosted using Heroku and I have opted to have the site automatically deployed directly from the master branch which allows the site to update automatically upon new commits to the master branch.

Please note that before proceeding, you will need the following installed on your machine:

- [PIP](https://pypi.org/project/pip/)
- [Python 3](https://www.python.org/)
- [GIT](https://git-scm.com/)
- Your chosen IDE, such as [Visual Studio Code](https://code.visualstudio.com/download)
As well as an account with the following providers - these are free accounts so no payment is required for the basic versions:

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Heroku](https://www.heroku.com/)
- [Cloudinary](https://cloudinary.com/)

### Step 1 - Run Locally

To run this project locally, you can follow these steps:

1. Go to the repository for [**Recipe Workshop**](https://github.com/Andy-Osborne/Recipe-Workshop).
2. Below the repository name, you will see a green button with the text **Code**.
3. Click on this button and a box will appear with further options. You can either click **Download zip** to and extract the zip file to your chosen folder or you can press on the button called **Clone with HTTPS**.
4. If you do press the button to clone, then this will clone URL for the Recipe Workshop repository.
5. In your local IDE, open **Git Bash**. Please check that **Git** has been installed in your IDE.
6. Change the **current** working directory to the location where you want the cloned directory to be made.
7. Type ``git clone`` and then paste in the URL you took from the **Clone with HTTPS** button.
    - An example of what the command would look like is below:

        ``git clone https://github.com/Andy-Osborne/Recipe-Workshop.git``

8. You can cut ties with the original GitHub repository by typing in:

    - ``git remote rm origin``

===

A virtual environment is recommended before proceeding. I personally used ``pipenv`` and will show you the steps to use this. For the following commands and going forward, the use of ``python -m`` before a terminal command may not be required on your particular machine.

===

1. The following command will install ``pipenv`` and allow you to create virtual environments.

    ```Python
    python -m pip install pipenv
    ```

2. The following command will install the latest version of Python into its own environment.

    ```Python
    python -m pipenv --three
    ```

3. To install packages you can use the following command:

    ```Python
    python -m pipenv install PACKAGE_NAME
    ```

4. To start your environment shell, you can use the following command:

    ```Python
    python -m pipenv shell
    ```

5. To install the required modules for Recipe Workshop, please do the following command:

    ```Python
    python -m pip -r requirements.txt
    ```

6. In your local IDE where you have the project for Recipe Workshop, you will need to create a file called ``env.py``. You can refer to this [env_sample.py](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/env_sample.py) on what you will need to input.

7. You will need to create your database with MongoDB. Please name it ``recipe_workshop`` and include three collections: ``newsletter``, ``recipe`` and ``users``. I have included example structures of these collections in json format which can be found in the [schemas folder](https://github.com/Andy-Osborne/Recipe-Workshop/tree/master/schemas).

8. Please setup your free account with Cloudinary as this is used to host the images that are uploaded by the users.

9. You are now ready to run the application from your IDE. Please run the following command:

    ```Python
    python run.py
    ```

10. You can access the local version of the website by going to ``http://127.0.0.1:5000``

### Step 2 - Deploying to Heroku

In order to deploy Recipe Workshop to Heroku, you will need to do the following once you have setup your account:

1. Create the ``requirements.txt`` if it is no longer in your local repository. This can be achieved by doing the following command in the terminal of your IDE:

    ```Python
    python -m pip freeze --local > requirements.txt
    ```

2. Create a new file in your repository named ``Procfile``. It is important that this file has a capital ``P`` or it will not work correctly. Once created, input the following text in the document:

    ```Python
    web: python run.py
    ```

3. You can now commit the newly created files to into your projects GitHub using the ``git add``,``git commit -m "Some message`` and finally ``git push``. Note: Change the commit message to suit your actual commit and whether it is the initial commit.

4. In your Heroku account, click on the ``New`` button in the top right hand side of the screen, followed by ``Create new app``. Choose a unique name for your website and the region you want it to be deployed in. Note: Some regions may charge so have a look at the available options.

5. Once your app has been created, you will be redirected to the ``Deploy`` section, if you have not been then just click on the ``Deploy`` tab. Choose your ``Deployment Method``, I recommend using the option to connect to your GitHub as you then have the option for ``Automatic Deployment`` going forward. You may need to give Heroku permission to connect to your GitHub profile.

6. You now need to setup the config variables for the site, this will use the information you inputted into your ``env.py``. Go to ``Settings`` then click on the button ``Reveal Config Vars``.

7. You can populate the ``config vars`` as follows (replacing the generic value with your information):

    |Key   | Value   |
    |:-:|:-:|
    | IP  |0.0.0.0 |
    | PORT  | 5000  |
    | CLOUDINARY_URL  | <cloudinary_url>   |
    | MONGO_DBNAME  | <database_name>  |
    | MONGO_URI  | ``mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority``   |
    | SECRET_KEY  | <your_secret_key>  |

    - If you get lost and are not sure where to find your your information for MongoDb, you can refer to their [getting started documentation](https://docs.atlas.mongodb.com/getting-started/).

    - You can obtain the cloudinary URL from the dashboard of your account just under ``Account Details`` after logging in.

8. Once done, you can now deploy the website back in the ``Deploy`` tab section.

9. You can now either deploy the website using the ``Enable Automatic Deploys`` option which will deploy a new version after each change in the connect GitHub repository or you can click on ``Deploy Branch`` under the ``Manual Deploy`` section. Note: Make sure that the branch selected is the ``master`` branch.

10. You have now successfully deployed a live version of this site.

## Credits

### Recipes and Recipe Images

All recipes and images uploaded by me were taken from [BBC Good Food](https://www.bbcgoodfood.com/).

### Site Images

The images used for the Login and Registration page, as well as the default profile picture were taken [Pexels](https://www.pexels.com/), which is a stock image library.

The logo used for the site was created by Becky Catlin.

### Privacy Policy Generator

I used [Privacy Policies](https://www.privacypolicies.com/) to generate a privacy policy for the website and styled the information and HTML given.

### Code Credits

1. The code for creating a custom template datetime filter was taken from [Rip Tutorial](https://riptutorial.com/flask/example/4779/format-datetime-in-a-jinja2-template) and edited to suit my needs.

2. The idea for including an ``env_sample.py`` so other developers who fork my code will know what they need to include in their ``env.py`` came from [Precious Ijege](https://github.com/precious-ijege).

3. The RegEx used within the pattern for recipe name and description inputs was taken from this post - [Stack Overflow](https://stackoverflow.com/a/35702586) and edited to suit my needs.

4. The code for the stick footer was taken from the post by [CSS-tricks](https://css-tricks.com/couple-takes-sticky-footer/).

5. The code for adding the correct prefixes was done using [Autoprefixer](https://autoprefixer.github.io/)

### Learning Resources

- Throughout my journey of creating this site, I was continuously learning and improving my knowledge and I used the following resources to achieve this:

- [Code Institute](https://codeinstitute.net/).

- [Codecademy](https://www.codecademy.com/).

- [Plurasight](https://www.pluralsight.com/).

- [w3schools](https://www.w3schools.com/).

- [Cloudinary Documentation](https://cloudinary.com/documentation/image_upload_api_reference) which allowed me to understand how I could use their API to upload and transform images.

- [Julian Nash](https://www.youtube.com/watch?v=BUmUV8YOzgM&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L) - The YouTube series by Julian helped me get a better understanding of Flask and gave me the idea on how I could structure my Flask application.

- [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) - Provided a lot of useful videos to help further improve my understanding of Flask.

- [Stack Overflow](https://stackoverflow.com/) - Really useful for general queries.

### Acknowledgements

A special thanks to:

- My Code Institute Mentor, [Precious Ijege](https://github.com/precious-ijege) for his support during the project.
- Code Institute Student, [Simon](https://github.com/jumboduck) for taking the time to review my site and providing feedback.

## Disclaimer

This site has been created entirely for **educational purposes** only and is not intended to be used in any other capacity.
