import { useEffect, useState } from "react";
import MyChart from "./ChartTeste";

const SendChart = () => {
  const [sensorData, setSensorData] = useState();
  async function fetchData() {
    const response = await fetch(import.meta.env.VITE_BACKEND_URL + "/receber_ultimo", {headers:  {'ngrok-skip-browser-warning': 'true'}});
    const data = await response.json();
    setSensorData(data);
    // console.log(data);
    //console.log(sensorData[0]);
    console.log("ESTOU NA SENDCHART");
  }

  useEffect(() => {
    const timer = setInterval(() => {
      fetchData();
    }, 100);
    return () => {
      clearInterval(timer);
    };
  }, []);

  return <MyChart sensor_data={sensorData} />;
};

export default SendChart;
