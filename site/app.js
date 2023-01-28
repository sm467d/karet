import React from 'react';
import './App.css';
import { db } from './firebase';

function App() {
  const handleSubmit = async (e) => {
    e.preventDefault();
    const phoneNumber = e.target.phoneNumber.value;
    try {
      await db.collection('phoneNumbers').add({ phoneNumber });
      console.log('Phone number added to Firestore');
    } catch (error) {
      console.log('Error adding phone number to Firestore:', error);
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Phone Number:
          <input type="text" name="phoneNumber" />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
