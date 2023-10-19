import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import './CustomWebcam.css';

const CustomWebcam: React.FC = () => {
  const webcamRef = useRef<Webcam | null>(null);
  const [capturing, setCapturing] = useState(false);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const [recordedChunks, setRecordedChunks] = useState<Blob[]>([]);

  // Initialize the webcam and start capturing
  const startCapture = () => {
    const stream = webcamRef.current?.stream;
    if (stream) {
      const mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm;codecs=vp9', videoBitsPerSecond: 5000000 });
      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          setRecordedChunks([...recordedChunks, event.data]);
        }
      };
      mediaRecorder.onstop = () => {
        setCapturing(false);
      };
      setMediaRecorder(mediaRecorder);
      mediaRecorder.start();
      setCapturing(true);
    }
  };

  // Stop capturing
  const stopCapture = () => {
    mediaRecorder?.stop();
  };

  // Download the captured video
  const downloadVideo = () => {
    const blob = new Blob(recordedChunks, { type: 'video/mp4' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    document.body.appendChild(a);
    a.style.display = 'none';
    a.href = url;
    a.download = 'captured-video.mp4';
    a.click();
    window.URL.revokeObjectURL(url);
  };

  return (
    <div className='webcam-container'>
      <Webcam audio={false} ref={webcamRef} width={1280} height={720}/>
      <div className="button-actions-div">
        {capturing ? (
          <button onClick={stopCapture}>Parar</button>
        ) : (
          <button onClick={startCapture}>Gravar</button>
        )}
        {recordedChunks.length > 0 && (
          <button onClick={downloadVideo}>Download</button>
        )}
      </div>
    </div>
  );
};

export default CustomWebcam;


// TEM QUE AUMENTAR O TAMANHO DA CAMERA PROVAVELMENTE.


// https://github.com/DeltaCircuit/react-media-recorder