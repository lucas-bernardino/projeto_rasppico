import { useEffect, useState } from "react";
import { MdDeleteOutline } from "react-icons/md";
import { FaDownload } from "react-icons/fa";

import "./History.css"

function History() {

    const [collectionData, setCollectionData] = useState<any>();


    const getCollectionNames = async () => {
        try {
            const response = await fetch("http://150.162.217.7:3001/collections");
            const collections = await response.json();
            const { collectionNames } = collections;
            setCollectionData(collectionNames);
        } catch (error) {
            setCollectionData(null)
        }
    }

    useEffect(() => {
        getCollectionNames();
    }, [])

    return (
        <div className="collections">
            {collectionData ? collectionData.map((item: string) => (
                <div className="coll-box">
                    <div className="coll-name">
                        <p className="item">{item}</p>
                        <div className="icons">
                            <MdDeleteOutline />
                            <FaDownload />
                        </div>
                    </div>
                </div>
            )) : <p></p>}
        </div>
    )

}

export default History;