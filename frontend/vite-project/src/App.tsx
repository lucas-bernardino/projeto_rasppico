import "./App.css";
import Sensor from "../components/Sensor";
import Action from "../components/Action";

function App() {
  return (
    <div className="app">
      <div className="sensor-div">
        <Sensor />
      </div>
      <div className="div-action">
        <Action />
      </div>
    </div>
  );
}

export default App;

