console.log("Translation-form");


class WS  {
    constructor() {
        this.ws = new WebSocket(`ws:${window.location.host}/ws/translate/`);
        this.onmessage();
        this.message = null;
        this.recevied = false;
        this.interval = undefined;
        // this.onclose();
    }


    async send(data) {
        const stringifiedData = JSON.stringify(data);
        this.ws.send(stringifiedData)
    }

    async onmessage(callback) {
        this.ws.onmessage = async (event) => {
           document.querySelector(translationOuput).value = JSON.parse(event.data);
        }
    }
    async close() {
        this.ws.onclose = () => {
            console.log("ws Connection clonsed");
        }
    }

    async getMessage() {
        if (this.recevied) {
            // reset `this.recevied` and `this.message`
            this.recevied = false;
            retMes = this.message;
            this.message = null
            return retMes;
        }
        return null;
    }
}

// websocket instance
const ws = new WS();



const translationInput = "#translation-input";
const translationOuput = "#translation-output";
const translationButton = "#translate-button";


/**
 * Read data from the `translationInput`
 * @param {HTMLTableElement} table - The target HTML table
 * @param {Array} data - The array of cell header names
 */
const translateOnTranslationButton = async function () {
    let interval = undefined;
    document.querySelector(translationButton).onclick = async  () => {
        const data = document.querySelector(translationInput).value;
        if (data) {
            ws.send(data);
        } else {
            alert("No data!");
        }
        
    }
}


const  translateOnEnter = async function() {
    document.querySelector(translationInput).addEventListener("keydown", async function(event) {
        if ((event.ctrlKey === true) && (event.key === "Enter")) {
            const data = document.querySelector(translationInput).value;
            if (data) {
                ws.send(data);
            } else {
                alert("No data!");
            }
            
        }
    })
}



translateOnTranslationButton();
translateOnEnter();