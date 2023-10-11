import './Sensor.css'


function Sensor() {

  return (
    <div className='sensor-container'>
      
      <div className="sensor-box">
        <div className="sensor-title"> Velocidade </div>
        <div className="sensor-data-title">
          Velocidade Angular X:
          <div className="sensor-data-value">90.45</div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Y:
          <div className="sensor-data-value">80.87</div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Z:
          <div className="sensor-data-value">70.12</div>
        </div>
      </div>
    
      <div className="sensor-box">
        <div className="sensor-title"> Aceleração </div>
        <div className="sensor-data-title">
          Aceleracao Angular X:
          <div className="sensor-data-value">90.45</div>
        </div>
        <div className="sensor-data-title">
          Aceleracao Angular Y:
          <div className="sensor-data-value">80.87</div>
        </div>
        <div className="sensor-data-title">
          Aceleracao Angular Z:
          <div className="sensor-data-value">70.12</div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Eixo </div>
        <div className="sensor-data-title">
          Roll:
          <div className="sensor-data-value">90.45</div>
        </div>
        <div className="sensor-data-title">
          Pitch:
          <div className="sensor-data-value">80.87</div>
        </div>
        <div className="sensor-data-title">
          Yaw:
          <div className="sensor-data-value">70.12</div>
        </div>
      </div>
    
      <div className="sensor-box">
        <div className="sensor-title"> Magnético </div>
        <div className="sensor-data-title">
          Magnético X:
          <div className="sensor-data-value">90.45</div>
        </div>
        <div className="sensor-data-title">
          Magnético Y:
          <div className="sensor-data-value">80.87</div>
        </div>
        <div className="sensor-data-title">
          Magnético Z:
          <div className="sensor-data-value">70.12</div>
        </div>
      </div>

    </div>
  )
}

export default Sensor
