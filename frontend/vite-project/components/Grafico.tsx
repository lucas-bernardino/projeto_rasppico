import { useEffect, useState } from "react";
import "./Grafico.css"

import { MdOutlineToggleOff } from "react-icons/md";
import { MdOutlineToggleOn } from "react-icons/md";
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

    return (
        
        <>
        {flagShow ? (
            <div className="page-container">
                <div className="container-text">
                    <div className="container">
                        <div className="opcao">
                            <p className="text">VELOCIDADE</p>
                            <div className="icons-div">
                                {enumChoice.velocidade ? 
                                (<MdOutlineToggleOn className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, velocidade: false}))}/>) 
                                : ((<MdOutlineToggleOff className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, velocidade: true}))}/>))}
                            </div>
                        </div>
                        <div className="opcao">
                            <p className="text">ACELERACAO</p>
                            <div className="icons-div">
                                {enumChoice.aceleracao ? 
                                (<MdOutlineToggleOn className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, aceleracao: false}))}/>) 
                                : ((<MdOutlineToggleOff className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, aceleracao: true}))}/>))}
                            </div>
                        </div >
                        <div className="opcao">
                            <p className="text">EIXO</p>
                            <div className="icons-div">
                                {enumChoice.eixo ? 
                                (<MdOutlineToggleOn className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, eixo: false}))}/>) 
                                : ((<MdOutlineToggleOff className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, eixo: true}))}/>))}
                            </div>
                        </div >
                        <div className="opcao">
                            <p className="text">OUTROS</p>
                            <div className="icons-div">
                                {enumChoice.outros ? 
                                (<MdOutlineToggleOn className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, outros: false}))}/>) 
                                : ((<MdOutlineToggleOff className="icon-mark" onClick={() => setEnumChoice(prevState => ({...prevState, outros: true}))}/>))}
                            </div>
                        </div >
                    </div>
                </div>

                <div className="container-chart">
                    <ChartTeste sensor_data={sensorData} enumChoice={enumChoice}/>
                </div>
            </div>
        ) : null}
        </>
    )
}

export default Grafico;