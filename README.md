# goit-python-hw-08

You need to implement a useful function to display a list of colleagues who need to be congratulated on their birthdays this week.

You have a list of vocabularies called users, each vocabulary in it must have the keys name and birthday. This structure represents a model of a list of users with their names and birthdays. name is a string with the user's name, and birthday is a datetime object that contains the birthday.

Your task is to write a function get_birthdays_per_week that takes a list of users as input and prints to the console (using print) a list of users who need to be congratulated by day.
Terms of acceptance

get_birthdays_per_week displays birthdays in the format:

```
Monday: Bill, Jill
Friday: Kim, Jan
```

Users who had a birthday on the weekend should be congratulated on Monday.
For testing purposes, it is convenient to create a test list of users and fill it in yourself.
The function displays users with birthdays a week ahead of the current day.
The week starts on Monday.
