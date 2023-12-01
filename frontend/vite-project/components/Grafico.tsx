import { useEffect, useState } from "react";
import "./Grafico.css"

import { FaXmark } from "react-icons/fa6";
import { IoCheckmarkSharp } from "react-icons/io5";
import ChartTeste from "./ChartTeste";

interface Choice {
    velocidade: boolean,
    aceleracao: boolean,
    eixo: boolean
    outros: boolean,
}

interface GraficoProps {
    flagShow: boolean,
}

function Grafico ({flagShow} : GraficoProps) {

    const [sensorData, setSensorData] = useState();
    async function fetchData() {
        const response = await fetch("http://150.162.217.186:3001/receber_ultimo");
        const data = await response.json();
        setSensorData(data);
      }

    useEffect(() => {
        const timer = setInterval(() => {
            fetchData()
        }, 100);
        return () => { clearInterval(timer) }
    }, [])


    let [enumChoice, setEnumChoice] = useState<Choice>({
        velocidade: false,
        aceleracao: false,
        eixo: false,
        outros: false
    })

    // TODO: VER COMO MUDAR A INTERFACE A CADA CLICK SEM ALTERAR OS OUTROS VALORES PRA PODER MOSTRAR UM GRAFICO DE CADA VEZ.

// You can use the spread operator (...) to keep the previous state and only change the specific property you want. Here’s how you can do it:

// <IoCheckmarkSharp className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, velocidade: !prevState.velocidade}))}/>

// In this example, when the IoCheckmarkSharp icon is clicked, it will toggle the velocidade property of the enumChoice state while keeping the other properties unchanged. You can do the same for the other properties as well. Just replace velocidade with the property you want to change. This way, you can change the values inside of your enumChoice without changing the previous values.

    return (
        
        <>
        {flagShow ? (
            <div className="page-container">
                <div className="container-text">
                    <div className="container">
                        <div className="opcao">
                            <p className="text">VELOCIDADE</p>
                            <div className="icons-div">
                                <IoCheckmarkSharp className="icon-mark" onClick={() => {setEnumChoice()}}/>
                                <FaXmark className="icon-mark"/>
                            </div>
                        </div>
                        <div className="opcao">
                            <p className="text">ACELERACAO</p>
                            <div className="icons-div">
                                <IoCheckmarkSharp className="icon-mark"/>
                                <FaXmark className="icon-mark"/>
                            </div>
                        </div >
                        <div className="opcao">
                            <p className="text">EIXO</p>
                            <div className="icons-div">
                                <IoCheckmarkSharp className="icon-mark"/>
                                <FaXmark className="icon-mark"/>
                            </div>
                        </div >
                        <div className="opcao">
                            <p className="text">OUTROS</p>
                            <div className="icons-div">
                                <IoCheckmarkSharp className="icon-mark"/>
                                <FaXmark className="icon-mark"/>
                            </div>
                        </div >
                    </div>
                </div>

                <div className="container-chart">
                    <ChartTeste sensor_data={sensorData} />
                </div>
            </div>
        ) : null}
        </>
    )
}

export default Grafico;