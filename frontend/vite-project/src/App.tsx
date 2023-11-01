import './App.css'
import Sensor from '../components/Sensor'
import WebcamUser from '../components/WebcamUser';
import Action from '../components/Action';
import Chart from '../components/Chart';
import SendChart from '../components/SendChart';


function App() {

  return (
    <div className="App">
      <div className="sensor-div">
        <Sensor />
      </div>
      <div className="webcam-info">
        {/* <WebcamUser /> */}
        <Action />
      </div>
      <div>
        <SendChart />
      </div>
    </div>
  )
}

export default App

// https://github.com/samuelweckstrom/react-record-webcam

// https://stackoverflow.com/questions/67828731/react-webcam-recording-replay-re-recording-storing