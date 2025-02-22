import React, { useEffect, useState} from 'react';
import api from '../api.js';
import './searchFoodForm.css';

const SearchFoodForm = ({ searchFood }) => {
    const [allFoods, setAllFoods] = useState([]);
    const [foodName, setFoodName] = useState('');
    const [amount, setAmount] = useState(0);

    const namesList = async () => {
        const response = await api.get('/names-list');
        console.log("Names:");
        console.log(response.data.names);
        setAllFoods(response.data.names);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        if (foodName) {
            searchFood(foodName, amount);
            //setFoodName('');
        }
    }

    useEffect(() => {
        namesList();
    }, [])

    return (
        <form onSubmit={handleSubmit}>
            <div className='form-element'>
                <label>Food:</label>
                <input 
                    type='text' 
                    list='names-list'
                    value={foodName}
                    onChange={(e) => setFoodName(e.target.value)}
                    placeholder='Search food...'
                />
                <datalist id='names-list'>
                    {allFoods.map((name, index) => (
                        <option key={index} value={name}>{name}</option>
                    ))}
                </datalist>
            </div>
            <div className='form-element'>
                <label>Amount (g):</label>
                <input 
                    type='number'
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                />
            </div>
            <button type='submit' className='form-element'>Add</button>
        </form>
    )
}

export default SearchFoodForm;