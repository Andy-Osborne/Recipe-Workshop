# Recipe Workshop Testing

All code used for Recipe Workshop was extensively tested through manual process during every stage of development to ensure that it works as intended and any bugs found were fixed. The responsive design of the website was tested on various devices and browsers.

## Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made.

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

6. I want to be able to view and search for recipes that have been uploaded to the website.

7. I want to be able to search for different recipes whether it is by name, ingredient or dish type.

8. I want to be able to rate the recipes that I have tried so others know that the recipe is good and to share my appreciation with the author.

9. I want to be able to create an account on the website which will allow me to edit recipes that I have created.

10. I want to ensure that when I create an account, my password is only known to me and cannot be seen by the website admin.

11. I want to be able to update my password or email address.

12. I want to be able to upload my own recipes for other users to try.

13. I want to be able to upload a picture for my recipe.

14. I want to be able to manage my recipe, or even delete it from the website.

15. I want to be able to create a profile page and upload an image of myself and an introduction for other users to see when they view my recipes.
