

window.addEventListener('load', function() {
   console.log("Custom JS file loaded");
   let operationContainers = document.querySelectorAll(".container.operations");
   
   for (let opContainer of operationContainers) {
      opContainer.innerHTML = `<b>Supported operations:</b><br/> ${opContainer.innerHTML}`
   }
   // const classes = document.getElementsByClassName("class");
   let tables = document.getElementsByClassName('py-attribute-table');

   for (let table of tables) 
      document.getElementById(table.getAttribute('data-move-to-id')).parentElement.querySelector("dd").prepend(table);
});