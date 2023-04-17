const classes = document.getElementsByClassName("class");
const tables =  document.getElementsByClassName('py-attribute-table');

for (let i = 0; i < tables.length; i++) {
   const table = tables[i];

   move_to_id = table.getAttribute('data-move-to-id');
   console.log(move_to_id);
   found = document.getElementById(move_to_id);
   console.log(found);
   found.innerHTML += table;

}