import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [product, setProduct] = useState("");
  const [margin, setMargin] = useState(20);
  const [data, setData] = useState(null);

  const handleSubmit = async () => {
    const res = await axios.post(import.meta.env.VITE_API_URL + "/scrape", {
      product,
      condition: "new",
      margin,
      marketplaces: ["amazon", "ebay", "walmart", "etsy"]
    });
    setData(res.data);
  };

  return (
    <div className="p-4">
      <input className="border p-2" placeholder="Product name" onChange={(e) => setProduct(e.target.value)} />
      <input className="border p-2 ml-2" type="number" value={margin} onChange={(e) => setMargin(e.target.value)} />
      <button onClick={handleSubmit} className="bg-blue-500 text-white px-4 py-2 ml-2">Scrape</button>
      {data && (
        <div className="mt-4">
          <h2 className="text-xl">Recommended Price: {data.recommended_price}</h2>
          <ul>
            {data.results.map((r, i) => <li key={i}>{r.marketplace}: ${r.price}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
