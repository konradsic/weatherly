window.addEventListener('load', function() {
   console.log("Custom JS file loaded");
   // const classes = document.getElementsByClassName("class");
   let tables = document.getElementsByClassName('py-attribute-table');

   for (let table of tables) 
      document.getElementById(table.getAttribute('data-move-to-id')).append(table);
});