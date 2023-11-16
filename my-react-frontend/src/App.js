import React, { useState } from 'react';
import LiveData from './LiveData';
import SetValues from './SetValues';

function App() {
  const [selectedComponent, setSelectedComponent] = useState('liveData');

  return (
    <div>
      <select onChange={(e) => setSelectedComponent(e.target.value)}>
        <option value="liveData">Live Data</option>
        <option value="setValues">Set Values</option>
      </select>

      {selectedComponent === 'liveData' && <LiveData />}
      {selectedComponent === 'setValues' && <SetValues />}
    </div>
  );
}

export default App;
