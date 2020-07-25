# Recipe-Workshop

[Recipe Workshop](http://recipeworkshop.herokuapp.com/) is an interactive and responsive website that allows users to create an account, browse recipes, upload and share their own cooking recipe creations.

The website has been built with CRUD functionality in mind and allows users access to Create recipes and accounts, Read recipes that have been uploaded, Update recipes and their account details, and Delete their recipes from the website.

I have created this website to cater to all users with an emphasis on those who are looking to either find a recipe to try out and bake or looking to share their latest creation with the world.

I have used HTML, CSS, [Bootstrap Framework](https://getbootstrap.com/), [jQuery](https://jquery.com/), Python, [Flask](https://palletsprojects.com/p/flask/), and [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to build this project. This forms part of my ongoing portfolio of work.

![Preview of Recipe Workshop](https://res.cloudinary.com/andy-osborne/image/upload/v1594915079/Recipe_Workshop/Responsive_glyerl.png)

## Demo

A live demo of the website is hosted through Heroku and can be found [here](http://recipeworkshop.herokuapp.com/).

## Table of Contents

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Technologies Used**](#technologies-used)

3. [**Features**](#features)
    - [**Existing Features**](#existing-features)

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

- **Navbar** - I decided to use ``#6EBDC7``(Glacier) I chose this colour as it really stood on the site as the psychology from blue can imprint on visitors that of quality, wisdom, productivity and calmness. Whilst there are negative sides to blue depending on the shade used with food-related websites, I feel the shade used avoids.

- **Navbar and Primary User Interaction Buttons** - I decided to use ``#EA9C76``(Dark Salmon) as this not only stood out well against either a White or Glacier Blue background, it also complimented those colours and stood out to the user.

- **Font Colour** - I decided to use the default colour for the fonts as this suited the simple approach of a recipe website and I felt it didn't need to change.

- **Link Colours**
    1) For the links when in hover state I used ``#EA9C76``(Dark Salmon) as mentioned before, this colour really stood out without being to garish and complimented the overall site colour scheme.

    2) For the profile link from a recipe page, I used ``#947232``(Buttered Rum) for the standard colour as I felt that it complimented the sites overall colour scheme and it didn't contrast too heavily compared to the black text to instantly make the user lose focus on what they were reading.

### Fonts

- [**Averia Serif Libre**](https://fonts.google.com/specimen/Averia+Serif+Libre) - I used this font for the site headers as it reminded me of the typography you would see in recipe books which aids in helping the user feel at "home" on this recipe website.

- [**PT Sans**](https://fonts.google.com/specimen/PT+Sans) - I used this font for the text within modals as it had a great quirky feel to it that complimented Spicy Rice.

### Wireframes

- The wireframes for the initial layout of the website were created using [whimsical](https://whimsical.com/) and you can view the wireframes for Recipe Workshop [here](https://github.com/Andy-Osborne/Recipe-Workshop/tree/master/wireframes).

- The wireframes include a design layout for Desktop, as well as portrait and landscape designs for Tablet and Mobile.

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

5. [Flask](https://palletsprojects.com/p/flask/) - The flask microframework was used to aid in the construction of the website and its built-in tools like Jinja templating.

6. [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - This was used to connect to the NoSQL database, MongoDB.

7. [Flask-Paginate](https://flask-paginate.readthedocs.io/en/master/) - This was used to paginate the search results.

8. [passlib.hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) - This was used for salting and hashing user passwords.

9. [MongoDB Atlas](https://www.mongodb.com/) - This was used as the NoSQL database that stores all user recipes, profiles, etc.

10. [Bootstrap Framework](https://getbootstrap.com/) - This was used to create the overall responsiveness of the website through the use of their flexible grid layout.

11. [Cloudinary](https://cloudinary.com/) - This was used to not only host the images used on the website but also allowed users to upload/delete their images through the use of their API.

12. [Google Fonts](https://fonts.google.com/) - I used Google Fonts to obtain the fonts used on the website which are "Averia Serif Libre" and "PT Sans".

13. [GitHub](https://github.com/) - I used to store my repository for the project and record all my commits.

14. [Heroku](https://www.heroku.com/) - I used Heroku to deploy the live version of my site.

15. [Autoprefixer](https://autoprefixer.github.io/) - I used this project to make sure all CSS prefixes were used where required to ensure cross-browser compatibility.

16. [Visual Studio Code](https://code.visualstudio.com/) - I used this to write the code for my site.

## Features

### Existing Features

#### User Authentication

The site features user authentication which allows users to:

- Register for an account.

- Sign into their account and gain access to more of the sites functionality such as adding & managing recipes and creating their own profile.

- Users are able to update their account password and email.

- All passwords are hashed and salted before being sent to the server.

#### Landing Page

The landing page page consists of of multiple features that have been implemented:

- Search Bar - When a user views the landing page they are greeted by a hero image with a search bar on it that allows them to search for recipes by key word, ingredients, names, or course.

- Top Rated Recipe - The top rated recipe is below the search bar and is the second item the user sees on the page. This recipe changes based on the recipe with the most likes so it will constantly change according to user interaction on recipes. When the mouse hovers over the recipes picture it adds a zoom effect which slowly zooms into the image.

- Recent Recipes - This area shows the 8 most recently added recipes that users have uploaded to the database with their image, recipe name and a short description. The description disappears on mobile views to ensure a better view experience for the user. On desktop, when the mouse hovers over the recipes picture it adds a zoom effect which slowly zooms into the image. The order that the recent recipes are displayed are based on the date and time they have been submitted.

- Newsletter Sign Up Banner - At the bottom of the page there is a newsletter sign up form where the user can enter their email in to sign up for the mailing list.

  - If the user is logged in, their session username is included with their email so the banner will no longer show for them going forward.
  
  - If there is no user logged in, then it will show for repeat visits.
  
  - If the user then signs up to the site and re-enters their email it will add their username against the email in the database and no longer show for them.
  
  - After hitting submit, the form area disappears and is replaced by a confirmation text. When the mouse hovers over the "Join Now" button it changes colour to green which stands out against the banner.

#### Navigation Bar

- The navigation bar sticks to the top of the page and scrolls down with the user as the explore the page.

- Conditional Statements have been used from Jinja templating to achieve the following:

  - If the user is on the landing page, the search bar does not show however this will show to the user if they are on any other page as the landing page contains a search bar for the user to use.

  - An active class is applied to the navigation links to highlight to the user what page they are on as that link will be shown in a different colour.

  - If there is no user logged in, the navigation bar will show the "Home", "Sign Up", and "Login" as well as the search bar when not on landing page.

  - If there is a user logged into session then the navigation bar will show "Home", "Add Recipe", "Profile" and "Logout" in addition to the search bar. Additionally, a check is done to see if the user is visiting their own profile or someone elses. If it is not their own profile then the active class is not applied to the profile link.

  - When a user hovers over the navigational links, they marginally increase in size to add an extra level of interactivity to help stimulate the users senses.

#### Profile

- When a user registers for an account on the site they get assigned a profile which is linked to their username.

- The account owner is able to add a blurb about themselves on their profile page and upload a profile picture which is sent through the Cloudinary API. This information is viewable to other users who look at that persons profile. If the user does not upload a profile picture or add a blurb about themselves then a default picture and blurb is used.

- The account owner is able to change their account password and email from the account management modal. This is only viewable by the account owner and is only generated in the HTML code should the session user and user profile be the same. The default function of the form has been disabled in jQuery and sent through as an AJAX request to server which allows a flash message to confirm to the user on what has been done and the modal to stay open rather than the page refreshing and closing the modal.

- The profile page shows the recipes that have been created by the user and are interactive links so users can click on them to view those recipes.

- The use of conditional statements available from Jinja have been used as the "Welcome .." text at the top of the page changes to greet the user themselves if it's their profile or states "Welcome to the Profile of .." where .. is the profile owner.  

- In addition, the text used to show the recipes uses two conditional statements:
  
  - The first statement changes based on whether it is the owner or a visiter viewing the page. This will either show "My recipes" or "Their recipe creations". The decision to use "My" recipes is to make the user feel at home.

  - The second statement is when the user has not yet created any recipes and changes based on whether it is the owner or a visitor viewing the page. If it's the owner, the text asks them to submit a recipe and provides the link, otherwise placeholder text is shown to the visitor saying to check back soon.

#### Add Recipe

When a user is logged in they are able to access the "Add Recipe" page.

- Users are able to upload an image with their recipe which is uploaded to Cloudinary through their API in a similar fashion to the profile image. When a user uploads their image this is then verified by the jQuery functionality I built that checks:

  - If the file extension is an acceptable file - JPG, JPEG or PNG. If it is then it checks to see if the file size is below 2MB. Assuming all conditions are passed, then a message appears saying that a "Valid Image Uploaded".

  - If an invalid file type or too large of an image has been uploaded, then a message appears to the user and the submit button of the form is disabled until the image has been changed.

      ![Image Validator](https://res.cloudinary.com/andy-osborne/image/upload/v1595539637/Recipe_Workshop/Image%20Validator.gif)

- As the amount of ingredients and steps required to make a recipe vary from recipe to recipe, I have included custom jQuery code that are linked to + or - buttons within the form and a message that informs them that they can press either to add or remove a row. This allows for a dynamic form that a user can interact with.

#### Manage Recipe

If the user viewing a recipe is the recipe owner, the will see a button to manage the recipe which will allow them to update the recipe or delete it.

The information in the recipe is populated using the information from the database. The user is able to click on a button in the form to upload a new image.

- This will then unhide the image upload inputs for the form and add the required ``enctype`` to the form and ``required`` attribute to the input.
  
- When a new image has been chosen, it will be validated as per the initial image upload.

- If the user decides to cancel the image change then they can press the cancel button which will hide the input and remove the added attributes.

If the user decides they want to delete the recipe, they can press on the "Delete Recipe" button.

- This will launch a modal asking them if they are sure they want to delete the recipe.

- If the user presses "Confirm" then the recipe will be deleted, otherwise they can press cancel and the modal will close.

The user is able to add and remove rows for the ingredients and recipe steps.

Once a user is happy with their changes, they can press the submit button to send their updates for the recipe.

#### View Recipe

Users are able to view the uploaded recipes by either searching for them or by clicking on a link for that recipe.

- The layout of the recipe page adapts based on the media device it is being viewed on.

  - On small screen to medium screen devices - Due to the small size of the screen I opted to use buttons to show/hide the recipe ingredients and steps. Each of these have their own button that the user can click on and adds an additional interactivity for the user.

    ![no results search query](https://res.cloudinary.com/andy-osborne/image/upload/v1595538056/Recipe_Workshop/My_Video-min-min_t0x5mm.gif)  

  - On large screen and above devices - the steps and ingredients are shown at all times.

- At the bottom of the recipe page there is a button that a user can click to "like" the recipe. Only a user who is logged in can interact with the button otherwise if there is no user in session then the button is disabled and has a message asking that user to log in so they can like the recipe.

  - When a logged in user interacts with the button, an AJAX request is made which sends information to the server that includes the session username and increments the like on the recipe by 1. This is updated asynchronously within the page so it does not refresh as this could irritate a user. If the user has previously liked the recipe and presses the button again, then this is a treated as the user unliking the recipe and it removes their username from the liked_by field in the database and decreases the recipe likes by 1.

  - When a user likes a recipe the icon changes to a filled in red heart and when a user unlikes the recipe, it returns to its default red outlined heart with no fill.

#### Search Functionality

The search functionality allows a user to search for various key terms based on the index created within the server. The index allows a full text search functionality and searches in the following fields:

- Recipe Name
- Ingredients
- Recipe Course (i.e. breakfast, brunch, lunch etc)
- Recipe Description
- Recipe Author

The results are then displayed according to its meta score, which is how closely the result matches the search term.

When the search results page has been generated for the user, the results are limited to 4 per page and uses pagination to allow the user to click through to view the results. In addition to this, in the top left corner of the search results page it shows the user how many results were found for their search term.

If no results are found, text is shown to the user saying no results were found - an example is given below:

![no results search query](https://res.cloudinary.com/andy-osborne/image/upload/v1595537460/Recipe_Workshop/noresults_rngdbl.png)

#### Privacy Policy

The site includes a privacy policy that was generated through a privacy policy generator however; as the site is for educational purposes only, the contact email address is a placeholder.

#### 404 Page

The site includes a custom 404 page that shows a message to the user when they try to go to a link/page that does not exist.

### Features To Be Implemented

#### Admin Page

- I want to introduce an Admin section to the site that would allow the administrator to manage/delete recipes and users.

#### Additional User Login Functionaliy

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

## Testing

### Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made.

- CSS - All styling was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure it was valid and no errors were made.

- jQuery - All my script was run through the [JSHint](https://jshint.com/) validator and no errors were found.

- Python - All code was run through [PEP8](http://pep8online.com/) and the [SolarLint](https://www.sonarlint.org/) plugin for VSCode was used. One issue is outstanding which is a ternary conditional statement being 85 characters long rather than 79 characters.

## Credits

### Recipes & Recipe Images

All recipes and images uploaded by me were taken from [BBC Good Food](https://www.bbcgoodfood.com/).

### Site Images

The images used for the Login and Registration page, as well as the default profile picture were taken [Pexels](https://www.pexels.com/), which is a stock image library.

### Privacy Policy Generator

I used [Privacy Policies](https://www.privacypolicies.com/) to generate a privacy policy for the website and styled the information and HTML given.

### Code Credits

1. The code for creating a custom template datetime filter was taken from [Rip Tutorial](https://riptutorial.com/flask/example/4779/format-datetime-in-a-jinja2-template) and edited to suit my needs.

2. The idea for including an ``env_sample.py`` so other developers who fork my code will know what they need to include in their ``env.py`` came from [Precious Ijege](https://github.com/precious-ijege).

### Acknowledgements

A special thanks to:

- My Code Institute Mentor, [Precious Ijege](https://github.com/precious-ijege) for his support during the project.
- Code Institute Student, [Simon](https://github.com/jumboduck) for taking the time to review my site and providing feedback.

### Learning Resources

- Throughout my journey of creating this site, I was continuously learning and improving my knowledge and I used the following resources to achieve this:

- [Code Institute](https://codeinstitute.net/).

- [Codecademy](https://www.codecademy.com/).

- [Plurasight](https://www.pluralsight.com/).

- [w3schools](https://www.w3schools.com/).

- [Cloudinary Documentation](https://cloudinary.com/documentation/image_upload_api_reference) which allowed me to understand how I could use their API to upload and transform images.

## Disclaimer

This site has been created entirely for **educational purposes** only and is not intended to be used in any other capacity.
