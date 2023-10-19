import './App.css'
import Sensor from '../components/Sensor'
import WebcamUser from '../components/WebcamUser';
import Action from '../components/Action';


function App() {

  return (
    <div className="App">
      <div className="sensor-div">
        <Sensor />
      </div>
      <div className="webcam-info">
        {/* <Webcam width={800} height={400}/> */}
        <WebcamUser />
        <Action />
      </div>
    </div>
  )
}

export default App

// https://github.com/samuelweckstrom/react-record-webcam

// https://stackoverflow.com/questions/67828731/react-webcam-recording-replay-re-recording-storing