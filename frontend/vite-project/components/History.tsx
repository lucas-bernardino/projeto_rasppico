import { useEffect, useState } from "react";
import { MdDeleteOutline } from "react-icons/md";
import { FaDownload } from "react-icons/fa";

import "./History.css";

function History() {
  const [collectionData, setCollectionData] = useState<string[] | null>();

  const getCollectionNames = async () => {
    try {
      const response = await fetch(import.meta.env.VITE_BACKEND_URL + "/collections", {headers: {'ngrok-skip-browser-warning': 'true'}});
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
    await fetch(import.meta.env.VITE_BACKEND_URL + "/delete", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        'ngrok-skip-browser-warning': 'true'
      },
      body: JSON.stringify({ collectionName: collectionName }),
    });
  };

  const handleDownloadButton = async (collectionName: string) => {
    try {
      const response = await fetch(import.meta.env.VITE_FLASK_URL + "/download?" + new URLSearchParams({ name: collectionName }), {headers: {'ngrok-skip-browser-warning': 'true'}});
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
