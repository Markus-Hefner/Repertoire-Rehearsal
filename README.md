# Repertoire Rehearsal

Repertoire Rehearsal is meant for the busy, on call musician who, without much rehearsal time, has to go on stage. Knowing in advance of what one is capable of playing makes planning so much easier.

For this, Repertoire Rehearsal is a central place to store the titles and additional information of all the musical pieces one is able to play at first try - an Index of all the performance-ready songs.

Future features will help to accelerate the learning process so that one's songs are performance-ready even faster.

![Mockup](readmedocs/Mockup.png "Mockup")

## Table of Contents

- User Stories
- Features
- Future Features
- Typography and Colour Schemes
- Wireframes
- Technology
- Testing
- Deployment
- Credits

## User Stories

### First Time Visitor Goals
- As a first time visitor of this site I immediately want to know what it is about and what it has to offer.

### Returning and Frequent Visitor Goals
- As a returning or frequent visitor of the site I want to log in and see the pieces I'm able to play and add new ones with ease.

## Features
- template: base.html

  - It is roughly devided into three section: header, main and footer.

  Header and Navbar

    - Depending on the log-in status of the user the navbar changes

      NOT logged-in users

      ![Homepage-not-logged-in](readmedocs/Homepage-not-logged-in.png "Homepage not logged-in")

      logged-in user

      ![Homepage-logged-in](readmedocs/Homepage-logged-in.png "Homepage logged-in")

      - At very top is an announcement section.
      - The header section below displays the title of the page.
      - Below the user finds the navbar which changes depending on the login status. Here are also the links for registering and logging in.
      - Below that is a short welcome message and the login status.

  Main

    - The main content changes depending on the log-in status and which template is used.
      
        NOT logged-in users (besides the singup and login page (see below) only one template is available for users who are not logged-in.)

      - Template: song_list.html

        ![Homepage-not-logged-in](readmedocs/Homepage-not-logged-in.png "Homepage not logged-in")

        - The user is presented with a short introductory text and the callout to register or login

        logged-in users

      - Template: song_list.html

        ![Homepage-logged-in](readmedocs/Homepage-logged-in.png "Homepage logged-in")

        - At the top of the main section the user directly finds the 'Add new song'-form to quickly add new songs.
        - Below the user finds his/her repertoire with clickable songs.

      - Template: song_rehearsal.html

        ![Song-detail-screen](readmedocs/Song-detail-screen.png "Song detail screen")

        - Here the user gets more information about the song.
        - Furthermore he/she can edit or delete the song via two buttons.

      - Template: song_edit.html

        ![Edit-song-screen](readmedocs/Edit-song-screen.png "Edit song screen")

        - On this screen the user can edit song and save it to the database with the 'Update'-button.

      - Template: song_delete_warning.html

        ![Deletion-warning-screen](readmedocs/Deletion-warning-screen.png "Deletion warning screen")

        - Before the user can delete song she/he is asked again for a confirmation.

      - Templates: signup.html, login.html and logout.html

        ![Signup-page](readmedocs/Signup-page.png "Signup page")

        ![Signin-page](readmedocs/Signin-page.png "Signin page")

        ![Signout-screen](readmedocs/Signout-screen.png "Signout screen")

        - These standard signup, login and logout pages in the style of the site.
        - On the logout page the user is asked again for a confirmation.
      
  Footer

    ![Footer](readmedocs/Footer.png "Footer")

    - The footer section will later contain all the social links, where the user can meet fellow musicians.

## Future Features

- Adding a Practice Coach did not make it in the MVP. However, it would be the next step in developing the site. On the song detail page (song_rehearsal.html) would be another field called "Next due date" as well as several buttons with which the user could judge his/her performance during practice. On this basis a new due date for the next practice would be automatically set. Thus using spaced repetition the learning effect would enhanced making the pieces ready for performance even after several weeks or even months not having played them. For that an extra field in the :model:`repertoire.Song` was already created.

## Typography and Colour Schemes

### Typography
- The font Lato was used because of its simple and easy to read typography, since in a busy enviroment (like on stage) there is often not much time to decipher elaborate writing.

