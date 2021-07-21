# Reasons for site #
This website has been created to:-
* Encourage people to make changes to their garden
* Suggest garden ideas that will make it more wildlife friendly
* Give people a place to share ideas
* Raise awareness of environmental issues
* Aid conservation
* Provide a source of income by promoting sales of ready-made wildlife friendly products.

# Features
Features across pages and features for individual pages are listed.
A link to the [wireframe](docs/Wildlife_Patch_wireframe.pdf) is provided. The wireframe shows mock-ups of the main pages of the app including views on devices of different screen widths. There have been some changes to the design since the wireframe was created in order to improve the app. 

## Features across all pages
* Navigation bar with links to other pages of the app, dropdown menu for tablet or mobile view.
* Light green background color.
* Colours and styles are the same for each page for navigation bar and background colour.
* Pages are read only unless user registers or logs in.
* Logging in as an admin gives access to more pages and more options for manipulating data.
* There are links to buying ready-made wildlife friendly products so the site can benefit financially.
## Features on pages before the user signs in
* Message encouraging users to sign in
* Navbar menu contains home, surveys, people's projects, create account and login pages
## Features on the pages after the user signs in
* Navbar menu contains home, surveys, people's projects, profile and add own project contact users and logout 
## Features on pages if administrator signs in
* Navbar menu contains home, surveys, people's projects, profile, add own project, manage category, contact users and logout  
## Features on the home page
* The home page contains a list of projects within collapsible elements.
* List of projects selected by the administrator of the website
* There is a search function that targets project name and parts of task description
* There is a reset button linked to the search function to clear the search
## Features on the wildlife surveys page
For the Wildlife Surveys page, the top results are listed 

* Royal Society for the Protection of Birds
* People’s Trust for Endangered Species
* National Biodiversity Network
* National Trust
* The Wildlife Trusts
* Woodlands.co.uk
* Buglife

A link is provided for all these groups on the Surveys page.
This may change over time so the admin has the options to add, edit and delete links.
Everyone can read the links.

## Features on the people's projects page
* The people's projects page contains a list of projects within collapsible elements.
* Projects created by the website's users appear on this page
* There is a search function that targets project name and parts of task description
* There is a reset button linked to the search function to clear the search
## Features on the create account page
* Input fields for username, password, email
* Submit button
* Message and button that redirects user to login in case user already has an account.
## Features on the login page
* Input fields for username, password, email
* Submit button
* Message and button that redirects user to create account in case user doesn't have an account.
## Features on the profile page
* Username appears on the profile page
* User's own projects appear on the page.
* User is able to create, update and delete projects that appear on the profile page.
## Features on the categories page
* Categories are displayed on categories page
* Each category has an edit button and a delete button
* Clicking edit button opens the edit category page
* There is an add category button which opens onto add category page
* This page controls the category choice for the projects that are added to the home page or the people's projects page.
## Features on the add category page
* Input field for category name
* Submit button
* Reset button to return the admin user to categories with no action taken.
## Features on the edit category page
* Input field for category name
* Small images can be added to each category in the form of a url address
* Submit button
## Features on the add project page
* Select category field
* Input fields for task name, task description, finish date, estimated cost, estimated time
* date picker is linked to 'finish date' field to keep consistency of dates in the database
* Submit button
* Username automatically added to database when the submit button is clicked
## Features on the edit project page
* Select category field
* Input fields for task name, task description, finish date, estimated cost, estimated time
* date picker is linked to 'finish date' field to keep consistency of dates in the database
* Submit button

# Data
There is a description of the design of data in the [link](docs/data.pdf)
# Technologies used

