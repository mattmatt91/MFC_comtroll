import React, { useEffect, useState } from 'react';

function LiveData() {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://gascontrol:8000/data'); // Adjust URL as needed
      const result = await response.json();
      setData(result);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Live Data</h2>
      {/* Render your data in a table or similar structure */}
    </div>
  );
}

export default LiveData;
