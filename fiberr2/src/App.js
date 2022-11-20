import logo from './logo.svg';
import './App.css';
import Webcam from "react-webcam";
import Info from './Info';
const WebcamComponent = () => <Webcam />;
function App() {
  return (
    <div className="App">
     <WebcamComponent/> 
    <div>
      <Info/>
    </div>
    </div>
  );
}

export default App;
