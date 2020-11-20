# DISRUPT 21 - CYBERSECURITY FIAP CHALLENGE

This project was made to the Disrupt 21 Cybersecurity Challenge. The objective was to create a software that exposes data leaks.

## Objective
This code needs to read the email that tou input into the code execution window and after that it will query into HaveIBeenPwnd database searching for the inputted email, if the code finds some breach where your email was leaked, it will return to the user ther service/web-sites where the email was leaked.

## Code operation
### main.py

The main.py file is the initial file, so you have to run this file to work. After you start the execution of the file it will ask you to input an email, after that the code will do some validations to confirm if the email is a valida account to search, validations like if it have a "@" in the email and if the email have a valid end like .com/.net/.tech/.io, if the inputted email pass by these validations, so the main code will send the inputted email to the emailver.py.

### emailVer.py
The emailVer.py is the code responsible for make the request into HaveIBeenPwned database, and depending of the return it will show a determined value into the user's screen, if the request returns that the email was leaked, so in the user's screen will be printed all the breachs where it was leaked, but if the request returns that the email never war leaked so the code will print that the email never was leaked.

At the end of all it will ask you if do you want to make another search, if yes it'll ask the user again for other email, but if not the user just have to press any key that isn't "S" and press "Enter" or just press "Enter" and the code will end.

For more details about how the code works, please click in one of the links to check out : [main.py](https://github.com/Aracrack/motu_cybersecurity_disrupt21/blob/main/main-description.md), [emailVer.py](https://github.com/cruquera/motu_cybersecurity_disrupt21/blob/main/emailVer-description.md).
