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
            - [**Breakdown of Jinja Functionality in public_base.html**](#breakdown-of-jinja-functionality-in-public_base.html)
            - [**Breakdown of jQuery Functionality in public_base.html**](#breakdown-of-jquery-functionality-in-public_base.html)
            - [**Base Template - Breakdown of Views Used**](#base-template---breakdown-of-views-used)

        - [**Landing Page Template**](#base-template)
            - [**Breakdown of Jinja Functionality in index.html**](#breakdown-of-jinja-functionality-in-index.html)
            - [**Breakdown of jQuery Functionality in index.html**](#breakdown-of-jquery-functionality-in-index.html)
            - [**Landing Page Template - Breakdown of Views Used**](#landing-page---breakdown-of-views-used)

        - [**Register Page Template**](#register-template)
            - [**Breakdown of Jinja Functionality in register.html**](#breakdown-of-jinja-functionality-in-register.html)
            - [**Register Page Template - Breakdown of Views Used`**](#register-page---breakdown-of-views-used)

        - [**Login Page Template**](#login-template)
            - [**Breakdown of Jinja Functionality in login.html**](#breakdown-of-jinja-functionality-in-login.html)
            - [**Login Page Template - Breakdown of Views Used`**](#login-page---breakdown-of-views-used)

        - [**Logout Functionality**](#logout-functionality)
            - [**Logout Functionality- Breakdown of Views Used`**](#logout-functionality---breakdown-of-views-used)

        - [**Profile Page Template**](#profile-template)
            - [**Breakdown of Jinja Functionality in profile.html**](#breakdown-of-jinja-functionality-in-profile.html)
            - [**Breakdown of jQuery Functionality in profile.html**](#breakdown-of-jquery-functionality-in-profile.html)
            - [**Profile Page Template - Breakdown of Views Used`**](#profile-page---breakdown-of-views-used)

        - [**Helper Functions**](#helper-functions)
            - [**Image Upload**](#image-upload)
            - [**No Change In Account Information**](#no-change-in-account-information)
            - [*New Password Checker**](#new-password-checker)
            - [*Email Updater**](#email-updater)
            - [*Password Updater**](#password-updater)

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

    - The landing page of the website does things but how does it do this?

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

  - Bug Identified - **Navbar Covered Top of Each Pages Content*

    - As the Navbar is fixed to the top of the page, this caused an issue where content was covered by it.

  - Fix Applied:

    - To give the page content some breathing room, I added ``padding-top: 80px;`` to the ``.content`` class which resolved the issue.

##### Landing Page

- I tested that all writing, buttons and images on the landing page remained readable by the user and it adapted accordingly to the device it was being viewed on.

- Where the responsiveness of the website began to degrade, I created a media query to deal with any issues.

- In order to ensure that the site retained cross-browser responsiveness, I used the online CSS [Autoprefixer](https://autoprefixer.github.io/).

  - Bug Identified - **Search Bar Aligned to Left of Screen*

    - At certain media sizes, the search bar aligned itself to the left of the search div which was unintended

  - Fix Applied:

    - In order to correct this issue I used the bootstrap class of ``justify-content-center``

##### Search Results Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- No issues were discovered.

##### Recipe Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

  - Bug Identified - **Recipe Image Displayed Incorrectly on iPhone X*

    - When viewing the recipe page through the emulator the recipe page behaved and looked as expected however; when viewing the page on an actual iPhone X the recipe image became distorted and squished. After researching the issue, I discovered that it is a known bug on how Safari stretches images.

  - Fix Applied:

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

#### Base Template

I performed various tests to ensure that the conditional statements used within the base template are working as intended.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja functionality in ``public_base.html``

- Conditional Navbar Options

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

- Conditional ``active-page`` Class

  - Within the base template navbar links, there are conditional statements in each of the links classes. This essentially assigns the ``active-page`` class to a link if that is the page that the user is on.

  - I manually tested that this works as intended on every page of the website.

  - Note: The active class does not get applied to the profile link when a user is visiting someone elses profile. This is an intended design choice and not a bug.

  - No bugs were discovered with this functionality.

- Search Bar Functionality

  - I manually tested that the search bar functionality works as intended.

  - No bugs were discovered with this functionality.

##### Breakdown of jQuery functionality in ``public_base.html``

- Adding and Remove ``.btn-zoom``

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

##### Breakdown of Jinja functionality in ``index.html``

- Highest Rated Recipe

  - I verified that the information displayed under the ``Top Rated Recipe`` and the information inputted through the use of ``for`` loop is that of the recipe which has received the most likes.

  - This was done by manually changing the rating of a recipe to allow me to know which recipe details should be displayed.

  - No issues were discovered.

- Most Recent Recipes

  - I verified that the information displayed under the ``Most Recent Recipes`` and their respective Recipe Names and images are recorded against the correct item.

  - This was done by manually checking each recipe individually to ensure that the right name was against the right picture and that when clicking on one of these recipes that it redirected the user to the right recipe.

  - No issues were discovered.

- Newsletter Banner

  - The newsletter banner section uses three conditional statements that checks:
  
    - If there is no user in session, then it displays the newsletter banner.

    - If there is a user in session but it's not in the ``signups`` variable that gets passed through from the view then it shows the newsletter banner.

    - If the session username is in the ``signups`` variable then it does not show the banner.

  - I manually checked each conditional statement by doing the following:

    - I tested the first condition by visiting the landing page and not being signed into an account. The newsletter banner was visible. I then inputted an email and submitted the form and moved to a different page and back again to see if the banner still showed.

      - No issues were discovered under this condition as the banner remained visible as no user was in session.

    - I tested the second and third condition by logging in and visiting the landing page as this meant a user was now in session. The newsletter banner was visible. I then inputted an email and submitted the form and moved to a different page and back again to see if the banner still showed.

      - No issues were discovered under this condition as the banner was visible on first visit and then no longer visible on subsequent visits.

##### Breakdown of jQuery functionality in ``index.html``

- Newsletter AJAX Function

  - I verified that when a user enters their email and presses the submit button that the following happens:

    - The form is validated first to ensure it meets requirements setout in the HTML form type - i.e. it must be an email that matches the designated pattern. If the form is validated, then it can proceed to the next step otherwise the standard HTML validation message is shown.

    - The form request is received by the backend and processed.

    - The banner title div and newsletter form is hidden.

    - A response message is displayed to the user.

  - No issues were discovered with the functionality of sending the information to the backend & server however; an unintended bug was discovered before the message could be shown.

  - Bug Identified - **Page Refreshes on submit*

    - When the user submits the form, the default function of the form is to refresh the page which prevents the user from seeing the response message.

  - Fix Applied:

    - In order to correct this issue I used ``event.preventDefault();`` to stop the default function of the form and allow the message to be shown to the user.

- Adding and Remove ``.image-zoom-class``

  - I verified that the jQuery functionality of adding and removing the ``.image-zoom-class`` to recent images on the landing page worked as intended.

  - This was done by moving the over each image to ensure that it zooms in and once the mouse leaves the image, the class is removed so the image reverts back to its default position.

  - No issues were discovered with this functionality.

##### Landing Page - Breakdown of Views Used

**Associated View - Route: ``/`` Function: ``index()``**

Breakdown of ``index()`` functionality:

- Highest Rated Recipe Query
  
  - I verified that this function works as intended and gets the recipe from the recipe collection that has the most amount of likes by liking various recipes to ensure that 1 recipe had more likes than another recipe. The results of this query is assigned to a Jinja variable and passed into the template as a ``list``.

- Recent Recipes Query

  - I verified that the 8 most recently added recipes to the recipe collection are displayed to users on the landing page and are shown in descending order which starts with the most recently added recipe. The results of this query is assigned to a Jinja variable and passed into the template as a ``list``.

  - **Bug Discovered** - Recipes Not shown in Order

    - This function was displaying the 8 recently added recipes however; if more than 8 recipes were added on the same day then the results shown were not correct as to the 8 **most** recently added recipes.

  - **Fix Applied**

    - This bug was caused by using ``datetime.date`` within the recipe submission field as it was very general. The fix applied was to use ``datetime.now()`` so the date entered against the recipe was much more specific and allowed the correct sorting and retrieving of the most recently added recipes.

- Newsletter Sign Up Query

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

#### Register Page Template

I performed various tests to ensure that the functionality of the register template works as intended, messages flash to the user and that the validation is completed.

I manually tested the link for the login page works and directs the user to the relevant page.

##### Breakdown of Jinja functionality in ``register.html``

For the registration page templating, I used ``flask_wtf`` and it's import ``Flaskform``

- Validation messages

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

- Checking if user is in session
  
  - When a user a loads the page, a conditional statement is run which checks to see whether a user is in session. The result of the conditional statement is saved in a variable.

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

- Salting and Hashing of Password

  - All passwords submitted are salted and hashed through the use of the ``passlib`` library. I verified that any passwords that have been submitted to the database are hashed.

  - No issues were discovered with this functionality.

#### Login Page Template

I performed various tests to ensure that the functionality of the login template works as intended, messages flash to the user and that the validation is completed.

I manually tested the link for the register page works and directs the user to the relevant page.

##### Breakdown of Jinja functionality in ``login.html``

For the login page templating, I used ``flask_wtf`` and it's import ``Flaskform``

- Validation messages

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

- Checking if user is in session
  
  - When a user a loads the page, a conditional statement is run which checks to see whether a user is in session. The result of the conditional statement is saved in a variable.

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

- Logs user out of session

  - When a user accesses this view, the ``session.clear()`` function is run and clears the session cookie.

  - I validated that this function works by logging into a user account and then accessing the view.

  - No issues were discovered in this functionality.

#### Profile Page Template

I performed various tests to ensure that the conditional statements used within the profile.html template are working as intended, all modals appear correctly and that all associated ``views`` and ``jQuery`` functionalities work.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja functionality in ``profile.html``

- Conditional Check - Profile Visitor

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

##### Breakdown of jQuery functionality in ``profile.html``

- Account Information Update AJAX Function

  - I verified that when the profile owner submits information in the Account Update Modal, that the following happens:

    - The form is validated first to ensure it meets requirements setout in the HTML form type - i.e. it must be an email that matches the designated pattern, if there is a password change then it meets the minimum length requirement. If the form is validated, then it can proceed to the next step otherwise the standard HTML validation message is shown.

    - The form request is received by the backend and processed.

    - The modal remains open on form submit so it can display the response message to the user.

    - A response message is displayed to the user based on whether it was an email update, a password update, both of these, no update, or if the current password entered was incorrect.

    - That response message is cleared after any subsequent update requests.

  - No issues were discovered with the functionality of sending the information to the backend & server.

- Account Management Modal - Password Change

  - I verified that the jQuery functionality of:

    - Adding and removing the required form label and password input.

    - The ``Change Password`` button hides on click and shows again if the user presses ``Cancel``.

    - The ``Cancel`` button shows after the user presses ``Change Password`` and hides after pressing ``Cancel``.

  - No issues were discovered with this functionality.

- Profile Update Form

  - I verified that the jQuery functionality of when a user clicks on the update profile button ``Add Now`` that the update profile form has the class ``.d-none`` removed so the user can interact with it.

  - No issues were discovered with this functionality.

- File Validation Function

  - I verified that the jQuery Function for validating image uploads works correctly and that:

    - A message is shown to the user if there is an error with the file upload such as incorrect file or file is too large, or if the image has been accepted.

    - That the submit button is disabled if the file is not acceptable and enabled if the file is acceptable.

    - That the messages disappear on file change to show the new validation message.

    - No issues were discovered with this functionality.

##### Profile Page - Breakdown of Views Used

**Associated View - Route: ``/profile/<username>`` Function: ``profile(username)``**

Breakdown of ``profile(username)`` functionality:

This view generates the profile of a user.

- It runs two queries on the database to find the user and to find any recipes they have made.

  - I verified that this functionality works as intended and no issues were discovered.

**Associated View - Route: ``/profile/update/<username>`` Function: ``update_profile(username)``**

Breakdown of ``update_profile(username)`` functionality:

- The first part of this function checks queries the database to find the user information.

- It then runs a conditional check to see if the person trying to access the view is logged in, and if they are then if their session username matches the username in the request.

  - If there is no username in session or if the username does not match, then the user is redirected to the landing page.

  - No issues were discovered with this functionality.

- The next stage processes the form request and uses [helper function - image upload](#image-upload) to update the users profile and insert the new profile information in the database.

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

#### Helper Functions

Below are the helper functions created to aid in reducing the repetitive code within the ``run.py``.

#### Image Upload

The ``upload_image()`` takes in two arguments:

- ``variable`` - This is the variable with the request.file assigned to it.

- ``folder_string`` - This is the name of the folder of where the image will be uploaded into Cloudinary.

The function will then use the ``global`` variable names ``image_url``, and ``image_id`` which it will assign values too after it has uploaded the image. These variables are then used to be submitted into the database with either the recipe or profile information.

- ``image_url`` - Contains the URL for the uploaded image.

- ``image_id`` - Contains the public image ID for the uploaded image and is used when the picture is being deleted.

I have verified that the functionality with this function works as intended by uploading the required file to Cloudinary and stores the correct information in the variables.

This function is used within [Profile View](#profile-page---breakdown-of-views-used), [Add Recipe View]() and [Manage Recipe View]().

#### No Change In Account Information

The ``no_change_check()`` takes in four arguments:

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

#### New Password Checker

The ``new_pass_check()`` takes two arguments:

- new - This is the new password submitted with the account update.

- conf - This is the confirmation password submitted with the account update.

If both of these values match then a boolean value of True is returned, else it returns False.

I verified this function worked correctly by passing through a matching password and confirmation password, and a non-matching pair of passwords. The expected values were returned.

#### Email Updater

The ``email_update()`` takes two arguments:

- user_id - This is the user id related for the record to be updated.

- new_email - This is the new email submitted with the account update.

This function updates the email in the users document in the user collection.

I have verified that this function correctly updates the users information.

#### Password Updater

The ``password_update()`` takes two arguments:

- user_id - This is the user id related for the record to be updated.

- new_password - This is the new password submitted with the account update.

This function updates the password in the users document in the user collection.

I have verified that this function correctly updates the users information.
