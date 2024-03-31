$(document).ready(function(){
  $(".form-wrapper .button").click(function(){
    var button = $(this);
    var currentSection = button.parents(".section");
    var currentSectionIndex = currentSection.index();
    var headerSection = $('.steps li').eq(currentSectionIndex);
    currentSection.removeClass("is-active").next().addClass("is-active");
    

    

    
  });
});

function update2(){
  const infoDiv = document.getElementById("info");
  var name = document.createElement("INPUT");
  //var type = document.getElementsByTagName();
  name.setAttribute("type", "text");
  name.setAttribute("name","pname");
  name.setAttribute("id" , "pname");
  name.setAttribute("placeholder" , "Process Name" );

  var time = document.createElement("INPUT");
  time.setAttribute("type", "text");
  time.setAttribute("name","time");
  time.setAttribute("id" , "time");
  time.setAttribute("placeholder" , "Brust Time" );
  infoDiv.appendChild(name);
  infoDiv.appendChild(time);
  if ($('input[name=radio1]:checked', '#myForm').val() == "s3"){
  var priority = document.createElement("INPUT");
  priority.setAttribute("type", "text");
  priority.setAttribute("name","priority");
  priority.setAttribute("id" , "priority");
  priority.setAttribute("placeholder" , "priority" );
  infoDiv.appendChild(priority);
  }
}
function update(){
  const infoDiv = document.getElementById("info");
  if ($('input[name=radio1]:checked', '#myForm').val() == "s4"){
    var robin = document.createElement("INPUT");
    robin.setAttribute("type", "text");
    robin.setAttribute("name","robin");
    robin.setAttribute("id" , "robin");
    robin.setAttribute("placeholder" , "Quantum" );
    infoDiv.appendChild(robin);
    }

  var name = document.createElement("INPUT");
  //var type = document.getElementsByTagName();
  name.setAttribute("type", "text");
  name.setAttribute("name","pname");
  name.setAttribute("id" , "pname");
  name.setAttribute("placeholder" , "Process Name" );

  var time = document.createElement("INPUT");
  time.setAttribute("type", "text");
  time.setAttribute("name","time");
  time.setAttribute("id" , "time");
  time.setAttribute("placeholder" , "Brust Time" );
  infoDiv.appendChild(name);
  infoDiv.appendChild(time);
  if ($('input[name=radio1]:checked', '#myForm').val() == "s3"){
  var priority = document.createElement("INPUT");
  priority.setAttribute("type", "text");
  priority.setAttribute("name","priority");
  priority.setAttribute("id" , "priority");
  priority.setAttribute("placeholder" , "priority" );
  infoDiv.appendChild(priority);
  }
}
