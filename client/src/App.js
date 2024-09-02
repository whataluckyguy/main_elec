import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000")
      .then((res) => res.json())
      .then((fetchedData) => setData(fetchedData.message));
  }, []);

  return <h1>{data}</h1>;
}

export default App;
