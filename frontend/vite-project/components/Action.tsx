import { FaDownload, FaPlay } from "react-icons/fa";
import { AiFillDelete } from "react-icons/ai";
import { BsFileBarGraphFill } from "react-icons/bs";
import {BiStopwatch} from "react-icons/bi";
import Grafico from "./Grafico"

import "./Actions.css";
import { useState } from "react";

function Action () {

    const [flagShow, setFlagShow] = useState(false);

    const handleDownload = async () => {
        try {
            const response = await fetch('http://150.162.217.7:5000/csv');
            const blob = await response.blob();
            const url = window.URL.createObjectURL(new Blob([blob]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'data.csv');
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          } catch (error) {
            console.error('Error downloading file:', error);
          }
    }

    return (
        <div className="additional-info">
            <div className="ac1 action-div">
                <FaPlay className="icon" /> MONITORAR
            </div>
            <div className="ac2 action-div">
                <AiFillDelete className="icon" />DELETAR
            </div>
            <div className="grafico-container">
                <div className="ac3 action-div" onClick={() => {setFlagShow(!flagShow)}}>
                    <BsFileBarGraphFill className="icon" onClick={() => {setFlagShow(!flagShow)}} />GRÁFICOS
                </div>
                <Grafico flagShow={flagShow}/>
            </div>
            <div className="ac4 action-div">
                <BiStopwatch className="icon" />PARAR
            </div>
            <div className="ac5 action-div" onClick={handleDownload}>
                <FaDownload className="icon" onClick={handleDownload} />BAIXAR
            </div>
        </div>
    )
}

export default Action;