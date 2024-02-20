console.log("Translation-form");

const translationInput = "#translation-input";
const translationOuput = "#translation-output";
const translationButton = "#translate-button";

/**
 * Read data from the `translationInput`
 * @param {HTMLTableElement} table - The target HTML table
 * @param {Array} data - The array of cell header names
 */
const translateOnTranslationButton = async function () {
    document.querySelector(translationButton).onclick = () => {
        // console.log(document.querySelector(translationInput).value);
        
        document.querySelector(translationOuput).value = document.querySelector(translationInput).value;
    }
}


const  translateOnEnter = async function() {
    document.querySelector(translationInput).addEventListener("keydown", async function(event) {
        // if (event.Key === "Ctrl + Enter") {
        //     console.log(await translateOnTranslationButton());
        // }
        if ((event.ctrlKey === true) && (event.key === "Enter")) {
            // console.log("Control and Enter")
            document.querySelector(translationOuput).value = document.querySelector(translationInput).value;
        }
    })
}



translateOnTranslationButton();
translateOnEnter();