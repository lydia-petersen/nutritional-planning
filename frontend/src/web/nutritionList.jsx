import React, { useEffect, useState } from 'react';
import api from '../api.js';
import './nutritionList.css'
import './searchFoodForm.jsx';
import SearchFoodForm from './searchFoodForm.jsx';


const NutritionList = () => {
    const [foods, setFoods] = useState([]);
    const [totals, setTotals] = useState(new Array(7).fill(0));
    //[0]=name, [1]=amount(g), [2]=calories, [3]=protein, [4]=carbs, [5]=sugar, [6]=fat, [7]=sodium

    const searchFood = async (foodName, amount) => {
        try {
            const response = await api.get('/foods/' + foodName + '/amount/' + amount);
            console.log("Response:");
            console.log(response.data)
            let newFood = [foodName, parseFloat(amount), parseFloat(response.data.cals), parseFloat(response.data.protein), parseFloat(response.data.carbs), parseFloat(response.data.sugar), parseFloat(response.data.fat), parseFloat(response.data.sodium)];
            let newTotals = []
            for (let i = 0; i < totals.length; ++i) {
                newTotals.push(Math.round((totals[i] + newFood[i+1]) * 100, 2) / 100);
            }
            setTotals(newTotals);

            setFoods([...foods, newFood]);
        } catch (e) {
            console.error("Error finding food choice:", e);
        }
    };

    const deleteFromTable = (event) => {
        console.log(event.target.value);
        let index = parseInt(event.target.value);
        let toBeRemoved = foods[index];
        let newTotals = [];
        for (let i = 0; i < totals.length; ++i) {
            newTotals.push(Math.round((totals[i] - toBeRemoved[i+1]) * 100, 2) / 100);
        }
        setTotals(newTotals);
        setFoods(foods.filter((food, i) => i !== index));
    }

    return (
        <>
        <SearchFoodForm searchFood={searchFood} />
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Amount (g)</th>
                    <th>Calories</th>
                    <th>Protein</th>
                    <th>Carbs</th>
                    <th>Sugar</th>
                    <th>Fat</th>                    
                    <th>Sodium</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {foods.map((food, i) => (
                    <tr key={i}>
                        {food.map((nutrient, j) => (
                            <td key={j}>{nutrient}</td>
                        ))}
                        <td>
                            <button value={i} onClick={deleteFromTable} className='delete'>X</button>
                        </td>
                    </tr>
                ))}
            </tbody>
            <tfoot>
                <tr key={foods.length}>
                    <td>Total:</td>
                    {totals.map((value, i) => (
                        <td key={i}>{value}</td>
                    ))}
                    <td></td>
                </tr>
            </tfoot>
        </table>
        </>
    );
};

export default NutritionList;