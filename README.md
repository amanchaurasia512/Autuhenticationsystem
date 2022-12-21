# Autuhentications
This full authentications by django 
user can login and register
Forgetpassword 
change password


There are a few alternative ways to send email in Django without having to enable the "Less secure app access" option in Google:

Use a third-party email service that provides an API for sending email, such as SendGrid or Mailgun. 
These services usually require you to create an account and obtain an API key, which you can then use to send email through their API.

Use an email client library, such as email, imaplib, or smtplib, to send email directly from Django. 
This option requires more setup and maintenance than using a third-party service, but it allows you to have more control over the email sending process.

Use Django's built-in email sending functionality and specify an SMTP server that does not require the "Less secure app access" option to be enabled. 
For example, you can use an SMTP server provided by your company or hosting provider.
