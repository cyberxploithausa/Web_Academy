## What is access control?

Access control is the application of constraints on who or what is authorized to perform actions or access resources. In the context of web applications, access control is dependent on authentication and session management:

- **Authentication** confirms that the user is who they say they are.
- **Session management** identifies which subsequent HTTP requests are being made by that same user.
- **Access control** determines whether the user is allowed to carry out the action that they are attempting to perform.

Broken access controls are common and often present a critical security vulnerability. Design and management of access controls is a complex and dynamic problem that applies business, organizational, and legal constraints to a technical implementation. Access control design decisions have to be made by humans so the potential for errors is high.
![[Pasted image 20240614214457.png]]

## Vertical privilege escalation

If a user can gain access to functionality that they are not permitted to access then this is vertical privilege escalation. For example, if a non-administrative user can gain access to an admin page where they can delete user accounts, then this is vertical privilege escalation.

## Unprotected functionality

At its most basic, vertical privilege escalation arises where an application does not enforce any protection for sensitive functionality. For example, administrative functions might be linked from an administrator's welcome page but not from a user's welcome page. However, a user might be able to access the administrative functions by browsing to the relevant admin URL.

For example, a website might host sensitive functionality at the following URL:

`https://insecure-website.com/admin`

This might be accessible by any user, not only administrative users who have a link to the functionality in their user interface. In some cases, the administrative URL might be disclosed in other locations, such as the `robots.txt` file:

`https://insecure-website.com/robots.txt`

Even if the URL isn't disclosed anywhere, an attacker may be able to use a wordlist to brute-force the location of the sensitive functionality.

## LAB 1:  Unprotected admin functionality
This lab has an unprotected admin panel.

Solve the lab by deleting the user `carlos`.

## Solutions

-> Capture the request and navigate the root directory `/`
-> change to `/robots.txt` and view the response which returns `/administrator-panel` to be disallowed.
![[Pasted image 20240614220219.png]]
-> Visit the `/administrator-panel` page by removing the `robots.txt` 
![[Pasted image 20240614220755.png]]
-> Inspect the response and navigate to the carlos user for deletion `/adminstrator-panel/delete?username=carlos`
![[Pasted image 20240614221139.png]]

## Unprotected functionality - Continued

In some cases, sensitive functionality is concealed by giving it a less predictable URL. This is an example of so-called "security by obscurity". However, hiding sensitive functionality does not provide effective access control because users might discover the obfuscated URL in a number of ways.

Imagine an application that hosts administrative functions at the following URL:

`https://insecure-website.com/administrator-panel-yb556`

This might not be directly guessable by an attacker. However, the application might still leak the URL to users. The URL might be disclosed in JavaScript that constructs the user interface based on the user's role:

```javascript
<script> 
	var isAdmin = false; 
	if (isAdmin) { 
			... var adminPanelTag = document.createElement('a'); 
				adminPanelTag.setAttribute('https://insecure-website.com/administrator-panel-yb556'); 
				adminPanelTag.innerText = 'Admin panel'; 
			...
		 } 
</script>
											
```

This script adds a link to the user's UI if they are an admin user. However, the script containing the URL is visible to all users regardless of their role.
## LAB 2: Unprotected admin functionality with unpredictable URL
This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user `carlos`.

## Solution
-> No need of using burp as it will lead to rabbit hole. `view-page source` and search for the javascript

![[Pasted image 20240614232954.png]]
-> use the above `/admin-h9i6zn` in the browser
![[Pasted image 20240614233143.png]]
## Parameter-based access control methods

Some applications determine the user's access rights or role at login, and then store this information in a user-controllable location. This could be:

- A hidden field.
- A cookie.
- A preset query string parameter.

The application makes access control decisions based on the submitted value. For example:

`https://insecure-website.com/login/home.jsp?admin=true https://insecure-website.com/login/home.jsp?role=1`

This approach is insecure because a user can modify the value and access functionality they're not authorized to, such as administrative functions.

## LAB 3: User role controlled by request parameter
This lab has an admin panel at `/admin`, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
