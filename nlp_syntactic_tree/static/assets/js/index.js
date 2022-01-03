const exampleList=document.querySelectorAll('.exampleItem');
const resultList=document.querySelectorAll('.result-item');
const inputSentence=document.querySelector('.input-sentence');
const btnDelete=document.querySelector('.btn-delete');
const btnDeleteAll=document.querySelector('.btn-clear');
const btnParse=document.querySelector('.btn-form');
const result=document.querySelector('.result-item');

exampleList.forEach(function (example, index) {
    example.onclick = function(e) {
        inputSentence.value = example.innerText;
    }
})

btnDelete.onclick = function(e) {
    e.preventDefault();
    result.classList.add('dp-none');
}

// btnParse.onclick= function(e) {
//     e.preventDefault();
//     if(result.classList.contains('dp-none')) {
//         result.classList.remove('dp-none');
//     };
// }

btnDeleteAll.onclick = function(e) {
    e.preventDefault();
    resultList.forEach(function (result) {
        result.classList.add('dp-none');
    });
}