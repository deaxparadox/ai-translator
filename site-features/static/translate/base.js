const copyToClipboard = async () => {
    document.querySelector("#copy-button").onclick = async () => {
        document.querySelector("#input-data").select();
        document.execCommand("copy");
    }
}

if ('speechSynthesis' in window) {
    // Speech Synthesis is supported 🎉
    console.log("true")
} else {
    // Speech Synthesis is not Supported 😞 
    console.log("false")
}

let utterance = new SpeechSynthesisUtterance("Educative.io");
speechSynthesis.speak(utterance);

speechSynthesis.getVoices();

function getVoices() {
    let voices = speechSynthesis.getVoices();
    if (!voices.length) {
        let utterance = new SpeechSynthesisUtterance("");
        speechSynthesis.speak(utterance);
        voices = speechSynthesis.getVoices();
    }
    return voices;
}

let textToSpeak = "I Love Educative.io";

let speakData = new SpeechSynthesisUtterance();
speakData.volume = 1; // From 0 to 1
speakData.rate = 1; // From 0.1 to 10
speakData.pitch = 2; // From 0 to 2
speakData.text = textToSpeak;
speakData.lang = 'en';
speakData.voice = getVoices()[0];

speechSynthesis.speak(speakData);


copyToClipboard();