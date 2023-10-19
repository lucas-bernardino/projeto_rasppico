import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import './WebcamUser.css';


export default function TentaivaWebcam() {
  const webcamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const [capturing, setCapturing] = useState(false);
  const [recordedChunks, setRecordedChunks] = useState([]);

  const handleDataAvailable = useCallback(
    ({ data }) => {
      if (data.size > 0) {
        setRecordedChunks((prev) => prev.concat(data));
      }
    },
    [setRecordedChunks]
  );

  const handleStartCaptureClick = useCallback(() => {
    setCapturing(true);
    mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
      mimeType: "video/webm",
    });
    mediaRecorderRef.current.addEventListener(
      "dataavailable",
      handleDataAvailable
    );
    mediaRecorderRef.current.start();
  }, [webcamRef, setCapturing, mediaRecorderRef, handleDataAvailable]);

  const handleStopCaptureClick = useCallback(() => {
    mediaRecorderRef.current.stop();
    setCapturing(false);
  }, [mediaRecorderRef, setCapturing]);

  const handleDownload = useCallback(() => {
    if (recordedChunks.length) {
      const blob = new Blob(recordedChunks, {
        type: "video/webm",
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      document.body.appendChild(a);
      a.style = "display: none";
      a.href = url;
      a.download = "react-webcam-stream-capture.webm";
      a.click();
      window.URL.revokeObjectURL(url);
      setRecordedChunks([]);
    }
  }, [recordedChunks]);

  const videoConstraints = {
    width: 1920,
    height: 1080,
    facingMode: "user",
  };

  return (
    <div className="webcam-container">
      <Webcam
        ref={webcamRef}
        videoConstraints={videoConstraints}
        screenshotQuality={1}
        height={500}
      />
      <div className="button-actions-div">
      {capturing ? (
        <button className="btn-webcam btn-webcam-stop" onClick={handleStopCaptureClick}>Parar</button>
      ) : (
        <button className="btn-webcam btn-webcam-record" onClick={handleStartCaptureClick}>Gravar</button>
      )}
      {recordedChunks.length > 0 && (
        <button className="btn-webcam btn-webcam-download" onClick={handleDownload}>Download</button>
      )}
      </div>
    </div>
  );
}