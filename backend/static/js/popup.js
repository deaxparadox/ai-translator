console.log("Popup JS")

const URLPopup = "http://localhost:9000/history/create";

const translatePopups = async (data, token) => {
    const body = JSON.stringify({ english: data, "token": token })
    console.log(body, body.length)
    return await fetch(URLPopup, {
        "method": 'POST',
        "headers": {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        },
        "dataType": 'json',
        "body": body,
    })
}

const liAppendItem = async (message) => {
    `
    <li class="info">
        <div class="message-close-button">
            <button onclick="closeMesssages(this)" type="button">⨯</button>
        </div>
        <p class="message-display-p">
            ` + message + `
        </p>
    </li>
`

} 

const translatePopupText = async (element) => {
    const token = "5ff94268-1bfc-4cfd-94c0-3aeb51d6e001";
    const f = await translatePopups(element.innerText, token);
    const data = await f.json();
    document.querySelector("#popup-translated-text").value = data.hindi;
}