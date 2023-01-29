import React, { useState } from 'react';
import './App.css';
import { db } from './firebase';

function App() {
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const phoneNumber = e.target.phoneNumber.value;
    if (phoneNumber.length !== 10) {
      setError("Please enter a valid phone number (e.g 1234567890) with area code in front (No Hyphens!)");
      setSuccess("");
      return;
    }
    try {
      await db.collection('phoneNumbers').add({ phoneNumber });
      setSuccess("Success! Be on the lookout for Celestial Events!");
      setError("");
    } catch (error) {
      setError("Error adding phone number to Firestore: " + error);
      setSuccess("");
    }
  }

  return (
    <div className="container">
      <form onSubmit={handleSubmit} className="form">
        <label>
          Phone Number:
          <input type="text" name="phoneNumber" className="input" />
        </label>
        <p className={`message error`}>
            {error}
          </p>
        <button type="submit" className="submit-button">Submit</button>
        <p className={`message success`}>
            {success}
          </p>
      </form>
    </div>
  );
}

export default App;

