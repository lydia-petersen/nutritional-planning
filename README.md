<a id="readme-top"></a>

<div align="center">

  <h3 align="center">Nutritional Planning</h3>
  <p align="center">
    A tool to help plan a balanced diet
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-the-program">Running the Program</a></li>
      </ul>
    </li>
    <li><a href="#future-improvements">Future Improvements</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a simple and convenient way to explore the nutritional content of foods.  Users can search for a food item and specify the amount they'd like to consume. The application will then display the complete nutritional breakdown for that serving size.

Key features include:

* **Food Search:** Easily search for a wide variety of foods. The foods and their nutritional qualities are stored in a file database.
* **Custom Amounts:** Specify the exact quantity of food you're interested in. The amount is only measured in grams so far.
* **Nutritional Information:**  View a detailed breakdown of the nutritional value, including protein, carbohydrates, and fats
* **Multiple Food Tracking:** Add multiple food items to your meal and see the combined nutritional totals.  This allows you to easily calculate the nutritional value of entire meals.
* **Food Deletion:** Remove any food item from your tracked list if you change your mind or make a mistake.

This tool is perfect for anyone looking to monitor their diet, track their nutrient intake, or simply learn more about the nutritional content of the foods they eat.  Whether you're following a specific diet, trying to eat healthier, or just curious about food nutrition, this project aims to provide a user-friendly and informative experience.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation

If the follwing are not installed, follow the instructions below to set up your computer:

1. Clone the repo
   ```sh
   git clone https://github.com/lydia-petersen/nutritional-planning.git
   ```
2. Install NPM packages in the 'frontend' folder:
   ```sh
   npm install
   npm install axios
   ```
3. Navigate to the 'backend folder' run the command:
   ```sh
   pip install -r ./requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
### Running the Program

To run the nutritional planning program do the following:

1. Open two different terminals in your code editor
2. Navigate to the 'backend' folder and run the main python file:
   ```sh
   python ./main.py
   ```
3. On the second terminal navigate to the 'frontend' folder and run the command:
   ```sh
   npm run dev
   ```
4. A local URL will appear. Click on it to access the program
   
   Note: If the URL is something other than http://localhost:5173, copy it, add it to the origins list in main.py, and restart the program

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Future Improvements

The functionality of this project is limited at present, but below are some ideas for how to improve it in the future.

* Allow multiple ways to measure the food (e.g. 1 slice of bread instead of 50g)
* Make the database expandable. Create a form where the user can add a food to the database. Integrate AI to search the nutritional qualities of the new food.
* Correlate the nutritional results with the Canadian food guide based on the height and weight of the user so they could see how much they should be eating.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Lydia Petersen

LinkedIn: https://www.linkedin.com/in/lydia-petersen-189434241/

Project Link: [https://github.com/lydia-petersen/nutritional-planning](https://github.com/lydia-petersen/nutritional-planning)

<p align="right">(<a href="#readme-top">back to top</a>)</p>