# Requisition System

This is a project I made for my assessment at Whitecliffe College. I'm still a beginner at programming, so I kept it simple. It's a purchase requisition system in Python. In my first assessment I did it with separate functions, and this time I made it with one class called Requisition.

## What it does

The program asks for a date, staff ID, staff name and a list of items with prices. It adds up the prices and gives each requisition an ID that starts at 10001.

If the total is under $500, the requisition is approved straight away and gets a reference number: the staff ID plus the last 3 digits of the requisition ID, like FN19001. If the total is $500 or more, it stays pending until the manager answers.

After you enter all the requisitions, it prints them with the statistics. Then the manager goes through each pending one and presses A to approve it, N to not approve it or S to skip it, then Enter. If nothing is pending, it says "No matches for pendings". At the end it prints everything again with the new counts.

## How to run it

Run requisition_system.py with Python and answer each question as it appears. Type numbers for the prices, because letters make it crash. Answer yes to "Add another requisition" to keep going, and no when you're done.

## How I made it

I had never used Git or GitHub before this, so it was all new. I built the code in stages and made a commit after each one.

My second commit failed the first time. Git said "no changes added to commit" because I hadn't saved the file or run git add. After I did both, it worked.