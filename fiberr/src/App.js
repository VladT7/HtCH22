import logo from "./logo.svg";
import "./App.css";
import Home from "./pages/Home";
import { BrowserRouter, Route, Routes, useNavigate } from "react-router-dom";

function App() {

  return (
      <div className="App">
        <Home />
      </div>
  );
}

export default App;
