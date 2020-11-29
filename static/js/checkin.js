const video = document.getElementById('video')
const buttonCap = document.getElementById('startbutton')
const img = document.getElementById('photo')
var select = document.querySelector('select#videoSource');
let currentStream;
var myVar = null;
var canvas2 = null;

Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(navigator.mediaDevices.enumerateDevices().then(gotDevices))

select.onchange = function () {
    console.log("change");
    if (typeof currentStream !== 'undefined') {
        stopMediaTracks(currentStream);
    }
    const videoConstraints = {};
    if (select.value === '') {
        videoConstraints.facingMode = 'environment';
    } else {
        videoConstraints.deviceId = {exact: select.value};
        console.log(videoConstraints);
    }
    const constraints = {
        video: videoConstraints,
        audio: false
    };

    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
            currentStream = stream;
            video.srcObject = stream;
        })
        .then(gotDevices)
        .catch(error => {
            // console.log(error);
        });
}

function gotDevices(deviceInfos) {
    window.deviceInfos = deviceInfos; // make available to console
    console.log('Available input and output devices:', deviceInfos);
    for (const deviceInfo of deviceInfos) {
        const option = document.createElement('option');
        option.value = deviceInfo.deviceId;
        if (deviceInfo.kind === 'videoinput') {
            option.text = deviceInfo.label || `Camera ${select.length + 1}`;
            select.appendChild(option);
        }
    }
    if (typeof currentStream == 'undefined') {
        startVideo();
    }
}

function startVideo() {
    navigator.getUserMedia({video: {}},
        stream => {
            video.srcObject = stream;
            currentStream = stream;
        },
        err => console.log(err)
    )
}

function stopMediaTracks(stream) {
    console.log("stop");
    // clearInterval(myVar);
    stream.getTracks().forEach(track => {
        track.stop();
    });
}

video.addEventListener('stop', () => {
    console.log("vidio stop")
});

video.addEventListener("ended", () => {
    console.log("video stop");
});

video.addEventListener('play', () => {

    clearInterval(myVar)
    var canvas = faceapi.createCanvasFromMedia(video)
    canvas2 = canvas;
    // canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    var canvas_content = document.getElementById('canvas')

    canvas_content.append(canvas)
    var displaySize = {width: video.width, height: video.height}


    faceapi.matchDimensions(canvas, displaySize)

    myVar = setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections)


        // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)


        buttonCap.onclick = video.onclick = function () {
            canvas.getContext("2d").drawImage(video, 0, 0, 320, 240)
            var imgage = canvas.toDataURL("image/png;base64,")
            console.log(imgage)
            download(imgage);
            img.src = imgage
        };
    }, 100)


})