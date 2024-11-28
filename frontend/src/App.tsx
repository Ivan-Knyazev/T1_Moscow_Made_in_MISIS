import { useState } from "react";
import "./App.css";
import MainPage from "./pages/Main";
import DigitalAssistant from "./components/DigitalAssistant";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      {/* <MainPage /> */}
      <DigitalAssistant />
    </>
  );
}

export default App;
