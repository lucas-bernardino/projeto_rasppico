import './Sensor.css'
import { useState, useEffect } from "react";

function Sensor() {

  // dar o fetch na API que recebeu os dados da rasp.

  const [sensorData, setSensorData] = useState([]);

  async function getSensorData() {
    const response = await fetch("http://127.0.0.1:3000/receber_ultimo");
    const data = await response.json();
    setSensorData(data);
    console.log(data);
    //console.log(sensorData[0]);
  }

  useEffect(() => {

    const interval = setInterval(() => {
      getSensorData();
    }, 100);

    return () => clearInterval(interval);
  }, []); // https://iq.js.org/questions/react/how-to-update-a-component-every-second

  // SE NAO RODAR DA PRIMEIRA VEZ, PRECISA RODAR O SERVIDOR, RODAR O PYTHON REQUEST, COMENTAR TODO ESSE RETURN, CARREGAR A PAGINA, DEPOIS DESCOMENTA O RETURN E VAI ESTAR TUDO OK
  // ARRUMAR ESSE BUG

  return (
    <div className='sensor-container'>
      
      <div className="sensor-box">
        <div className="sensor-title"> Velocidade </div>
        <div className="sensor-data-title">
          Velocidade Angular X
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["vel_x"]}</div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Y
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["vel_y"]}</div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Z
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["vel_z"]}</div>
        </div>
      </div>
    
      <div className="sensor-box">
        <div className="sensor-title"> Aceleração </div>
        <div className="sensor-data-title">
          Aceleracao Angular X
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["acel_x"]}</div>
        </div>
        <div className="sensor-data-title">
          Aceleracao Angular Y
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["acel_y"]}</div>
        </div>
        <div className="sensor-data-title">
          Aceleracao Angular Z
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["acel_z"]}</div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Eixo </div>
        <div className="sensor-data-title">
          Roll
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["roll"]}</div>
        </div>
        <div className="sensor-data-title">
          Pitch
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["pitch"]}</div>
        </div>
        <div className="sensor-data-title">
          Yaw
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["yaw"]}</div>
        </div>
      </div>
    
      <div className="sensor-box">
        <div className="sensor-title"> Magnético </div>
        <div className="sensor-data-title">
          Magnético X
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["mag_x"]}</div>
        </div>
        <div className="sensor-data-title">
          Magnético Y
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["mag_y"]}</div>
        </div>
        <div className="sensor-data-title">
          Magnético Z
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["mag_z"]}</div>
        </div>
      </div>


      <div className="sensor-box">
        <div className="sensor-title"> Esterçamento </div>
        <div className="sensor-data-title">
          Graus
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["temp"]}</div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Rotações </div>
        <div className="sensor-data-title">
          RPM
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["temp"]}</div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Temperatura </div>
        <div className="sensor-data-title">
          Temperatura Atual
          <div className="sensor-data-value">{sensorData[0] && sensorData[0]["temp"]}</div>
        </div>
      </div>

    </div>
  )
}

export default Sensor
