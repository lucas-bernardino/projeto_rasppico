import Chart from "react-apexcharts";

import { useState, useEffect } from "react";

import "./Chart.css"


interface DataProps {
    sensor_data: any
}

interface ChartData {
    options: {
      chart: {
        id: 'realtime',
        height: 350,
        type: 'line',
      };
      xaxis: {
        categories: string[];
      };
    };
    series: {
      name: string;
      data: number[];
    }[];
  }

const MyChart = ({ sensor_data }: DataProps) => {

    const [chart1, setChart1] = useState<ChartData | null>(null);

    const [createdAt, setCreatedAt] = useState<string[]>([]);
    
    const [pontosY1, setPontosY1] = useState<number[]>([]);

    const [pontosY2, setPontosY2] = useState<number[]>([]);

    const [pontosY3, setPontosY3] = useState<number[]>([]);

    useEffect(() => {

        if (sensor_data && sensor_data.length > 0)
        {

            setCreatedAt([...createdAt, sensor_data[0]["createdAt"].slice(11, 19)]);

            setPontosY1([...pontosY1, sensor_data[0]["acel_x"]]);
    
            setPontosY2([...pontosY2, sensor_data[0]["acel_y"]]);

            setPontosY3([...pontosY3, sensor_data[0]["acel_z"]]);

    
            setChart1({
                options: {
                    chart: {
                      id: "realtime",
                      height: 350,
                      type: 'line',
                    },
                    xaxis: {
                      categories: createdAt
                    }
                  },
                  series: [
                    {
                      name: "series-1",
                      data: pontosY1
                    },
                    {
                      name: "series-2",
                      data: pontosY2
                    },
                    {
                      name:"series-3",
                      data: pontosY3
                    }
                  ]
            })

        }

        
        
    }, [sensor_data])

    

    return (
        <div className="chart-container">
            <div className="sensor-chart">
            {chart1 &&
            <Chart 
            options={chart1.options}
            series={chart1.series}
            width={1000}
            type="line"
            />}
            </div>
        </div>
    )
}

export default MyChart;

// https://www.youtube.com/watch?v=yAI9fbbH-rM

// ESSE VIDEO USA A API QUE TEM TODOS OS DADOS E QUANDO É ADICIONADO MAIS UM NESSA API ELE MUDA O GRÁFICO
// ENTAO, TEM QUE MUDAR O PROPS QUE É PASSADO PRA ESSE COMPONENTE. PQ AGR A GENTE TA PASSANDO SO O ULTIMO
// TEM QUE PEGAR A API QUE MANDA TODOS OS DADOS E USAR NELA. 
