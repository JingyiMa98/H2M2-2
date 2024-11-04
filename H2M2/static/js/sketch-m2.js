let divData, suggestions_text, speech, startBtn, stopBtn, canvas;
let selectedImg, lightImg, wateringImg, humidityImg, temperatureImg, pruningImg, propagationImg;
let img_is_selected = false;

function preload(){
    lightImg = loadImage("imgs/light.jpg");
    wateringImg = loadImage("imgs/watering.jpg");
    humidityImg = loadImage("imgs/humidity.jpg");
    temperatureImg = loadImage("imgs/temperature.jpg");
    pruningImg = loadImage("imgs/pruning.jpg");
    propagationImg = loadImage("imgs/propagation.jpg");
}

function setup(){
    canvas = createCanvas(600, 620);
    canvas.parent('canvas-div');
    divData = document.querySelector("#canvas-div");

    speech = new p5.Speech(); // speech synthesis object
    
    suggestions_style = divData.dataset.style || "Light"; 

    // Start button setup
    let startBtnDiv = document.querySelector('#startBtnDiv');
    startBtn = createButton('Read it');
    startBtn.parent(startBtnDiv);
    startBtn.class('btn btn-primary');
    startBtn.mousePressed(startSpeaking);

    // Stop button setup
    let stopBtnDiv = document.querySelector('#stopBtnDiv');
    stopBtn = createButton('Stop it');
    stopBtn.parent(stopBtnDiv);
    stopBtn.class('custom-stop-btn');
    stopBtn.mousePressed(stopSpeaking);
    
}

function draw(){
    background(255);
    fill(0);
    rectMode(CENTER);

    suggestions_text = divData.dataset.suggestions || "Waiting for the suggestions...";

    let display_text = "Suggestions style: " + suggestions_style + "\n\n" + suggestions_text;

    if(img_is_selected){
        tint(255, 255, 255, 40);
        image(selectedImg, 0, 0, 600, 620);
    }

    textSize(18);
    textWrap(WORD);
    text(display_text, width / 2, height / 2, width - 100, height - 100);
}

function startSpeaking(){
    if(suggestions_text !== "Waiting for the suggestions...") {
        img_is_selected = true;

        switch (suggestions_style) {
            case "Light":
                selectedImg = lightImg;
                speech.setVoice(0);
                speech.setPitch(0.01);
                speech.setRate(0.5);
                break;
            case "Watering":
                selectedImg = wateringImg;
                speech.setVoice(1);
                speech.setPitch(1);
                speech.setRate(1);
                break;
            case "Humidity":
                selectedImg = humidityImg;
                speech.setVoice(1);
                speech.setPitch(1.5);
                speech.setRate(1.5);
                break;
            case "Temperature":
                selectedImg = temperatureImg;
                speech.setVoice(2);
                speech.setPitch(2);
                speech.setRate(1);
                break;
            case "Pruning":
                selectedImg = pruningImg;
                speech.setVoice(0);
                speech.setPitch(2);
                speech.setRate(1);
                break;
            case "Propagation":
                selectedImg = propagationImg;
                speech.setVoice(2);
                speech.setPitch(1);
                speech.setRate(1);
                break;
            default:
                img_is_selected = false;
                break;
        }

        if (img_is_selected) {
            speech.speak(suggestions_text);
        }
    }
}

function stopSpeaking(){
    speech.stop();
}
