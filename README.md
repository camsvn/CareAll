# CareAll v0.1


## Features
CareAll is a python module which can be used for following functionalities:

* User Creation.
>Two types of users are available 'CareSeekers' and 'CareTakers'.
* Job creation and selection of applicants functionalities for CareSeekers.
* View jobs and apply for jobs functionalities for CareTakers.
* Limits the number users CareTakers can serve to 4.
* Wallet/Salary for CareTakers.
* Review and rating feature for both the users.
* View report functionality.

## Running the tests

Execute test.py ,automates tesing process and show results

### And coding style tests

Allow careseeker to create a new job and restrict creating another job while current job is active

```
careseeker.jobcreate(salary)
```

List active jobs for caretaker

```
caretaker.jobview()
```

Allow caretakers to apply for available active jobs

```
caretaker.apply(option)
```

List the users applied for specific careseekers

```
careseeker.viewapplication()
```

Allows careseekers to approve the applicants for the job.

```
careseeker.jobaccept()
```

Allow both careseekers and caretakers to review and rate themselves 

```
Person.review()
```

Shows the results of caretaker,careseeker couple and list of careseekers cared by caretaker

```
Person.report()
```
## Diagrams

Class Diagram:

![Image of Class Diagram for careall.py](https://github.com/camsvn/CareAll/blob/master/Class%20Diagram.png)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
