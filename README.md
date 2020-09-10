# task_manager

This Program allows the user to assign and manage tasks for various team members, writes it to a text file, and presents it in a legible manner.

Users are able to sign in and view tasks assigned to them and track there progress and mark wether the tasks are complete or not.

Users with admin privileges are responsible for assigning tasks to users and are able to view usage statistics. These reports
are generated into 2 seperate text files.

Register user makes sure that no duplicate usernames are made.

Add task lets you add a new task.

When the user selects View Mine:
o Displays all tasks in a manner that is easy to read. .
o Allows the user to select either a specific task by entering a number
or input ‘-1’ to return to the main menu.
o If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task .
If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that
describes whether the task has been completed or not should be
changed to ‘Yes’.
When the user chooses to edit a task, the
username of the person to whom the task is assigned or the due
date of the task can be edited. The task can only be edited if it has
not yet been completed.


task_overview.txt contains:
▪ The total number of tasks that have been generated and
tracked using the task_manager.py .
▪ The total number of completed tasks.
▪ The total number of uncompleted tasks.
▪ The total number of tasks that have'nt been completed and
that are overdue.
▪ The percentage of tasks that are incomplete.
▪ The percentage of tasks that are overdue.

user_overview.txt contains:
▪ The total number of users registered with task_manager.py .
▪ The total number of tasks that have been generated and
tracked using the task_manager.py .
