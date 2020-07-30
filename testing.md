# Recipe Workshop Testing

All code used for Recipe Workshop was extensively tested through manual process during every stage of development to ensure that it works as intended and any bugs found were fixed. The responsive design of the website was tested on various devices and browsers.

## Table of Contents

1. [**Code Validation**](#code-validation)

2. [**Testing Against User Stories**](#testing-against-user-stories)

3. [**Manual Testing**](#manual-testing)
    - [**Responsive Design Testing**](#responsive-design-testing)
        - [**Overview**](#overview)
            - [**Navbar**](#navbar)
            - [**Landing Page**](#landing-page)
            - [**Search Results Page**](#search-results-page)
            - [**Recipe Page**](#recipe-page)
            - [**Registration Page**](#registration-page)
            - [**Login Page**](#login-page)
            - [**Profile Page**](#profile-page)
            - [**Add Recipe Page**](#add-recipe-page)
            - [**Manage Recipe Page**](#manage-recipe-page)
            - [**Privacy Policy Page**](#privacy-policy-page)
            - [**404 Page**](#404-page)
            - [**Advertise With Us Page**](#advertise-with-us-page)

    - [**Functionality Testing**](#functionality-testing)

        - [**Base Template**](#base-template)
            - [**Breakdown of Jinja Functionality in Base Template**](#breakdown-of-jinja-functionality-in-base-template)
            - [**Breakdown of jQuery Functionality in Base Template**](#breakdown-of-jquery-functionality-in-base-template)
            - [**Base Template - Breakdown of Views Used**](#base-template---breakdown-of-views-used)

        - [**Landing Page Template**](#landing-page-template)
            - [**Breakdown of Jinja Functionality in Landing Page Template**](#breakdown-of-jinja-functionality-in-landing-page-template)
            - [**Breakdown of jQuery Functionality in Landing Page Template**](#breakdown-of-jquery-functionality-in-landing-page-template)
            - [**Landing Page Template - Breakdown of Views Used**](#landing-page---breakdown-of-views-used)

        - [**Register Page Template**](#register-page-template)
            - [**Breakdown of Jinja Functionality in Register Page Template**](#breakdown-of-jinja-functionality-in-register-page-template)
            - [**Register Page Template - Breakdown of Views Used**](#register-page---breakdown-of-views-used)

        - [**Login Page Template**](#login-page-template)
            - [**Breakdown of Jinja Functionality in Login Page Template**](#breakdown-of-jinja-functionality-in-login-page-template)
            - [**Login Page Template - Breakdown of Views Used**](#login-page---breakdown-of-views-used)

        - [**Logout Functionality**](#logout-functionality)
            - [**Logout Functionality- Breakdown of Views Used**](#logout-functionality---breakdown-of-views-used)

        - [**Profile Page Template**](#profile-page-template)
            - [**Breakdown of Jinja Functionality in Profile Page Template**](#breakdown-of-jinja-functionality-in-profile-page-template)
            - [**Breakdown of jQuery Functionality in Profile Page Template**](#breakdown-of-jquery-functionality-in-profile-page-template)
            - [**Profile Page Template - Breakdown of Views Used**](#profile-page---breakdown-of-views-used)

        - [**Search Page Template**](#search-page-template)
            - [**Breakdown of Jinja Functionality in Search Page Template**](#breakdown-of-jinja-functionality-in-search-page-template)
            - [**Search Page Template - Breakdown of Views Used**](#search-page---breakdown-of-views-used)

        - [**Recipe Page Template**](#recipe-page-template)
            - [**Breakdown of Jinja Functionality in Recipe Page Template**](#breakdown-of-jinja-functionality-in-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Recipe Page Template**](#breakdown-of-jquery-functionality-in-recipe-page-template)
            - [**Recipe Page Template - Breakdown of Views Used**](#recipe-page---breakdown-of-views-used)

        - [**Add Recipe Page Template**](#add-recipe-page-template)
            - [**Breakdown of Jinja Functionality in Add Recipe Page Template**](#breakdown-of-jinja-functionality-in-add-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Add Recipe Page Template**](#breakdown-of-jquery-functionality-in-add-recipe-page-template)
            - [**Add Recipe Page Template - Breakdown of Views Used**](#add-recipe-page---breakdown-of-views-used)

        - [**Manage Recipe Page Template**](#manage-recipe-page-template)
            - [**Breakdown of Jinja Functionality in Manage Recipe Page Template**](#breakdown-of-jinja-functionality-in-manage-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Manage Recipe Page Template**](#breakdown-of-jquery-functionality-in-manage-recipe-page-template)
            - [**Manage Recipe Page Template - Breakdown of Views Used**](#manage-recipe-page---breakdown-of-views-used)

        - [**Privacy Page Template**](#privacy-page-template)
            - [**Privacy Page Page Template - Breakdown of Views Used**](#privacy-policy-page---breakdown-of-views-used)

        - [**Advertise Page Template**](#advertise-page-template)
            - [**Advertise Page Page Template - Breakdown of Views Used**](#advertise-policy-page---breakdown-of-views-used)

        - [**404 Page Template**](#404-page-template)

        - [**404 Page Template**](#410-page-template)

        - [**404 Page Template**](#500-page-template)

        - [**Helper Functions**](#helper-functions)
            - [**Image Upload**](#image-upload)
            - [**No Change In Account Information**](#no-change-in-account-information)
            - [**New Password Checker**](#new-password-checker)
            - [**Email Updater**](#email-updater)
            - [**Password Updater**](#password-updater)
            - [**Recipe Steps**](#recipe-steps)
            - [**Recipe Ingredients**](#recipe-ingredients)

## Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made. I used the [Web Developer](https://chrispederick.com/work/web-developer/) plugin for the chrome browser to pass the local HTML into the W3C validator on every page of the website.

- CSS - All styling was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure it was valid and no errors were made.

- jQuery - All my script was run through the [JSHint](https://jshint.com/) validator and no errors were found.

- Python - All code was run through [PEP8](http://pep8online.com/) and the [SolarLint](https://www.sonarlint.org/) plugin for VSCode was used. All code is PEP8 compliant.

## Testing Against User Stories

The below goes through of of the user stores listed in the UX section of the [README.md](https://github.com/Andy-Osborne/Recipe-Workshop/blob/master/README.md).

**As a user, I want:**

1. I want the landing page of the website to be visually appealing to me as this sets my expectation for the rest of the website.

    - The landing page of the website uses soft colours that compliment each other to make the user feel at home.
    - There are various pictures of food such as the search banner and the recipe images that are uploaded by users to help reinforce to the user that the site is about food and sharing recipes.
    - The user is not bombarded by blocks of text and images but has enough white space to help them focus on the main elements of the website as they scroll through the landing page.
    - The interactivity of the landing page helps the user understand immediately what they can interact with - such as expanding navbar buttons, images that zoom in as the cursor scrolls over it, and buttons/links that change colour on hover.

2. I want to be able to see the most liked recipe on the landing page of the website so I am able to try this recipe out for myself.

    - This user story has been achieved by having the most liked recipe (displayed as Top Rated Recipe on the website) appear on the front page which dynamically changes according to the recipe with the most likes.

    - This recipe is larger than the recently added recipes and does not have any other image to either side of it so it immediately draws the users focus.

3. I want to be able to see recently added recipes on the landing page as these can give me inspiration of what I can search for, or even try them out myself.

    - This has been achieved by displaying the 8 most recent recipes added to the database.

    - To ensure the most recent recipes are displayed, the user of ``datetime.now()`` has been used when the recipe is submitted to the database. Before displaying on the landing page, the results from the recipe collection are sorted by the "submitted field".

        ```Python
        recent_recipes = recipe.find().sort("submitted", -1).limit(8)
        ```

4. I want to be able to navigate myself around the site with ease and with as little guidance as necessary.

    - This has been achieved by clearly labeling all buttons and links that a user can interact with in addition to this, when a user hovers over a link or button it will either increase in size on mouse hover or it will change colour.

    - When recipes are displayed, for instance in a search result or on the landing page, the entire image and text area are links.

    - When the user is on certain pages such as the landing page, their profile page, the login or registration page, or add recipe page then the corresponding link in the navbar is assigned the active class to make it a different colour and stand out to the user.

5. I want the website to be responsive and adjust accordingly to the screen I am viewing it on.

    - This has been achieved through the use of relative measurements when designing each section of the website so that they can adjust according to the size of the media device the user is using.

    - In addition to this, Media Queries have been used to ensure that the website responds and displays as intended on the main types of devices a user might use.

6. I want to be able to view and search for recipes that have been uploaded to the website.

    - This has been achieved by showing the recent recipes on the landing page in addition to this, the user is able to search for recipes using the search bar functionality.

    - A feature that will be implemented at a later date will allow a user to search for all recipes uploaded.

7. I want to be able to search for different recipes whether it is by name, ingredient or dish type.

    - A user is able to use the search functionality which uses the search term and returns recipes that resemble that term.

8. I want to be able to rate the recipes that I have tried so others know that the recipe is good and to share my appreciation with the author.

    - This has been achieved by allowing a user who has logged into their account to rate a recipe when they view it. If there is no user logged in, it has a message below it asking them to log in so they can rate the recipe.

    - The use of AJAX functionality has been implemented to allow a use to interact with the like button which will asynchronously update the number of likes count and change the favicon used for the like button to stimulate the users senses.

    - When a user clicks on the like button for the first time, it increments the like count by 1 and changes the favicon to a filled in red heart. If they click it again then it decrements the count by 1 and changes the favicon to a blank heart with a red outline.

9. I want to be able to create an account on the website which will allow me to edit recipes that I have created.

    - This has been achieved through the use of user authentication and allows a user to register and login to the website. Once the user logged in they have access to a wider range of option such as creating and managing their recipes.

10. I want to ensure that when I create an account, my password is only known to me and cannot be seen by the website admin.

    - This has been achieved through the use of passlib.hash. This salts and hashes the users password before it is stored in the database so no-one but the user will know the password.

11. I want to be able to update my password or email address.

    - This has been achieved through the creation of the Account Management Modal within the users profile section. Only the profile owner is able to see this button and it allows them to change their email and/or password.

    - The use of AJAX functionality has been used so that when the user submits their changes, the modal remains open and the request is done asynchronously to allow the response message to be displayed to the user.

    - When a user submits any changes to their account information, this is validated on the backend a message is returned to display to the user to let them know whether the information has been updated or if it has not been updated due to either:

        - The information submitted is the same as the information already stored in the database so no change has been made.
        - The incorrect account password has been entered.
        - The new passwords do not match.

12. I want to be able to upload my own recipes for other users to try.

    - This has been achieved by allowing a user who is logged into their account on the website can add a new recipe.

13. I want to be able to upload a picture for my recipe.

    - This has been achieved through the use of the Cloudinary API. It allows a user to upload an image with their recipe which is stored with the image hosting service Cloudinary. When the image is uploaded, it provides a URL for the image which is stored with the recipe.

14. I want to be able to manage my recipe, or even delete it from the website.

    - This has been achieved by adding the field recipe_author to the recipe document and through the use of conditional statements within the recipe page.

    - If the session use is the same as the recipe_author, then an option is shown to the user to allow them to edit the recipe. Once the user clicks on this, they are taken to the edit recipe page where the recipe information is pre-populated for them using the recipe information previously submitted.

    - On the manage recipe page, the user is able to delete the recipe by pressing on the "Delete Recipe" button. If the user clicks it then a modal is launched to ask the user if they are sure they want to delete the recipe? This has been added to ensure recipes are not accidentally deleted.

    - When a user deletes their recipe, the image from Cloudinary is also deleted.

15. I want to be able to create a profile page and upload an image of myself and an introduction for other users to see when they view my recipes.

    - This has been achieved as when a user registers for the site, their registered username is used to create their profile.

    - When the user updates their profile information to include a short description and profile picture, the information is stored in their user document within the database and the profile image is stored in Cloudinary.

    - If the user does not update their profile information then a default profile description and image is used.

## Manual Testing

I have detailed the manual testing undertaken during the development stage to ensure that all aspects of the game work as intended.

### Responsive Design Testing

During every stage of development, I used a variety of tools to test out the layout of the website to ensure that it remained responsive at various screen sizes, that the website retained the correct look, and all elements were displayed correctly and readable by the user.

For testing the various media screen sizes, I used the built-in options that were available through the Chrome browser as well using the [Responsive Test Tool Website](http://responsivetesttool.com/) as this gave access to a wider range of screen and device sizes.

All tests were performed on the following browsers:

- Google Chrome
- Opera
- Microsoft Edge
- Mozilla Firefox
- Safari

All testing was performed at the following screen sizes:

- Mobile Phones/ Small Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Nexus 7, iPod Touch, Galaxy Note 3, Nexus 6P, LG G5
  - Physical Devices - iPhone X and Samsung S9

- Tablet Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Samsung Galaxy Tab 2, iPad Pro 9.7, iPad Pro 9.7, iPad mini, HTC Nexus 9
  - Physical Devices - iPad Air

- Laptop/Desktop Devices (Portrait and Landscape).
  - Emulated Screen Sizes - 1024 x 600, 1280 x 800, 1366 x 768, 1440 x 900, 1680 x 1050, 1920 x 1080
  - Physical Devices - 18" Laptop, 22" Monitor, 14" laptop

Each test was performed using the following table:

| Action                |No User Logged In   |User Logged In    |
|---|---|---|
|Landing Page           |Result - Any issues|Result - Any issues|
|Search Results Page    |Result - Any issues|Result - Any issues|
|Recipe Page            |Result - Any issues|Result - Any issues|
|Register Page          |Result - Any issues|Result - Any issues|
|Log In Page            |Result - Any issues|Result - Any issues|
|Profile Page - Own     |Result - Any issues|N/A                |
|Profile Page - Other   |Result - Any issues|N/A                |
|Add Recipe             |Result - Any issues|Result - Any issues|
|Manage Recipe          |Result - Any issues|Result - Any issues|
|Privacy Policy         |Result - Any issues|Result - Any issues|

#### Overview

This website was intended to be responsive across all media devices such as mobile phones, tablets and desktops/laptops as the primary purpose of the website is to enable users to view and create recipes that others can see and users will want to be able to take their chosen media device with them to their kitchen.

To ensure the website and content remains responsive, I tested the layout at every stage of development on the various screen sizes and devices listed in the previous section. If the content did not display as intended, I corrected the styling of the elements and added Media Queries so that the design will adjust to device being viewed.

The overall site was designed using the Bootstrap Framework to make use of their flex layout. In addition to this I used relative measurements in my styling where possible, rather than absolute measurements to allow the elements to adapt to screen size changes before a new media query would need to be introduced.

![Responsive Testing Summary Table](https://res.cloudinary.com/andy-osborne/image/upload/v1595945531/Recipe_Workshop/Responsive_Testing_n0u6x8.png)

##### Navbar

- I tested to ensure that the Navbar is correctly displayed at all times and the buttons within it responded and acted as intended.

  - **Bug Identified** - Navbar Covered Top of Each Pages Content

    - As the Navbar is fixed to the top of the page, this caused an issue where content was covered by it.

  - **Fix Applied**:

    - To give the page content some breathing room, I added ``padding-top: 80px;`` to the ``.content`` class which resolved the issue.

##### Landing Page

- I tested that all writing, buttons and images on the landing page remained readable by the user and it adapted accordingly to the device it was being viewed on.

- Where the responsiveness of the website began to degrade, I created a media query to deal with any issues.

- In order to ensure that the site retained cross-browser responsiveness, I used the online CSS [Autoprefixer](https://autoprefixer.github.io/).

  - **Bug Identified** - Search Bar Aligned to Left of Screen

    - At certain media sizes, the search bar aligned itself to the left of the search div which was unintended

  - **Fix Applied**:

    - In order to correct this issue I used the bootstrap class of ``justify-content-center``

##### Search Results Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- No issues were discovered.

##### Recipe Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

  - **Bug Identified** - Recipe Image Displayed Incorrectly on iPhone X

    - When viewing the recipe page through the emulator the recipe page behaved and looked as expected however; when viewing the page on an actual iPhone X the recipe image became distorted and squished. After researching the issue, I discovered that it is a known bug on how Safari stretches images.

  - **Fix Applied**:

    - To fix this issue, I applied ``height: 100% !important;`` to the ``.recipe-image`` class which fixed the issue and the image displayed as expected.

##### Registration Page

- I tested to ensure that the registration form, flash messages and background image are displayed correctly to the user and that they kept a consistent flow between different media devices.

- After testing the registration page, a decision was made to remove the background image on smaller screen sizes as the user could either see a small portion of the image or none at all in order to provide a better user experience.

##### Login Page

- I tested to ensure that the login form, flash messages and background image are displayed correctly to the user and that they kept a consistent flow between different media devices.

- The background image was removed on the same screen sizes as the registration page to ensure a consistent flow between the two pages.

- No bugs were discovered.

##### Profile Page

- I tested to ensure that the buttons, profile image, profile text and recipe results are displayed correctly to the user and that they kept a consistent flow between different media devices.

- I tested to ensure that the modal used for Account Management displayed correctly to the user and that the validation messages were clear.

- No issues were discovered.

##### Add Recipe Page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages remained clear to the user at all times.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- No issues were discovered.

##### Manage Recipe Page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages remained clear to the user at all times.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested to ensure that the modal used for confirming the deletion of the recipe displayed correctly to the user and appeared correctly on all media screen sizes.

- No issues were discovered.

##### Privacy Policy Page

- I tested to ensure that the text  content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

##### 404 Page

- I tested to ensure that the text content and image displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

#### Advertise With Us Page

- I tested to ensure that the text content and image displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

### Functionality Testing

At all instances within the below testing summaries, I ensured that the correct information was displayed within the jinja ``{% block TAG_NAME %}`` tags.

#### Base Template

I performed various tests to ensure that the conditional statements used within the base template are working as intended.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Base Template

- Conditional Navbar Options:

  - Within the base template, there are three conditional statements used to show a user various options:

    - A user who is not logged in should only be able to see the additional options for ``Register`` and ``Login``.

      - I tested that this conditional statement works by logging out of a user account and verifying that the options presented in the navbar are correct.

      - In addition, I logged into an account and tested that a signed in user will not see the options for registering and logging into an account.

      - No issues were found with this functionality.

    - A user who is logged in should be able to see the additional options for ``Add Recipe``, ``Profile`` and ``Logout``.

      - I tested that this conditional statement works as intended by logging into an account and verifying that the options shown are as expected.

      - In addition, I logged out of the account to clear the user session and verified that these options are not shown to a user who is not logged into an account.

      - No issues were found with this functionality.

    - The search option should not be shown to a user when they are on the landing page.

      - I tested this by navigating to the landing page and checking to see if the search bar is shown in the Navbar. The search bar did not appear as the expected.

      - I tested that the search bar will show in the Navbar when the user is on any other page other than the landing page.

      - These tests were performed as a user who is logged into an account and a user who is not logged into an account to ensure there is consistency in the expected results.

      - No issues were found with this functionality.

- Conditional ``active-page`` Class:

  - Within the base template navbar links, there are conditional statements in each of the links classes. This essentially assigns the ``active-page`` class to a link if that is the page that the user is on.

  - I manually tested that this works as intended on every page of the website.

  - Note: The active class does not get applied to the profile link when a user is visiting someone elses profile. This is an intended design choice and not a bug.

  - No bugs were discovered with this functionality.

- Search Bar Functionality

  - I manually tested that the search bar functionality works as intended.

  - No bugs were discovered with this functionality.

##### Breakdown of jQuery Functionality in Base Template

- Adding and Remove ``.btn-zoom``:

  - I verified that the jQuery functionality of adding and removing the ``.btn-zoom`` to navbar menu buttons when the mouse hovers over it and removes it once the mouse leaves.

  - No issues were discovered with this functionality.

##### Base Template - Breakdown of Views Used

**Associated View - Route: ``/search`` Function: ``get_search()``**

Breakdown of ``get_search()`` functionality:

- This takes the input from the search form and then redirects the user to the search results page view by passing in the forms input value as a variable argument:

    ```Python
    search_term=request.form.get("search_field")
    ```

- No issues were discovered with the functionality of this view

#### Landing Page Template

I performed various tests to ensure that the conditional statements used within the index.html template are working as intended and that all associated ``views`` and ``jQuery`` functionalities work.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Landing Page Template

- Highest Rated Recipe:

  - I verified that the information displayed under the ``Top Rated Recipe`` and the information inputted through the use of ``for`` loop is that of the recipe which has received the most likes.

  - This was done by manually changing the rating of a recipe to allow me to know which recipe details should be displayed.

  - No issues were discovered.

- Most Recent Recipes:

  - I verified that the information displayed under the ``Most Recent Recipes`` and their respective Recipe Names and images are recorded against the correct item.

  - This was done by manually checking each recipe individually to ensure that the right name was against the right picture and that when clicking on one of these recipes that it redirected the user to the right recipe.

  - No issues were discovered.

- Newsletter Banner:

  - The newsletter banner section uses three conditional statements that checks:
  
    - If there is no user in session, then it displays the newsletter banner.

    - If there is a user in session but it's not in the ``signups`` variable that gets passed through from the view then it shows the newsletter banner.

    - If the session username is in the ``signups`` variable then it does not show the banner.

  - I manually checked each conditional statement by doing the following:

    - I tested the first condition by visiting the landing page and not being signed into an account. The newsletter banner was visible. I then inputted an email and submitted the form and moved to a different page and back again to see if the banner still showed.

      - No issues were discovered under this condition as the banner remained visible as no user was in session.

    - I tested the second and third condition by logging in and visiting the landing page as this meant a user was now in session. The newsletter banner was visible. I then inputted an email and submitted the form and moved to a different page and back again to see if the banner still showed.

      - No issues were discovered under this condition as the banner was visible on first visit and then no longer visible on subsequent visits.

##### Breakdown of jQuery Functionality in Landing Page Template

- Newsletter AJAX Function:

  - I verified that when a user enters their email and presses the submit button that the following happens:

    - The form is validated first to ensure it meets requirements setout in the HTML form type - i.e. it must be an email that matches the designated pattern. If the form is validated, then it can proceed to the next step otherwise the standard HTML validation message is shown.

    - The form request is received by the backend and processed.

    - The banner title div and newsletter form is hidden.

    - A response message is displayed to the user.

  - No issues were discovered with the functionality of sending the information to the backend & server however; an unintended bug was discovered before the message could be shown.

  - **Bug Identified** - Page Refreshes on submit

    - When the user submits the form, the default function of the form is to refresh the page which prevents the user from seeing the response message.

  - **Fix Applied**:

    - In order to correct this issue I used ``event.preventDefault();`` to stop the default function of the form and allow the message to be shown to the user.

- Adding and Remove ``.image-zoom-class``:

  - I verified that the jQuery functionality of adding and removing the ``.image-zoom-class`` to recent images on the landing page worked as intended.

  - This was done by moving the over each image to ensure that it zooms in and once the mouse leaves the image, the class is removed so the image reverts back to its default position.

  - No issues were discovered with this functionality.

##### Landing Page - Breakdown of Views Used

**Associated View - Route: ``/`` Function: ``index()``**

Breakdown of ``index()`` functionality:

- Highest Rated Recipe Query:
  
  - I verified that this function works as intended and gets the recipe from the recipe collection that has the most amount of likes by liking various recipes to ensure that 1 recipe had more likes than another recipe. The results of this query is assigned to a Jinja variable and passed into the template as a ``list``.

- Recent Recipes Query:

  - I verified that the 8 most recently added recipes to the recipe collection are displayed to users on the landing page and are shown in descending order which starts with the most recently added recipe. The results of this query is assigned to a Jinja variable and passed into the template as a ``list``.

  - **Bug Discovered** - Recipes Not shown in Order

    - This function was displaying the 8 recently added recipes however; if more than 8 recipes were added on the same day then the results shown were not correct as to the 8 **most** recently added recipes.

  - **Fix Applied**

    - This bug was caused by using ``datetime.date`` within the recipe submission field as it was very general. The fix applied was to use ``datetime.now()`` so the date entered against the recipe was much more specific and allowed the correct sorting and retrieving of the most recently added recipes.

- Newsletter Sign Up Query:

  - I verified that the newsletter query and conditional statement worked as intended and successful checks to see where the session user has previously signed up for the newsletter.

    - **Bug Discovered** - NoneType Error Returned

      - An error was raised when searching the newsletter collection for either a username that was not in the collection or when there was no user logged into session as this meant that there was no username.

    - **Fix Applied**

      - In order to fix this bug, I created the below conditional statement that first checks to see if there is a username in session and if there is a username then it will run a check in the newsletter collection. If the value of ``newsletter_check`` is ``None`` then it assigns the variable ``signups`` and empty string, else if there is a value in ``newsletter_check`` variable then that username is assigned to the ``signups`` variable. The value of this  variable is then passed into the Jinja template.

      ```Python
          if "username" in session:
            newsletter_check = newsletter.find_one({
              "username": session["username"]})

          if newsletter_check is None:
              signups = ""
          else:
              signups = session["username"]
        ```

**Associated View - Route: ``/search`` Function: ``get_search()``**

- Breakdown of ``get_search()`` functionality:

  - This takes the input from the search form and then redirects the user to the search results page view by passing in the forms input value as a variable argument:

    ```Python
    search_term=request.form.get("search_field")
    ```

- No issues were discovered with the functionality of this view

**Associated View - Route: ``/newsletter`` Function: ``newsletter_register()``**

- Breakdown of ``newsletter_register()`` functionality:

  - This view processes the form information sent by the AJAX function:

    - It saves the email address associated with form and saves it to variable ``email``.

    - It queries the newsletter collection to see if this email address exists.

    - It uses the variable ``username`` and runs a conditional check to see if there is a user in session. If there is a user in session then it saves the username in this variable, otherwise an empty string is saved.

    - A conditional statement is then run based on whether the email already exists in the database collection and the appropriate message is then sent back to the AJAX functionality and displayed to the user.

      - I validated that this functionality works as intended and the correct message is shown to the user in the following scenarios:

        - A user who is not logged in and has not signed up before.

        - A user who is not logged in and has signed up before.

        - A user who is logged in and not signed up before.

        - A user who previously signed up when not logged in, and then tries to sign up once they have logged in.

- No issues were discovered with the functionality of this view and the database collection updated as expected.

#### Register Page Template

I performed various tests to ensure that the functionality of the register template works as intended, messages flash to the user and that the validation is completed.

I manually tested the link for the login page works and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Register Page Template

For the registration page templating, I used ``flask_wtf`` and it's import ``Flaskform``

- Validation messages:

  - I verified that the correct validation messages are shown to the user based on the response from either the forms validation itself or the flash messages sent from the backend.

  - This was done by manually inputting information into each field and inputting the wrong information. For instance:

    - For the username field:

      - I inputted special characters and whitespace to see if the form would be accepted.

        - The form returned the expected flash message of "Please use only lowercase, uppercase, or numbers" and would not submit the form.

      - I inputted a username that was already in the database which should raise a error message and not submit.

        - The form returned the expected flash message of "Username already taken. Choose a different username." and would not submit the form.

      - I inputted a username that was less than 3 characters in length and one that was more than 20 characters in length which should each raise an error message and not submit.

        - The form returned the expected flash message on each occasion of "Field must be between 3 and 20 characters long." and would not submit the form.

    - For the email field:

      - I inputted a string of text that was not an email format.

        - The form returned the expected flash message of "Invalid email address.`" and would not submit the form.

      - I inputted an email that was already in the database which should raise a error message and not submit.

        - The form returned the expected flash message of "Email already in use. Please use login." and would not submit the form.

    - For the Password and Password Confirmation field:

      - I inputted a password that did not match to see if the form would be accepted.

        - The form returned the expected flash message of "Field must be equal to password." and would not submit the form.

      - I inputted a password that was below the minimum length of 8 characters which should raise a error message and not submit.

        - The form returned the expected flash message of "Field must be at least 8 characters long." and would not submit the form.

  - No issues were discovered.

##### Register Page - Breakdown of Views Used

**Associated View - Route: ``/register`` Function: ``user_registration()``**

Breakdown of ``user_registration()`` functionality:

- Checking if user is in session:
  
  - When a user loads the page, a conditional statement is run which checks to see whether a user is in session. The result of the conditional statement is saved in a variable.

    - If a user is in session then their session username is saved to the ``username`` variable.

    - If no user is in session then an empty string is saved in the ``username`` variable.

    - If the variable does not contain an empty string, it means a user is logged into a session and then it redirects the user to their profile page as they do not need to access the registration page.

      - I verified that this works as intended by logging into a user account and trying to access the registration page by entering in the url for it. I was redirected to the profile page of the user in session.

      - I tested the functionality again by logging out the account and accessing the registration page. It allowed me to view the page as intended.

      - No issues were discovered in this functionality.

- Validating the form on ``POST``:

  - The ``UserRegistration()`` class is instantiated prior to the stage of validating the form data. Once the form information has been received, the ``form.validate_on_submit()`` is run alongside it which is part of ``Flask-WTF``.

  - If the information submitted is validated, two queries on the database are run to count the amount of times the submitted username and email address appear in the user collection. This information is then used in a conditional statement.

  - I verified that the conditional statement works as intended by doing the following:

    - I inputted form data that contained a username that was already database, an email that was already in the database, and a unique username and email.

      - On each of the scenarios the correct response message was flashed in the form template.

      - On successful registration, the username was placed in the session cookie and redirected to the profile page.

      - No issues were discovered in this functionality.

- Salting and Hashing of Password:

  - All passwords submitted are salted and hashed through the use of the ``passlib`` library. I verified that any passwords that have been submitted to the database are hashed.

  - No issues were discovered with this functionality.

#### Login Page Template

I performed various tests to ensure that the functionality of the login template works as intended, messages flash to the user and that the validation is completed.

I manually tested the link for the register page works and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Login Page Template

For the login page templating, I used ``flask_wtf`` and it's import ``Flaskform``

- Validation messages:

  - I verified that the correct validation messages are shown to the user based on the response from either the forms validation itself or the flash messages sent from the backend.

  - This was done by manually inputting information into each field as follows:

    - Email that was not in the database:

      - The form returned the expected flash message of "Incorrect e-mail/password combination.".

    - I inputted an email that was in the database and an incorrect password.

      - The form returned the expected flash message of "Incorrect e-mail/password combination." and would not log me in.

    - I inputted an email that was in the database and the correct password.

      - The form information was accepted and redirected me to my profile page.

  - No issues were discovered.

##### Login Page - Breakdown of Views Used

**Associated View - Route: ``/login`` Function: ``login()``**

Breakdown of ``login()`` functionality:

- Checking if user is in session:
  
  - When a user loads the page, a conditional statement is run which checks to see whether a user is in session. The result of the conditional statement is saved in a variable.

    - If a user is in session then their session username is saved to the ``username`` variable.

    - If no user is in session then an empty string is saved in the ``username`` variable.

    - If the variable does not contain an empty string, it means a user is logged into a session and then it redirects the user to their profile page as they do not need to access the login page.

      - I verified that this works as intended by logging into a user account and trying to access the login page by entering in the url for it. I was redirected to the profile page of the user in session.

      - I tested the functionality again by logging out the account and accessing the login page. It allowed me to view the page as intended.

      - No issues were discovered in this functionality.

- Validating the form on ``POST``:

  - The ``UserLogin()`` class is instantiated prior to the stage of validating the form data. Once the form information has been received, the ``form.validate_on_submit()`` is run alongside it which is part of ``Flask-WTF``.

  - If the information submitted is validated, a query is run on the user collection in the database to try and find a match for the submitted email.

  - If the user is found, then it uses the ``passlib`` library to verify the password inputted against the password stored in the database.

  - I verified that the conditional statement works as intended by doing the following:

    - I inputted an email that was not in the database, an email with the incorrect password, and an email with the correct password.

      - On each of the scenarios the correct response message was flashed in the form template.

      - On successful login, the username was placed in the session cookie and redirected to the profile page.

      - No issues were discovered in this functionality.

#### Logout Functionality

I tested that when the user clicks on the logout button, clears the session cookie and logs out the user.

##### Logout Functionality - Breakdown of Views Used

**Associated View - Route: ``/logout`` Function: ``logout()``**

Breakdown of ``login()`` functionality:

- Logs user out of session:

  - When a user accesses this view, the ``session.clear()`` function is run and clears the session cookie.

  - I validated that this function works by logging into a user account and then accessing the view.

  - No issues were discovered in this functionality.

#### Profile Page Template

I performed various tests to ensure that the conditional statements used within the profile.html template are working as intended, all modals appear correctly and that all associated ``views`` and ``jQuery`` functionalities work.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Profile Page Template

- Conditional Check - Profile Exists:

  - A conditional check is run on the value of ``user_profile`` variable passed in by the view.

    - If the variable contains an empty string, then a message is displayed to the user saying that we could not find the profile they were looking for.

    - If the variable contains the user information then the profile is generated accordingly.

      - No issues were discovered with this functionality.

- Conditional Check - Profile View:

  - The conditional statements used within the profile.html that checks whether the visitor of the page is the profile owner or a visitor. The following is what is expected to show based on each condition (profile owner or visitor):

    - If the person viewing the page is the profile owner, then the following should show to the user:

      - The profile header should say "Welcome USERNAME".

      - It should show the button for account management.

      - It should show the option for updating their profile if they have not updated it yet.

      - If the user has not updated their profile information then a default profile image and text should be shown.

      - The text for the recipe section should say "My Recipes".

      - It should show text under the recipe section and a button to create a recipe if the user has not created one yet, otherwise it should show their recipes.

      - The Account Management Modal should generate within the HTML document.

    - If the person viewing the page is the not the profile owner, then the following should show to the user:

      - The profile header should say "Welcome to the profile of USERNAME".

      - If the user has not updated their profile information then a default profile image and text should be shown.

      - The text for the recipe section should say "Their recipe creations:".

      - It should show text under the recipe section and a default message if the user has not created one yet, otherwise it should show their recipes.

        - In order to verify the above, I logged in as a user and visited my profile. All of the above was generated as expected and no issues were found.

        - In addition, I visited another users profile and could not see the above information as expected as set out in the conditional statements.

        - No issues were discovered.

##### Breakdown of jQuery Functionality in Profile Page Template

- Account Information Update AJAX Function:

  - I verified that when the profile owner submits information in the Account Update Modal, that the following happens:

    - The form is validated first to ensure it meets requirements setout in the HTML form type - i.e. it must be an email that matches the designated pattern, if there is a password change then it meets the minimum length requirement. If the form is validated, then it can proceed to the next step otherwise the standard HTML validation message is shown.

    - The form request is received by the backend and processed.

    - The modal remains open on form submit so it can display the response message to the user.

    - A response message is displayed to the user based on whether it was an email update, a password update, both of these, no update, or if the current password entered was incorrect.

    - That response message is cleared after any subsequent update requests.

  - No issues were discovered with the functionality of sending the information to the backend & server.

- Account Management Modal - Password Change:

  - I verified that the jQuery functionality of:

    - Adding and removing the required form label and password input.

    - The ``Change Password`` button hides on click and shows again if the user presses ``Cancel``.

    - The ``Cancel`` button shows after the user presses ``Change Password`` and hides after pressing ``Cancel``.

  - No issues were discovered with this functionality.

- Profile Update Form:

  - I verified that the jQuery functionality of when a user clicks on the update profile button ``Add Now`` that the update profile form has the class ``.d-none`` removed so the user can interact with it.

  - No issues were discovered with this functionality.

- File Validation Function:

  - I verified that the jQuery Function for validating image uploads works correctly and that:

    - A message is shown to the user if there is an error with the file upload such as incorrect file or file is too large, or if the image has been accepted.

    - That the submit button is disabled if the file is not acceptable and enabled if the file is acceptable.

    - That the messages disappear on file change to show the new validation message.

    - No issues were discovered with this functionality.

##### Profile Page - Breakdown of Views Used

**Associated View - Route: ``/profile/<username>`` Function: ``profile(username)``**

Breakdown of ``profile(username)`` functionality:

This view generates the profile of a user.

- It runs two queries on the database to find the user and to find any recipes they have made and hasa conditional statement that assigns a value to the ``user_profile`` variable based on whether the username is found in the user collection.

  - I verified that this functionality works as intended and no issues were discovered.

**Associated View - Route: ``/profile/update/<username>`` Function: ``update_profile(username)``**

Breakdown of ``update_profile(username)`` functionality:

- The first part of this function checks queries the database to find the user information.

- It then runs a conditional check to see if the person trying to access the view is logged in, and if they are then if their session username matches the username in the request.

  - If there is no username in session or if the username does not match, then the user is redirected to the landing page.

  - No issues were discovered with this functionality.

- The next stage processes the file request and uses helper function - [image upload](#image-upload) to update the users profile and insert the new profile information in the database.

  - I tested to that the information updates correctly and that the new profile image and text is displayed instead of the default information.

  - No issues were discovered with this functionality.

It runs two queries on the database to find the user and to find any recipes they have made.

I verified that this functionality works as intended and no issues were discovered.

**Associated View - Route: ``/profile/account_management`` Function: ``update_account()``**

Breakdown of ``update_account()`` functionality:

- This view processes the information sent from the Account Management modal.

  - It first checks to see if a password has been submitted with the form and assigns the values of the new password and confirmation password to a variable if there has been.

    - No issues were detected with this conditional statement and the correct values are assigned to the variables if the new password has been submitted.

  - It then finds the users document in the user collection and assigns the current email and hashed password to their respective variables.

  - It then runs the [helper function - no change in account information](#no-change-in-account-information) to check to see if there has been a change in the users information and returns a message to the user through the AJAX function.

    - No issues were found when testing either of these functionalities.

  - If there has been a change in the account information, the current hashed password is checked against the entered password through the use of the ``passlib`` library.

    - If the password does not match then a message is shown to the user through the AJAX function.

      - No issues were found when testing this functionality with both matching and non-matching passwords and the correct message was displayed.

    - If the passwords match then it proceeds to update the users account according to what the changes are.

      - If the user is updating their email and password then the helper function [new password checker](#new-password-checker) is run:

        - If the value returned is True, then the helper functions [email updater](#email-updater) and [password updater](#password-updater) are run and a success message is returned.

        - If the value is False, then a error message is returned and shown to the user.

          - I tested that this functionality works correctly and the correct message is shown to the user. Please see the individual helper functions for the tests performed.

      - If the user is only updating their email then a check is run to see if the new email is the same as the old email.

        - If the value returned is True, then the helper functions [email updater](#email-updater) and a success message is returned.

        - If the value is False, then a error message is returned and shown to the user.

          - I tested that this functionality works correctly and the correct message is shown to the user.

      - If the user is only updating their password then the helper function [new password checker](#new-password-checker) is run:

        - If the value returned is True, then the helper function [password updater](#password-updater) is run and a success message is returned.

        - If the value is False, then a error message is returned and shown to the user.

          - I tested that this functionality works correctly and the correct message is shown to the user. Please see the individual helper function for the tests performed.

    - No issues were found when testing either of these functionalities.

#### Search Page Template

I performed various tests to ensure that the functionality of the search template works as intended and that the pagination works as intended.

I manually tested the link for the login page works and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Search Page Template

For the search page templating, I used a mixture of conditional statements and the pagination styling from ``flask-pagination``

- Conditional Statement - Search Results:

  - The conditional statement works as follows:

    - If a user searches for key word that does not exist in the database then a message should appear to the user saying that there are no results and a message.

      - If the user is logged in it should suggest they add their own recipe to the database.

      - If a user is not logged in then it should suggest they login to their account and add their own recipe to share with others.

      - There were no issues with this functionality and the expected message showed when testing against both scenarios as listed above.

    - If the user searches for a key word that does exist in the database, then the a page with search results should be shown and the results should be displayed in order according to the ``textScore``.

      - I tested the results are shown correctly and in order by testing it with different terms such as ``egg`` and ``chicken``.

      - No issues were found with this functionality.

- Pagination:

  - The pagination for the page is handled by ``flask-pagination``.

    - I verified that the pagination feature was working as expected as within the search results page, a variable is passed through and displayed to the user which shows the amount of search results found.

    - The amount of results per page is limited to 4. I verified that the correct amount of results are displayed and that the right amount of pages are generated based on the returned results - i.e. 8 results generated 2 pages.

    - If the results are less than 4 then all results are shown on one page and the pagination links do not show as they are not required.

    - No issues were discovered with this functionality.

- Conditional Statement - Like Count Text

  - A conditional statement has been used to change the text for the amount of likes a recipe has:

    - If the like count for a recipe is 0, then the text shown is liked by no users.

    - If the like count for a recipe 1, then the text shown is liked by 1 user.

    - If the like count is greater than 1, the text shown is liked by X users.

      - I tested this functionality by checking various recipes that have 0 likes, 1 like, and recipes with likes that are greater than 1 to ensure the statement works correctly.

      - No issues were discovered.

##### Search Page - Breakdown of Views Used

**Associated View - Route: ``/search/<search_term>`` Function: ``search_recipes(search_term)``**

Breakdown of ``search_recipes(search_term)`` functionality:

- Creating a text index:
  
  - The first part of this view creates the index which is used for the ``search_results`` query.

  - I verified that his works correctly as the results generated from the search query look for the search term in the defined indexes.

- Search Result Query:

  - The ``search_result`` query takes the ``search_term`` passed in from the ``/search`` view mentioned in the [**Base Template**](#base-template) and [**Landing Page Template**](#landing-page-template).

  - This uses the MongoDB ``$meta`` projection operator and ``textScore`` metadata to:

    - Search for the ``search_term`` within the defined index

    - Sort the results by the ``textScore`` value.

    - Skips ``X`` results defined by the ``per_page`` variable used for ``Flask-paginate`` less 1.

    - Limits results by 4 which is the value of ``per_page``

    - No issues were discovered by the functionality of this query and it returned the expected results.

  - In addition to the above, another variable used is to count the number of documents that contain the ``search_term`` used and is passed into the ``search.html`` template.

    - No issues were discovered with this query.

- Flask-paginate:

  - This is an extension that has been imported into the application and works as intended.

  - No issues were discovered with the results shown from this extension within the ``search.html`` template.

#### Recipe Page Template

I verified that the recipe page displays the correct recipe information as expected and that all buttons work as intended.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Recipe Page Template

- Conditional Check - Recipe Author:

  - A conditional statement is run to check whether the viewer of the recipe is the recipe author.

    - If the username in session of the person viewing the page is the same as the ``recipe_author`` field then it must generate the ``Manage Your Recipe`` button in the HTML code.

    - If the user is not, then this button should not be generated.

      - I tested that this functionality works as intended by viewing a recipe I create to check if the button is generated and viewable to me.

      - I tested that I was not able to see this button within the page and the HTML code by viewing a recipe that was not created by me.

        - I verified that this works as intended and found no issues.

- Recipe Information:

  - I verified that the information is correctly inputted into the recipe document, including the amount of steps and ingredients, as per the recipe document in the database.

    - No issues were discovered.

- Conditional Check - Like Function:

  - I verified that the conditional statement for like function works as intended:

    - If a user is not logged in, then it shows the amount of likes the recipe has and displays a message saying that the user needs to log into their account to like this recipe.

    - If a user is logged into their account has not liked the recipe then it shows an empty heart with the amount of likes next to it.

    - If the user is logged into their account and has like the recipe then it shows a coloured in heart and the number of likes next to it.

      - I verified each of these conditions works intended and no errors were found in this functionality.

##### Breakdown of jQuery Functionality in Recipe Page Template

- Like Update AJAX Function:

  - I verified that when a user clicks on the "Like" button within the recipe page, the following happens:
  
    - The correct information is sent to the backend and processes.

    - The "Like" icon and like count update accordingly:

      - If a user who hasn't like the recipe before clicks on the button, the HTML icon is changed to a coloured in heart and the new like count is displayed.

      - If a user who has liked the recipe before clicks on the button, the HTML icon is changed to a empty heart and the new like count is displayed.

        - I tested this functionality by pressing the like button multiple times to ensure that it updates and displays the correct information.

        - No issues were discovered with this functionality.
  
- Recipe Steps and Ingredient Toggle Button:

  - I verified that this functionality works as intended and that when a user clicks on the button, the relevant information (step list or ingredient) is shown or hidden from the user.

    - No issues were discovered with this functionality.

##### Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/recipe/<recipe_id>/<recipe_name>`` Function: ``get_recipe(recipe_id, recipe_name)``**

Breakdown of ``get_recipe(recipe_id, recipe_name)`` functionality:

This view generates the recipe page for the intended recipe.

- It runs a query on the database to find the queried recipe based on its ``recipe_id`` and then returns the found recipe which is based into the recipe template.

  - No issues were discovered with this query functionality and the correct information was returned.

**Associated View - Route: ``/like/<recipe_id>`` Function: ``like(recipe_id))``**

Breakdown of ``like(recipe_id)`` functionality:

This view handles the recipe like functionality which is used in the ``recipe.html`` template and works alongside the AJAX function.

- ``find_recipe`` Query:

  - When the form information is received from the AJAX function, it queries the database to find the recipe that is being liked and saves the information to the ``find_recipe`` variable which is then used later in the view.

    - No issues were discovered with this query functionality and the correct information was returned.

- Conditional Statement - Updating Document and Returning Like Count:

  - A conditional statement is run to check whether the user liking the recipe is in the ``liked_by`` field within the recipes document.

    - If the user is not in the ``liked_by`` field then it adds the username to the field, increments the ``likes`` field by 1.

    - If the user is in the ``liked_by`` field then it removes the username from the field and decrements the ``likes`` field by 1.

    - In both instance, the new ``likes`` count is returned to the AJAX functionality to enable it to update the HTML and display the new count.

      - **Bug Identified**- New value for likes not being sent through

        - After a user liked/unliked the recipe, the new value for ``likes`` was not being sent through to the AJAX function.

      - **Fix Applied**:

        - To fix this issue, I moved the variable ``new_like`` which queries the ``likes`` field in the recipes document, to after the ``update_one`` has been completed to ensure the query is using the latest value.

#### Add Recipe Page Template

I verified that the add recipe page displays as expected and that all buttons work as intended.

##### Breakdown of Jinja Functionality in Add Recipe Page Template

No additional Jinja statements were used within the creation of this page outside of the required block tags.

I verified that all HTML input elements with required tags and patterns worked as intended.

- **Bug Identified** - Recipe Could be Submitted Twice

  - When a user submitted the recipe, they could accidentally submit the same hitting the submit button twice within quick succession.

- **Fix Applied**

  - To address this issue I added a jQuery function to disable the submit button after a valid form has been submitted once.

##### Breakdown of jQuery Functionality in Add Recipe Page Template

- Remaining Character Length - Recipe Name & Recipe Description

  - I verified that the function that updates the HTML text for both the Recipe Name & Recipe Description remaining characters works as intended and that the remaining characters are displayed to the user.

  - I verified that when the max character count is reached that the HTML text turns red for that field.

    - **Bug Identified** - Keyup Event Not Working for Mobile Devices

      - The keyup event worked correctly for Desktops and displayed the correct information to the user however on a mobile phone, the keyup events were not being registered.

    - **Fix Applied**

      - To address this issue I amended the jQuery to include input, as follows:

      ```Javascript
      .on("keyup input", ...)
      ```

- File Validation Function:

  - I verified that the jQuery Function for validating image uploads works correctly and that:

    - A message is shown to the user if there is an error with the file upload such as incorrect file or file is too large, or if the image has been accepted.

    - That the submit button is disabled if the file is not acceptable and enabled if the file is acceptable.

    - That the messages disappear on file change to show the new validation message.

    - No issues were discovered with this functionality.

- Adding / Removing Input Fields for Steps and Ingredient:

  - I verified that when a user presses the "+" or "-" under the relevant ingredient or step input that it adds or removes a field input.
  
    - When an input was added, I made sure that the input element was correct and had the necessary attributes.

    - When an input was removed, I made sure that it was the last child input that was removed.

    - **Bug Identified** - User could remove all the inputs from the respective ingredient/step field

      - A user could keep on clicking the remove button and remove all inputs for either the steps or/and ingredient field.

    - **Fix Applied**

      - To address this I applied a conditional statement that adds the ``disabled`` attribute to the corresponding remove button when there is only one input remaining and this attribute is removed when a user adds an input as follows:

      ```Javascript
      $("#remove_ingredient").on("click", () => {
          let ingredientLength = $("#ingredient").children("input").length;

          if( ingredientLength <= 1) {
              $("#remove_ingredient").attr("disabled", "disabled");
          } else {
              $("#ingredient input:last-child").remove();
          }
      });
      ```

    - The following line of code was added to the corresponding add button:

    ```Javascript
    $("#remove_ingredient").removeAttr("disabled", "disabled");
    ```
  
- Functionality to Address Double Submit Bug:

  - As mentioned in the previous section, a bug was identified that allowed a user to submit the same recipe twice if they clicks on the submit button in quick succession. This led to implementing the below code which resolved that bug:

    ```Javascript
      $(".recipe-submit").on("click", function (event) {
        let validForm = this.form.checkValidity();

        if (validForm) {
            event.preventDefault();
            $(this).attr("disabled", "disabled");
            $(this).closest("form").submit();
        }
    });
    ```  

##### Add Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/create_recipe`` Function: ``add_recipe()``**

Breakdown of ``add_recipe()`` functionality:

- Conditional Statement - Verifying User in Session:
  
  - When a user loads the page, a conditional statement is run which checks to see whether a user is in session. The result of the conditional statement is saved in a variable.

    - If a user is in session then their session username is saved to the ``username`` variable.

    - If no user is in session then an empty string is saved in the ``username`` variable.

    - If there is no user in session, then they are redirected to the login page as only logged in users can submit recipes.

      - I tested this functionality by trying to access the add recipe page when not logged in and using an account that is logged in. This functionality works as intended.

- Inserting Form Information into the Database:

  - When the form information has been validated and submitted to the backend, the fields from the form are assigned to variables which can be used to create a new document that is inserted into the database.

    - Two helper functions are used for the steps and ingredient fields as these can be dynamic according to what the user has inputted.

      - The helper functions are [**Recipe Steps**](#recipe-steps) and [**Recipe Ingredients**](#recipe-ingredients).

    - The file request uses the helper function - [image upload](#image-upload) to upload the image for the recipe and store the ``image_url`` and ``image_id`` in the associated variables within  the document to be inserted.

    - I verified that all the information submitted from the form correctly gets uploaded to the database and no errors were found.

#### Manage Recipe Page Template

I verified that the manage recipe page displays as expected and that all buttons work as intended.

##### Breakdown of Jinja Functionality in Manage Recipe Page Template

- I verified that the current recipe information was correctly populated within the form so the user was able to see their previous information and update it where required.

- I verified that all the validation elements within the form worked as expected.

- I verified that the conditional statement for adding the ``selected`` attribute to the dropdown lists worked correctly and selected the correct option based on the database information.

##### Breakdown of jQuery Functionality in Manage Recipe Page Template

- Upload New Image Functionality:

  - I verified that when the user clicks on the "Upload New Image" button that the following happens:

    - The "Upload New Image" button and the text for changing the image has the class ``.d-none`` added and the "Cancel" button has the same class removed.

    - The class of ``.d-none``is removed from the div that holds the form label and input for uploading a new file.

    - The attr ``enctype="multipart/form-data"`` is added onto the form.

    - The user is able to upload an image which is verified accordingly and has any relevant message displayed to them.

    - The image is submitted with the form when the user updates the recipe.

  - I verified that when the user presses the the "Cancel" button then the following happens:

    - The "Upload New Image" button and the text for changing the image has the class ``.d-none`` removed and the "Cancel" button has the same class added.

    - The class of ``.d-none``is added from the div that holds the form label and input for uploading a new file.

    - The attr ``enctype="multipart/form-data"`` is removed from the form.

    - Any image added to the file input by the user is not submitted with the form if they press submit.

- Delete Recipe Modal:

  - I verified that the modal is launched when the user presses delete recipe.

  - I verified that when the user presses cancel in the modal, the modal closes.

  - I verified that when the user presses the confirmation button that the recipe is deleted.

- For the remaining functionalities, please refer to [**Breakdown of jQuery Functionality in create_recipe.html**](#breakdown-of-jquery-functionality-in-create_recipe.html) as the same functionalities used within there are applicable to this as well.

  - Each function was individually verified to ensure that they work as intended and no additional bugs or errors were raised.

##### Manage Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/manage/<recipe_id>`` Function: ``manage_recipe(recipe_id)``**

Breakdown of ``manage_recipe(recipe_id)`` functionality:

- Querying Recipe Details

  - A Query is run to obtain the details of the recipe that has been sent along to the route and this information is assigned to a variable ``edit_recipe`` which is then passed to the passed into the template to show the recipe information for the user.

- Conditional Statement - Verifying User in Session:
  
  - When a user loads the page, a conditional statement is run which checks to see whether there is a user in session and if so, if that user is the same as the ``recipe_author``. The result of the conditional statement is saved in a variable.

    - If a user is in session then their session username is saved to the ``username`` variable.

    - If no user is in session then an empty string is saved in the ``username`` variable.

    - If there is no user in session, then they are redirected to the login page as only logged in users can submit recipes.

      - I tested this functionality by trying to access the add recipe page when not logged in and using an account that is logged in. This functionality works as intended.

**Associated View - Route: ``/update/<recipe_id>`` Function: ``update_recipe(recipe_id)``**

Breakdown of ``update_recipe(recipe_id)`` functionality:

- Inserting Form Information into the Database:

  - When the form information has been validated and submitted to the backend, the fields from the form are assigned to variables which can be used to create a new document that is inserted into the database.

    - Two helper functions are used for the steps and ingredient fields as these can be dynamic according to what the user has inputted.

      - The helper functions are [**Recipe Steps**](#recipe-steps) and [**Recipe Ingredients**](#recipe-ingredients).

      - The form request information is then used to update the existing record in the database.

        - I verified that this functionality works correctly and that the information is correctly updated.

    - If a new image has been submitted then the following happens:

      - The existing ``image_id`` is queried from the database, then it is assigned to a variable ``public_id``.

      - The old image is deleted from Cloudinary using ``cloud.destroy(public_id)``

      - The file request then uses the helper function - [image upload](#image-upload) to upload the new image for the recipe and store the ``image_url`` and ``image_id`` in the associated variables within the document to be updated.

      - The new information for the image is then used to update the existing image details within the database.

        - I verified that this functionality works correctly, the image is deleted from Cloudinary and that the information in the database for the image is correctly updated.

**Associated View - Route: ``/delete/<recipe_id>`` Function: ``delete_recipe(recipe_id)``**

Breakdown of ``delete_recipe(recipe_id)`` functionality:

- Querying Recipe Details

  - A Query is run to obtain the details of the recipe that has been sent along to the route and this information is assigned to a variable ``recipe_check``. This variable is then used to obtain the ``recipe_author`` value.

- Conditional Statement - Verifying User in Session:
  
  - When tries to access this view, a conditional statement is run which checks to see whether there is a user in session and if so, if that user is the same as the ``recipe_author``. The result of the conditional statement is saved in a variable.

    - If a user is in session then their session username is saved to the ``username`` variable.

    - If no user is in session then an empty string is saved in the ``username`` variable.

    - If there is no user in session, then they are redirected to the login page as only logged in users can submit recipes.

      - I tested this functionality by trying to access it when not logged in and using an account that is logged in. This functionality works as intended.

    - If the session user accessing this view is the recipe author then it proceeds to delete the recipe from the database and remove the image from Cloudinary.

      - I verified that this functionality works as intended, the recipe is removed from the database and the image is removed from Cloudinary.
  
#### Privacy Policy Page Template

I verified that the privacy policy page displays as expected.

##### Privacy Policy Page - Breakdown of Views Used

**Associated View - Route: ``/privacy`` Function: ``privacy()``**

Breakdown of ``privacy()`` functionality:

I verified that this work works correctly and when the user access it, they are redirected the relevant page.

#### Advertise Page Template

I verified that the advertise with us page displays as expected.

##### Advertise Page - Breakdown of Views Used

**Associated View - Route: ``/advertise`` Function: ``advertise()``**

Breakdown of ``advertise()`` functionality:

I verified that this work works correctly and when the user access it, they are redirected the relevant page.

#### 404 Page Template

I verified that the custom 404 page correctly generates and is displayed to the user when they access a view that does not exist.

#### 410 Page Template

I have not verified that the page correctly catches the error as I was unable to generate the 410 error. I did create a view to test that the 410.html displays correctly.

#### 500 Page Template

I verified that the custom 500 page correctly generates and is displayed to the user when they access a view that does not exist. I tested this view by adding a recipe, copying the URL, deleting the recipe, then trying to access this URL.

#### Helper Functions

Below are the helper functions created to aid in reducing the repetitive code within the ``run.py``.

##### Image Upload

The ``upload_image()`` function takes in two arguments:

- ``variable`` - This is the variable with the request.file assigned to it.

- ``folder_string`` - This is the name of the folder of where the image will be uploaded into Cloudinary.

This function is then assigned to the relevant variable names ``image_url``, and ``image_id`` which it will assign values too after it has uploaded the image. These variables are then used to be submitted into the database with either the recipe or profile information.

- ``image_url`` - Contains the URL for the uploaded image.

- ``image_id`` - Contains the public image ID for the uploaded image and is used when the picture is being deleted.

I have verified that the functionality with this function works as intended by uploading the required file to Cloudinary and stores the correct information in the variables.

This function is used within [Profile View](#profile-page---breakdown-of-views-used), [Add Recipe View](#add-recipe-page---breakdown-of-views-used) and [Manage Recipe View](manage-recipe-page---breakdown-of-views-used).

##### No Change In Account Information

The ``no_change_check()`` function takes in four arguments:

- email - This is the current email for the users account.

- new_email - This is the new email submitted with the account update.

- password - This is the current password for the users account.

- new_password - This is the new password submitted with the account update.

This function runs conditional checks to see if there has been a change in the information submitted, and makes use of the ``passlib`` to verify the passwords. If there has been a change then a boolean value is returned. If the information is the same as what is held on record then it returns True, else it returns False.

I have verified that this function works correctly by testing against the various scenarios of:

- Same email and same password - returned the expected value of True.

- New email and same password - returned False

- New email and password - returned False

- Same email and new password - returned False

##### New Password Checker

The ``new_pass_check()`` function takes two arguments:

- new - This is the new password submitted with the account update.

- conf - This is the confirmation password submitted with the account update.

If both of these values match then a boolean value of True is returned, else it returns False.

I verified this function worked correctly by passing through a matching password and confirmation password, and a non-matching pair of passwords. The expected values were returned.

##### Email Updater

The ``email_update()`` function takes two arguments:

- user_id - This is the user id related for the record to be updated.

- new_email - This is the new email submitted with the account update.

This function updates the email in the users document in the user collection.

I have verified that this function correctly updates the users information.

##### Password Updater

The ``password_update()`` function takes two arguments:

- user_id - This is the user id related for the record to be updated.

- new_password - This is the new password submitted with the account update.

This function updates the password in the users document in the user collection.

I have verified that this function correctly updates the users information.

##### Recipe Steps

The ``recipe_steps()`` function takes one argument:

- req - This is request.form.

This function is then assigned to the relevant variable ``steps_list`` the value of the list.

The function then iterates over the request.form, looks for the key ``step`` then appends the value to the ``steps_list`` variable.

I have verified that this function correctly and assigns all the steps to the right variable which is then used by the relevant view.

##### Recipe Ingredients

The ``recipe_ingredients()`` function takes one argument:

- req - This is request.form.

This function is then assigned to the relevant variable ``ingredients_list`` the value of the list.

The function then iterates over the request.form, looks for the key ``ingredients`` then appends the value to the ``ingredients_list`` variable.

I have verified that this function correctly and assigns all the ingredients to the right variable which is then used by the relevant view.