### Colour Schemes
- The color scheme consists of plain white and a kind of red (  #ce3232). The red is referring to the curtain of a stage further underlining that the app is about getting from the rehearsal room on stage. However, to not overwhelm the user with a popping red more modern, cleaner, "lighter" red was chosen: russet. For better contrast white was chosen as the text color against the russet.

### Overall Design
- Images or other distracting elements were not used to keep it clean and fast.

## Wireframes

- Homepage (not logged-in)

![Homepage-(not-logged-in)](readmedocs/Homepage-(not-logged-in).png "Homepage (not logged-in)")

- Register page

![Register](readmedocs/Register.png "Register")

- Login page

![Login](readmedocs/Login.png "Login")

- Homepage (logged-in)

![Homepage-(logged-in)](readmedocs/Homepage-(logged-in).png "Homepage (logged-in)")

- Song details page

![Song-details](readmedocs/Song-details.png "Song details")

- Song edit page

![Edit-song](readmedocs/Edit-song.png "Edit song")

- Song delete warning page

![Song-delete-warning](readmedocs/Song-delete-warning.png "Song delete warning")

- Signout page

![Signout](readmedocs/Signout.png "Signout")


## Technology

- vscode was used for writing and editing the code.
- GitHub is used for storing the code.
- favicon.io was used to turn a png-graphic into usable code to paste into the head element in order to get a favicon.
- Google Fonts provides the Lato font.
- Heroku is used to deploy the code

## Testing

### Code Validation

The W3C Markup Validator, W3C CSS Validator Services and the CI Python Linter were used to check the code of all HTML, CSS and Python files.

Results:

#### HTML

- song_list.html (not logged-in)

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2F
  via direct input: ![repertoire-page-not-logged-HTML-validation-via-direct-input](readmedocs/repertoire-page-not-logged-HTML-validation-via-direct-input.png "repertoire page not logged HTML validation via direct input")

- song_list.html (logged-in)

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2F
  via direct input: ![repertoire-page-logged-in-HTML-validator-via-direct-input](readmedocs/repertoire-page-logged-in-HTML-validator-via-direct-input.png "repertoire page logged in HTML validator via direct input")

- song_rehearsal.html

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2F35%2F
  via direct input: ![song_rehearsal-page-logged-in-HTML-validator-via-direct-input](readmedocs/song_rehearsal-page-logged-in-HTML-validator-via-direct-input.png "song_rehearsal page logged in HTML validator via direct input")

- song_edit.html

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2F35%2Fedit%2F
  via direct input: ![song_edit-page-logged-in-HTML-validator-via-direct-input](readmedocs/song_edit-page-logged-in-HTML-validator-via-direct-input.png "song_edit page logged in HTML validator via direct input")

- song_delete_warning.html

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2F35%2Fdelete_warning%2F
  via direct input: ![song_delete_warning-page-logged-in-HTML-validator-via-direct-input](readmedocs/song_delete_warning-page-logged-in-HTML-validator-via-direct-input.png "song_delete_warning page logged in HTML validator via direct input")

- singup.html

  via URI: https://repertoire-rehearsal-14a907e71fba.herokuapp.com/accounts/signup/
  via direct input: ![signup-page-HTML-validation-via-direct-input](readmedocs/signup-page-HTML-validation-via-direct-input.png "signup page HTML validation via direct input")

  Errors are caused by the code that is inserted by Django.

- login.html

  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2Faccounts%2Flogin%2F
  via direct input: ![login-page-HTML-validation-via-direct-input](readmedocs/login-page-HTML-validation-via-direct-input.png "login page HTML validation via direct input")

- logout.html
  via URI: https://validator.w3.org/nu/?doc=https%3A%2F%2Frepertoire-rehearsal-14a907e71fba.herokuapp.com%2Faccounts%2Flogout%2F
  via direct input: ![logout-page-logged-in-HTML-validator-via-direct-input](readmedocs/logout-page-logged-in-HTML-validator-via-direct-input.png "logout page logged in HTML validator via direct input")

#### CSS

- CSS

  ![CSS-validator](readmedocs/CSS-validator.png "CSS validator")

#### Python

- repertoire\admin.py

  ![repertoire_admin.py-validator](readmedocs/repertoire_admin.py-validator.png "repertoire_admin.py validator")

- repertoire\apps.py

  ![repertoire_apps.py-validator](readmedocs/repertoire_apps.py-validator.png "repertoire_apps.py validator")

- repertoire\forms.py

  ![repertoire_forms.py-validator](readmedocs/repertoire_forms.py-validator.png "repertoire_forms.py validator")

- repertoire\models.py

  ![repertoire_models.py-validator](readmedocs/repertoire_models.py-validator.png "repertoire_models.py validator")

- repertoire\test_forms.py

  ![repertoire_test_forms.py-validator](readmedocs/repertoire_test_forms.py-validator.png "repertoire_test_forms.py validator")

- repertoire\test_views.py

  ![repertoire_test_views.py-validator](readmedocs/repertoire_test_views.py-validator.png "repertoire_test_views.py validator")

- repertoire\views.py

  ![repertoire_views.py-validator](readmedocs/repertoire_views.py-validator.png "repertoire_views.py validator")


### External Links
- None.

### Assessibility

- Login page

  Lighthouse report for mobile:

  ![login-page-Lighthouse-report-mobile](readmedocs/login-page-Lighthouse-report-mobile.png "login page Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![login-page-Lighthouse-report-desktop](readmedocs/login-page-Lighthouse-report-desktop.png "login page Lighthouse report desktop")

- Logout

  Lighthouse report for mobile:

  ![logout-page-logged-in-Lighthouse-report-mobile](readmedocs/logout-page-logged-in-Lighthouse-report-mobile.png "logout page logged in Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![logout-page-logged-in-Lighthouse-report-desktop](readmedocs/logout-page-logged-in-Lighthouse-report-desktop.png "logout page logged in Lighthouse report desktop")

- Homepage (logged-in)

  Lighthouse report for mobile:

  ![repertoire-page-logged-in-Lighthouse-report-mobile](readmedocs/repertoire-page-logged-in-Lighthouse-report-mobile.png "repertoire page logged in Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![repertoire-page-logged-in-Lighthouse-report-desktop](readmedocs/repertoire-page-logged-in-Lighthouse-report-desktop.png "repertoire page logged in Lighthouse report desktop")

- Homepage (not logged-in)

  Lighthouse report for mobile:

  ![repertoire-page-not-logged-in-Lighthouse-report-mobile](readmedocs/repertoire-page-not-logged-in-Lighthouse-report-mobile.png "repertoire page not logged in Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![repertoire-page-not-logged-in-Lighthouse-report-desktop](readmedocs/repertoire-page-not-logged-in-Lighthouse-report-desktop.png "repertoire page not logged in Lighthouse report desktop")

- Signup page

  Lighthouse report for mobile:

  ![signup-page-Lighthouse-report-mobile](readmedocs/signup-page-Lighthouse-report-mobile.png "signup page Lighthouse report mobile")

  Lighthouse report for desktop:

  ![signup-page-Lighthouse-report-desktop](readmedocs/signup-page-Lighthouse-report-desktop.png "signup page Lighthouse report desktop")

- Song delete warning page

  Lighthouse report for mobile:

  ![song_delete_warning-page-logged-in-Lighthouse-report-mobile](readmedocs/song_delete_warning-page-logged-in-Lighthouse-report-mobile.png "XYsong_delete_warning page logged in Lighthouse report mobileZ")

  Lighthouse report for desktop:
  
  ![song_delete_warning-page-logged-in-Lighthouse-report-desktop](readmedocs/song_delete_warning-page-logged-in-Lighthouse-report-desktop.png "song_delete_warning page logged in Lighthouse report desktop")

- Song edit page

  Lighthouse report for mobile:

  ![song_edit-page-logged-in-Lighthouse-report-mobile](readmedocs/song_edit-page-logged-in-Lighthouse-report-mobile.png "song_edit page logged in Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![song_edit-page-logged-in-Lighthouse-report-desktop](readmedocs/song_edit-page-logged-in-Lighthouse-report-desktop.png "song_edit page logged in Lighthouse report desktop")

- Song details page

  Lighthouse report for mobile:

  ![song_rehearsal-page-logged-in-Lighthouse-report-mobile](readmedocs/song_rehearsal-page-logged-in-Lighthouse-report-mobile.png "song_rehearsal page logged in Lighthouse report mobile")

  Lighthouse report for desktop:
  
  ![song_rehearsal-page-logged-in-Lighthouse-report-desktop](readmedocs/song_rehearsal-page-logged-in-Lighthouse-report-desktop.png "song_rehearsal page logged in Lighthouse report desktop")


### User Stories - Test Cases

- As a first time visitor of this site I immediately want to know what it is about and what it has to offer.
    - Due to the short introductory text the user knows exactly what to expect from the site.

- As a returning or frequent visitor of the site I want to log in and see the pieces I'm able to play and add new ones with ease.
    - Due to the clean and simplistic layout the user can navigate with ease. Since the 'Add new song'-form is at the top of the homepage the user can quickly add new songs.

- For more user stories visit the open Kanban board on the GitHub repo https://github.com/users/Markus-Hefner/projects/12/views/1?pane=issue&itemId=102081528&issue=Markus-Hefner%7CRepertoire-Rehearsal%7C13

### Feature Testing

#### Automated Testing
- Test results:

  ![test_views-and-test_forms-results](readmedocs/test_views-and-test_forms-results.png "test_views and test_forms results")

#### Manual Testing
| Start                | Feature             | User Action | Outcome | Test Result | Image             |
| :------------------: | :------------------ | :---------: | :------ | :---------: | :---------------: |
| song_list.html, signup.html, login.html (not logged in) | 'Home'-button | click | Homepage (song_list.html) with introductory text is displayed | passed | ![Homepage-not-logged-in](readmedocs/Homepage-not-logged-in.png "Homepage not logged-in") |
| song_list.html, signup.html, login.html (not logged in) | 'Register'-button | click | The signup page is displayed | passed | ![Signup-page](readmedocs/Signup-page.png "Signup page") |
| song_list.html, signup.html, login.html (not logged in) | 'Login'-button | click | The signin page is displayed | passed | ![Signin-page](readmedocs/Signin-page.png "Signin page") |
| signup.html | 'Sign Up'-form with 'Sign Up'-button | fill out the necessary information and click on 'Sign Up'-button | New account is created and redirected to the homepage (song_list.html) with the 'Add new song'-Form and the repertoire is displayed | passed | ![User-Create-new-user-Form-filled-out-before-submission](readmedocs/User-Create-new-user-Form-filled-out-before-submission.png "User Create new user Form filled out before submission") ![User-Create-new-user-Homepage-after-submission](readmedocs/User-Create-new-user-Homepage-after-submission.png "User Create new user Homepage after submission") ![Admin-Users-before-new-user-is-created](readmedocs/Admin-Users-before-new-user-is-created.png "Admin Users before new user is created") ![Admin-Users-after-new-user-is-created](readmedocs/Admin-Users-after-new-user-is-created.png "Admin Users after new user is created") |
| song_list.html, logout.html, song_rehearsal.html, song_edit.html, song_delete_warning (logged in) | 'Home'-button | click | Homepage (song_list.html) with the 'Add new song'-Form and the repertoire is displayed | passed | ![Homepage-after-user-is-logged-in-1](readmedocs/Homepage-after-user-is-logged-in-1.png "Homepage after user is logged in 1") ![Homepage-after-user-is-logged-in-2](readmedocs/Homepage-after-user-is-logged-in-2.png "Homepage after user is logged in 2") |
| song_list.html, logout.html, song_rehearsal.html, song_edit.html, song_delete_warning (logged in) | 'Logout'-button | click | Logout page is displayed with 'Sign Out'-button | passed | ![Signout-screen](readmedocs/Signout-screen.png "Signout screen") |
| song_list.html | 'Add new song'-form with 'Add song'-button | fill out the necessary information and click on 'Add song'-button | Song is added to the database and displayed in the repertoire | passed | ![User-Songlist-before-adding-a-new-song](readmedocs/User-Songlist-before-adding-a-new-song.png "User Songlist before adding a new song") ![User-Songlist-after-adding-a-new-song](readmedocs/User-Songlist-after-adding-a-new-song.png "User Songlist after adding a new song") ![Admin-Songlist-before-adding-a-new-song](readmedocs/Admin-Songlist-before-adding-a-new-song.png "Admin Songlist before adding a new song") ![Admin-Songlist-after-adding-a-new-song](readmedocs/Admin-Songlist-after-adding-a-new-song.png "Admin Songlist after adding a new song") |
| song_list.html (with songs already added to the repertoire) | Link to song details | click on the title of the song | Song details (song_rehearsal.html) are displayed along with an 'Edit Song'- and 'Delete Song'-button | passed | ![Song-detail-screen](readmedocs/Song-detail-screen.png "Song detail screen") |
| song_rehearsal.html | 'Edit Song'-buttun | click | Form is displayed to edit the information about the song | passed | ![Edit-song-screen](readmedocs/Edit-song-screen.png "Edit song screen") |
| song_rehearsal.html | Form and 'Update'-button | fill out the necessary information and click on 'Update'-button | Song details with edits are displayed | passed | ![User-Song-info-before-editing](readmedocs/User-Song-info-before-editing.png "User Song info before editing") ![User-Song-info-after-editing](readmedocs/User-Song-info-after-editing.png "User Song info after editing") ![Admin-Song-info-before-editing](readmedocs/Admin-Song-info-before-editing.png "Admin Song info before editing") ![Admin-Song-info-after-editing](readmedocs/Admin-Song-info-after-editing.png "Admin Song info after editing") |
| song_rehearsal.html | 'Delete Song'-buttun | click | Warning (song_delete_warning.html) is displayed whether one really wants to delete the song or not with 'Yes'- and 'No'-button | passed | ![Deletion-warning-screen](readmedocs/Deletion-warning-screen.png "Deletion warning screen") |
| song_delete_warning.html | 'No'-button | click | Song details (song_rehearsal.html) are displayed | passed | ![Song-detail-screen](readmedocs/Song-detail-screen.png "Song detail screen") |
| song_delete_warning.html | 'Yes'-button | click | Homepage (song_list.html) with the 'Add new song'-Form and the repertoire is displayed without the deleted song. Song is also deleted from the database | passed | ![User-Songlist-before-deletion](readmedocs/User-Songlist-before-deletion.png "User Songlist before deletion") ![User-Songlist-after-deletion](readmedocs/User-Songlist-after-deletion.png "User Songlist after deletion") ![Admin-Songlist-before-deletion](readmedocs/Admin-Songlist-before-deletion.png "Admin Songlist before deletion") ![Admin-Songlist-after-deletion](readmedocs/Admin-Songlist-after-deletion.png "Admin Songlist after deletion") |
| logout.html | 'Sign Out'-button | click | Homepage (song_list.html) with introductory text and sign out message is displayed | passed | ![Homepage-not-logged-in](readmedocs/Homepage-not-logged-in.png "Homepage not logged-in") |

### Bugs

- Currently there are no known unfixed bugs.

### Supported Screens and Browsers
  - The website was tested with Firefox and Google Chrome.
  - It was viewed stretched from a width of 370px up to a width of 3000px with no layout problems.

## Deployment

### GitHub and Heroku

Prerequisites:
- A GitHub account
- A Heroku account

Steps:
- Log into your GitHub account
- Fork or clone this repository https://github.com/Markus-Hefner/Repertoire-Rehearsal into your own repositories
- Log into your Heroku account
- Click on 'New' in the upper right-hand corner.
- From the dropdown menu select 'Create new app'.
- Give the app a name of your choosing (preferably 'Repertoire Rehearsal').
- Choose your location.
- (Don't add to pipeline.)
- Click on the 'Settings'-tab.
- Click on 'Reveal Config Vars' (you might have to scroll down).
- As 'KEY' type or copy 'DATABASE_URL' (without the quotes) and as 'VALUE' the URL of your database
- Click on 'Add'.
- As one more 'KEY' type or copy 'SECRET_KEY' (without the quotes) and as 'VALUE' a random key of your choosing (help: https://randomkeygen.com/ and then at least 'Strong Passwords')
- Click on the 'Resources'-tab and check if there is 'Eco Dynos' as dyno type selected. If not click on 'Change Dyno Type' and change that.
- Check if there are NO add-ons for this app.
- Click on the 'Deploy'-tab.
- Under 'Deployment Method' choose 'GitHub'.
- Search for your copy of the repository and choose it.
- Click on 'Deploy Branch' and wait until the built is done.

## Credits

- Thanks to my Mentor Rohit Sharma from Code Institute. Thank you very much for your help!