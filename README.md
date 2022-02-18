# Sudoku Solver

## Aim of the project
This project was developed as a final project in the first semester of university.

## The problem of solving sudoku
Sudoku is an **exact cover** problem, meaning that in order to solve sudoku correctly a set of constraints must by satisfied under the condition that each constraint is satisfied exactly once. These constraints for 9x9 sudoku are:
1. Each square must be filled with exactly one number.
2. In each row there must be each number from 1 to 9 exactly once.
3. In each column there must be each number from 1 to 9 exactly once.
4. In each block of 3x3 there must be each number from 1 to 9 exactly once.

## Algorithm X
Algorithm X is used to find an exact cover for a given sudoku. When an exact cover is found, then a solution which satisfies all constraints is found.

## Dancing Links
Dancing Links is a technique used to represent a table used by Algorithm X. Instead of using 2D array, linked lists are used. The main advantage of this approach is that for every cell it is easy to find the nearest neighbouring cell containing 1 because every cell contains a reference to nearest neighbouring cell containing 1. Also by altering links in a column or in a row it is easy to delete or "undelete" any column or row from the table.

## Modes of the application
1. Application has a mode called **Sudoku Solver** which takes an incomplete sudoku as an input and returns a solution (if there is one).
2. Mode **Sudoku Helper** is supposed to guide the user through the solution. The user can either check the partial solution or if they do not know how to continue with the solution, they can request a hint.