* [HTML](https://html.spec.whatwg.org)
* [CSS](https://www.w3schools.com/css/css_website_layout.asp)
* [JQuery](https://jquery.com)
* [Python](https://www.python.org)
* [MongoDB](https://www.mongodb.com)
* [Flask](https://flask.palletsprojects.com)
* [Materialize](https://materializecss.com)

# Testing

## Manual Testing
Across all pages, the nav bar shows a menu of Home, Wildlife Surveys, People's Projects, Create Account, Login.

If user creates an account or logs in, the nav bar menu adjusts to show Home, Wildlife Surveys, People's Projects, Profile, Add own project, Logout.

If user is an administrator, the menu shows Home, Wildlife Surveys, People's Projects, Profile, Add own project, Manage Categories, Contact Users and Logout.
### Home page
The home page contains a list of projects within collapsible elements.
Collapsibles are accordion elements that expand when clicked on, allows information to be hidden if not required by the user.
Add, edit and delete buttons are available if the user is a site administrator (admin)
Typing in the search bar and pressing return or clicking the submit button should reduce the list of projects to only those that match the search words in the project name or project description.
Clicking on the reset button should return the page to the full list of projects that should appear there.
### Wildlife Surveys
The wildlife surveys page contains all the most relevent external links to wildlife surveys.
Add, edit and delete buttons are included if the user is an admin.
### People's Projects
This page should display projects submitted by app users using collapsible elements.
Add, edit and delete buttons are available if the user is a site administrator (admin) or if the project is the user's own project.
Typing in the search bar and pressing return or clicking the submit button should reduce the list of projects to only those that match the search words in the project name or project description.
Clicking on the reset button should return the page to the full list of projects that should appear there.
### Create Account
Form should accept entries for username, password and email address and contain a submit button. Also, there is a link provided at the bottom in case the user already has an account and needs to get to the login page. The page should not allow the form to be submitted without all fields being filled in.
### Login
Form should accept entries for username, password and email address and contain a submit button. Also, there is a link provided at the bottom of the page in case the user does not yet have an account and needs to get to the create account page.
### Profile page
Profile page should show username and all projects submitted by that user only. It also allows the user to create, read, update and delete any of those projects.
### Add own project
This page should request category name, task name, task description, estimated cost, estimated time to complete, image as a url address and an image description. All categories are required except the category name, because a project may not fit easily into a category due to the variety within conservation and wildlife topics. If the admin chooses to move the project up to the home page, a category can be chosen or a new one can be created to accommodate the project.
### Manage Categories
This page is displayed if the user is an admin, it displays all the project categories.
The admin is allowed to create, update and delete categories so that the admin can control the project categories.
### Contact Users
This page is displayed if the user is an admin, it displays all usernames with contact emails. This is useful, for example, if the admin moves a project up to the home page list because it is a good project. 
### Logout
If clicked, a message will flash that says 'You have logged out'. The nav bar menu should adjust to show Home, Wildlife Surveys, People's Projects, Create Account, Login as before.
### Responsiveness
Check that different screen-widths display correctly for all devices.
See [link](docs/Responsiveness.pdf)
### Web browsers
Check that the app displays correctly for different browsers, Chrome, Microsoft Bing, Firefox, Avast

## Testing tools
### Code validators
Check that HTML and CSS code is free from errors, see [link](docs/Code_validators.pdf)
### JavaScript code quality
Check that Javascript code is free from errors, see [link](docs/JShint.pdf)
### Python validation
Check that Python code is free from errors, see [link](docs/Python_validation.pdf)
### Performance
Check that the app performance is acceptable using [Lighthouse](docs/Lighthouse_performance.pdf) (in Chrome browser). The initial performance results were used to make improvements to readability of text, and a meta description was added.
# Bugs
One bug was created by incorrect addresses for css and JavaScript [see link](docs/Bugs.pdf)

# Credits
[Random keygen](https://randomkeygen.com). This website generates passwords and secret keys that are hard to crack. One was used for the Flash secret key from Env.py file in this project.

[Font Awesome](https://fontawesome.com). This website is useful for icons, several are used in this project.

[W3C Markup Validation service](https://validator.w3.org). This website checks HTML code and provides a report.

[W3C CSS Validation service](https://jigsaw.w3.org/css-validator). This website checks CSS code and provides a report.

[JShint](https://jshint.com), This website test Javascript for errors and issues.

[Snyk](https://snyk.io), This website tests Python code for errors.

Tim Nelson’s miniproject from Code Institute. This project was useful as a template because it used MongoDB for the database, it used flash messages, it displayed projects in a task manager app, it had create account, login and user profile pages.
## Media
The following images were taken from [Pixabay](https://pixabay.com)

[Chrysanthemums](https://cdn.pixabay.com/photo/2019/04/21/01/12/chrysanthemum-4143241__340.jpg)

[Sunflower](https://cdn.pixabay.com/photo/2016/09/04/12/05/sun-flower-1643795_960_720.jpg)

[Bug-shelter](https://cdn.pixabay.com/photo/2018/04/22/11/05/background-3340740_960_720.jpg)

[Flower](https://cdn.pixabay.com/photo/2018/07/29/21/32/flowers-3571119_960_720.jpg)

[Flower](https://cdn.pixabay.com/photo/2018/07/15/00/39/flowers-3538726_960_720.jpg)

[bugs](https://cdn.pixabay.com/photo/2014/06/15/11/00/bug-369229__340.jpg)

[birds](https://cdn.pixabay.com/photo/2020/01/25/10/35/blue-tit-4792149_960_720.jpg)

[bats](https://cdn.pixabay.com/photo/2020/02/28/13/21/bat-4887509_960_720.jpg)

[hedgehogs](https://cdn.pixabay.com/photo/2018/09/25/21/54/hedgehog-3703244_960_720.jpg)

[aquatic life](https://cdn.pixabay.com/photo/2019/10/04/22/07/frog-4526640_960_720.jpg)

[food](https://cdn.pixabay.com/photo/2018/08/12/19/49/grains-3601581__340.jpg)

[maintenance](https://cdn.pixabay.com/photo/2017/08/03/16/44/landscape-2577207__340.jpg)

[pest control](https://cdn.pixabay.com/photo/2016/06/07/07/46/snail-1441138_960_720.jpg)

[shelter](https://cdn.pixabay.com/photo/2015/12/09/18/12/insect-house-1085197_960_720.jpg)

[ponds](https://cdn.pixabay.com/photo/2016/06/07/20/20/water-lilies-1442497__340.jpg)




