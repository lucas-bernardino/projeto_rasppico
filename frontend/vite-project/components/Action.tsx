import { FaDownload, FaPlay } from "react-icons/fa";
import { AiFillDelete } from "react-icons/ai";
import { BsFileBarGraphFill } from "react-icons/bs";
import {BiStopwatch} from "react-icons/bi";

import "./Actions.css";

function Action () {


    return (
        <div className="additional-info">
            <div className="ac1 action-div">
            <FaPlay className="icon" /> MONITORAR
            </div>
            <div className="ac2 action-div">
            <AiFillDelete className="icon" />DELETAR
            </div>
            <div className="ac3 action-div">
            <BsFileBarGraphFill className="icon" />GRÁFICOS
            </div>
            <div className="ac4 action-div">
            <BiStopwatch className="icon" />PARAR
            </div>
            <div className="ac5 action-div">
            <FaDownload className="icon" />BAIXAR
            </div>
        </div>
    )
}

export default Action;