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
        axisTicks: {
          show: true, // Show X-axis ticks
          color: string, // Set the color of X-axis ticks
        },
        labels: {
          style: {
            colors: string, // Set the color of X-axis labels
          },
        },
      };
      yaxis: {
        min: number, // Set the minimum value for the Y-axis
        max: number, // Set the maximum value for the Y-axis
        labels: {
          style: {
            colors: string[], // Set the color of Y-axis labels
          },
        },
        axisTicks: {
          show: true, // Show Y-axis ticks
          color: string, // Set the color of Y-axis ticks
        },
      },
    };
    series: {
      name: string;
      data: number[];
    }[];
  }

interface ChoiceProps {
    velocidade: boolean,
    aceleracao: boolean,
    eixo: boolean
    outros: boolean,
}

function ChartTeste({ sensor_data, enumChoice }: DataProps & {enumChoice : ChoiceProps}) {

    const [chartAceleracao, setChartAceleracao] = useState<ChartData | null>(null);

    let [createdAt, setCreatedAt] = useState<string[]>([]);

    let [pontosY1, setPontosY1] = useState<number[]>([]);

    let [pontosY2, setPontosY2] = useState<number[]>([]);

    let [pontosY3, setPontosY3] = useState<number[]>([]);


    const [chartVelocidade, setChartVelocidade] = useState<ChartData | null>(null);

    let [pontosY4, setPontosY4] = useState<number[]>([]);

    let [pontosY5, setPontosY5] = useState<number[]>([]);

    let [pontosY6, setPontosY6] = useState<number[]>([]);

    
    const [chartEixo, setChartEixo] = useState<ChartData | null>(null);

    let [pontosY7, setPontosY7] = useState<number[]>([]);

    let [pontosY8, setPontosY8] = useState<number[]>([]);

    let [pontosY9, setPontosY9] = useState<number[]>([]);


    const [chartOutros, setChartOutros] = useState<ChartData | null>(null);

    let [pontosY10, setPontosY10] = useState<number[]>([]);


    useEffect(() => {

        if (sensor_data && sensor_data.length > 0)
        {

            if (createdAt.length === 50)
            {
              setCreatedAt(prevCreatedAt => prevCreatedAt.slice(20));

              setPontosY1(prevPontosY1 => prevPontosY1.slice(20));
              setPontosY2(prevPontosY2 => prevPontosY2.slice(20));
              setPontosY3(prevPontosY3 => prevPontosY3.slice(20));

              setPontosY4(prevPontosY4 => prevPontosY4.slice(20));
              setPontosY5(prevPontosY5 => prevPontosY5.slice(20));
              setPontosY6(prevPontosY6 => prevPontosY6.slice(20));

              setPontosY7(prevPontosY7 => prevPontosY7.slice(20));
              setPontosY8(prevPontosY8 => prevPontosY8.slice(20));
              setPontosY9(prevPontosY9 => prevPontosY9.slice(20));
            
              setPontosY10(prevPontosY10 => prevPontosY10.slice(20));
            
            }
            
            setCreatedAt(prevCreatedAt => [...prevCreatedAt, sensor_data[0]["createdAt"].slice(11, 19)]);
            setPontosY1(prevPontosY1 => [...prevPontosY1, sensor_data[0]["acel_x"]]);
            setPontosY2(prevPontosY2 => [...prevPontosY2, sensor_data[0]["acel_y"]]);
            setPontosY3(prevPontosY3 => [...prevPontosY3, sensor_data[0]["acel_z"]]);

            setPontosY4(prevPontosY4 => [...prevPontosY4, sensor_data[0]["vel_x"]]);
            setPontosY5(prevPontosY5 => [...prevPontosY5, sensor_data[0]["vel_y"]]);
            setPontosY6(prevPontosY6 => [...prevPontosY6, sensor_data[0]["vel_z"]]);

            setPontosY7(prevPontosY7 => [...prevPontosY7, sensor_data[0]["roll"]]);
            setPontosY8(prevPontosY8 => [...prevPontosY8, sensor_data[0]["pitch"]]);
            setPontosY9(prevPontosY9 => [...prevPontosY9, sensor_data[0]["yaw"]]);

            setPontosY10(prevPontosY10 => [...prevPontosY10, sensor_data[0]["esterc"]]);

    
            setChartAceleracao({
                options: {
                    chart: {
                      id: "realtime",
                      height: 350,
                      type: 'line',
                    },
                    xaxis: {
                      categories: createdAt,
                      axisTicks: {
                        show: true, // Show X-axis ticks
                        color: '#ff0000', // Set the color of X-axis ticks
                      },
                      labels: {
                        style: {
                          colors: '#ff0000', // Set the color of X-axis labels
                        },
                      },
                    },
                    yaxis: {
                      min: -20,
                      max: 20,
                      labels: {
                        style: {
                          colors: ['#00ff00'], // Set the color of Y-axis labels
                        },
                      },
                      axisTicks: {
                        show: true, // Show Y-axis ticks
                        color: '#0000ff', // Set the color of Y-axis ticks
                      },
                    },
                  },
                  series: [
                    {
                      name: "Acel X",
                      data: pontosY1
                    },
                    {
                      name: "Acel Y",
                      data: pontosY2
                    },
                    {
                      name:"Acel Z",
                      data: pontosY3
                    }
                  ]
                  
            })


            setChartVelocidade({
                options: {
                    chart: {
                      id: "realtime",
                      height: 350,
                      type: 'line',
                    },
                    xaxis: {
                      categories: createdAt,
                      axisTicks: {
                        show: true, // Show X-axis ticks
                        color: '#ff0000', // Set the color of X-axis ticks
                      },
                      labels: {
                        style: {
                          colors: '#ff0000', // Set the color of X-axis labels
                        },
                      },
                    },
                    yaxis: {
                      min: -800,
                      max: 800,
                      labels: {
                        style: {
                          colors: ['#00ff00'], // Set the color of Y-axis labels
                        },
                      },
                      axisTicks: {
                        show: true, // Show Y-axis ticks
                        color: '#0000ff', // Set the color of Y-axis ticks
                      },
                    },
                  },
                  series: [
                    {
                      name: "Vel X",
                      data: pontosY4
                    },
                    {
                      name: "Vel Y",
                      data: pontosY5
                    },
                    {
                      name:"Vel Z",
                      data: pontosY6
                    }
                  ]
            })

            setChartEixo({
              options: {
                  chart: {
                    id: "realtime",
                    height: 350,
                    type: 'line',
                  },
                  xaxis: {
                    categories: createdAt,
                    axisTicks: {
                      show: true, // Show X-axis ticks
                      color: '#ff0000', // Set the color of X-axis ticks
                    },
                    labels: {
                      style: {
                        colors: '#ff0000', // Set the color of X-axis labels
                      },
                    },
                  },
                  yaxis: {
                    min: -180,
                    max: 180,
                    labels: {
                      style: {
                        colors: ['#00ff00'], // Set the color of Y-axis labels
                      },
                    },
                    axisTicks: {
                      show: true, // Show Y-axis ticks
                      color: '#0000ff', // Set the color of Y-axis ticks
                    },
                  },
                },
                series: [
                  {
                    name: "Roll",
                    data: pontosY7
                  },
                  {
                    name: "Pitch",
                    data: pontosY8
                  },
                  {
                    name:"Yaw",
                    data: pontosY9
                  }
                ]
          })

          setChartOutros({
            options: {
                chart: {
                  id: "realtime",
                  height: 350,
                  type: 'line',
                },
                xaxis: {
                  categories: createdAt,
                  axisTicks: {
                    show: true, // Show X-axis ticks
                    color: '#ff0000', // Set the color of X-axis ticks
                  },
                  labels: {
                    style: {
                      colors: '#ff0000', // Set the color of X-axis labels
                    },
                  },
                },
                yaxis: {
                  min: 0,
                  max: 360,
                  labels: {
                    style: {
                      colors: ['#00ff00'], // Set the color of Y-axis labels
                    },
                  },
                  axisTicks: {
                    show: true, // Show Y-axis ticks
                    color: '#0000ff', // Set the color of Y-axis ticks
                  },
                },
              },
              series: [
                {
                  name: "Estercamento",
                  data: pontosY10
                }
              ]
        })

        }

        
        
    }, [sensor_data])

    

    return (
      <div className="sensor-chart">
      {chartVelocidade && enumChoice.velocidade &&
      <Chart 
      options={chartVelocidade.options}
      series={chartVelocidade.series}
      width={600}
      type="line"
      />}
      {chartAceleracao && enumChoice.aceleracao &&
      <Chart 
      options={chartAceleracao.options}
      series={chartAceleracao.series}
      width={600}
      type="line"
      />}
      {chartEixo && enumChoice.eixo &&
      <Chart 
      options={chartEixo.options}
      series={chartEixo.series}
      width={600}
      type="line"
      />}
      {chartOutros && enumChoice.outros &&
      <Chart 
      options={chartOutros.options}
      series={chartOutros.series}
      width={600}
      type="line"
      />}
      
      </div>
    )
}

export default ChartTeste;

// https://www.youtube.com/watch?v=yAI9fbbH-rM

// ESSE VIDEO USA A API QUE TEM TODOS OS DADOS E QUANDO É ADICIONADO MAIS UM NESSA API ELE MUDA O GRÁFICO
// ENTAO, TEM QUE MUDAR O PROPS QUE É PASSADO PRA ESSE COMPONENTE. PQ AGR A GENTE TA PASSANDO SO O ULTIMO
// TEM QUE PEGAR A API QUE MANDA TODOS OS DADOS E USAR NELA. 
