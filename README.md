

## florclick.cart (e-commerce website testing)

### Description:
This project was created as an example of my work on a framework of automated website testing. 

Used:
* Python
* Selenium
* Behave (Gherkin/BDD)
* Allure reports


### Prerequisites:

Python installed is required. [Tutorial here](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/)

Allure installed is required too. [Tutorial here](https://www.programsbuzz.com/article/how-install-allure-windows) 

You also need to have installed Java to get Allure reports. [Tutorial here](https://devwithus.com/install-java-windows-10/)


### How to run it:
After downloading the repository on your local machine, execute the following steps:

* Install Selenium on terminal
```
pip install selenium
```
* Install Behave on terminal
```
pip install behave
```
* Install Allure on terminal
```
pip install allure-behave
```

Then, run the test in the terminal as it follows:
```
behave -f allure_behave.formatter:AllureFormatter -o reports/ features
```
It will create a .json file into the 'reports' folder.
For converting the .json file into an Allure report, execute this command in the terminal:

```
allure serve reports/
```

### Author:
Mercedes Pérez [MerPC](https://github.com/MerPC)

[mmcomesana@protonmail.com](mailto:mmcomesana@protonmail.com)

### License:
Distributed under the [MIT License](https://license.md/licenses/mit-license/)


