--- User Credentials ---
1. SuperUser (Access Admin Page)
-> username: sherminchai
-> password: 12345

2. Head Office User
-> username: houser
-> password: headoffice123

3. District Office User
-> username: douser
-> password: districtoffice123

4. Branch Location User
-> username: bluser
-> password: branchlocation123



--- Webpage Explantion and Functions ---
Index Page(index.html)
-> Login Option (For admin who has created an account)
-> Create Admin Account (For new admins)

Create Admin Account(createadmin.html)
-> Fill up username, email, password and confirm password fields
-> Select the head office checkbox to gain permission
-> Can access head office, district office and branch location webpages
-> Can create new user and assign permission to them
-> Can add district office and branch location accordingly to the database
-> Lead to Login page after admin register successfully

Login Page(login_view.html)
-> Enter username and password
-> Lead to Head Office Dashboard

Head Office Dashboard(dashboardHO.html)
-> Admin can choose the different options available on this page
-> Head Office Page -> headoffice.html
-> District Office Page -> districtoffice.html
-> Branch Location Page -> branchlocation.html
-> Create New User -> createuser.html
-> Add Location -> addlocation.html

Head Office Page(headoffice.html)
-> Display headoffice.html 

District Office Page(districtoffice.html)
-> Display all the district office that I have added in the database

Branch Location Page(branchlocation.html)
-> Display all the branch locations based on their district in different categories
-> A user from the branch location will automatically be directed to this page upon log in

Create New User Page(createuser.html)
-> Fill up the username, email, password and confirm password fields
-> Select the checkbox according to which permission you want to grant them access to
-> District Office - Can access district office and branch location webpages
-> Branch Location - Can only access branch location webpage

Add Location Page(addlocation.html)
-> Allow admin to add district office name to the DistrictOfficeList database
-> Allow admin to add branch location name and add them to the different district available accordingly
-> Go back to the districtoffice and branchlocation webpages to see the newly added entries

District Office Dashboard(dashboardDO.html)
-> Allow a user from the district office to access both the districtoffice and branchlocation webpages
-> Choosing the options will lead them to the respective webpage



--- IMPORTANT THINGS TO NOTE ---
-> Need to tick the correct checkbox for different users in order to gain access to the webpages
-> Required to log in to access the webpages based on the permission granted
-> Need to select which districtofficelist to add the branch location to successfully add them to the DistrictOfficeList
