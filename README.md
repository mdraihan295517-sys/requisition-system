# Requisition System

Hi, this is a project I made for my assessment at Whitecliffe College. I'm still a beginner at programming, so it's pretty simple. It's a purchase requisition system in Python. In my first assessment I wrote it with separate functions, and this time I rebuilt it as one class called Requisition.

## What it does

Someone enters their date, staff ID, name and a list of items with prices. The program adds up the prices and gives the requisition an ID, starting from 10001.

If the total is under $500, it's approved straight away and gets a reference number: the staff ID plus the last 3 digits of the requisition ID, like FN19001. If it's $500 or more, it stays pending until a manager approves it or says no.

You can print all the requisitions, and the program counts how many are approved, pending and not approved.

## How to run it

Run requisition_system.py with Python. It makes 5 test requisitions and prints them with the counts. Then the manager answers the ones over $499 and everything prints again. At the end it asks if you want to enter your own requisition. Type no to stop.

## How I made it

I'd used GitHub for few times before this, so it was little bit new for me. I made 3 commits for the code: the class with __init__, the add and approve methods, and then the rest of the methods with the tests.

My second commit failed the first time. Git said "no changes added to commit" because I hadn't saved the file or run git add. Once I did both, it went through.

