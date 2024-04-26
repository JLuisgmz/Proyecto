console.log('Si funciona')

const video = document.getElementById('video-element')
if(navigator.mediaDevices.getUserMedia){
    navigator.mediaDevices.getUserMedia({video:true})
    .then((stream) => {
        video.srcObject = stream
    })
}
