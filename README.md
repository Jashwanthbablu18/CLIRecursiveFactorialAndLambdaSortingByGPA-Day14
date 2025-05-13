# 🧠 Day 14 - Lambda Functions & Recursion

Welcome to **Day 14** of my **#30DaysOfPythonChallenge**!  
Today’s focus is on two powerful Python concepts: **Lambda Functions** and **Recursion**.

---

## 📌 Topic
**Lambda Functions** and **Recursion** — essential tools for writing clean, efficient, and expressive code.

---

## 🧠 What I Built

1. 🔁 **Recursive Factorial Calculator**  
   - A function that computes the factorial of a number by calling itself.
   - Demonstrates how recursion breaks a big problem into smaller subproblems.

2. 📊 **Lambda-based GPA Sorter**  
   - A one-liner lambda function that sorts a list of student dictionaries by GPA.
   - Shows how to use lambda with `sorted()` and custom keys.

---

## 🛠️ Concepts Used

- `def factorial(n): return n * factorial(n-1)`
- Lambda syntax: `lambda args: expression`
- `sorted(list, key=lambda x: x['gpa'], reverse=True)`
- Input validation and flow control

---

## 📦 How to Run

```bash
python Day-14Code.py
