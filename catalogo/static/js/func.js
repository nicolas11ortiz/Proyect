var x;
x=$(document);
x.ready(inicializarEventos);

function inicializarEventos()
{
  var x;
  x=$("#boton1");
  x.click(ocultarItem);
}

function ocultarItem()
{
  var x;
  x=$("#lista1 div");
  x.hide();
}