// Diseño de los editores con codemirror
let editor = document.getElementById("editor");
editor = CodeMirror.fromTextArea(document.getElementById("editor"),{
    mode: "rust",
    theme: "darcula",
    lineNumbers: true,
    autoCloseTags: true
});
editor.setSize("560px", "590px");

let editor2 = document.getElementById("editor2");
editor2 = CodeMirror.fromTextArea(document.getElementById("editor2"),{
    mode: "javascript",
    theme: "darcula",
    lineNumbers: true,
    autoCloseTags: true
});
editor2.setSize("560px", "590px");

// Codigo para agregar pestañas

let numero = 1;

function agregarPestania(){
    numero++;
    const contenedorbutton = document.getElementById("buttontextareas");
    const newbutton = document.createElement("li");
    newbutton.className = "listaPestana";
    const newlink = document.createElement("a");
    newlink.className = "pestanaActiva";
    newlink.setAttribute("data-bs-toggle", "tab");
    newlink.setAttribute("href", `#tab${numero}`);
    newlink.innerHTML = `tab${numero}`;
    newbutton.appendChild(newlink);
    contenedorbutton?.appendChild(newbutton);
    const contenedortextareas = document.getElementById("textareas");
    const newdivtext = document.createElement("div");
    newdivtext.className = "tabla";
    newdivtext.id = `tab${numero}`;
    const newtextarea = document.createElement("textarea");
    newtextarea.className = "numerado";
    editor.setSize("560px", "590px");
    newdivtext.appendChild(newtextarea);
    contenedortextareas?.appendChild(newdivtext);
}

/*function obtenerTexto(){
    let contenido = editor.getValue();
    //console.log(texto);

    var newpost ={
        Texto: contenido,
    }

    fetch('http://localhost:3000/text', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newpost)
    })
    .then(response => response.json())
    //.then(response => response.json())
    .then(data=>{
        console.log(data.Salida);
        editor2.setValue(data.Salida);
    })
}*/

function comenzar(){
    let archivos = document.getElementById("archivos");
    archivos.addEventListener("change", procesar, false);
    //editor.setValue("hola");
}

function procesar(e){
    //editor.setValue("hola");
    var archivos = e.target.files;
    var mi_archivo = archivos[0];
    var lector = new FileReader();
    lector.readAsText(mi_archivo);
    lector.addEventListener("load", mostrarWeb, false);
}

function mostrarWeb(e){
    var resultado = e.target.result;
    editor.setValue(resultado);
}

window.addEventListener("load", comenzar, false);