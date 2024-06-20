// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [variation, setVariation] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(`Fetching variation for email: ${email}`);
    try {
      const response = await axios.get(`http://127.0.0.1:8011/api/feature-flag/${email}/`);
      console.log('Response data:', response.data);
      setVariation(response.data.variation);
    } catch (error) {
      console.error('Error fetching the variation:', error);
      setVariation('Error fetching the variation');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Feature Flag Variation Fetcher</h1>
        <form onSubmit={handleSubmit}>
          <label>
            User Email:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </label>
          <button type="submit">Fetch Variation</button>
        </form>
        {variation && <p>Variation: {variation}</p>}
      </header>
    </div>
  );
}

export default App;
