# Models

## User

A user represent a single Twiduler account, it's a [User](https://docs.djangoproject.com/fr/1.9/ref/contrib/auth/#user-model) from **django.contrib.auth**

name | description
-----|------------
username | Required. 30 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.
first_name | Optional. 30 characters or fewer.
last_name | Optional. 30 characters or fewer.
email | Optional. Email address.
password | Required. A hash of, and metadata about, the password. (Django doesn't store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the [password documentation](https://docs.djangoproject.com/en/1.9/topics/auth/passwords/).
groups | Many-to-many relationship to Group
user_permissions | Many-to-many relationship to Permission
is_staff | Boolean. Designates whether this user can access the admin site.
is_active | Boolean. Designates whether this user account should be considered active. We recommend that you set this flag to False instead of deleting accounts; that way, if your applications have any foreign keys to users, the foreign keys won’t break. This doesn’t necessarily control whether or not the user can log in. Authentication backends aren’t required to check for the is_active flag, and the default backends do not. If you want to reject a login based on is_active being False, it’s up to you to check that in your own login view or a custom authentication backend. However, the AuthenticationForm used by the login() view (which is the default) does perform this check, as do the permission-checking methods such as has_perm() and the authentication in the Django admin. All of those functions/methods will return False for inactive users.
is_superuser | Boolean. Designates that this user has all permissions without explicitly assigning them.
last_login | A datetime of the user’s last login.
date_joined | A datetime designating when the account was created. Is set to the current date/time by default when the account is created.
