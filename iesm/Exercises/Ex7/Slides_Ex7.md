---
title: Exercise Session 7
subtitle: IESM Fall 2022-2023
date: December 9, 2022
author: "Andrea Levy, Beatriz Bueno Mouriño, Simon Dürr, Sophia Johnson" 
output: beamer_presentation
---

# Course Reminders

Course Reminders:

* No interviews today! Report and interviews for Exercise 6 will be due Monday 12.12. 
* Exercise 7 will extend over two sessions: Friday 09.12 and Monday 12.12. 
* Exercises 8 and 9 will not have interviews and will have due dates in January. Plus, we only keep the best grades of 8 of 9 reports : )
* Oral exam schedule will be sent on Moodle today

# Exercise 7 - Troubleshooting, Pitfalls, Traps
In this set of exercises, we will practice recognizing and accounting for common problems we face in computational chemistry. Get excited for error messages.

![](/data/iesm/img_slides/Ex7/ex7_goals.png) 

# Coding & Input Errors
* In the first part of exercise 7, we’ll hunt for output mistakes which typically arrive via two vectors: the coding or the system input.


	![](/data/iesm/img_slides/Ex7/ex7_errors.png){width=75%}


# Accounting for Dispersion Effects
* Sometimes we code well and provide a viable system input but we didn't carefully evaluate the methods or tools we need to describe our system and its properties adequately.

* In the second part of exercise 7, we'll evaluate the types of systems easily described by DFT and which types of systems may need special consideration. 


# Accounting for Dispersion Effects (continued)
* Some functionals are better at accounting for dispersion interactions:
$$E_{\text{disp}} \propto - C_6/R^6$$
* Some functionals are designed to take dispersion effects into account:
$$v_C^{nl}(\mathbf{r}) = \int f(\mathbf{r},\mathbf{r}')\,d\mathbf{r}'$$
* Other functionals can be improved with corrective functions. D3 and BJ corrections are popular. Here's a D3 correction format:
$$E_{\text{B3LYP-D3}} = E_{\text{B3LYP}} + E_{\text{D3, 2-body}} + E_{\text{ATM, 3-body}}$$

# Choosing Integration Grid Size
* Additionally, we can benefit from thinking about how our software performs a calculation and benchmark some of the software parameters. 
* So in the last part of the exercise we evaluate our integration grid parameters. The density of the integration grid can become a crucial factor in an accurate calculation, especially for newer DFT functionals. 
* "The integration is usually performed on a three-dimensional real-space grid obtained by partitioning the multicenter integral into atomic contributions using a nuclear weight function."
* "The Lebedev-Euler-Maclaurin integration grids are represented by two numbers—n,m—with n denoting the number of radial points and m the number of angular points. "

Images and quoted text from: Morgante, M and Peverati, R. Int. J. Quantum Chem. 2020. https://doi.org/10.1002/qua.26332


# Choosing Integration Grid Size (continued)
 ![](/data/iesm/img_slides/Ex7/ex7_grid.png){width=80%}

Images and quoted text from: Morgante, M and Peverati, R. Int. J. Quantum Chem. 2020. https://doi.org/10.1002/qua.26332

# Exercise 7 - Tips
**Tips!**

Some suggestions:

* Troubleshoot together. It's more fun and effective! And realistic!
* Some calculations make take time to run. Calculations for the second part of Ex 7 can be done collaboratively using the [same sheet](https://docs.google.com/spreadsheets/d/1Yv4AvdKp-8laRF9-oGNbqaUAOvYGqgJF-sCjOWPguEw/edit) as we did for exercise 6 (also posted on Moodle).
* For the first part of the exercises, you can write the report by describing or showing the error and then describing how you solved it. 

