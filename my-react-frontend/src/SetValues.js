import React, { useState } from 'react';

function SetValues() {
  const [commands, setCommands] = useState({
    wash: { gas_1: false, gas_2: false, solid: false },
    mix: { gas_1: 0, gas_2: 0, solid: 0 },
    total_flow: 0,
    portion_wet: 0,
    flow_wash: 0,
  });

  const handleSubmit = async () => {
    await fetch('/exec_cmds', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(commands),
    });
  };

  // Add input fields for each value in the commands object
  // Use checkboxes for boolean values and input fields for numbers

  return (
    <div>
      <h2>Set Values</h2>
      {/* Form elements to modify the commands state */}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default SetValues;
