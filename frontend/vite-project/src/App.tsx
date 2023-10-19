import './App.css'
import Sensor from '../components/Sensor'
import CustomWebcam  from '../components/CustomWebcam'
import WebcamTest from '../components/WebcamTest'

function App() {

  return (
    <div className="App">
      <div className="sensor-div">
        <Sensor />
      </div>
      <div className="webcam-div">
        <WebcamTest />
      </div>
    </div>
  )
}

export default App
