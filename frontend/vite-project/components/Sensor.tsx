import "./Sensor.css";
import { useState, useEffect } from "react";

function Sensor() {
  // dar o fetch na API que recebeu os dados da rasp.

  const [sensorData, setSensorData] = useState([]);

  async function getSensorData() {
    const response = await fetch(import.meta.env.VITE_BACKEND_URL + "/receber_ultimo", {headers: {'ngrok-skip-browser-warning': 'true'}});
    const data = await response.json();
    setSensorData(data);
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
    <div className="sensor-container">
      <div className="sensor-box">
        <div className="sensor-title"> Velocidade Angular</div>
        <div className="sensor-data-title">
          Velocidade Angular X
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["vel_x"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Y
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["vel_y"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Velocidade Angular Z
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["vel_z"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Módulo
          <div className="sensor-data-value">
            {sensorData[0] &&
              Number(
                Math.sqrt(
                  sensorData[0]["vel_x"] ** 2 +
                    sensorData[0]["vel_y"] ** 2 +
                    sensorData[0]["vel_z"] ** 2,
                ),
              ).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Aceleração </div>
        <div className="sensor-data-title">
          Aceleração X
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["acel_x"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Aceleração Y
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["acel_y"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Aceleração Z
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["acel_z"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Módulo
          <div className="sensor-data-value">
            {sensorData[0] &&
              Number(
                Math.sqrt(
                  sensorData[0]["acel_x"] ** 2 +
                    sensorData[0]["acel_y"] ** 2 +
                    sensorData[0]["acel_z"] ** 2,
                ),
              ).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Eixo </div>
        <div className="sensor-data-title">
          Roll
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["roll"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Pitch
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["pitch"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Yaw
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["yaw"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Módulo
          <div className="sensor-data-value">
            {sensorData[0] &&
              Number(
                Math.sqrt(
                  sensorData[0]["roll"] ** 2 +
                    sensorData[0]["pitch"] ** 2 +
                    sensorData[0]["yaw"] ** 2,
                ),
              ).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Magnético </div>
        <div className="sensor-data-title">
          Magnético X
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["mag_x"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Magnético Y
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["mag_y"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Magnético Z
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["mag_z"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Módulo
          <div className="sensor-data-value">
            {sensorData[0] &&
              Number(
                Math.sqrt(
                  sensorData[0]["mag_x"] ** 2 +
                    sensorData[0]["mag_y"] ** 2 +
                    sensorData[0]["mag_z"] ** 2,
                ),
              ).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Esterçamento </div>
        <div className="sensor-data-title">
          Graus
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["esterc"]).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Rotações </div>
        <div className="sensor-data-title">
          RPM
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["rot"]).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Temperatura </div>
        <div className="sensor-data-title">
          Temperatura Atual
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["temp"]).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Velocidade </div>
        <div className="sensor-data-title">
          Velocidade Linear Atual
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["veloc"]).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Posição </div>
        <div className="sensor-data-title">
          Longitude:
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["long"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Latitude:
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["lat"]).toFixed(2)}
          </div>
        </div>
      </div>

      <div className="sensor-box">
        <div className="sensor-title"> Pressão </div>
        <div className="sensor-data-title">
          Velocidade Roda:
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["press_ar"]).toFixed(2)}
          </div>
        </div>
        <div className="sensor-data-title">
          Altitude:
          <div className="sensor-data-value">
            {sensorData[0] && Number(sensorData[0]["altitude"]).toFixed(2)}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Sensor;
