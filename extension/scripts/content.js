// const article = document.querySelector("article");

// // `document.querySelector` may return null if the selector doesn't match anything.
// if (article) {
//   const text = article.textContent;
//   const wordMatchRegExp = /[^\s]+/g; // Regular expression
//   const words = text.matchAll(wordMatchRegExp);
//   // matchAll returns an iterator, convert to array to get word count
//   const wordCount = [...words].length;
//   const readingTime = Math.round(wordCount / 200);
//   const badge = document.createElement("p");
//   // Use the same styling as the publish information in an article's header
//   badge.classList.add("color-secondary-text", "type--caption");
//   badge.textContent = `⏱️ ${readingTime} min read`;

//   // Support for API reference docs
//   const heading = article.querySelector("h1");
//   // Support for article docs with date
//   const date = article.querySelector("time")?.parentNode;

//   (date ?? heading).insertAdjacentElement("afterend", badge);
// }
// const stack = [];
// console.log(document.querySelector("body").children)

console.log("Translating page...")


const URL2 = 'http://localhost:9000/history/create'

const translate2 = async (data, token) => {
    const body = JSON.stringify({english: data, "token": token})
    console.log(body, body.length)
    return await fetch(URL2, {
        "method": 'POST',
        "headers": {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        },
        "dataType": 'json',
        "body": body,
    })
}

const translate_content = async (text) => {
    const token = "5ff94268-1bfc-4cfd-94c0-3aeb51d6e001";
    const j = await translate2(text, token);
    const data = await j.json();
    current.text = data.hindi;
}

const queue = [];
const translate_nav = async () => {
    const element = document.querySelector("body");
    queue.push(element);
    while (queue.length > 0) {
        current = queue.shift();
        if (current.children.length === 0) {

            if (
                (current.tagName === "LINK") ||(current.tagName === "SCRIPT") || 
                (current.tagName === "IMG") || (current.tagName === "TEXTAREA")
                || (current.tagName === "DIV")
            ) {
                continue
            }

            else if (current.tagName === "INPUT") {
                console.log(current.value)
                text = current.value
                await translate_content(text);
            } else if (current.tagName === "P") {
                console.log(current.innerText)
                text = current.innerText
                await translate_content(text);
            }
            else {
                console.log(current)
                console.log(current.text)
                text = current.text
                await translate_content(text);
            }
            console.log(current)

        } else {
            for (let children of current.children) {
                queue.push(children)
            }
        }
    }
}

translate_nav();