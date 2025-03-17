// Selecionando elementos
const texto = document.getElementById("texto");
const btnTrocarTexto = document.getElementById("btnTrocarTexto");
const btnMudarCor = document.getElementById("btnMudarCor");
const btnToggle = document.getElementById("btnToggle");
const btnAdicionar = document.getElementById("btnAdicionar");
const container = document.getElementById("container");
const btnMudarCorFundo = document.getElementById("btnMudarCorFundo");
const btnAdicionarInput = document.getElementById("btnAdicionarInput");
const erro = document.getElementById("erro");
const inputsContainer = document.getElementById("inputsContainer");
const textoExibido = document.getElementById("textoExibido");
const btnEnviar = document.getElementById("btnEnviar");
const btnRemover = document.getElementById("btnRemover");

let removendo = false; // Variável que controla o modo de remoção

// Alterar o texto do parágrafo
btnTrocarTexto.addEventListener("click", () => {
  texto.textContent = "O texto foi modificado!";
});

// Mudar a cor do parágrafo
btnMudarCor.addEventListener("click", () => {
  texto.classList.toggle("destacado");
});

// Esconder/Mostrar o texto
btnToggle.addEventListener("click", () => {
  texto.classList.toggle("oculto");
});

// Adicionar um novo elemento dinamicamente
btnAdicionar.addEventListener("click", () => {
  let novoParagrafo = document.createElement("p");
  novoParagrafo.textContent = "Novo elemento adicionado!";
  container.appendChild(novoParagrafo);
});

// Ativa o modo de remoção
btnRemover.addEventListener("click", function (event) {
  removendo = !removendo;
  if (removendo) {
    btnRemover.textContent = "Remoção Ativada - Clique nos elementos";
  } 
  else {
    btnRemover.textContent = "Ativar Remoção";
  }
  event.stopPropagation();
});

// Remove o elemento clicado (cuidado para não remover o body todo KJASHDSAKJSDH)
document.addEventListener("click", function (event) {
    if (removendo && event.target.id !== "btnRemover") {
      event.preventDefault();
      event.stopImmediatePropagation();
      event.target.remove();
    }
  }, true
);

// Muda a cor de fundo
btnMudarCorFundo.addEventListener("click", function () {
  document.body.style.backgroundColor = gerarCor();
});

// Função para gerar uma cor aleatória, peguei da internet :)
function gerarCor() {
  let cor = Math.floor(Math.random() * 16777215).toString(16);
  return "#" + cor.padStart(6, "0");
}

// Adiciona o input (se já tiver um input ativo, mostra um erro)
btnAdicionarInput.addEventListener("click", function () {
  if (inputsContainer.children.length > 0) {
    erro.style.display = "block";
  } 
  else {
    erro.style.display = "none";
    let input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Digite algo aqui...";
    inputsContainer.appendChild(input);
    inputsContainer.appendChild(btnEnviar);
    btnEnviar.style.display = "block";
  }
});

// Mostra o conteúdo dos inputs
btnEnviar.addEventListener("click", function () {
  let inputs = document.querySelectorAll("#inputsContainer input");
  textoExibido.innerHTML = "";
  inputs.forEach(function (input) {
    let p = document.createElement("p");
    p.textContent = input.value;
    textoExibido.appendChild(p);
  });
  btnEnviar.style.display = "none";
  inputsContainer.innerHTML = "";
  erro.style.display = "none";
});
