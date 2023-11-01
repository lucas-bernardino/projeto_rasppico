import { useEffect, useState } from "react"
import MyChart from "./ChartTeste";


const SendChart = () => {

    const [sensorData, setSensorData] = useState();
    async function fetchData() {
        const response = await fetch("http://150.162.217.130:3000/receber_ultimo");
        const data = await response.json();
        setSensorData(data);
        // console.log(data);
        //console.log(sensorData[0]);
      }

    useEffect(() => {
        const timer = setInterval(() => {
            fetchData()
        }, 100);
        return () => { clearInterval(timer) }
    }, [])

    return (
        <MyChart sensor_data={sensorData} />
    )
}

export default SendChart