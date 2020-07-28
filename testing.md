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

