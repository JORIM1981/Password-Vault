# Password-Vault   [![codebeat badge](https://codebeat.co/badges/6abc3126-4580-41a0-bc48-d44f9327fdeb)](https://codebeat.co/projects/github-com-jorim1981-password-vault-master)  
#### 22/05/2020
#### By **Jorim Midumbi Okong'o Opondo**
## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves. 

## User Stories

- As a user, you can create a password vault account with your details, a login username and password.
- As a user, you can store your already existing account credentials in the application. 
- As a user, you can create new account credentials in the application. 
- As a user, you have the option of putting in a password that you want to use for the new credential account.
- As a user, you can view your various account credentials and their passwords in the application.
- As a user, you can delete a credentials account that you no longer need in the application.


## Requirements

- Python version 3.8.2.
- Pip version 3
- Pyperclip

##### Technologies Used

- This project was generated with [Python version 3.8.2.]

##### Setup Instructions and Installation

- Clone this repository to a location in your file system.`git clone https://github.com/JORIM1981/Password-Vault.git`
- Open terminal command line then navigate to the root folder of the application.
- code . or atom . based on the text editor you have.
- To run the application, open the cloned file in terminal and run the following commands:
        $ chmod +x interface.py
        $ ./run.py
- To run test for the application
        $ python3 user_test.py


## Behaviour Driven Development

 Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./interface.py```|Hello Welcome to your Accounts Password Vault... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|


## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs

If you find a bug, kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.


## Contact Information

If you have any question or contributions, please email me at [okongo.midumbi.opondo@gmail.com]


### License

*MIT*
Copyright (c) 2020 **Jorim Midumbi Okongo Opondo**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
