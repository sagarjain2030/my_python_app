import React, { useState } from 'react';

function App() {
  const [result, setResult] = useState(null);

  const fetchResult = async () => {
    const response = await fetch('/api/add/1/2');
    const data = await response.json();
    setResult(data.result);
  };

  return (
    <div>
      <button onClick={fetchResult}>Add 1 and 2</button>
      {result && <p>Result: {result}</p>}
    </div>
  );
}

export default App;
