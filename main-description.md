In the main code we just have one import that is a import of a the emailVer code (from emailVer import hibpEmailVerification).

The main code is inside of a "infinite" while loop that just breaks depending on the users answer at the end of one execution, after the insertion of the email by the user the code will do two validations, the first one is if email have "@" into his body and shortly thereafter verifies if the email body have ".com/.tech/.io/.net/etc".

If the email inputted pass both the validations, the inputted email wil be send to the emailVer function to verify if the email have been leaked. If the email was leaked it'll print in the user's screen all the services/web-sites that it was leaked, and if the emails wasn't leaked it'll return a text informing that the email never was leaked.

After all the execution the code will ask to the user if he/she wants to search if another email was leaked, if the user's answer "S" the code will run again, and if the user's inserts any other key or press "Enter" the code breaks.
