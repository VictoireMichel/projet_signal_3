

const { createWorker } = require('tesseract.js')
const PSM = require('tesseract.js/src/constants/PSM.js')
const worker = createWorker()
const image = './images/newCadran.png'



async function getTextFromImage() {
    await worker.load()
    await worker.loadLanguage('eng')
    await worker.initialize('eng')


    await worker.setParameters({
        tessedit_pageseg_mode: PSM.CIRCLE_WORD, // traite l'image en tant qu'un seul mot -> meilleure solution pour nous
        tessedit_char_whitelist: '0123456789',
    })




    const { data: { text } } = await worker.recognize(image); // retourne un objet avec une propriété DATA qui lui,
                                                              // est aussi un objet avec une propriété TEXT qui contient le résultat final

    await worker.terminate()

    return text

}

getTextFromImage()
    .then(console.log)


