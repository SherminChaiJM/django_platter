# Django Platter

## User Credentials

### SuperUser
- **Username:** `sherminchai`
- **Password:** `12345`

### Head Office User
- **Username:** `houser`
- **Password:** `headoffice123`

### District Office User
- **Username:** `douser`
- **Password:** `districtoffice123`

### Branch Location User
- **Username:** `bluser`
- **Password:** `branchlocation123`

<br>

## Webpages and Functions

### Index Page (`index.html`)
- **Login Option:** For existing admins to log in.
- **Create Admin Account:** For creating new admin accounts.

### Create Admin Account (`createadmin.html`)
- **Form Fields:** Username, Email, Password, Confirm Password.
- **Permissions:** Select Head Office checkbox to gain full access.
- **Access:** Can access Head Office, District Office, and Branch Location webpages.
- **Functionality:** Create new users and assign permissions; Add District Office and Branch Location entries.
- **Redirect:** Leads to Login page after successful registration.

### Login Page (`login_view.html`)
- **Form Fields:** Username and Password.
- **Redirect:** Leads to Head Office Dashboard upon successful login.

### Head Office Dashboard (`dashboardHO.html`)
- **Options:** 
  - Head Office Page (`headoffice.html`)
  - District Office Page (`districtoffice.html`)
  - Branch Location Page (`branchlocation.html`)
  - Create New User (`createuser.html`)
  - Add Location (`addlocation.html`)

### Head Office Page (`headoffice.html`)
- **Display:** Information relevant to the Head Office.

### District Office Page (`districtoffice.html`)
- **Display:** List of all District Offices added to the database.

### Branch Location Page (`branchlocation.html`)
- **Display:** Branch locations categorized by District Offices.
- **Note:** Users from Branch Locations are directed to this page upon login.

### Create New User Page (`createuser.html`)
- **Form Fields:** Username, Email, Password, Confirm Password.
- **Permissions:**
  - District Office: Access to District Office and Branch Location pages.
  - Branch Location: Access only to Branch Location page.

### Add Location Page (`addlocation.html`)
- **Functionality:** 
  - Add new District Office entries to the DistrictOfficeList database.
  - Add Branch Location entries and associate them with existing District Offices.
- **Redirect:** Returns to `districtoffice.html` and `branchlocation.html` to view newly added entries.

### District Office Dashboard (`dashboardDO.html`)
- **Options:** 
  - Access both `districtoffice.html` and `branchlocation.html`.
  - Navigate to the respective webpages as needed.

<br>

### IMPORTANT THINGS TO NOTE
- Need to tick the correct checkbox for different users in order to gain access to the webpages
- Required to log in to access the webpages based on the permission granted
- Need to select which districtofficelist to add the branch location to successfully add them to the DistrictOfficeList
