import { useEffect, useState } from "react";
import { MdDeleteOutline } from "react-icons/md";
import { FaDownload } from "react-icons/fa";

import "./History.css";

function History() {
  const [collectionData, setCollectionData] = useState<string[] | null>();

  const getCollectionNames = async () => {
    try {
      const response = await fetch("http://192.168.0.8:3001/collections");
      const collections = await response.json();
      const { collectionNames } = collections;
      setCollectionData(collectionNames);
    } catch (error) {
      setCollectionData(null);
    }
  };

  useEffect(() => {
    getCollectionNames();
  }, []);

  const handleDeleteButton = async (collectionName: string) => {
    await fetch("http://192.168.0.8:3001/delete", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ collectionName: collectionName }),
    });
  };

  const handleDownloadButton = async (collectionName: string) => {
    try {
      const response = await fetch(
        "http://192.168.0.8:5000/download?" +
          new URLSearchParams({ name: collectionName }),
      );
      const blob = await response.blob();
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "data.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error("Error downloading file:", error);
    }
  };

  return (
    <div className="collections">
      {collectionData ? (
        collectionData.map((item: string) => (
          <div className="coll-box" key={item}>
            <div className="coll-name">
              <p className="item">{item}</p>
              <div className="icons">
                <MdDeleteOutline onClick={() => handleDeleteButton(item)} />
                <FaDownload onClick={() => handleDownloadButton(item)} />
              </div>
            </div>
          </div>
        ))
      ) : (
        <p></p>
      )}
    </div>
  );
}

export default History;