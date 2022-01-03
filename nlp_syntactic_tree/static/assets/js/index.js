const exampleList=document.querySelectorAll('.exampleItem');
const inputSentence=document.querySelector('.input-sentence');

const resultSentence=document.querySelector('.result-sentence');

exampleList.forEach(function (example, index) {
    example.onclick = function(e) {
        inputSentence.value = example.innerText;
    }
})
