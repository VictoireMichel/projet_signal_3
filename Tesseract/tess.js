const { createWorker } = require('tesseract.js')
const PSM = require('tesseract.js/src/constants/PSM.js')
const worker = createWorker()
const image = './images/test.png'



async function getTextFromImage() {
    await worker.load()
    await worker.loadLanguage('eng')
    await worker.initialize('eng')


    await worker.setParameters({
        tessedit_pageseg_mode: PSM.AUTO, // mode auto pour la segmentation de la page -> ici recherche toutes les lignes
        tessedit_char_whitelist: '0123456789',
    })






    const { data: { text } } = await worker.recognize(image); // retourne un objet avec une propriété DATA qui lui,
                                                              // est aussi un objet avec une propriété TEXT qui contient le résultat final

    await worker.terminate()

    return text

}

getTextFromImage()
    .then(console.log)


